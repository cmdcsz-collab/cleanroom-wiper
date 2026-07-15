import zipfile, os, re, shutil
os.chdir('D:/AI项目/无尘布项目')

with zipfile.ZipFile('无尘布产品目录_Cleanroom_Wiper_Catalog_orig.odg', 'r') as z:
    content = z.read('content.xml').decode('utf-8')
    all_files = {name: z.read(name) for name in z.namelist()}

# Find page boundaries
page_tags = list(re.finditer(r'<draw:page[ >]', content))
closing_tags = list(re.finditer(r'</draw:page>', content))

# Get page 4's frame
p4_start = page_tags[3].start()
p4_gt = content.index('>', p4_start) + 1
p4_close = closing_tags[3].start()
p4_inner = content[p4_gt:p4_close]

# Scale page 4's image to fit in ~14cm height
old_h = re.search(r'svg:height=\"([^\"]+)\"', p4_inner)
old_w = re.search(r'svg:width=\"([^\"]+)\"', p4_inner)
old_x = re.search(r'svg:x=\"([^\"]+)\"', p4_inner)
old_y = re.search(r'svg:y=\"([^\"]+)\"', p4_inner)

old_h_cm = float(old_h.group(1).replace('cm',''))
old_w_cm = float(old_w.group(1).replace('cm',''))

# Scale to 14cm height, center horizontally
new_h = 14.0
scale = new_h / old_h_cm
new_w = old_w_cm * scale
new_x = (21 - new_w) / 2
new_y = 15.5  # Below page 5 content (ends at ~15cm)

# Create modified frame
new_frame = p4_inner
new_frame = new_frame.replace(old_x.group(0), f'svg:x=\"{new_x:.3f}cm\"')
new_frame = new_frame.replace(old_y.group(0), f'svg:y=\"{new_y}cm\"')
new_frame = new_frame.replace(old_w.group(0), f'svg:width=\"{new_w:.3f}cm\"')
new_frame = new_frame.replace(old_h.group(0), f'svg:height=\"{new_h}cm\"')

# Insert into page 5 (before closing tag)
p5_close = closing_tags[4].start()
new_content = content[:p5_close] + '\n' + new_frame + '\n' + content[p5_close:]

# Remove page 4 (adjust indices)
p4_start_new = new_content.find('<draw:page draw:name=\"page4\"')
p4_close_new = new_content.find('</draw:page>', p4_start_new) + len('</draw:page>')
new_content2 = new_content[:p4_start_new] + new_content[p4_close_new:]

# Update company name in content.xml
new_content3 = new_content2.replace('深圳源洁', '深圳永新源')
new_content3 = new_content3.replace('Shenzhen Yuanjie', 'Shenzhen Yongxinyuan')

# Also update styles.xml for company name
styles = all_files.get('styles.xml', b'').decode('utf-8')
styles2 = styles.replace('深圳源洁', '深圳永新源')
styles2 = styles2.replace('Shenzhen Yuanjie', 'Shenzhen Yongxinyuan')

# Also update meta.xml
meta = all_files.get('meta.xml', b'').decode('utf-8')
meta2 = meta.replace('深圳源洁', '深圳永新源')
meta2 = meta2.replace('Shenzhen Yuanjie', 'Shenzhen Yongxinyuan')

# Write the merged ODG
tmp_odg = '无尘布产品目录_Cleanroom_Wiper_Catalog_new.odg'
with zipfile.ZipFile(tmp_odg, 'w', zipfile.ZIP_DEFLATED) as zout:
    for name, data in all_files.items():
        if name == 'content.xml':
            zout.writestr(name, new_content3.encode('utf-8'))
        elif name == 'styles.xml':
            zout.writestr(name, styles2.encode('utf-8'))
        elif name == 'meta.xml':
            zout.writestr(name, meta2.encode('utf-8'))
        else:
            zout.writestr(name, data)

print('Created new ODG with merged pages 4-5 and new company name')
