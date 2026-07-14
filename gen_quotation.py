#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_CN = "MicrosoftYaHei"
for fp in ["C:/Windows/Fonts/msyh.ttc","C:/Windows/Fonts/simhei.ttf","C:/Windows/Fonts/simsun.ttc"]:
    try:
        if os.path.exists(fp):
            pdfmetrics.registerFont(TTFont(FONT_CN, fp))
            break
    except:
        pass
else:
    FONT_CN = "Helvetica"

OUTPUT = "wiper_quotation.pdf"
doc = SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=15*mm, bottomMargin=15*mm, leftMargin=15*mm, rightMargin=15*mm)
PW = A4[0] - 30*mm
def ms(fn, sz, ld, al=TA_LEFT, tc=HexColor("#333"), sb=0, sa=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld, alignment=al, textColor=tc, spaceBefore=sb, spaceAfter=sa)
st = ms(FONT_CN, 22, 30, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
ss = ms("Helvetica", 14, 20, TA_CENTER, HexColor("#555"), 0, 6*mm)
h1 = ms(FONT_CN, 15, 20, TA_LEFT, HexColor("#1a3a5c"), 5*mm, 3*mm)
bd = ms(FONT_CN, 9, 13, TA_LEFT, HexColor("#333"), 0, 1.5*mm)
bs = ms(FONT_CN, 8, 11, TA_LEFT, HexColor("#555"), 0, 1*mm)
cr = ms(FONT_CN, 8, 11, TA_CENTER)
ch = ms(FONT_CN, 8.5, 12, TA_CENTER, white)
ft = ms(FONT_CN, 7.5, 10, TA_CENTER, HexColor("#888"))

def tbl(hd, data, cw_pct, hc="#1a3a5c"):
    cw = [p/100*PW for p in cw_pct]
    rows = [[Paragraph(h, ch) for h in hd]]
    for row in data:
        rows.append([Paragraph(str(c), cr) for c in row])
    t = Table(rows, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),HexColor(hc)),
        ("TEXTCOLOR",(0,0),(-1,0),white),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("GRID",(0,0),(-1,-1),0.5,HexColor("#ccc")),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[HexColor("#f5f8fc"),white]),
    ]))
    return t

story = []
story.append(Spacer(1, 30*mm))
story.append(Paragraph("<b>\u65e0\u5c18\u5e03 \u00b7 \u62a5\u4ef7\u5355</b>", st))
story.append(Paragraph("Cleanroom Wiper \u00b7 Quotation", ss))
story.append(Spacer(1, 10*mm))
story.append(Paragraph("<b>Supplier:</b> Wuxi Yuanjie Cleanroom Products", bd))
story.append(Paragraph("<b>Date:</b> July 5, 2026", bd))
story.append(Paragraph("<b>Validity:</b> 30 days", bd))
story.append(Paragraph("<b>Version:</b> V1.0", bd))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("<b>Trade Terms:</b> EXW Wuxi / FOB Shanghai / CIF Destination Port", bd))
story.append(Paragraph("<b>Currency:</b> USD", bd))
story.append(Paragraph("<b>MOQ:</b> 100 packs per SKU", bd))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("--- Reference prices, subject to order confirmation ---", ms(FONT_CN, 9, 12, TA_CENTER, HexColor("#cc0000"))))
story.append(PageBreak())
story.append(Paragraph("<b>1. DS Series - Electronic Grade</b>", h1))
story.append(Paragraph("Material: Polyester+Nylon Knitted | Class 100~1000 | 100pcs/pack | Laser Cut", bs))
story.append(Spacer(1, 2*mm))
ds_h = ["Model","Size","EXW(USD)","FOB SH(USD)","CIF TR(USD)","CIF AE(USD)","CIF PL(USD)"]
ds_d = [["DS-0404","4x4(10cm)","0.55","0.75","0.95","0.90","1.00"],["DS-0606","6x6(15cm)","0.90","1.15","1.40","1.35","1.45"],["DS-0909","9x9(23cm)","1.50","1.80","2.10","2.05","2.20"],["DS-1212","12x12(30cm)","2.40","2.75","3.15","3.05","3.25"],["DS-1818","18x18(45cm)","4.50","5.00","5.60","5.50","5.80"]]
story.append(tbl(ds_h, ds_d, [40,50,35,38,38,38,38]))
story.append(Paragraph("EXW=Factory; FOB SH=Shanghai; CIF TR=Istanbul; CIF AE=Dubai; CIF PL=Gdansk", bs))
story.append(Paragraph("FOB includes domestic transport + customs ~.20-0.50/pack", bs))
story.append(PageBreak())
story.append(Paragraph("<b>2. KH Series - Industrial Wipes</b>", h1))
story.append(Paragraph("Material: Polyester Knitted (Non-cleanroom) | 100pcs/pack", bs))
story.append(Spacer(1, 2*mm))
kh_h = ["Model","Size","EXW(USD)","FOB SH(USD)","CIF TR(USD)","CIF RU(USD)"]
kh_d = [["KH-0606","6x6(15cm)","0.45","0.65","0.85","0.90"],["KH-0909","9x9(23cm)","0.80","1.05","1.30","1.35"],["KH-1212","12x12(30cm)","1.30","1.60","1.95","2.00"]]
story.append(tbl(kh_h, kh_d, [40,50,35,38,40,40], "#2b5a8c"))
story.append(Paragraph("KH weight TBD (factory confirmation pending). Industrial grade.", bs))
story.append(PageBreak())
story.append(Paragraph("<b>3. Customization Premium</b>", h1))
story.append(Spacer(1, 2*mm))
c_h = ["Item","Premium","Notes"]
c_d = [["Custom Size","+10~20%","Depends on variance"],["Vacuum Pack","+.05/pack","Higher cleanliness"],["Double Bagged","+.03/pack","Class 100~1000"],["LOGO Printing","+-30/setup","Setup + per-pack fee"],["Ultrasonic Cut","+.02/pack","Alt. to laser cut"],["Cold Cut","-.03/pack","Low cost, less edge seal"]]
story.append(tbl(c_h, c_d, [40,40,60]))
story.append(PageBreak())
story.append(Paragraph("<b>4. Volume Discount</b>", h1))
story.append(Spacer(1, 2*mm))
d_h = ["Order Qty","Discount","Series"]
d_d = [["100~500 packs","Base Price","DS/KH"],["501~2,000 packs","-5%","DS/KH"],["2,001~5,000 packs","-10%","DS/KH"],["5,001+ packs","-15%","Negotiable"]]
story.append(tbl(d_h, d_d, [55,40,45]))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("<b>5. Sample Policy</b>", h1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("- Free samples: 5 packs per SKU for first-time clients (excl. shipping)", bd))
story.append(Paragraph("- Shipping: client pays international courier (~-60 DHL to major countries)", bd))
story.append(Paragraph("- Urgent: DHL express collect, 2-3 business days delivery", bd))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("<b>6. Payment Terms</b>", h1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("- First order: 100% T/T in advance", bd))
story.append(Paragraph("- Returning clients: 30% deposit + 70% before shipment", bd))
story.append(Paragraph("- L/C at sight accepted for orders >,000", bd))
story.append(Paragraph("- Western Union / PayPal for small sample orders", bd))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("--- Subject to final order contract ---", ms(FONT_CN, 9, 12, TA_CENTER, HexColor("#888"))))
doc.build(story)
sz = os.path.getsize(OUTPUT)
print(f"OK: {OUTPUT} ({sz//1024} KB)")