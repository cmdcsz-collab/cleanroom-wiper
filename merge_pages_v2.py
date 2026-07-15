import zipfile, os, re, shutil, io
from xml.etree import ElementTree as ET

os.chdir('D:/AI项目/无尘布项目')

# Read the ODG
with zipfile.ZipFile('无尘布产品目录_Cleanroom_Wiper_Catalog.odg', 'r') as z:
    content_xml = z.read('content.xml').decode('utf-8')

# Find page boundaries
page_tags = list(re.finditer(r'<draw:page[ >]', content_xml))
closing_tags = list(re.finditer(r'</draw:page>', content_xml))

p3_start = page_tags[2].start()
p3_content_start = content_xml.index('>', page_tags[2].start()) + 1
p3_end = closing_tags[2].start() + len('</draw:page>')

p4_start = page_tags[3].start()
p4_content_start = content_xml.index('>', page_tags[3].start()) + 1
p4_end = closing_tags[3].start() + len('</draw:page>')

# Get page 4's inner content (the image frame)
p4_inner = content_xml[p4_content_start:closing_tags[3].start()]
print('Page 4 inner content:')
print(p4_inner[:500])

# Get page 3 open tag
p3_open_tag = content_xml[p3_start:p3_content_start]
print()
print('Page 3 open tag:', p3_open_tag)
