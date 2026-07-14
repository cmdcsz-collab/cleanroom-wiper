#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn 主动开发客户实战指南 — 无尘布外贸出海
LinkedIn Active Customer Development Playbook
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem, KeepTogether
)
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

OUTPUT = "LinkedIn主动开发客户_Playbook.pdf"
doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
                        topMargin=15*mm, bottomMargin=15*mm,
                        leftMargin=15*mm, rightMargin=15*mm)
PW = A4[0] - 30*mm

def ms(fn, sz, ld, al=TA_LEFT, tc=HexColor("#333"), sb=0, sa=0):
    return ParagraphStyle("x", fontName=fn, fontSize=sz, leading=ld,
                          alignment=al, textColor=tc,
                          spaceBefore=sb, spaceAfter=sa)

st  = ms(FONT_CN, 22, 30, TA_CENTER, HexColor("#1a3a5c"), 0, 4*mm)
ss  = ms("Helvetica", 14, 20, TA_CENTER, HexColor("#555"), 0, 6*mm)
h1  = ms(FONT_CN, 15, 21, TA_LEFT, HexColor("#1a3a5c"), 6*mm, 3*mm)
h2  = ms(FONT_CN, 12, 17, TA_LEFT, HexColor("#2b5a8c"), 4*mm, 2*mm)
h3  = ms(FONT_CN, 10.5, 15, TA_LEFT, HexColor("#333"), 3*mm, 1.5*mm)
bd  = ms(FONT_CN, 9, 14, TA_LEFT, HexColor("#333"), 0, 1.5*mm)
bs  = ms(FONT_CN, 8, 12, TA_LEFT, HexColor("#555"), 0, 1*mm)
ft  = ms(FONT_CN, 7, 10, TA_CENTER, HexColor("#888"))
tc  = ms(FONT_CN, 9, 13, TA_CENTER, HexColor("#1a3a5c"), 1*mm, 1*mm)
hc  = ms(FONT_CN, 9, 13, TA_CENTER, white)
box = ms(FONT_CN, 9, 14, TA_LEFT, HexColor("#1a3a5c"), 1*mm, 1*mm)

def section_box(text, bg="#e8f0f8"):
    """Create a highlighted info box"""
    t = Table([[Paragraph(text, ms(FONT_CN, 9, 14, TA_LEFT, HexColor("#1a3a5c"), 2*mm, 2*mm))]],
              colWidths=[PW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor(bg)),
        ("BOX", (0,0), (-1,-1), 0.5, HexColor("#1a3a5c")),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

story = []

# ===== Cover =====
story.append(Spacer(1, 25*mm))
story.append(Paragraph("<b>LinkedIn 主动开发客户实战指南</b>", st))
story.append(Paragraph("LinkedIn Active Customer Development Playbook", ss))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("<b>供应商:</b> 无锡源洁无尘布（Yuanjie Cleanroom Products）", bd))
story.append(Paragraph("<b>产品:</b> DS系列电子级无尘布 / KH系列工业擦拭布", bd))
story.append(Paragraph("<b>目标市场:</b> 土耳其 / 中东 / 东欧 / 独联体", bd))
story.append(Paragraph("<b>版本:</b> V1.0 | 2026年7月", bd))
story.append(Spacer(1, 15*mm))

story.append(section_box(
    "为什么用LinkedIn开发外贸客户？\n"
    "• 全球B2B专业人士首选社交平台，8.3亿+用户\n"
    "• 直接触达采购经理、工厂厂长、企业决策者\n"
    "• 相比展会（成本高）和阿里国际站（竞争激烈），LinkedIn精准且免费\n"
    "• 建立行业专业形象后，客户会主动找上门"
))
story.append(PageBreak())

# ===== Table of Contents =====
story.append(Paragraph("<b>目录 / Contents</b>", h1))
story.append(Spacer(1, 3*mm))
toc_items = [
    "1. 准备工作：Profile 优化（让客户主动搜到你）",
    "2. 目标客户画像：谁是你的理想客户？",
    "3. 高效搜索技巧：Sales Navigator & 免费方法",
    "4. 连接请求话术（300字符内的艺术）",
    "5. 连接后跟进序列（7天转化流程）",
    "6. InMail & 消息模板分市场版",
    "7. 内容营销策略：从被看到被信任",
    "8. 转化流程：从好友到询盘到订单",
    "9. 每日/每周执行计划",
    "10. 工具推荐 & 效率提升技巧",
    "附录：常用中英文行业术语对照",
]
for item in toc_items:
    story.append(Paragraph(item, bd))
story.append(PageBreak())

# ===== Section 1: Profile =====
story.append(Paragraph("<b>1. 准备工作：Profile 优化</b>", h1))
story.append(Paragraph("你的LinkedIn就是你的24小时免费业务员。优化好Profile，客户会主动搜索到你。", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>1.1 头像 / Profile Photo</b>", h2))
story.append(Paragraph("• 使用专业商务照：正装、微笑、背景干净", bd))
story.append(Paragraph("• 不要用产品图、公司LOGO、风景照", bd))
story.append(Paragraph("• 尺寸：400×400像素以上，面部占画面的60%", bd))
story.append(Spacer(1, 1*mm))

story.append(Paragraph("<b>1.2 背景图 / Background Banner</b>", h2))
story.append(Paragraph("• 设计一张1584×396像素的横幅", bd))
story.append(Paragraph("• 包含：公司名称 + 核心产品 + 工厂实拍 + 联系方式", bd))
story.append(Paragraph("• 示例文案：Cleanroom Wiper Manufacturer | DS Series Class 100-1000 | Factory Direct", bd))
story.append(Spacer(1, 1*mm))

story.append(Paragraph("<b>1.3 标题 / Headline（最重要的部分）</b>", h2))
story.append(section_box(
    "推荐标题模板（中英文）：\n\n"
    "1. Cleanroom Wiper Manufacturer | Factory Direct | DS/KH Series | Custom Sizes & Packaging\n\n"
    "2. 无尘布工厂直供 | 电子级DS系列 / 工业级KH系列 | 激光封边 | 接受定制\n\n"
    "3. Export Sales Manager at Yuanjie Cleanroom | Helping distributors source quality wipers at competitive prices\n\n"
    "💡 标题要包含关键词（cleanroom wiper, manufacturer, factory），这样客户搜索时才能找到你"
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>1.4 About / 个人简介</b>", h2))
story.append(Paragraph("用第一人称写，内容包括：", bd))
story.append(Paragraph("• 你是谁 + 公司介绍", bd))
story.append(Paragraph("• 核心产品 + 优势（价格低、工厂直供、可定制）", bd))
story.append(Paragraph("• 目标市场 + 交货方式（FOB/CIF/EXW）", bd))
story.append(Paragraph("• 行动呼吁：欢迎联系获取产品目录和报价", bd))
story.append(Paragraph("• 关键词：cleanroom wiper, industrial wipes, polyester knitted, laser cut", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>About 中文示例：</b>", h3))
story.append(section_box(
    "我在源洁无尘布负责出口销售，我们工厂位于江苏无锡，专业生产无尘布和工业擦拭布超过10年。\n\n"
    "核心产品：\n"
    "• DS系列电子级无尘布 — Class 100~1000，涤纶+锦纶针织，激光封边\n"
    "• KH系列工业擦拭布 — 性价比高，适用一般工业清洁\n\n"
    "优势：工厂直供价格，尺寸/包装/LOGO可定制，MOQ灵活。\n"
    "目标市场：土耳其、中东、东欧。可安排FOB上海或CIF到港。\n\n"
    "欢迎联系获取详细产品目录和报价！WhatsApp: [+86xxx]"
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>About English Example:</b>", h3))
story.append(section_box(
    "Export Sales Manager at Yuanjie Cleanroom Products, a professional manufacturer of cleanroom wipers based in Wuxi, China.\n\n"
    "Our products:\n"
    "• DS Series Electronic Grade — Class 100~1000, Polyester+Nylon knitted, laser-sealed edges\n"
    "• KH Series Industrial Wipes — Cost-effective for general industrial cleaning\n\n"
    "Why work with us: Factory-direct pricing, custom sizes/packaging/LOGO, flexible MOQ.\n"
    "FOB Shanghai / CIF to major ports. Serving Turkey, Middle East, and Eastern Europe.\n\n"
    "DM me for catalog & pricing! WhatsApp: [+86xxx]"
))
story.append(PageBreak())

# ===== Section 2: Target Audience =====
story.append(Paragraph("<b>2. 目标客户画像</b>", h1))
story.append(Paragraph("不是所有人都值得加。精准的目标才能带来有效询盘。", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>2.1 理想客户画像 / ICP</b>", h2))

icp_data = [
    ["维度", "目标客户特征"],
    ["行业", "电子制造、半导体、汽车零部件、制药、医疗器械"],
    ["职位", "Procurement Manager, Supply Chain Director, Factory Manager, Operations Manager, Plant Manager"],
    ["公司规模", "50~500人（太大难接触决策者，太小需求不稳定）"],
    ["地区", "土耳其（伊斯坦布尔）、中东（阿联酋/沙特）、东欧（波兰/捷克/匈牙利）、独联体"],
    ["角色", "进口商/分销商（最优先）、终端工厂（次优先）"],
]
icp_t = Table(
    [[Paragraph(c, tc if i==0 else bd) for c in row] for i, row in enumerate(icp_data)],
    colWidths=[PW*0.3, PW*0.7]
)
icp_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(icp_t)
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>2.2 搜索关键词清单</b>", h2))
kw_data = [
    ["英文关键词", "中文关键词"],
    ["cleanroom wiper distributor", "无尘布 进口商"],
    ["industrial wipes supplier", "工业擦拭布 采购"],
    ["cleanroom consumables trading", "无尘室耗材 贸易商"],
    ["wiper manufacturer Turkey", "擦拭布 工厂 土耳其"],
    ["cleanroom supplies procurement", "洁净室耗材 采购经理"],
    ["ESD / cleanroom products", "防静电/无尘产品 分销"],
    ["semiconductor consumables buyer", "半导体耗材 采购"],
    ["pharmaceutical cleanroom buyer", "制药 无尘室 采购"],
]
kw_t = Table(
    [[Paragraph(c, tc if i==0 else bd) for c in row] for i, row in enumerate(kw_data)],
    colWidths=[PW*0.5, PW*0.5]
)
kw_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#2b5a8c")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
]))
story.append(kw_t)
story.append(PageBreak())

# ===== Section 3: Search Techniques =====
story.append(Paragraph("<b>3. 高效搜索技巧</b>", h1))
story.append(Paragraph("免费版LinkedIn也可以找到大量目标客户，配合Sales Navigator效果翻倍。", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>3.1 免费版搜索技巧</b>", h2))
story.append(Paragraph("在LinkedIn搜索框中使用以下搜索串（Search Strings）：", bd))
story.append(Spacer(1, 1*mm))

searches = [
    '"procurement manager" AND "cleanroom" AND "Turkey"',
    '"purchasing manager" AND "wiper" OR "wipes"',
    '"supply chain" AND "electronics" AND "Istanbul"',
    '"factory manager" AND "cleanroom" AND "Poland"',
    '"operations director" AND "semiconductor" AND "Dubai"',
    '"import manager" AND "industrial" AND "UAE"',
    '"distributor" AND "cleanroom" AND "Saudi Arabia"',
    '"plant manager" AND "automotive" AND "Czech"',
]
for s in searches:
    story.append(Paragraph(f"  ▸ {s}", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>3.2 Sales Navigator 高级搜索（强烈推荐）</b>", h2))
story.append(Paragraph("Sales Navigator (付费，约$80/月) 可以大幅提升效率：", bd))
story.append(Paragraph("• 按职位关键词 + 地区 + 公司规模 + 行业精准筛选", bd))
story.append(Paragraph("• 每月150个InMail额度，直接给非好友发消息", bd))
story.append(Paragraph("• 查看谁在搜索你的产品相关关键词", bd))
story.append(Paragraph("• 保存搜索并接收新客户提醒", bd))
story.append(Paragraph("• 推荐搜索条件配置：", bd))
story.append(Paragraph("  - 地区：Turkey / UAE / Poland / Czech Republic", bd))
story.append(Paragraph("  - 职位：(procurement OR purchasing OR supply chain) AND (manager OR director)", bd))
story.append(Paragraph("  - 行业：Electronics Manufacturing / Semiconductor / Automotive / Pharmaceuticals", bd))
story.append(Paragraph("  - 公司规模：51-200 / 201-500 员工", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>3.3 拓展技巧：人脉扩散法</b>", h2))
story.append(Paragraph("• 找到一位目标客户后，查看他的「同类」和「联系人」", bd))
story.append(Paragraph("• 加入LinkedIn行业群组：Cleanroom Technology, Semiconductor Manufacturing, Industrial Supply Chain", bd))
story.append(Paragraph("• 关注目标公司的Page，看谁在互动，互动的就是潜在客户", bd))
story.append(Paragraph("• 用Google搜索 \"[company name] procurement manager linkedin\" 直接定位", bd))
story.append(PageBreak())

# ===== Section 4: Connection Templates =====
story.append(Paragraph("<b>4. 连接请求话术（300字符的艺术）</b>", h1))
story.append(Paragraph("LinkedIn连接请求有300字符限制。必须一句话说清身份、价值、行动呼吁。", bd))
story.append(Paragraph("核心公式：称呼 + 自我介绍 + 为什么加他 + 行动呼吁", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>模板A：通用版（适用于大部分场景）</b>", h2))
story.append(section_box(
    "Hi [Name], I'm a cleanroom wiper manufacturer from China (factory-direct). "
    "Our DS Series (Class 100-1000) is popular in [Market]. "
    "Looking to connect with industry professionals. "
    "Would you like to see our product catalog?"
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>模板B：针对采购经理</b>", h2))
story.append(section_box(
    "Hi [Name], I see you're in procurement at [Company]. "
    "We manufacture cleanroom wipers at factory-direct prices — "
    "potential cost savings for your supply chain. "
    "Interested in connecting?"
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>模板C：针对分销商/贸易商（最推荐）</b>", h2))
story.append(section_box(
    "Hello [Name], we're seeking distribution partners in [Country] "
    "for our cleanroom wiper line. Factory prices, flexible MOQ, "
    "custom branding. If open to new lines, would love to connect!"
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>模板D：短促有力版</b>", h2))
story.append(section_box(
    "Hi [Name], cleanroom wiper manufacturer from China. "
    "Competitive factory pricing. "
    "Looking to connect with [industry] professionals in [Country]. "
    "Catalog available upon request."
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>模板E：推荐参观 / 展会邀请</b>", h2))
story.append(section_box(
    "Hi [Name], we're exhibiting at [exhibition name] this [month]. "
    "Showcasing our cleanroom wiper line. "
    "Would you like to see samples? Happy to connect and discuss."
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>进阶技巧：</b>", h2))
story.append(Paragraph("✅ 加好友前先查看对方Profile，找共同点（校友、同行、共同群组）", bd))
story.append(Paragraph("✅ 用对方母语打招呼（土耳其语Merhaba、阿拉伯语Marhaba）可提高通过率30%+", bd))
story.append(Paragraph("✅ 不要发链接、不要立即推销，先建立关系", bd))
story.append(Paragraph("✅ 每周添加20~30个新连接，保持节奏", bd))
story.append(PageBreak())

# ===== Section 5: Follow-up Sequence =====
story.append(Paragraph("<b>5. 连接后跟进序列（7天转化流程）</b>", h1))
story.append(Paragraph("对方通过连接请求后，你有黄金72小时来跟进。不要拖延！", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>👉 Day 1：感谢 + 自我介绍</b>", h2))
story.append(section_box(
    "Thanks for connecting! I'm [Name] from Yuanjie Cleanroom Products in Wuxi, China.\n\n"
    "We specialize in manufacturing cleanroom wipers:\n"
    "• DS Series (Electronic Grade): Class 100~1000, 4\"×4\" to 18\"×18\"\n"
    "• KH Series (Industrial Grade): Cost-effective for general cleaning\n\n"
    "Would you be interested in our product catalog and FOB pricing? Happy to share."
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>👉 Day 3：价值传递（无回复时）</b>", h2))
story.append(section_box(
    "Hi [Name], following up on my previous message.\n\n"
    "Quick highlights of what we offer:\n"
    "• Factory-direct pricing — no middleman markups\n"
    "• Custom sizes, packaging, and LOGO printing available\n"
    "• MOQ as low as 100 packs per SKU\n"
    "• Samples available for evaluation\n\n"
    "What's the best way to reach you? Email or WhatsApp?"
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>👉 Day 7：最终跟进 + 免打扰</b>", h2))
story.append(section_box(
    "Hi [Name], just one last follow-up. If the timing isn't right, no problem at all!\n\n"
    "I'll leave my contact info here in case you ever need:\n"
    "• WhatsApp: [+86xxxx]\n"
    "• Email: [your@email.com]\n\n"
    "Feel free to reach out anytime. Wishing you a great week ahead!"
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>核心原则：</b>", h2))
story.append(Paragraph("• 不催单、不pushy，每个消息都要提供价值", bd))
story.append(Paragraph("• 每一条消息都简短（不超过100词）", bd))
story.append(Paragraph("• 没有回复也不气馁，过1个月再尝试一次", bd))
story.append(Paragraph("• 始终保持专业和礼貌", bd))
story.append(PageBreak())

# ===== Section 6: InMail Templates by Market =====
story.append(Paragraph("<b>6. InMail & 消息模板（分市场版）</b>", h1))
story.append(Paragraph("不同市场的客户关注点不同。针对性地调整话术，转化率更高。", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>🇹🇷 土耳其市场 — 价格敏感型</b>", h2))
story.append(section_box(
    "Merhaba [Name],\n\n"
    "I'm reaching out from Yuanjie Cleanroom in China. We manufacture cleanroom wipers "
    "(DS electronic grade, Class 100-1000) at very competitive factory prices.\n\n"
    "I understand the Turkish market is price-sensitive — our factory-direct model "
    "means we can offer better pricing than trading companies.\n\n"
    "Key products popular in Turkey: DS-0606 (6×6\"), DS-0909 (9×9\")\n"
    "CIF Istanbul delivery available.\n\n"
    "Would you like to see our catalog? Size and packaging can be customized.\n\n"
    "Teşekkürler! (Thank you)"
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>🇦🇪 中东市场 — 品质 + 信任型</b>", h2))
story.append(section_box(
    "Hello [Name],\n\n"
    "We are a Chinese cleanroom wiper manufacturer looking for reliable partners in the UAE.\n\n"
    "Our products are used in electronics, semiconductor, and pharmaceutical cleanrooms "
    "(Class 100-1000). We offer:\n"
    "• High-quality laser-sealed edge wipers\n"
    "• Professional packaging suitable for cleanroom entry\n"
    "• CIF Dubai / Jebel Ali delivery\n"
    "• Bulk and custom packaging options\n\n"
    "Would you be open to a quick call to discuss potential cooperation?"
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>🇵🇱🇨🇿 东欧市场 — 合规 + 品质型</b>", h2))
story.append(section_box(
    "Dear [Name],\n\n"
    "I'm contacting you from Yuanjie Cleanroom Products, a Chinese manufacturer "
    "of premium cleanroom wipers.\n\n"
    "For the European market, we can arrange RoHS compliance testing. "
    "Our products offer excellent quality at competitive pricing.\n\n"
    "Popular sizes in your market: DS-0909 (9×9\"), DS-1212 (12×12\")\n"
    "CIF Gdansk / Hamburg available.\n\n"
    "Would you be interested in discussing a trial order?"
))
story.append(PageBreak())

# ===== Section 7: Content Strategy =====
story.append(Paragraph("<b>7. 内容营销策略：从被看到被信任</b>", h1))
story.append(Paragraph("发布有价值的内容，让潜在客户主动接触你。这是LinkedIn长效获客的关键。", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>7.1 内容选题方向</b>", h2))
content_table = [
    ["内容类型", "示例", "发布频率"],
    ["工厂实拍+生产过程", "无尘布激光切割视频", "每周1次"],
    ["产品优势对比", "激光封边 vs 冷裁对比", "每2周1次"],
    ["客户案例", "某土耳其客户成功案例", "每月1次"],
    ["行业科普", "Class 100 vs Class 1000区别", "每2周1次"],
    ["出口知识", "中国到土耳其的物流方案", "每月1次"],
    ["生活方式+工作", "工厂日常/团队介绍", "每月1~2次"],
]
ct = Table(
    [[Paragraph(c, hc if i==0 else bd) for c in row] for i, row in enumerate(content_table)],
    colWidths=[PW*0.28, PW*0.42, PW*0.3]
)
ct.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(ct)
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>7.2 英文帖文模板</b>", h2))
story.append(section_box(
    "📦 Just shipped another container of DS Series cleanroom wipers to Turkey!\n\n"
    "Our factory-direct model means competitive pricing without sacrificing quality.\n\n"
    "DS Series highlights:\n"
    "✅ Laser-sealed edges — minimal particle shedding\n"
    "✅ Class 100~1000 cleanroom compatible\n"
    "✅ Custom sizes: 4×4\" to 18×18\"\n"
    "✅ Private labeling available\n\n"
    "Looking for distribution partners in Turkey & Middle East.\n"
    "DM me for catalog & pricing! 📩"
))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>7.3 中文帖文模板</b>", h2))
story.append(section_box(
    "🇨🇳 无锡源洁无尘布 ｜ 工厂直供 ｜ 诚招海外代理\n\n"
    "我们专注生产无尘布/擦拭布10年+，核心优势：\n"
    "✅ DS系列电子级：Class 100~1000，激光封边，低发尘\n"
    "✅ KH系列工业级：高性价比，适用一般车间清洁\n"
    "✅ 尺寸/包装/LOGO均可定制\n"
    "✅ MOQ灵活，样品可寄\n\n"
    "目标市场：土耳其、中东、东欧、独联体\n"
    "欢迎采购经理、分销商联系！"
))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>7.4 互动技巧</b>", h2))
story.append(Paragraph("• 在目标客户发的帖文下留言（有价值评论，不是广告）", bd))
story.append(Paragraph("• 关注行业大V，在他们的帖文下露脸", bd))
story.append(Paragraph("• 发帖时@相关公司或行业机构", bd))
story.append(Paragraph("• 使用话题标签：#cleanroom #wiper #manufacturing #supplychain #ChinaSupplier", bd))
story.append(Paragraph("• 最佳发布时间：周二~周四 上午8-10点 / 下午4-6点（目标市场当地时间）", bd))
story.append(PageBreak())

# ===== Section 8: Conversion Flow =====
story.append(Paragraph("<b>8. 转化流程：从好友到询盘到订单</b>", h1))
story.append(Paragraph("把LinkedIn好友转化成实际客户的标准化流程：", bd))
story.append(Spacer(1, 3*mm))

flow_steps = [
    ["步骤", "动作", "工具", "预期结果"],
    ["1", "搜索+添加好友（每天20人）", "LinkedIn / Sales Nav", "每周100+新连接"],
    ["2", "通过后24h内发感谢消息", "LinkedIn DM", "20~30%回复率"],
    ["3", "发送产品目录PDF + 报价", "WhatsApp / Email", "10~15%继续沟通"],
    ["4", "确认需求+推荐型号", "WhatsApp / WeChat", "5~8%发正式询盘"],
    ["5", "寄样品 / 发PI", "Email + 快递", "3~5%确认样品"],
    ["6", "跟进样品+确认订单", "WhatsApp / Email", "1~2%下首单"],
    ["7", "交付+维护+返单", "长期跟进", "复购率目标30%+"],
]
flow_t = Table(
    [[Paragraph(c, hc if i==0 else bd) for c in row] for i, row in enumerate(flow_steps)],
    colWidths=[PW*0.1, PW*0.25, PW*0.35, PW*0.3]
)
flow_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(flow_t)
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>转化率预估（每100个新连接）：</b>", h2))
story.append(Paragraph("100个连接 → 30个回复 → 15个有兴趣 → 8个要报价 → 3个寄样品 → 1~2个下首单", bd))
story.append(Paragraph("按每周加100人，月均400人计算，每月稳定获取4~8个有效询盘，转化1~2个订单。", bd))
story.append(PageBreak())

# ===== Section 9: Daily Plan =====
story.append(Paragraph("<b>9. 每日/每周执行计划</b>", h1))
story.append(Paragraph("成功来自持续的执行。以下是一周的执行节奏：", bd))
story.append(Spacer(1, 3*mm))

story.append(Paragraph("<b>📅 周一：客户搜索 + 添加好友（1小时）</b>", h2))
story.append(Paragraph("• 搜索2~3个关键词，找到30个目标客户", bd))
story.append(Paragraph("• 逐个查看Profile，个性化修改加好友邀请", bd))
story.append(Paragraph("• 记录到CRM或Excel", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>📅 周二：跟进上周通过的好友（30分钟）</b>", h2))
story.append(Paragraph("• 发感谢消息 + 介绍公司", bd))
story.append(Paragraph("• 有回复的转到WhatsApp/Email继续沟通", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>📅 周三：内容发布 + 互动（30分钟）</b>", h2))
story.append(Paragraph("• 发布一篇帖文（工厂实拍/产品知识/行业见解）", bd))
story.append(Paragraph("• 在5~10个目标客户的帖文下留言", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>📅 周四：跟进 + 深度沟通（1小时）</b>", h2))
story.append(Paragraph("• 跟进未回复的连接（Day 3 / Day 7模板）", bd))
story.append(Paragraph("• 与有兴趣的客户深入沟通需求", bd))
story.append(Spacer(1, 2*mm))

story.append(Paragraph("<b>📅 周五：闭环 + 下周准备（30分钟）</b>", h2))
story.append(Paragraph("• 记录本周进展：新加好友数、聊天数、潜在客户数", bd))
story.append(Paragraph("• 准备下周的搜索关键词列表", bd))
story.append(Paragraph("• 清理已成交或已关闭的线索", bd))
story.append(Spacer(1, 5*mm))

story.append(section_box(
    "💡 小贴士：\n"
    "• 坚持最重要，前两周效果不明显是正常的\n"
    "• 每周至少发3条朋友圈式的内容帖\n"
    "• 记录什么话术转化率高，持续优化\n"
    "• 目标客户国家的节假日要避开（如斋月、圣诞节等）"
))
story.append(PageBreak())

# ===== Section 10: Tools =====
story.append(Paragraph("<b>10. 工具推荐 & 效率提升技巧</b>", h1))
story.append(Spacer(1, 2*mm))

tools = [
    ["工具", "用途", "费用"],
    ["LinkedIn Sales Navigator", "高级搜索、InMail、潜在客户提醒", "~$80/月"],
    ["Dux-Soup", "自动访问Profile、自动加好友", "免费版可用"],
    ["Hunter.io", "查找企业邮箱", "免费25次/月"],
    ["Apollo.io", "B2B数据库+邮箱+LinkedIn集成", "免费版可用"],
    ["Notion / Excel", "客户关系管理（CRM）", "免费"],
    ["Canva", "制作帖子图片、Profile背景图", "免费"],
    ["Grammarly", "英文写作辅助", "免费"],
    ["WhatsApp Business", "海外客户即时沟通", "免费"],
]
tool_t = Table(
    [[Paragraph(c, hc if i==0 else bd) for c in row] for i, row in enumerate(tools)],
    colWidths=[PW*0.35, PW*0.4, PW*0.25]
)
tool_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#2b5a8c")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(tool_t)
story.append(Spacer(1, 5*mm))

story.append(Paragraph("<b>⚠️ 避坑指南 / 常见禁忌</b>", h2))
story.append(Paragraph("❌ 不要通过好友后立即发长篇广告——先建立关系", bd))
story.append(Paragraph("❌ 不要每天加超过50人——容易被LinkedIn限制账号", bd))
story.append(Paragraph("❌ 不要复制粘贴一模一样的消息——被举报Spam", bd))
story.append(Paragraph("❌ 不要只加人不聊天——连接数量不如质量重要", bd))
story.append(Paragraph("✅ 每天登录互动，保持账号活跃度", bd))
story.append(Paragraph("✅ 新账号先养1~2周（每天看看、点点赞），再开始加人", bd))
story.append(Paragraph("✅ 加好友频率：第二天20人、第三天30人、以后每天30~40人", bd))
story.append(PageBreak())

# ===== Appendix =====
story.append(Paragraph("<b>附录：常用中英文行业术语对照</b>", h1))
story.append(Spacer(1, 3*mm))

glossary = [
    ["中文", "English"],
    ["无尘布 / 无尘擦拭布", "Cleanroom Wiper / Cleanroom Wipe"],
    ["工业擦拭布", "Industrial Wipe / Industrial Wiper"],
    ["电子级", "Electronic Grade"],
    ["涤纶+锦纶针织", "Polyester + Nylon Knitted"],
    ["激光封边", "Laser-sealed Edge / Laser Cut"],
    ["超声波切割", "Ultrasonic Cut"],
    ["冷裁", "Cold Cut"],
    ["发尘量", "Particle Emission / Linting"],
    ["Class 100 ~ Class 1000", "ISO Class 5 ~ ISO Class 6"],
    ["真空包装", "Vacuum Pack / Vacuum Bagging"],
    ["双层包装", "Double Bagged"],
    ["私人标签 / 贴牌", "Private Label / OEM"],
    ["样品包", "Sample Pack / Sample Kit"],
    ["出厂价", "EXW (Ex Works)"],
    ["船上交货", "FOB (Free On Board)"],
    ["到岸价", "CIF (Cost, Insurance, Freight)"],
    ["形式发票", "PI (Proforma Invoice)"],
    ["起订量", "MOQ (Minimum Order Quantity)"],
    ["采购经理", "Procurement Manager / Purchasing Manager"],
    ["供应链总监", "Supply Chain Director"],
    ["分销商 / 经销商", "Distributor / Reseller"],
    ["首单 / 试单", "Trial Order / First Order"],
    ["复购 / 返单", "Repeat Order"],
]
gl_t = Table(
    [[Paragraph(c, hc if i==0 else bd) for c in row] for i, row in enumerate(glossary)],
    colWidths=[PW*0.38, PW*0.62]
)
gl_t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#ccc")),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story.append(gl_t)
story.append(Spacer(1, 8*mm))
story.append(Paragraph("--- End of LinkedIn Playbook ---", ft))
story.append(Paragraph("Version V1.0 | Created: 2026-07-14 | Powered by Yuanjie Cleanroom Products", ft))

doc.build(story)
sz = os.path.getsize(OUTPUT)
print(f"OK: {OUTPUT} ({sz//1024} KB)")
