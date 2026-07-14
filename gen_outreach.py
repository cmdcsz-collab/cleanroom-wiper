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
    except: pass
else: FONT_CN = "Helvetica"

OUTPUT = "wiper_outreach.pdf"
doc = SimpleDocTemplate(OUTPUT, pagesize=A4, topMargin=15*mm, bottomMargin=15*mm, leftMargin=15*mm, rightMargin=15*mm)
PW = A4[0] - 30*mm
def ms(fn, sz, ld, al=TA_LEFT, tc=HexColor("#333"), sb=0, sa=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld, alignment=al, textColor=tc, spaceBefore=sb, spaceAfter=sa)
st = ms(FONT_CN, 20, 28, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
ss = ms("Helvetica", 12, 18, TA_CENTER, HexColor("#555"), 0, 6*mm)
h1 = ms(FONT_CN, 14, 20, TA_LEFT, HexColor("#1a3a5c"), 5*mm, 3*mm)
h2 = ms(FONT_CN, 11, 16, TA_LEFT, HexColor("#2b5a8c"), 3*mm, 2*mm)
bd = ms(FONT_CN, 9, 14, TA_LEFT, HexColor("#333"), 0, 2*mm)
bs = ms(FONT_CN, 8, 12, TA_LEFT, HexColor("#555"), 0, 1*mm)
ft = ms(FONT_CN, 7.5, 10, TA_CENTER, HexColor("#888"))

story = []
story.append(Spacer(1, 20*mm))
story.append(Paragraph("<b>Cleanroom Wiper - Outreach Toolkit</b>", st))
story.append(Paragraph("LinkedIn Messages & Cold Email Templates", ss))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("<b>Supplier:</b> Wuxi Yuanjie Cleanroom Products", bd))
story.append(Paragraph("<b>Target Markets:</b> Turkey, Middle East, Eastern Europe, Russia/CIS", bd))
story.append(Paragraph("<b>Version:</b> V1.0 | July 2026", bd))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("Contents:", bd))
story.append(Paragraph("1. LinkedIn Connection Request Templates", bd))
story.append(Paragraph("2. LinkedIn Message Templates (After Connection)", bd))
story.append(Paragraph("3. Cold Email Templates by Target Market", bd))
story.append(Paragraph("4. Follow-up Sequences", bd))
story.append(PageBreak())

# Section 1: LinkedIn Connection
story.append(Paragraph("<b>1. LinkedIn Connection Request Templates</b>", h1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("<b>Template A - General (300 char limit)</b>", h2))
story.append(Paragraph("Hi [Name], I'm reaching out from Wuxi Yuanjie Cleanroom Products in China. We specialize in high-quality cleanroom wipers (Class 100-1000) at competitive factory-direct prices. Would love to connect and explore if we can support your business.", bd))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Template B - For Procurement / Purchasing Managers</b>", h2))
story.append(Paragraph("Hello [Name], I see you're in procurement at [Company]. We're a Chinese manufacturer of cleanroom wipers (DS electronic & KH industrial series) with factory-direct pricing. Currently expanding to [Market]. Would be great to connect.", bd))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Template C - For Distributors / Resellers</b>", h2))
story.append(Paragraph("Hi [Name], we're looking for distribution partners in [Country] for our cleanroom wiper line. Factory-direct supply, competitive pricing, flexible MOQ. Interested in discussing a partnership?", bd))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Template D - Short & Direct</b>", h2))
story.append(Paragraph("Hello [Name], cleanroom wiper manufacturer from China here. Competitive pricing, Class 100-1000. Looking to connect with professionals in [industry/sector].", bd))
story.append(PageBreak())

# Section 2: After Connection
story.append(Paragraph("<b>2. LinkedIn Follow-up Messages (After Connection)</b>", h1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("<b>Message 1 - Introduction</b>", h2))
story.append(Paragraph("Thanks for connecting! Wuxi Yuanjie Cleanroom Products specializes in manufacturing cleanroom wipers and industrial wipes. Our key products:", bd))
story.append(Paragraph("- DS Series (Electronic Grade): Class 100~1000, 4x4 to 18x18 inches", bd))
story.append(Paragraph("- KH Series (Industrial Grade): Cost-effective for general industrial use", bd))
story.append(Paragraph("- MOQ: 100 packs per SKU | Custom sizes, packaging & LOGO available", bd))
story.append(Paragraph("Would you be interested in our product catalog or pricing? Happy to share.", bd))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("<b>Message 2 - Price-focused</b>", h2))
story.append(Paragraph("Hi [Name], as a factory-direct supplier, we offer very competitive pricing:", bd))
story.append(Paragraph("- DS-0909 (9x9 inch, electronic grade): from \.50/pack EXW", bd))
story.append(Paragraph("- DS-0606 (6x6 inch): from \.90/pack EXW", bd))
story.append(Paragraph("- Free samples available for evaluation", bd))
story.append(Paragraph("Can I send you our full price list?", bd))
story.append(Spacer(1, 4*mm))
story.append(Paragraph("<b>Message 3 - Sample Offer</b>", h2))
story.append(Paragraph("Would you like to evaluate our quality with free samples? We can send 5 packs per SKU of our best-selling models. You just cover the shipping (approx. \-60 via DHL).", bd))
story.append(PageBreak())

# Section 3: Cold Email Templates
story.append(Paragraph("<b>3. Cold Email Templates by Target Market</b>", h1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("<b>For Turkey (Price-sensitive market)</b>", h2))
story.append(Paragraph("Subject: Competitive cleanroom wiper pricing - factory direct from China", bd))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("Dear [Name],", bd))
story.append(Paragraph("I'm writing from Wuxi Yuanjie Cleanroom Products, a Chinese manufacturer of cleanroom wipers. We are looking to enter the Turkish market with very competitive pricing.", bd))
story.append(Paragraph("Our DS Series electronic-grade wipers (Class 100~1000) start from just \.90/pack EXW for 6x6 inch size. We also offer industrial-grade KH series for more cost-sensitive applications.", bd))
story.append(Paragraph("Key advantages:", bd))
story.append(Paragraph("- Factory-direct pricing, no middleman markups", bd))
story.append(Paragraph("- Flexible MOQ: 100 packs per SKU", bd))
story.append(Paragraph("- Free samples available", bd))
story.append(Paragraph("- Custom sizes, packaging & LOGO printing", bd))
story.append(Paragraph("Would you be open to reviewing our product catalog and price list?", bd))
story.append(Paragraph("Best regards,", bd))
story.append(Paragraph("[Your Name]", bd))
story.append(Paragraph("Wuxi Yuanjie Cleanroom Products | [Email] | [WhatsApp]", bd))
story.append(Spacer(1, 6*mm))
story.append(Paragraph("<b>For Middle East (Quality + Packaging focus)</b>", h2))
story.append(Paragraph("Subject: Premium cleanroom wipers from China - suitable for [Country] market", bd))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("Dear [Name],", bd))
story.append(Paragraph("Wuxi Yuanjie Cleanroom Products specializes in high-quality cleanroom wipers for the electronics and semiconductor industries. Our DS Series (Class 100~1000) is ideal for cleanroom environments.", bd))
story.append(Paragraph("We offer:", bd))
story.append(Paragraph("- Laser-cut sealed edges for low particle emission", bd))
story.append(Paragraph("- Professional packaging with custom branding options", bd))
story.append(Paragraph("- FOB Shanghai or CIF Dubai delivery", bd))
story.append(Paragraph("- Competitive pricing for the Middle East market", bd))
story.append(Paragraph("Would you be interested in receiving our catalog and FOB/CIF pricing?", bd))
story.append(PageBreak())

story.append(Paragraph("<b>For Eastern Europe (RoHS-aware)</b>", h2))
story.append(Paragraph("Subject: Cleanroom wipers with competitive pricing - FOB Shanghai / CIF Gdansk", bd))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("Dear [Name],", bd))
story.append(Paragraph("We are a Chinese manufacturer of cleanroom wipers looking to expand to the Polish and Czech markets. Our products are suitable for electronics manufacturing, automotive, and pharmaceutical industries.", bd))
story.append(Paragraph("We understand the European market requires RoHS compliance - this can be arranged through third-party testing. Our pricing is very competitive for the Eastern European market.", bd))
story.append(Paragraph("Key products:", bd))
story.append(Paragraph("- DS Series electronic grade (Class 100~1000) - popular sizes 9x9, 12x12 inch", bd))
story.append(Paragraph("- KH Series industrial grade for general cleaning", bd))
story.append(Paragraph("- CIF Gdansk delivery available", bd))
story.append(Paragraph("Would you like to discuss potential cooperation?", bd))
story.append(Spacer(1, 6*mm))
story.append(Paragraph("<b>For Russia / CIS (Price-first approach)</b>", h2))
story.append(Paragraph("Subject: Industrial wipes at factory prices - direct from China", bd))
story.append(Spacer(1, 1*mm))
story.append(Paragraph("Dear [Name],", bd))
story.append(Paragraph("We manufacture industrial-grade polyester wipes that are widely used in general industrial cleaning, automotive workshops, and manufacturing facilities.", bd))
story.append(Paragraph("Our KH Series is specifically designed for cost-sensitive industrial applications:", bd))
story.append(Paragraph("- Starting from just \.45/pack EXW", bd))
story.append(Paragraph("- Bulk packing available for even lower costs", bd))
story.append(Paragraph("- Flexible payment terms for first orders", bd))
story.append(Paragraph("We can ship CIF to St. Petersburg or other Russian ports.", bd))
story.append(Paragraph("Interested in discussing?", bd))
story.append(Spacer(1, 6*mm))
story.append(PageBreak())

# Section 4: Follow-ups
story.append(Paragraph("<b>4. Follow-up Sequences</b>", h1))
story.append(Spacer(1, 2*mm))
story.append(Paragraph("<b>Sequence A - 3-Email Follow-up</b>", h2))
story.append(Paragraph("Email 1 (Day 0): Initial outreach - product catalog + value proposition", bd))
story.append(Paragraph("Email 2 (Day 4): Follow-up - \"Did you receive my previous email?\" + key selling points", bd))
story.append(Paragraph("Email 3 (Day 8): Final follow-up - offer free samples + best price", bd))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Sequence B - LinkedIn-to-Email Pipeline</b>", h2))
story.append(Paragraph("Step 1: Send LinkedIn connection request (Template A-D above)", bd))
story.append(Paragraph("Step 2: After accepted, send Message 1 (introduction with catalog offer)", bd))
story.append(Paragraph("Step 3: If no reply in 5 days, send Message 2 (price-focused)", bd))
story.append(Paragraph("Step 4: If still no reply, find their email and send cold email", bd))
story.append(Paragraph("Step 5: Follow up on email after 4 days", bd))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Best Practices</b>", h2))
story.append(Paragraph("- Research the prospect's company before reaching out", bd))
story.append(Paragraph("- Reference their industry or specific use case", bd))
story.append(Paragraph("- Keep initial messages under 150 words", bd))
story.append(Paragraph("- Always include a clear call-to-action", bd))
story.append(Paragraph("- Use WhatsApp for faster response in Turkey & Middle East", bd))
story.append(Paragraph("- For Eastern Europe, emphasize quality + compliance", bd))
story.append(Paragraph("- For Russia/CIS, emphasize price + bulk availability", bd))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("--- End of Outreach Toolkit ---", ft))
story.append(Paragraph("Version V1.0 | Created: 2026-07-05", ft))

doc.build(story)
sz = os.path.getsize(OUTPUT)
print(f"OK: {OUTPUT} ({sz//1024} KB)")