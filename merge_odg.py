import zipfile, os, re, shutil, io
os.chdir('D:/AI项目/无尘布项目')

with zipfile.ZipFile('无尘布产品目录_Cleanroom_Wiper_Catalog.odg', 'r') as z:
    content = z.read('content.xml').decode('utf-8')

# Find page boundaries  
page_tags = list(re.finditer(r'<draw:page[ >]', content))
closing_tags = list(re.finditer(r'</draw:page>', content))

# Extract page 4's frame - it's a single image frame
p4_start = page_tags[3].start()
p4_gt = content.index('>', page_tags[3].start()) + 1
p4_end_tag = closing_tags[3].start()
p4_inner = content[p4_gt:p4_end_tag]

# Modify the frame to position it below page 3 content
# Last element on page 3 ends at y=24.898cm, so place at y=25.2cm
old_y = re.search(r'svg:y="([^"]+)"', p4_inner)
old_h = re.search(r'svg:height="([^"]+)"', p4_inner)
old_w = re.search(r'svg:width="([^"]+)"', p4_inner)
old_x = re.search(r'svg:x="([^"]+)"', p4_inner)

print(f'Old: x={old_x.group(1)} y={old_y.group(1)} w={old_w.group(1)} h={old_h.group(1)}')

# Calculate new dimensions to fit in available ~4.5cm height
old_h_cm = float(old_h.group(1).replace('cm',''))
old_w_cm = float(old_w.group(1).replace('cm',''))

# Scale to fit in 4cm height
new_h = 4.0
scale = new_h / old_h_cm
new_w = old_w_cm * scale
new_x = (21 - new_w) / 2  # Center horizontally on A4
new_y = 25.3  # Below last page 3 element

print(f'New: x={new_x:.3f}cm y={new_y}cm w={new_w:.3f}cm h={new_h}cm')

# Apply the changes
new_frame = p4_inner.replace(old_y.group(0), f'svg:y=\"{new_y}cm\"')
new_frame = new_frame.replace(old_h.group(0), f'svg:height=\"{new_h}cm\"')
new_frame = new_frame.replace(old_w.group(0), f'svg:width=\"{new_w:.3f}cm\"')
new_frame = new_frame.replace(old_x.group(0), f'svg:x=\"{new_x:.3f}cm\"')

# Insert into page 3 (before closing tag)  
p3_close_close = closing_tags[2].start()
new_content = content[:p3_close_close] + '\n' + new_frame + '\n' + content[p3_close_close:]

# Remove page 4 (adjust indices after insertion)
# Page 4 now starts further in the file
new_p4_start = new_content.find('<draw:page draw:name=\"page4\"')
new_p4_close = new_content.find('</draw:page>', new_p4_start) + len('</draw:page>')
final_content = new_content[:new_p4_start] + new_content[new_p4_close:]

# Save the modified ODG
with zipfile.ZipFile('无尘布产品目录_Cleanroom_Wiper_Catalog.odg', 'r') as z:
    all_files = {name: z.read(name) for name in z.namelist()}

import tempfile
tmp_odg = '无尘布产品目录_Cleanroom_Wiper_Catalog_merged.odg'
with zipfile.ZipFile(tmp_odg, 'w', zipfile.ZIP_DEFLATED) as zout:
    for name, data in all_files.items():
        if name == 'content.xml':
            zout.writestr(name, final_content.encode('utf-8'))
        else:
            zout.writestr(name, data)

print('Created merged ODG')
