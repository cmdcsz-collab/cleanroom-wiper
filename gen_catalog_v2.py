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

OUTPUT = "wiper_catalog_v2.pdf"
doc = SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=15*mm, bottomMargin=15*mm, leftMargin=15*mm, rightMargin=15*mm)
PW = A4[0] - 30*mm
WKDIR = os.path.dirname(os.path.abspath(__file__))

def ms(fn, sz, ld, al=TA_LEFT, cl=HexColor("#333"), be=0, af=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld, alignment=al, textColor=cl, spaceBefore=be, spaceAfter=af)

st = ms(FONT_CN, 22, 30, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
se = ms("Helvetica", 16, 22, TA_CENTER, HexColor("#555"), 0, 6*mm)
sh1 = ms(FONT_CN, 16, 22, TA_LEFT, HexColor("#1a3a5c"), 5*mm, 3*mm)
sh2 = ms(FONT_CN, 12, 17, TA_LEFT, HexColor("#2b5a8c"), 3*mm, 2*mm)
sb = ms(FONT_CN, 9.5, 14, TA_LEFT, HexColor("#333"), 0, 1.5*mm)
sc = ms(FONT_CN, 8, 11, TA_CENTER)
shc = ms(FONT_CN, 8.5, 12, TA_CENTER, white)
sf = ms(FONT_CN, 8, 11, TA_CENTER, HexColor("#888"))

def load_img(path, mh=60*mm):
    full = os.path.join(WKDIR, path)
    if not os.path.exists(full): return None
    try:
        pil = Image.open(full)
        if pil.mode != "RGB": pil = pil.convert("RGB")
        w, h = pil.size
        ih = min(h, mh)
        iw = w * (ih / h)
        buf = io.BytesIO()
        pil.save(buf, format="PNG")
        buf.seek(0)
        return RLImage(buf, width=iw, height=ih)
    except:
        return None

def mt(hd, data, cwp, hc="#1a3a5c"):
    cw = [w / sum(cwp) * PW for w in cwp]
    rows = [[Paragraph(h, shc) for h in hd]]
    for row in data:
        rows.append([Paragraph(c, sc) for c in row])
    t = Table(rows, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),HexColor(hc)),
        ("TEXTCOLOR",(0,0),(-1,0),white),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("GRID",(0,0),(-1,-1),0.5,HexColor("#ccc")),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    return t

story = []

# COVER
story.append(Spacer(1, 25*mm))
story.append(Paragraph("Cleanroom Wiper & Industrial Wipe Catalog", st))
story.append(Paragraph("Product Catalog", se))
story.append(Spacer(1, 8*mm))
ci = load_img("product_07.webp", 110*mm)
if ci: story.append(ci); story.append(Spacer(1, 5*mm))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("<b>Supplier:</b> Wuxi Yuanjie Cleanroom Products (Yuanjie)", sb))
story.append(Paragraph("<b>Version:</b> V1.0 | <b>Date:</b> July 2026", sb))
story.append(PageBreak())

# COMPANY
story.append(Paragraph("<b>1. Company Profile</b>", sh1))
story.append(Paragraph("Wuxi Yuanjie Cleanroom Products is a professional manufacturer of cleanroom wipers and industrial wipes based in Wuxi, Jiangsu, China. We supply high-quality cleaning solutions for the electronics, semiconductor, automotive, and pharmaceutical industries.", sb))
story.append(Spacer(1, 3*mm))
imgs = []
for i in [1,2,3,6]:
    img = load_img(f"product_{i:02d}.webp", 48*mm)
    if img: imgs.append(img)
if imgs:
    cw_imgs = [PW/len(imgs)]*len(imgs)
    t = Table([imgs], colWidths=cw_imgs)
    t.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
    story.append(t)
story.append(PageBreak())

# DS SERIES
story.append(Paragraph("<b>2. DS Series - Electronic Grade</b>", sh1))
story.append(Paragraph("Material: Polyester + Nylon Knitted | Cleanliness: Class 100~1000", sb))
story.append(Paragraph("Cut Method: Laser Cut (Standard) / Ultrasonic Cut / Cold Cut", sb))
story.append(Paragraph("Standard Colors: White, Blue, Ivory", sb))
story.append(Spacer(1, 2*mm))
ds_h = ["Model","Inch","cm","W(g)","Packing","Class"]
ds_d = [["DS-0404","4x4","10x10","0.12","100/pk","C100-1000"],
        ["DS-0606","6x6","15x15","0.25","100/pk","C100-1000"],
        ["DS-0909","9x9","22.5x22.5","0.45","100/pk","C100-1000"],
        ["DS-1212","12x12","30x30","0.70","100/pk","C100-1000"],
        ["DS-1818","18x18","45x45","1.85","100/pk","C100-1000"]]
story.append(mt(ds_h, ds_d, [50,40,40,35,50,50]))
dsi = load_img("product_04.webp", 50*mm)
if dsi: story.append(Spacer(1,3*mm)); story.append(dsi)
story.append(PageBreak())

# KH SERIES
story.append(Paragraph("<b>3. KH Series - Industrial Wipes</b>", sh1))
story.append(Paragraph("Material: Polyester Knitted (Non-cleanroom grade)", sb))
story.append(Paragraph("Grade: Industrial | Applications: General industrial cleaning, workshops", sb))
kh_h = ["Model","Inch","cm","W(g)","Packing"]
kh_d = [["KH-0606","6x6","15x15","TBD","100/pk"],
        ["KH-0909","9x9","22.5x22.5","TBD","100/pk"],
        ["KH-1212","12x12","30x30","TBD","100/pk"]]
story.append(mt(kh_h, kh_d, [55,45,45,45,55], "#2b5a8c"))
story.append(Paragraph("<b>Note:</b> KH weight data pending factory confirmation.", sb))
khi = load_img("product_05.webp", 50*mm)
if khi: story.append(Spacer(1,3*mm)); story.append(khi)
story.append(PageBreak())

# PACKAGING
story.append(Paragraph("<b>4. Packaging Options</b>", sh1))
pkg_d = [["Poly Bag","100 pcs/pack, standard packaging"],
         ["Vacuum Pack","For high-cleanliness requirements"],
         ["Double Bagged","For Class 100~1000 environments"],
         ["Bulk Pack","Industrial grade, cost-effective"]]
story.append(mt(["Type","Description"], pkg_d, [40,60]))
story.append(Spacer(1,3*mm))

story.append(Paragraph("<b>5. Customization</b>", sh1))
cust_d = [["Dimensions","Custom sizes available"],
          ["Packaging","Custom pack quantity and method"],
          ["LOGO Printing","Brand LOGO on packaging bags"],
          ["Cut Method","Laser / Ultrasonic / Cold Cut"]]
story.append(mt(["Item","Description"], cust_d, [40,60]))
story.append(Spacer(1,3*mm))

# CERTIFICATIONS
story.append(Paragraph("<b>6. Certifications & Quality</b>", sh1))
cert_d = [["ISO","Not yet","TBC with factory"],
          ["SGS","Not yet","Third-party testing available"],
          ["RoHS","Not yet","Recommended for EU export"]]
story.append(mt(["Certification","Status","Remarks"], cert_d, [25,25,50]))
story.append(Spacer(1,3*mm))
story.append(Paragraph("Product Advantages:", sh2))
story.append(Paragraph("- Factory-direct pricing, competitive for target markets", sb))
story.append(Paragraph("- Double-sided knitted structure, low particle emission", sb))
story.append(Paragraph("- Laser-cut sealed edges, reduced linting", sb))
story.append(Paragraph("- Flexible customization: size, packaging, LOGO", sb))
story.append(PageBreak())

# CONTACT
story.append(Paragraph("<b>7. Contact Information</b>", sh1))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("<b>Wuxi Yuanjie Cleanroom Products</b>", sh2))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Please fill in your contact details below:</b>", sb))
story.append(Paragraph("", sb))
story.append(Paragraph("Address: [___________________________]", sb))
story.append(Paragraph("Phone:   [___________________________]", sb))
story.append(Paragraph("Email:   [___________________________]", sb))
story.append(Paragraph("Website: [___________________________]", sb))
story.append(Paragraph("WhatsApp: [__________________________]", sb))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("<b>Target Markets</b>", sh2))
story.append(Paragraph("- Turkey: DS Series 6x6, 9x9 inch", sb))
story.append(Paragraph("- Middle East (UAE/Saudi): DS Series 6x6, 9x9 inch", sb))
story.append(Paragraph("- Eastern Europe (Poland/Czech): DS + KH Series", sb))
story.append(Paragraph("- Russia/CIS: KH Series industrial wipes", sb))
story.append(Paragraph("- Other markets: Contact us for inquiries", sb))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("* All specifications are for reference only, subject to actual products.", sf))
story.append(Paragraph("Version V1.0 | Created: 2026-07-03 | Updated: 2026-07-05", sf))

print("Building PDF...")
doc.build(story)
sz = os.path.getsize(OUTPUT)
print(f"OK: {OUTPUT} ({sz//1024} KB)")