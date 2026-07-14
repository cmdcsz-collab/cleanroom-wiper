#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中英双语无尘布产品目录 PDF 生成器
Bilingual Cleanroom Wiper Product Catalog PDF Generator
"""

import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black, navy
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage,
    Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

# ============================================================
# 1. Register Chinese Font
# ============================================================
# Try common Chinese fonts
CHINESE_FONTS = [
    ('C:/Windows/Fonts/msyh.ttc', 'MicrosoftYaHei'),        # Win10 SimHei
    ('C:/Windows/Fonts/simhei.ttf', 'SimHei'),
    ('C:/Windows/Fonts/msyh.ttf', 'MicrosoftYaHei'),
    ('C:/Windows/Fonts/simsun.ttc', 'SimSun'),
    ('C:/Windows/Fonts/STZHONGS.TTF', 'STZhongsong'),
]

FONT_NAME = 'Helvetica'
FONT_NAME_CN = 'Helvetica'

for font_path, font_name in CHINESE_FONTS:
    try:
        if os.path.exists(font_path):
            pdfmetrics.registerFont(TTFont(font_name, font_path))
            FONT_NAME_CN = font_name
            print(f"Registered font: {font_name} from {font_path}")
            break
    except Exception as e:
        print(f"Failed to load {font_path}: {e}")

if FONT_NAME_CN == 'Helvetica':
    print("WARNING: No Chinese font found, Chinese text may not display correctly")

# ============================================================
# 2. Output PDF
# ============================================================
OUTPUT_FILE = '无尘布产品目录_Cleanroom_Wiper_Catalog.pdf'
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = WORK_DIR

doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    topMargin=15*mm,
    bottomMargin=15*mm,
    leftMargin=15*mm,
    rightMargin=15*mm,
    title='无尘布产品目录 - Cleanroom Wiper Catalog',
    author='源洁无尘布（无锡）工厂'
)

# ============================================================
# 3. Styles
# ============================================================
PAGE_W = A4[0] - 30*mm  # usable width

styles = getSampleStyleSheet()

style_title = ParagraphStyle(
    'TitleCN', fontName=FONT_NAME_CN, fontSize=22, leading=30,
    alignment=TA_CENTER, spaceAfter=4*mm, textColor=HexColor('#1a3a5c')
)
style_subtitle = ParagraphStyle(
    'SubCN', fontName=FONT_NAME_CN, fontSize=11, leading=16,
    alignment=TA_CENTER, spaceAfter=2*mm, textColor=HexColor('#555555')
)
style_h1 = ParagraphStyle(
    'H1CN', fontName=FONT_NAME_CN, fontSize=16, leading=22,
    spaceBefore=5*mm, spaceAfter=3*mm, textColor=HexColor('#1a3a5c'),
    borderWidth=0, borderColor=HexColor('#1a3a5c'), borderPadding=2,
)
style_h2 = ParagraphStyle(
    'H2CN', fontName=FONT_NAME_CN, fontSize=13, leading=18,
    spaceBefore=3*mm, spaceAfter=2*mm, textColor=HexColor('#2b5a8c')
)
style_body = ParagraphStyle(
    'BodyCN', fontName=FONT_NAME_CN, fontSize=9.5, leading=14,
    alignment=TA_LEFT, spaceAfter=1.5*mm
)
style_body_en = ParagraphStyle(
    'BodyEN', fontName=FONT_NAME, fontSize=9, leading=13,
    alignment=TA_LEFT, spaceAfter=1.5*mm, textColor=HexColor('#444444')
)
style_cell = ParagraphStyle(
    'CellCN', fontName=FONT_NAME_CN, fontSize=8, leading=11,
    alignment=TA_CENTER
)
style_cell_en = ParagraphStyle(
    'CellEN', fontName=FONT_NAME, fontSize=7.5, leading=10,
    alignment=TA_CENTER
)
style_header_cell = ParagraphStyle(
    'HeaderCell', fontName=FONT_NAME_CN, fontSize=8.5, leading=12,
    alignment=TA_CENTER, textColor=white
)
style_footer = ParagraphStyle(
    'Footer', fontName=FONT_NAME_CN, fontSize=8, leading=11,
    alignment=TA_CENTER, textColor=HexColor('#888888')
)

# Helper: split Chinese | English
def cn_en(cn_text, en_text):
    return f"<b>{cn_text}</b><br/><font size='-1'>{en_text}</font>"

# ============================================================
# 4. Build Story
# ============================================================
story = []

# ---------- COVER PAGE ----------
story.append(Spacer(1, 30*mm))
story.append(Paragraph('无尘擦拭布 · 产品目录', style_title))
story.append(Paragraph('Cleanroom Wiper · Product Catalog', ParagraphStyle(
    'CoverEN', fontName=FONT_NAME, fontSize=16, leading=22,
    alignment=TA_CENTER, spaceAfter=6*mm, textColor=HexColor('#555555')
)))
story.append(Spacer(1, 10*mm))

# Cover image (use product_07 which is larger)
cover_img_path = os.path.join(IMAGE_DIR, 'product_07.webp')
if os.path.exists(cover_img_path):
    try:
        pil_img = Image.open(cover_img_path)
        w, h = pil_img.size
        # Scale to fit A4 width
        max_w = 140*mm
        ratio = min(max_w / w, 100*mm / h)
        img_w = w * ratio
        img_h = h * ratio
        # Save as PNG for reportlab
        pil_img.save('wiper_product.png', 'PNG')
        story.append(RLImage('wiper_product.png', width=img_w, height=img_h))
        story.append(Spacer(1, 5*mm))
        os.remove('wiper_product.png')
    except Exception as e:
        print(f"Cover image error: {e}")

story.append(Spacer(1, 10*mm))
story.append(Paragraph(cn_en('供应商：源洁无尘布（无锡）工厂', 'Supplier: Wuxi Yuanjie Cleanroom Products'), style_body))
story.append(Paragraph(cn_en('版本：V1.0 | 日期：2026年7月', 'Version: V1.0 | Date: July 2026'), style_body))
story.append(Paragraph(cn_en('联系方式：[请填写]', 'Contact: [Please fill in]'), style_body))
story.append(PageBreak())

# ---------- TABLE OF CONTENTS ----------
story.append(Paragraph(cn_en('目录', 'Table of Contents'), style_h1))
story.append(Spacer(1, 3*mm))
toc_items = [
    ('一、公司简介 / Company Profile', ''),
    ('二、DS系列 电子级无尘布 / DS Series Electronic Grade', ''),
    ('三、KH系列 工业擦拭布 / KH Series Industrial Wipes', ''),
    ('四、包装方式 / Packaging Options', ''),
    ('五、定制选项 / Customization', ''),
    ('六、认证与质量 / Certifications & Quality', ''),
    ('七、联系方式 / Contact Us', ''),
]
for item, _ in toc_items:
    story.append(Paragraph(item, style_body))
    story.append(Spacer(1, 1*mm))
story.append(PageBreak())

# ---------- 1. COMPANY PROFILE ----------
story.append(Paragraph(cn_en('一、公司简介', '1. Company Profile'), style_h1))
story.append(Paragraph(
    cn_en(
        '源洁无尘布（无锡）工厂是一家专业生产无尘擦拭布的企业，拥有多年的行业经验。'
        '产品广泛应用于半导体、电子制造、生物医药、精密仪器等领域的无尘室环境清洁。'
        '我们提供DS系列电子级无尘布和KH系列工业擦拭布两大产品线，满足不同客户的需求。',
        'Wuxi Yuanjie Cleanroom Products is a professional manufacturer of cleanroom wipers '
        'with years of industry experience. Our products are widely used in semiconductor, '
        'electronics manufacturing, biopharmaceutical, precision instrument cleanroom environments. '
        'We offer DS Series electronic grade and KH Series industrial wipes product lines.'
    ), style_body
))
story.append(Spacer(1, 3*mm))

# Product images row - show multiple products
img_row_data = []
for i in [1, 2, 3, 6]:
    img_path = os.path.join(IMAGE_DIR, f'product_{i:02d}.webp')
    if os.path.exists(img_path):
        try:
            pil_img = Image.open(img_path)
            w, h = pil_img.size
            ih = 55*mm
            iw = w * (ih / h)
            pil_img.save(f'row_img_{i}.png', 'PNG')
            img_row_data.append(RLImage(f'row_img_{i}.png', width=iw, height=ih))
            os.remove(f'row_img_{i}.png')
        except Exception as e:
            print(f"Row image {i} error: {e}")

if img_row_data:
    img_table = Table([img_row_data], colWidths=[PAGE_W/len(img_row_data)]*len(img_row_data))
    img_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(img_table)

story.append(PageBreak())

# ---------- 2. DS SERIES ----------
story.append(Paragraph(cn_en('二、DS系列 电子级无尘布', '2. DS Series — Electronic Grade Cleanroom Wiper'), style_h1))

# Material section
story.append(Paragraph(cn_en('材质 / Material', 'Material'), style_h2))
story.append(Paragraph(
    cn_en('涤纶 + 锦纶针织布', 'Polyester + Nylon Knitted'), style_body
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph(cn_en('洁净度 / Cleanliness', 'Cleanliness'), style_h2))
story.append(Paragraph(cn_en('Class 100~1000（百级~千级无尘室适用）', 'Class 100~1000'), style_body))
story.append(Spacer(1, 2*mm))

story.append(Paragraph(cn_en('切割方式 / Cut Method', 'Cut Method'), style_h2))
story.append(Paragraph(
    cn_en(
        '▪ 激光切割（标准，封边效果好，掉屑少）<br/>'
        '▪ 超声波切割（可选）<br/>'
        '▪ 冷裁（低成本选项，需确认）',
        '▪ Laser Cut (Standard, good edge sealing)<br/>'
        '▪ Ultrasonic Cut (Optional)<br/>'
        '▪ Cold Cut (Low-cost option, TBD)'
    ), style_body
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph(cn_en('常用颜色 / Standard Colors', 'Standard Colors'), style_h2))
story.append(Paragraph(cn_en('白色 White（标准）| 蓝色 Blue（可选）| 米黄 Ivory（可选）', 'White (Standard) | Blue (Optional) | Ivory (Optional)'), style_body))
story.append(Spacer(1, 3*mm))

# DS Series Spec Table
story.append(Paragraph(cn_en('型号规格表 / Model Specifications', 'Model Specifications'), style_h2))

ds_header = [
    Paragraph('型号<br/>Model', style_header_cell),
    Paragraph('规格(inch)<br/>Size(inch)', style_header_cell),
    Paragraph('规格(cm)<br/>Size(cm)', style_header_cell),
    Paragraph('克重(g/pcs)<br/>Weight(g/pcs)', style_header_cell),
    Paragraph('包装<br/>Packing', style_header_cell),
    Paragraph('洁净度<br/>Cleanliness', style_header_cell),
]

ds_data = [
    ['DS-0404', '4\"×4\"', '10×10 cm', '~0.12', '100片/包', 'Class 100~1000'],
    ['DS-0606', '6\"×6\"', '15×15 cm', '0.25', '100片/包', 'Class 100~1000'],
    ['DS-0909', '9\"×9\"', '22.5×22.5 cm', '0.45', '100片/包', 'Class 100~1000'],
    ['DS-1212', '12\"×12\"', '30×30 cm', '0.70', '100片/包', 'Class 100~1000'],
    ['DS-1818', '18\"×18\"', '45×45 cm', '1.85', '100片/包', 'Class 100~1000'],
]

ds_rows = [ds_header]
for row in ds_data:
    ds_rows.append([Paragraph(cell, style_cell) for cell in row])

col_widths = [55, 50, 55, 45, 50, 55]
col_widths = [w / sum(col_widths) * PAGE_W for w in col_widths]

ds_table = Table(ds_rows, colWidths=col_widths, repeatRows=1)
ds_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#1a3a5c')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME', (0,0), (-1,-1), FONT_NAME_CN),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('BACKGROUND', (0,1), (-1,-1), HexColor('#f5f8fc')),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#f5f8fc'), white]),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(ds_table)

# Image for DS series
img_path = os.path.join(IMAGE_DIR, 'product_04.webp')
if os.path.exists(img_path):
    try:
        pil_img = Image.open(img_path)
        w, h = pil_img.size
        ih = 60*mm
        iw = w * (ih / h)
        pil_img.save('row_img_1.png', 'PNG')
        story.append(Spacer(1, 3*mm))
        story.append(RLImage('row_img_1.png', width=iw, height=ih))
        os.remove('row_img_1.png')
    except Exception as e:
        print(f"DS image error: {e}")

story.append(PageBreak())

# ---------- 3. KH SERIES ----------
story.append(Paragraph(cn_en('三、KH系列 工业擦拭布', '3. KH Series — Industrial Wipes'), style_h1))

story.append(Paragraph(cn_en('材质 / Material', 'Material'), style_h2))
story.append(Paragraph(
    cn_en('涤纶针织布（非无尘室级别，适用于一般工业擦拭）',
          'Polyester Knitted (Non-cleanroom grade, for general industrial wiping)'), style_body
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph(cn_en('级别 / Grade', 'Grade'), style_h2))
story.append(Paragraph(
    cn_en('工业级（非电子级，洁净度无Class要求）',
          'Industrial Grade (Non-electronic grade, no cleanliness class requirement)'), style_body
))
story.append(Spacer(1, 3*mm))

# KH Series Spec Table
kh_header = [
    Paragraph('型号<br/>Model', style_header_cell),
    Paragraph('规格(inch)<br/>Size(inch)', style_header_cell),
    Paragraph('规格(cm)<br/>Size(cm)', style_header_cell),
    Paragraph('克重(g/pcs)<br/>Weight(g/pcs)', style_header_cell),
    Paragraph('包装<br/>Packing', style_header_cell),
]

kh_data = [
    ['KH-0606', '6\"×6\"', '15×15 cm', '待确认 TBD', '100片/包'],
    ['KH-0909', '9\"×9\"', '22.5×22.5 cm', '待确认 TBD', '100片/包'],
    ['KH-1212', '12\"×12\"', '30×30 cm', '待确认 TBD', '100片/包'],
]

kh_rows = [kh_header]
for row in kh_data:
    kh_rows.append([Paragraph(cell, style_cell) for cell in row])

kh_col_widths = [55, 55, 55, 55, 60]
kh_col_widths = [w / sum(kh_col_widths) * PAGE_W for w in kh_col_widths]

kh_table = Table(kh_rows, colWidths=kh_col_widths, repeatRows=1)
kh_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#2b5a8c')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('BACKGROUND', (0,1), (-1,-1), HexColor('#f0f4f8')),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(kh_table)
story.append(Spacer(1, 2*mm))

story.append(Paragraph(
    cn_en('⚠ 克重数据待工厂确认 / Weight data TBD from factory', '⚠ Weight data pending factory confirmation'),
    style_body
))

# KH Series image
for i in [5]:
    img_path = os.path.join(IMAGE_DIR, f'product_{i:02d}.webp')
    if os.path.exists(img_path):
        try:
            pil_img = Image.open(img_path)
            w, h = pil_img.size
            ih = 55*mm
            iw = w * (ih / h)
            pil_img.save('row_img_2.png', 'PNG')
            story.append(Spacer(1, 3*mm))
            story.append(RLImage('row_img_2.png', width=iw, height=ih))
            os.remove('row_img_2.png')
        except Exception as e:
            print(f"KH image error: {e}")
            break

story.append(PageBreak())

# ---------- 4. PACKAGING ----------
story.append(Paragraph(cn_en('四、包装方式', '4. Packaging Options'), style_h1))

pkg_header = [Paragraph(cn_en('包装形式', 'Packaging Type'), style_header_cell),
              Paragraph(cn_en('说明', 'Description'), style_header_cell)]
pkg_data = [
    [cn_en('普通袋装', 'Poly Bag'), cn_en('100片/包，标准包装', '100 pcs/pack, standard')],
    [cn_en('真空包装', 'Vacuum Pack'), cn_en('适用于对洁净度要求高的客户', 'For high cleanliness requirements')],
    [cn_en('双层包装', 'Double Bagged'), cn_en('适用于Class 100~1000环境', 'For Class 100~1000 environment')],
    [cn_en('散装', 'Bulk Pack'), cn_en('工业级擦拭布，低成本选项', 'Industrial grade, low-cost option')],
]

pkg_rows = [pkg_header] + [[Paragraph(c[0], style_cell), Paragraph(c[1], style_cell)] for c in pkg_data]
pkg_col_w = [PAGE_W*0.35, PAGE_W*0.65]
pkg_table = Table(pkg_rows, colWidths=pkg_col_w, repeatRows=1)
pkg_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#1a3a5c')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#f5f8fc'), white]),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(pkg_table)
story.append(Spacer(1, 5*mm))

# ---------- 5. CUSTOMIZATION ----------
story.append(Paragraph(cn_en('五、定制选项', '5. Customization Options'), style_h1))

cust_header = [Paragraph(cn_en('项目', 'Item'), style_header_cell),
               Paragraph(cn_en('说明', 'Description'), style_header_cell)]
cust_data = [
    [cn_en('尺寸', 'Dimensions'), cn_en('可按客户要求定制任意尺寸', 'Custom sizes available upon request')],
    [cn_en('包装', 'Packaging'), cn_en('可定制包装数量和方式', 'Custom packing quantity and method')],
    [cn_en('LOGO印刷', 'LOGO Printing'), cn_en('可印制客户品牌LOGO于包装袋', 'Custom LOGO printing on packaging')],
    [cn_en('切割方式', 'Cut Method'), cn_en('激光/超声波/冷裁可选', 'Laser/Ultrasonic/Cold Cut optional')],
]

cust_rows = [cust_header] + [[Paragraph(c[0], style_cell), Paragraph(c[1], style_cell)] for c in cust_data]
cust_table = Table(cust_rows, colWidths=pkg_col_w, repeatRows=1)
cust_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#1a3a5c')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#f5f8fc'), white]),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(cust_table)
story.append(Spacer(1, 5*mm))

# ---------- 6. CERTIFICATION ----------
story.append(Paragraph(cn_en('六、认证与质量', '6. Certifications & Quality'), style_h1))

cert_header = [Paragraph(cn_en('认证', 'Certification'), style_header_cell),
               Paragraph(cn_en('状态', 'Status'), style_header_cell),
               Paragraph(cn_en('备注', 'Remarks'), style_header_cell)]
cert_data = [
    ['ISO', cn_en('❌ 暂无', 'Not yet'),
     cn_en('需确认工厂是否可配合', 'Check with factory')],
    ['SGS', cn_en('❌ 暂无', 'Not yet'),
     cn_en('可安排第三方检测', 'Third-party testing available')],
    ['RoHS', cn_en('❌ 暂无', 'Not yet'),
     cn_en('出口欧盟建议获取', 'Recommended for EU export')],
]

cert_rows = [cert_header] + [[Paragraph(c[0], style_cell), Paragraph(c[1], style_cell), Paragraph(c[2], style_cell)] for c in cert_data]
cert_col_w = [PAGE_W*0.2, PAGE_W*0.3, PAGE_W*0.5]
cert_table = Table(cert_rows, colWidths=cert_col_w, repeatRows=1)
cert_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#1a3a5c')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#f5f8fc'), white]),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(cert_table)
story.append(Spacer(1, 3*mm))

story.append(Paragraph(
    cn_en(
        '产品优势 / Product Advantages：',
        'Product Advantages:'
    ), style_h2
))
story.append(Paragraph(
    cn_en(
        '▪ 源洁工厂直供，中间商底价，具备市场竞争力<br/>'
        '▪ 双面针织结构，发尘量低，适用于Class 100~1000无尘环境<br/>'
        '▪ 激光切割封边，减少掉毛掉屑<br/>'
        '▪ 尺寸、包装、LOGO均可定制',
        '▪ Factory-direct supply, competitive pricing<br/>'
        '▪ Double-sided knitted structure, low particle emission<br/>'
        '▪ Laser-cut sealed edges, reduced linting<br/>'
        '▪ Flexible customization: size, packaging, LOGO'
    ), style_body
))

story.append(PageBreak())

# ---------- 7. CONTACT ----------
story.append(Paragraph(cn_en('七、联系方式', '7. Contact Us'), style_h1))
story.append(Spacer(1, 5*mm))

story.append(Paragraph(cn_en('源洁无尘布（无锡）工厂', 'Wuxi Yuanjie Cleanroom Products'), style_h2))
story.append(Spacer(1, 3*mm))

contact_lines = [
    (cn_en('地址：[请填写]', 'Address: [Please fill in]')),
    (cn_en('电话：[请填写]', 'Tel: [Please fill in]')),
    (cn_en('邮箱：[请填写]', 'Email: [Please fill in]')),
    (cn_en('网站：[请填写]', 'Website: [Please fill in]')),
    '',
    (cn_en('目标市场 / Target Markets：', 'Target Markets:')),
    (cn_en('🇹🇷 土耳其 DS系列 6"×6", 9"×9"', 'Turkey - DS Series 6\"×6\", 9\"×9\"')),
    (cn_en('🇦🇪 中东（UAE/沙特）DS系列 6"×6", 9"×9"', 'Middle East - DS Series 6\"×6\", 9\"×9\"')),
    (cn_en('🇵🇱 东欧（波兰/捷克）DS+KH系列 9"×9", 12"×12"', 'Eastern Europe - DS+KH Series')),
    (cn_en('🇷🇺 俄罗斯/独联体 KH系列 6"×6", 9"×9"', 'Russia/CIS - KH Series')),
]
for line in contact_lines:
    if line:
        story.append(Paragraph(line, style_body))
        story.append(Spacer(1, 1*mm))
    else:
        story.append(Spacer(1, 3*mm))

story.append(Spacer(1, 8*mm))
story.append(Paragraph(
    cn_en(
        '* 本目录所有规格参数仅供参考，以实际产品为准。',
        '* All specifications are for reference only, subject to actual products.'
    ), style_footer
))
story.append(Paragraph(
    cn_en(
        '版本 V1.0 | 创建日期：2026-07-03',
        'Version V1.0 | Created: 2026-07-03'
    ), style_footer
))

# ============================================================
# 5. Build PDF
# ============================================================
print('Building PDF...')
doc.build(story)
print(f'PDF generated: {OUTPUT_FILE}')
print(f'File size: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB')
