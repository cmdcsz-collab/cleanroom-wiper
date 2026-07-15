import zipfile, os, re, shutil
os.chdir('D:/AI项目/无尘布项目')

with zipfile.ZipFile('无尘布产品目录_Cleanroom_Wiper_Catalog.odg', 'r') as z:
    content = z.read('content.xml').decode('utf-8')
    styles = z.read('styles.xml').decode('utf-8')

# Find page style dimensions
page_styles = re.findall(r'<style:page-layout[^>]*>.*?</style:page-layout>', styles, re.DOTALL)
for ps in page_styles:
    name = re.search(r'style:name="([^"]+)"', ps)
    dims = re.search(r'fo:page-width="([^"]+)".*?fo:page-height="([^"]+)"', ps)
    if name and dims:
        print(f'Style {name.group(1)}: {dims.group(1)} x {dims.group(2)}')

# Find all pages
page_starts = [m.start() for m in re.finditer(r'<draw:page ', content)]
page_ends_tag = [m.end() for m in re.finditer(r'</draw:page>', content)]
page_ends = [m.start()+len('</draw:page>') for m in re.finditer(r'</draw:page>', content)]

print(f'Total pages: {len(page_starts)}')

# Get page 3 content
p3_start = page_starts[2]
p3_tag_end = content.index('>', p3_start) + 1
p3_end = page_ends[2]
p3_xml = content[p3_start:p3_end]
print(f'Page 3 length: {len(p3_xml)} chars')

# Get page 4 content  
p4_start = page_starts[3]
p4_tag_end = content.index('>', p4_start) + 1
p4_end = page_ends[3]
p4_xml = content[p4_start:p4_end]
print(f'Page 4 length: {len(p4_xml)} chars')

# Get Y coordinates from page 3
y_vals = re.findall(r'svg:y="([^"]+)"', p3_xml)
print(f'Page 3 Y values: {y_vals[-5:]}')
