#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

FONT_CN = "MicrosoftYaHei"
try:
    pdfmetrics.registerFont(TTFont(FONT_CN, "C:/Windows/Fonts/msyh.ttc"))
except:
    FONT_CN = "Helvetica"

OUTPUT = "无尘布产品目录_Cleanroom_Wiper_Catalog.pdf"
doc = SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=15*mm, bottomMargin=15*mm, leftMargin=15*mm, rightMargin=15*mm)
PW = A4[0] - 30*mm

def cn_en(cn, en):
    return "<b>" + cn + "</b><br/><font size=\"-1\">" + en + "</font>"

def ms(fn, sz, ld, al=TA_LEFT, cl=HexColor("#333"), be=0, af=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld, alignment=al, textColor=cl, spaceBefore=be, spaceAfter=af)

st = ms(FONT_CN, 22, 30, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
set_ = ms("Helvetica", 16, 22, TA_CENTER, HexColor("#555"), 0, 6*mm)
sh1 = ms(FONT_CN, 16, 22, TA_LEFT, HexColor("#1a3a5c"), 5*mm, 3*mm)
sh2 = ms(FONT_CN, 12, 17, TA_LEFT, HexColor("#2b5a8c"), 3*mm, 2*mm)
sb = ms(FONT_CN, 9.5, 14, TA_LEFT, HexColor("#333"), 0, 1.5*mm)
sc = ms(FONT_CN, 8, 11, TA_CENTER)
shc = ms(FONT_CN, 8.5, 12, TA_CENTER, white)
sf = ms(FONT_CN, 8, 11, TA_CENTER, HexColor("#888"))

def load_img(path, mh=60*mm):
    if not os.path.exists(path): return None
    try:
        pil = Image.open(path)
        if pil.mode != "RGB": pil = pil.convert("RGB")
        w, h = pil.size
        ih = min(h, mh)
        iw = w * (ih / h)
        buf = io.BytesIO()
        pil.save(buf, format="PNG")
        buf.seek(0)
        return RLImage(buf, width=iw, height=ih)
    except Exception as e:
        print(f"Image error {path}: {e}")
        return None

def mt(hd, data, cwp, hc="#1a3a5c"):
    cw = [w / sum(cwp) * PW for w in cwp]
    rows = [[Paragraph(h, shc) for h in hd]]
    for row in data:
        rows.append([Paragraph(c, sc) for c in row])
    t = Table(rows, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),HexColor(hc)),("TEXTCOLOR",(0,0),(-1,0),white),("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("GRID",(0,0),(-1,-1),0.5,HexColor("#ccc")),("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    return t

story = []

# COVER
story.append(Spacer(1, 25*mm))
story.append(Paragraph("无尘擦拭布 · 产品目录", st))
story.append(Paragraph("Cleanroom Wiper · Product Catalog", set_))
story.append(Spacer(1, 8*mm))
ci = load_img("product_07.webp", 110*mm)
if ci: story.append(ci); story.append(Spacer(1, 5*mm))
story.append(Spacer(1, 8*mm))
story.append(Paragraph(cn_en("供应商：源洁无尘布（无锡）工厂", "Supplier: Wuxi Yuanjie Cleanroom Products"), sb))
story.append(Paragraph(cn_en("版本：V1.0 | 日期：2026年7月", "Version: V1.0 | Date: July 2026"), sb))
story.append(PageBreak())

# 1. Company
story.append(Paragraph(cn_en("一、公司简介", "1. Company Profile"), sh1))
story.append(Paragraph(cn_en("源洁无尘布（无锡）工厂是一家专业生产无尘擦拭布的企业。", "Wuxi Yuanjie Cleanroom Products is a professional manufacturer."), sb))
story.append(Spacer(1, 3*mm))
imgs = []
for i in [1,2,3,6]:
    img = load_img(f"product_{i:02d}.webp", 48*mm)
    if img: imgs.append(img)
if imgs:
    cw = [PW/len(imgs)]*len(imgs)
    t = Table([imgs], colWidths=cw)
    t.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
    story.append(t)
story.append(PageBreak())

# 2. DS Series
story.append(Paragraph(cn_en("二、DS系列 电子级无尘布", "2. DS Series - Electronic Grade"), sh1))
story.append(Paragraph(cn_en("材质：涤纶 + 锦纶针织布 | 洁净度：Class 100~1000", "Material: Polyester + Nylon Knitted | Cleanliness: Class 100~1000"), sb))
story.append(Paragraph(cn_en("切割方式：激光切割（标准）/ 超声波切割 / 冷裁", "Cut: Laser (Std) / Ultrasonic / Cold"), sb))
story.append(Spacer(1, 2*mm))
ds_h = ["Model", "Inch", "cm", "W(g)", "Packing", "Class"]
ds_d = [["DS-0404","4x4","10x10","0.12","100/pk","C100-1000"],["DS-0606","6x6","15x15","0.25","100/pk","C100-1000"],["DS-0909","9x9","22.5x22.5","0.45","100/pk","C100-1000"],["DS-1212","12x12","30x30","0.70","100/pk","C100-1000"],["DS-1818","18x18","45x45","1.85","100/pk","C100-1000"]]
story.append(mt(ds_h, ds_d, [50,40,40,35,50,50]))
dsi = load_img("product_04.webp", 50*mm)
if dsi: story.append(Spacer(1,3*mm)); story.append(dsi)
story.append(PageBreak())

# 3. KH Series
story.append(Paragraph(cn_en("三、KH系列 工业擦拭布", "3. KH Series - Industrial Wipes"), sh1))
story.append(Paragraph(cn_en("材质：涤纶针织布（非无尘室级别）", "Material: Polyester Knitted (Non-cleanroom)"), sb))
story.append(Paragraph(cn_en("级别：工业级", "Grade: Industrial"), sb))
kh_h = ["Model", "Inch", "cm", "W(g)", "Packing"]
kh_d = [["KH-0606","6x6","15x15","TBD","100/pk"],["KH-0909","9x9","22.5x22.5","TBD","100/pk"],["KH-1212","12x12","30x30","TBD","100/pk"]]
story.append(mt(kh_h, kh_d, [55,45,45,45,55], "#2b5a8c"))
story.append(Paragraph(cn_en("⚠ 克重数据待确认", "⚠ Weight TBD"), sb))
khi = load_img("product_05.webp", 50*mm)
if khi: story.append(Spacer(1,3*mm)); story.append(khi)
story.append(PageBreak())

# 4. Packaging
story.append(Paragraph(cn_en("四、包装方式", "4. Packaging"), sh1))
pkg_d = [[cn_en("普通袋装", "Poly Bag"),cn_en("100片/包", "100/pk")],[cn_en("真空包装", "Vacuum"),cn_en("高洁净度", "High clean")],[cn_en("双层包装", "Double Bag"),cn_en("Class100~1000", "C100-1000")],[cn_en("散装", "Bulk"),cn_en("低成本", "Low cost")]]
story.append(mt([cn_en("形式","Type"),cn_en("说明","Desc")], pkg_d, [40,60]))
story.append(Spacer(1,3*mm))

# 5. Customization
story.append(Paragraph(cn_en("五、定制选项", "5. Customization"), sh1))
cust_d = [[cn_en("尺寸","Size"),cn_en("定制任意尺寸","Custom")],[cn_en("包装","Pkg"),cn_en("数量方式定制","Custom pkg")],[cn_en("LOGO","LOGO"),cn_en("品牌LOGO印刷","Brand LOGO")],[cn_en("切割","Cut"),cn_en("激光/超声波/冷裁","Laser/U-sonic/Cold")]]
story.append(mt([cn_en("项目","Item"),cn_en("说明","Desc")], cust_d, [40,60]))
story.append(Spacer(1,3*mm))

# 6. Cert
story.append(Paragraph(cn_en("六、认证与优势", "6. Certifications"), sh1))
cert_d = [["ISO",cn_en("暂无","No"),cn_en("待确认","TBC")],["SGS",cn_en("暂无","No"),cn_en("可安排","Avail")],["RoHS",cn_en("暂无","No"),cn_en("建议","Rec")]]
story.append(mt([cn_en("认证","Cert"),cn_en("状态","Status"),cn_en("备注","Note")], cert_d, [25,25,50]))
story.append(Spacer(1,3*mm))
story.append(Paragraph(cn_en("工厂直供 · 低发尘 · 激光封边 · 灵活定制", "Direct supply · Low particle · Laser seal · Custom"), sb))
story.append(PageBreak())

# 7. Contact
story.append(Paragraph(cn_en("七、联系方式", "7. Contact"), sh1))
story.append(Spacer(1,3*mm))
story.append(Paragraph(cn_en("源洁无尘布（无锡）工厂", "Wuxi Yuanjie Cleanroom Products"), sh2))
for c in [cn_en("地址：[填写]","Addr: [fill]"),cn_en("电话：[填写]","Tel: [fill]"),cn_en("邮箱：[填写]","Email: [fill]")]:
    story.append(Paragraph(c, sb)); story.append(Spacer(1,1*mm))
story.append(Spacer(1,3*mm))
story.append(Paragraph("Target Markets", sh2))
for m in [cn_en("Turkey: DS","Turkey: DS"),cn_en("Middle East: DS","M.East: DS"),cn_en("E.Europe: DS+KH","E.Eur: DS+KH"),cn_en("Russia: KH","Russia: KH")]:
    story.append(Paragraph(m, sb)); story.append(Spacer(1,1*mm))
story.append(Spacer(1,8*mm))
story.append(Paragraph(cn_en("* 仅供参考","* For reference"), sf))
story.append(Paragraph("V1.0 | 2026-07-03", sf))

print("Building PDF...")
doc.build(story)
sz = os.path.getsize(OUTPUT)
print(f"OK: {OUTPUT} ({sz//1024} KB)")
