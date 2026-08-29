import os, zipfile
p = r'c:\Users\user\Documents\GitHub\Unjumble-Game\Unjumble-Game\Unjumble Game 피드백.xlsx'
print('EXISTS', os.path.exists(p))
if not os.path.exists(p):
    raise SystemExit(0)
with zipfile.ZipFile(p) as z:
    names = z.namelist()
    print('NAMES', names[:40])
    for name in names:
        if name.endswith('.xml') or name.endswith('.rels'):
            print('---', name)
            data = z.read(name)
            print(data[:400].decode('utf-8', 'replace'))
