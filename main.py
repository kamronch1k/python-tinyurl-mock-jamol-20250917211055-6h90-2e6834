import hashlib
s='jamolsafe'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
