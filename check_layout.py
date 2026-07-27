import zipfile, re
z = zipfile.ZipFile("D:/AI项目/无尘布项目/无尘布产品目录_Cleanroom_Wiper_Catalog.odg")
c = z.read("content.xml").decode("utf-8")
pages = re.findall(r"<draw:page[> ].*?</draw:page>", c, re.DOTALL)

p4 = pages[3]
frames = re.findall(r"<draw:frame[^>]*>.*?</draw:frame>", p4, re.DOTALL)
max_bottom = 0
for f in frames:
    ym = re.search(r'svg:y="([^"]+)"', f)
    hm = re.search(r'svg:height="([^"]+)"', f)
    if ym and hm:
        y = float(ym.group(1).replace("cm",""))
        h = float(hm.group(1).replace("cm",""))
        b = y + h
        if b > max_bottom:
            max_bottom = b
print("Page 4 content extends to: %.1f cm" % max_bottom)
print("A4 height: 29.7 cm")
print("Fits:", max_bottom <= 29.7)

# Check original page 5 frame extent
p5_orig = pages[4]  # original page 6 in new numbering
frames5 = re.findall(r"<draw:frame[^>]*>.*?</draw:frame>", p5_orig, re.DOTALL)
max_b = 0
for f in frames5:
    ym = re.search(r'svg:y="([^"]+)"', f)
    hm = re.search(r'svg:height="([^"]+)"', f)
    if ym and hm:
        b = float(ym.group(1).replace("cm","")) + float(hm.group(1).replace("cm",""))
        if b > max_b: max_b = b
print("Page 5 (orig 6) extends to: %.1f cm" % max_b)
