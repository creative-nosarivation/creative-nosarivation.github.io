import os, json, re

posts = []
posts_dir = 'posts'

for fname in sorted(
    [f for f in os.listdir(posts_dir) if f.endswith('.md')],
    reverse=True
):
    with open(os.path.join(posts_dir, fname), encoding='utf-8') as f:
        text = f.read()

    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()

    posts.append({
        'file': fname,
        'date': fm.get('date', ''),
        'category': fm.get('category', 'お知らせ'),
        'title': fm.get('title', fname.replace('.md', '')),
        'image': fm.get('image', '')
    })

out = os.path.join(posts_dir, 'index.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f'Generated {len(posts)} posts')
