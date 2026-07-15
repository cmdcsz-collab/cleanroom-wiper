import zipfile, os, re, shutil
os.chdir('D:/AI项目/无尘布项目')

with zipfile.ZipFile('无尘布产品目录_Cleanroom_Wiper_Catalog.odg', 'r') as z:
    content = z.read('content.xml').decode('utf-8')

# Find all draw frames in page 3
page_starts = [m.start() for m in re.finditer(r'<draw:page ', content)]
page_ends = [m.start()+len('</draw:page>') for m in re.finditer(r'</draw:page>', content)]

p3 = content[page_starts[2]:page_ends[2]]
p4 = content[page_starts[3]:page_ends[3]]

# Show all frames in page 3
frames3 = re.findall(r'<draw:frame[^>]*>.*?</draw:frame>', p3, re.DOTALL)
for i, f in enumerate(frames3):
    y = re.search(r'svg:y="([^"]+)"', f)
    h = re.search(r'svg:height="([^"]+)"', f)
    x = re.search(r'svg:x="([^"]+)"', f)
    w = re.search(r'svg:width="([^"]+)"', f)
    has_img = '<draw:image' in f
    text = bool(re.search(r'<text:', f))
    print(f'Frame {i}: x={x.group(1) if x else "?"} y={y.group(1) if y else "?"} w={w.group(1) if w else "?"} h={h.group(1) if h else "?"} text={text} img={has_img}')

print()
# Show page 4 frame
frames4 = re.findall(r'<draw:frame[^>]*>.*?</draw:frame>', p4, re.DOTALL)
for i, f in enumerate(frames4):
    y = re.search(r'svg:y="([^"]+)"', f)
    h = re.search(r'svg:height="([^"]+)"', f)
    x = re.search(r'svg:x="([^"]+)"', f)
    w = re.search(r'svg:width="([^"]+)"', f)
    print(f'Page4 Frame {i}: x={x.group(1) if x else "?"} y={y.group(1) if y else "?"} w={w.group(1) if w else "?"} h={h.group(1) if h else "?"}')
