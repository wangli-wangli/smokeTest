import hashlib

str = "15176128570"
m = hashlib.md5()
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()
str_md5 = str_md5.upper()
print("pw")
#vars.put("pw",str_md5)