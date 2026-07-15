import subprocess, json

# Create pages fresh
cmd = [
    'curl.exe', '-s', '-X', 'POST',
    'https://api.github.com/repos/cmdcsz-collab/cleanroom-wiper/pages',
    '-H', 'Authorization: Bearer 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',
    '-H', 'Accept: application/vnd.github+json',
    '-H', 'Content-Type: application/json',
    '-d', '{"source":{"branch":"main","path":"/"}}'
]
r = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
print(r.stdout[:500])
print('RC:', r.returncode)
