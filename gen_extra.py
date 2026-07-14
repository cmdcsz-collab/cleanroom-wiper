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

def ms(fn, sz, ld, al=TA_LEFT, tc=HexColor("#333"), sb=0, sa=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld, alignment=al, textColor=tc, spaceBefore=sb, spaceAfter=sa)

st = ms(FONT_CN, 20, 28, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
ss = ms("Helvetica", 12, 18, TA_CENTER, HexColor("#555"), 0, 6*mm)
h1 = ms(FONT_CN, 14, 20, TA_LEFT, HexColor("#1a3a5c"), 5*mm, 3*mm)
h2 = ms(FONT_CN, 11, 16, TA_LEFT, HexColor("#2b5a8c"), 3*mm, 2*mm)
bd = ms(FONT_CN, 9, 14, TA_LEFT, HexColor("#333"), 0, 2*mm)
bs = ms(FONT_CN, 8, 12, TA_LEFT, HexColor("#555"), 0, 1*mm)
cr = ms(FONT_CN, 8, 11, TA_CENTER)
ch = ms(FONT_CN, 8.5, 12, TA_CENTER, white)
ft = ms(FONT_CN, 7.5, 10, TA_CENTER, HexColor("#888"))
PW = A4[0] - 30*mm

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

# Sample Plan PDF
OUT1 = "wiper_sample_plan.pdf"
doc1 = SimpleDocTemplate(OUT1, pagesize=A4, topMargin=15*mm, bottomMargin=15*mm, leftMargin=15*mm, rightMargin=15*mm)
s = []
s.append(Spacer(1, 25*mm))
s.append(Paragraph("<b>Cleanroom Wiper - Sample Plan</b>", st))
s.append(Paragraph("Free Sample Program & Cost Analysis", ss))
s.append(Spacer(1, 6*mm))
s.append(Paragraph("<b>Supplier:</b> Wuxi Yuanjie Cleanroom Products", bd))
s.append(Paragraph("<b>Version:</b> V1.0 | July 2026", bd))
s.append(Spacer(1, 3*mm))

s.append(Paragraph("<b>1. Sample Program Overview</b>", h1))
s.append(Paragraph("Strategy: Offer free samples to serious buyers to demonstrate product quality and build trust. This reduces the buyer decision risk and accelerates first orders.", bd))
s.append(Spacer(1, 3*mm))

s.append(Paragraph("<b>2. Recommended Sample Kit - Starter Pack</b>", h1))
s.append(Paragraph("Target cost: Under USD 50 total sample cost + shipping", bd))
s.append(Spacer(1, 2*mm))
s.append(tbl(["SKU","Size","Qty","Unit Cost","Total"],
    [["DS-0406","6x6 (EQ)","5 pk","0.90","4.50"],
     ["DS-0606","6x6","5 pk","0.90","4.50"],
     ["DS-0909","9x9","5 pk","1.50","7.50"],
     ["DS-1212","12x12","3 pk","2.40","7.20"],
     ["KH-0606","6x6","5 pk","0.45","2.25"],
     ["KH-0909","9x9","5 pk","0.80","4.00"]],
    [40,40,30,35,35]))
s.append(Spacer(1, 2*mm))
s.append(Paragraph("Subtotal (samples): USD 30.00", bd))
s.append(Paragraph("Estimated DHL shipping: USD 35-60 (varies by destination)", bd))
s.append(Paragraph("Total cost to client: ~USD 65-90", bd))
s.append(Spacer(1, 4*mm))

s.append(Paragraph("<b>3. Sample Policy Terms</b>", h1))
s.append(Paragraph("- Free samples: First-time clients get up to 5 packs per SKU free", bd))
s.append(Paragraph("- Shipping: Client pays DHL/FedEx express shipping (collect or prepay)", bd))
s.append(Paragraph("- Lead time: Samples dispatched within 3 business days of shipping payment", bd))
s.append(Paragraph("- Delivery: 2-5 business days via DHL to major world cities", bd))
s.append(Paragraph("- Custom samples: For custom sizes/packaging, add USD 20-50 tooling fee", bd))
s.append(Spacer(1, 3*mm))

s.append(Paragraph("<b>4. Cost Breakdown for Free Sample Program</b>", h1))
s.append(Spacer(1, 2*mm))
s.append(tbl(["Cost Item","Amount (USD)","Notes"],
    [["Sample product cost","30.00","6 SKUs, 28 packs total"],
     ["Packaging & labeling","5.00","Professional packaging"],
     ["Documentation","3.00","Spec sheet + COA"],
     ["Total per sample kit","38.00","Supplier cost"],
     ["","",""],
     ["Client pays: shipping","35-60","DHL to destination"],
     ["Supplier cost per lead","38.00","Marketing investment"]],
    [60,40,60]))
s.append(Spacer(1, 3*mm))
s.append(Paragraph("Assuming 20% conversion rate, cost per acquired customer: ~USD 190", bd))
s.append(Spacer(1, 3*mm))

s.append(Paragraph("<b>5. Sample Request Process</b>", h1))
s.append(Paragraph("Step 1: Prospect expresses interest (email/LinkedIn/WhatsApp)", bd))
s.append(Paragraph("Step 2: Confirm shipping address and preferred SKUs", bd))
s.append(Paragraph("Step 3: Send PayPal invoice for shipping cost (or arrange DHL account)", bd))
s.append(Paragraph("Step 4: Dispatch samples within 3 working days", bd))
s.append(Paragraph("Step 5: Share tracking number with client", bd))
s.append(Paragraph("Step 6: Follow up 5-7 days after delivery for feedback", bd))
s.append(Spacer(1, 3*mm))

s.append(Paragraph("<b>6. First Order Conversion Tactics</b>", h1))
s.append(Paragraph("- Offer first-order discount: 5% off first order if placed within 30 days of sample delivery", bd))
s.append(Paragraph("- Include a personalized thank-you note in the sample package", bd))
s.append(Paragraph("- Add a first order checklist showing MOQ, payment, and shipping process", bd))
s.append(Paragraph("- Offer flexible payment terms (50% deposit, 50% before shipment) for first orders under USD 2,000", bd))
s.append(Spacer(1, 8*mm))
s.append(Paragraph("--- End of Document ---", ft))
s.append(Paragraph("Version V1.0 | Created: 2026-07-05", ft))
doc1.build(s)
sz1 = os.path.getsize(OUT1)
print(f"OK: {OUT1} ({sz1//1024} KB)")

# Market Strategy PDF
OUT2 = "wiper_market_strategy.pdf"
doc2 = SimpleDocTemplate(OUT2, pagesize=A4, topMargin=15*mm, bottomMargin=15*mm, leftMargin=15*mm, rightMargin=15*mm)
s2 = []
s2.append(Spacer(1, 25*mm))
s2.append(Paragraph("<b>Cleanroom Wiper - Market Strategy</b>", st))
s2.append(Paragraph("Target Market Entry Strategy & Action Plan", ss))
s2.append(Spacer(1, 6*mm))
s2.append(Paragraph("<b>Supplier:</b> Wuxi Yuanjie Cleanroom Products", bd))
s2.append(Paragraph("<b>Version:</b> V1.0 | July 2026", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>1. Market Selection Rationale</b>", h1))
s2.append(Paragraph("Target markets selected based on:", bd))
s2.append(Paragraph("- Lower certification requirements (no mandatory ISO/RoHS for initial entry)", bd))
s2.append(Paragraph("- Growing manufacturing and electronics sectors", bd))
s2.append(Paragraph("- Price-sensitive markets where factory-direct pricing is competitive", bd))
s2.append(Paragraph("- Manageable shipping costs and trade routes from Shanghai", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>2. Market Profiles</b>", h1))
s2.append(Spacer(1, 2*mm))
s2.append(Paragraph("<b>Turkey - Primary Target</b>", h2))
s2.append(Paragraph("- Key sectors: Electronics, automotive, textiles", bd))
s2.append(Paragraph("- Import duty: 2.5-5% on textile wipes (HS code 6307.10)", bd))
s2.append(Paragraph("- Shipping: CIF Istanbul ~25 days from Shanghai", bd))
s2.append(Paragraph("- Target price: DS-0909 < USD 2.10/pack CIF (very price sensitive)", bd))
s2.append(Paragraph("- Payment: T/T, open to L/C for larger orders", bd))
s2.append(Paragraph("- Channels: LinkedIn direct outreach + Turkish trade portals", bd))
s2.append(Paragraph("- Language: English sufficient, Turkish helpful for trust-building", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>UAE / Saudi Arabia - Quality Focus</b>", h2))
s2.append(Paragraph("- Key sectors: Electronics, oil & gas, construction", bd))
s2.append(Paragraph("- Import duty: 5% GCC common tariff", bd))
s2.append(Paragraph("- Shipping: CIF Dubai ~18 days from Shanghai", bd))
s2.append(Paragraph("- Target price: DS-0909 ~USD 2.05/pack CIF", bd))
s2.append(Paragraph("- Channels: LinkedIn + industry exhibitions (Arab Lab, etc.)", bd))
s2.append(Paragraph("- Important: Professional packaging and branding matter greatly", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>Poland / Czech Republic - Gateway to EU</b>", h2))
s2.append(Paragraph("- Key sectors: Automotive, electronics manufacturing, pharma", bd))
s2.append(Paragraph("- Import duty: 6-8% (EU common tariff)", bd))
s2.append(Paragraph("- Shipping: CIF Gdansk ~30 days from Shanghai", bd))
s2.append(Paragraph("- RoHS: Recommended, arrange SGS testing before entry", bd))
s2.append(Paragraph("- Channels: Email + LinkedIn + EU B2B platforms (Europages)", bd))
s2.append(Paragraph("- Note: Higher quality expectations, may need certification for pharma", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>Russia / CIS - Volume Play</b>", h2))
s2.append(Paragraph("- Key sectors: General industrial, automotive, manufacturing", bd))
s2.append(Paragraph("- Import duty: ~10-15% (verify current sanctions status)", bd))
s2.append(Paragraph("- Shipping: CIF St. Petersburg ~35-40 days", bd))
s2.append(Paragraph("- Focus: KH Series industrial wipes (lowest price point)", bd))
s2.append(Paragraph("- Channels: Email + Russian B2B portals (Pulscen, Tiu.ru)", bd))
s2.append(Paragraph("- Payment: T/T preferred, consider intermediary for sanctions compliance", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>3. Pricing Strategy</b>", h1))
s2.append(Paragraph("- Positioning: 15-25% below current market prices for comparable quality", bd))
s2.append(Paragraph("- Entry tactic: First order at 5% discount + free samples shipped quickly", bd))
s2.append(Paragraph("- Value-add: Free custom packaging design for first bulk order", bd))
s2.append(Paragraph("- Long-term: Build relationships - Increase order sizes - Improve margins", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>4. Logistics Strategy</b>", h1))
s2.append(Paragraph("- Forwarder: Partner with freight forwarder in Shanghai for FOB operations", bd))
s2.append(Paragraph("- Consolidation: Combine multiple SKUs per container to reduce per-unit cost", bd))
s2.append(Paragraph("- Container: 20GP for orders < 500 packs; 40HQ for bulk orders", bd))
s2.append(Paragraph("- Documents: Commercial invoice, packing list, bill of lading, COO", bd))
s2.append(Paragraph("- Insurance: Recommend 110% of CIF value for marine insurance", bd))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>5. 90-Day Action Plan</b>", h1))
s2.append(Spacer(1, 2*mm))
s2.append(tbl(["Week","Action","Target Market"],
    [["1-2","Setup LinkedIn profiles + outreach templates","All markets"],
     ["1-2","Research 100 target prospects per market","Turkey, UAE, PL, RU"],
     ["2-3","Send 25-50 connection requests per day","Priority: Turkey"],
     ["3-4","Follow up with connections, share catalog","All"],
     ["4-6","Target: 10 sample requests sent","Best responses"],
     ["6-8","Follow up on samples delivered","Active prospects"],
     ["8-10","Negotiate first orders","Best leads"],
     ["10-12","Target: 2-3 confirmed orders","Any market"],
     ["12+","Scale outreach + optimize pricing","Focus on best market"]],
    [35,80,45]))
s2.append(Spacer(1, 3*mm))

s2.append(Paragraph("<b>6. Risk Mitigation</b>", h1))
s2.append(Paragraph("- Payment risk: Start with 100% T/T for new clients; progress to 30/70 after trust", bd))
s2.append(Paragraph("- Quality risk: Send pre-shipment samples for approval before bulk production", bd))
s2.append(Paragraph("- Shipping risk: Use confirmed FOB/CIF terms, insure all shipments", bd))
s2.append(Paragraph("- Competition: Differentiate through responsiveness, flexibility, and speed", bd))
s2.append(Spacer(1, 8*mm))

s2.append(Paragraph("--- End of Document ---", ft))
s2.append(Paragraph("Version V1.0 | Created: 2026-07-05 | Wuxi Yuanjie Cleanroom Products", ft))
doc2.build(s2)
sz2 = os.path.getsize(OUT2)
print(f"OK: {OUT2} ({sz2//1024} KB)")