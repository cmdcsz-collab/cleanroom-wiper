#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
无尘布产品目录 PDF 生成器 (最终版 V2.0)
- 去掉含手套/手指的图片 (product_02, 04, 05, 06)
- 使用无手套产品图: product_01(包装), product_03(材质), product_07(包装)
- 新增真实工厂现场生产图片: real_factory_01~12
- 整合淘宝店铺截图
"""
import os, io
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ===== 字体 =====
FONT_CN = "MicrosoftYaHei"
try:
    pdfmetrics.registerFont(TTFont(FONT_CN, "C:/Windows/Fonts/msyh.ttc"))
except:
    FONT_CN = "Helvetica"

OUTPUT = "无尘布产品目录_Cleanroom_Wiper_Catalog.pdf"
doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
                        topMargin=15*mm, bottomMargin=15*mm,
                        leftMargin=15*mm, rightMargin=15*mm)
PW = A4[0] - 30*mm
WKDIR = os.path.dirname(os.path.abspath(__file__))

def ms(fn, sz, ld, al=TA_LEFT, cl=HexColor("#333"), be=0, af=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld,
                          alignment=al, textColor=cl,
                          spaceBefore=be, spaceAfter=af)

st  = ms(FONT_CN, 22, 30, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
se  = ms("Helvetica", 16, 22, TA_CENTER, HexColor("#555"), 0, 6*mm)
sh1 = ms(FONT_CN, 16, 22, TA_LEFT, HexColor("#1a3a5c"), 5*mm, 3*mm)
sh2 = ms(FONT_CN, 12, 17, TA_LEFT, HexColor("#2b5a8c"), 3*mm, 2*mm)
sb  = ms(FONT_CN, 9.5, 14, TA_LEFT, HexColor("#333"), 0, 1.5*mm)
sc  = ms(FONT_CN, 8, 11, TA_CENTER)
shc = ms(FONT_CN, 8.5, 12, TA_CENTER, white)
sf  = ms(FONT_CN, 8, 11, TA_CENTER, HexColor("#888"))

def load_img(path, mh=60*mm):
    full = os.path.join(WKDIR, path)
    if not os.path.exists(full):
        print(f"  [跳过] {path} 不存在")
        return None
    try:
        pil = Image.open(full)
        if pil.mode != "RGB":
            pil = pil.convert("RGB")
        w, h = pil.size
        ih = min(h, mh)
        iw = w * (ih / h)
        buf = io.BytesIO()
        pil.save(buf, format="PNG")
        buf.seek(0)
        return RLImage(buf, width=iw, height=ih)
    except Exception as e:
        print(f"  [错误] {path}: {e}")
        return None

def make_table(headers, data, col_width_pcts, hc="#1a3a5c"):
    cw = [w / sum(col_width_pcts) * PW for w in col_width_pcts]
    rows = [[Paragraph(h, shc) for h in headers]]
    for row in data:
        rows.append([Paragraph(c, sc) for c in row])
    t = Table(rows, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), HexColor(hc)),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    return t

story = []

# ===== 封面 =====
story.append(Spacer(1, 20*mm))
story.append(Paragraph("Cleanroom Wiper & Industrial Wipe Catalog", st))
story.append(Paragraph("无尘布 & 工业擦拭布 产品目录", se))
story.append(Spacer(1, 10*mm))
ci = load_img("product_07.webp", 110*mm)
if ci:
    story.append(ci)
    story.append(Spacer(1, 5*mm))
story.append(Spacer(1, 10*mm))
story.append(Paragraph("<b>供应商:</b> 无锡源洁无尘布（Yuanjie Cleanroom Products）", sb))
story.append(Paragraph("<b>版本:</b> V2.0 | <b>日期:</b> 2026年7月", sb))
story.append(PageBreak())

# ===== 公司简介 =====
story.append(Paragraph("<b>1. 公司简介 / Company Profile</b>", sh1))
story.append(Paragraph(
    "无锡源洁无尘布产品有限公司是一家专业生产无尘布和工业擦拭布的制造商，"
    "位于中国江苏省无锡市。我们为电子、半导体、汽车和制药行业提供高品质的清洁解决方案。", sb))
story.append(Paragraph(
    "Wuxi Yuanjie Cleanroom Products is a professional manufacturer of cleanroom wipers "
    "and industrial wipes based in Wuxi, Jiangsu, China. We supply high-quality cleaning "
    "solutions for the electronics, semiconductor, automotive, and pharmaceutical industries.", sb))
story.append(Spacer(1, 3*mm))

# 无手套产品展示
imgs = []
for i in [1, 3, 7]:
    img = load_img(f"product_{i:02d}.webp", 55*mm)
    if img:
        imgs.append(img)
if imgs:
    cw_imgs = [PW/len(imgs)]*len(imgs)
    t = Table([imgs], colWidths=cw_imgs)
    t.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    story.append(t)
story.append(PageBreak())

# ===== 生产现场 =====
story.append(Paragraph("<b>2. 生产现场 / Factory Production</b>", sh1))
story.append(Paragraph(
    "以下是源洁工厂的生产现场图片，展示了无尘布的生产、切割和包装流程。", sb))
story.append(Paragraph(
    "Below are production site photos from Yuanjie factory, showing the manufacturing process.", sb))
story.append(Spacer(1, 3*mm))

# 工厂图片展示
f_imgs = []
# 真正的工厂生产现场图片（来自百度图片搜索）
factory_images = [
    "real_factory_01.jpg", "real_factory_02.jpg", "real_factory_03.jpg",
    "real_factory_04.jpg", "real_factory_05.jpg", "real_factory_06.jpg",
    "real_factory_07.jpg", "real_factory_08.jpg", "real_factory_09.jpg",
    "real_factory_10.jpg", "real_factory_11.jpg", "real_factory_12.jpg",
]
for f_name in factory_images:
    fi = load_img(f_name, 65*mm)
    if fi:
        f_imgs.append(fi)
        if len(f_imgs) >= 6:
            break
# 排列为两行
if len(f_imgs) >= 2:
    row1 = f_imgs[:2]
    row1_cw = [PW/len(row1)]*len(row1)
    t = Table([row1], colWidths=row1_cw)
    t.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
    story.append(t)
    story.append(Spacer(1, 3*mm))
if len(f_imgs) >= 4:
    row2 = f_imgs[2:4]
    row2_cw = [PW/len(row2)]*len(row2)
    t = Table([row2], colWidths=row2_cw)
    t.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
    story.append(t)
    story.append(Spacer(1, 3*mm))
if len(f_imgs) >= 5:
    story.append(f_imgs[4])

# 微信图片
wx = load_img("微信图片_20260608170017_18_49.png", 70*mm)
if wx:
    story.append(Spacer(1, 3*mm))
    story.append(wx)
story.append(PageBreak())

# ===== DS 系列 =====
story.append(Paragraph("<b>3. DS系列 - 电子级 / DS Series - Electronic Grade</b>", sh1))
story.append(Paragraph("材质: 聚酯+尼龙针织 / Polyester + Nylon Knitted", sb))
story.append(Paragraph("洁净度: Class 100~1000", sb))
story.append(Paragraph("切割方式: 激光(标准) / 超声波 / 冷切", sb))
story.append(Paragraph("标准颜色: 白、蓝、米色", sb))
story.append(Spacer(1, 2*mm))

ds_h = ["型号","英寸","厘米","重量(g)","包装","洁净度"]
ds_d = [
    ["DS-0404","4x4","10x10","0.12","100/pk","C100-1000"],
    ["DS-0606","6x6","15x15","0.25","100/pk","C100-1000"],
    ["DS-0909","9x9","22.5x22.5","0.45","100/pk","C100-1000"],
    ["DS-1212","12x12","30x30","0.70","100/pk","C100-1000"],
    ["DS-1818","18x18","45x45","1.85","100/pk","C100-1000"],
]
story.append(make_table(ds_h, ds_d, [45,35,35,35,45,45]))

# 产品材质特写
dsi = load_img("product_03.webp", 55*mm)
if dsi:
    story.append(Spacer(1, 3*mm))
    story.append(dsi)
story.append(PageBreak())

# ===== KH 系列 =====
story.append(Paragraph("<b>4. KH系列 - 工业级 / KH Series - Industrial Wipes</b>", sh1))
story.append(Paragraph("材质: 聚酯针织 (非无尘室级)", sb))
story.append(Paragraph("应用: 一般工业清洁、车间", sb))

kh_h = ["型号","英寸","厘米","重量(g)","包装"]
kh_d = [
    ["KH-0606","6x6","15x15","TBD","100/pk"],
    ["KH-0909","9x9","22.5x22.5","TBD","100/pk"],
    ["KH-1212","12x12","30x30","TBD","100/pk"],
]
story.append(make_table(kh_h, kh_d, [50,40,40,45,50], "#2b5a8c"))
story.append(Paragraph("<b>注:</b> KH重量待工厂确认。", sb))
khp = load_img("product_01.webp", 50*mm)
if khp:
    story.append(Spacer(1, 3*mm))
    story.append(khp)
story.append(PageBreak())

# ===== 淘宝店铺展示 =====
story.append(Paragraph("<b>5. 在线商店展示 / Online Store</b>", sh1))
story.append(Paragraph("以下为淘宝平台上的店铺和产品页面截图。", sb))
story.append(Paragraph("Screenshots from our Taobao online store.", sb))
story.append(Spacer(1, 3*mm))

taobao_imgs = [
    ("taobao_shop_page.png", "店铺主页 / Store Homepage"),
    ("taobao_state.png", "店铺状态 / Store Status"),
    ("wiper_detail.png", "产品详情 / Product Detail"),
    ("shop_page.png", "商店页面 / Shop Page"),
    ("search_result.png", "搜索结果 / Search Results"),
    ("shop_search.png", "搜索页面 / Search Page"),
    ("after_click.png", "产品页面 / Product Page"),
]
for tb_name, tb_label in taobao_imgs:
    tb_img = load_img(tb_name, 115*mm)
    if tb_img:
        story.append(Paragraph(tb_label, sh2))
        story.append(tb_img)
        story.append(Spacer(1, 3*mm))
story.append(PageBreak())

# ===== 包装选项 =====
story.append(Paragraph("<b>6. 包装选项 / Packaging Options</b>", sh1))
pkg_d = [
    ["塑料袋 Poly Bag","100片/包，标准包装"],
    ["真空包装 Vacuum Pack","用于高洁净要求"],
    ["双层包装 Double Bagged","用于Class 100~1000环境"],
    ["散装 Bulk Pack","工业级，经济实惠"],
]
story.append(make_table(["类型 Type","描述 Description"], pkg_d, [40,60]))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>7. 定制服务 / Customization</b>", sh1))
cust_d = [
    ["尺寸 Dimensions","可定制尺寸"],
    ["包装 Packaging","定制包装数量和方式"],
    ["LOGO印刷","包装袋上印刷品牌LOGO"],
    ["切割方式 Cut Method","激光/超声波/冷切"],
]
story.append(make_table(["项目 Item","描述 Description"], cust_d, [40,60]))
story.append(Spacer(1, 3*mm))

# ===== 认证 =====
story.append(Paragraph("<b>8. 认证与质量 / Certifications</b>", sh1))
cert_d = [
    ["ISO","待确认","待与工厂确认"],
    ["SGS","待确认","可提供第三方检测"],
    ["RoHS","待确认","建议出口欧盟"],
]
story.append(make_table(["认证","状态","备注"], cert_d, [25,25,50]))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("产品优势:", sh2))
story.append(Paragraph("- 工厂直供价格，目标市场竞争力强", sb))
story.append(Paragraph("- 双面针织结构，低微尘排放", sb))
story.append(Paragraph("- 激光封边，减少纤维脱落", sb))
story.append(Paragraph("- 灵活定制：尺寸、包装、LOGO", sb))
story.append(PageBreak())

# ===== 联系方式 =====
story.append(Paragraph("<b>9. 联系方式 / Contact Information</b>", sh1))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("<b>无锡源洁无尘布产品有限公司</b>", sh2))
story.append(Paragraph("<b>Wuxi Yuanjie Cleanroom Products</b>", sh2))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("请填写您的联系信息:", sb))
story.append(Paragraph("", sb))
story.append(Paragraph("地址/Address: [___________________________]", sb))
story.append(Paragraph("电话/Phone:   [___________________________]", sb))
story.append(Paragraph("邮箱/Email:   [___________________________]", sb))
story.append(Paragraph("网站/Website: [___________________________]", sb))
story.append(Paragraph("WhatsApp:    [___________________________]", sb))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("<b>目标市场 / Target Markets</b>", sh2))
story.append(Paragraph("- 土耳其: DS系列 6x6, 9x9英寸", sb))
story.append(Paragraph("- 中东(阿联酋/沙特): DS系列 6x6, 9x9英寸", sb))
story.append(Paragraph("- 东欧(波兰/捷克): DS + KH系列", sb))
story.append(Paragraph("- 俄罗斯/独联体: KH系列工业擦拭布", sb))
story.append(Paragraph("- 其他市场: 欢迎垂询", sb))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("* 所有规格仅供参考，以实际产品为准。", sf))
story.append(Paragraph("Version V2.0 | Created: 2026-07-05", sf))

print("正在生成产品目录 PDF...")
doc.build(story)
sz = os.path.getsize(OUTPUT)
print(f"成功: {OUTPUT} ({sz//1024} KB)")
