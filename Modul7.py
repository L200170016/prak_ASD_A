#nama : Dessy Nur Azizah
#nim  : L200170016
#kelas: A


import re

#nomer1
s = open('Indonesia.txt', 'r')
teks = s.read()
s.close()
g = r"me\w+"
cocok = re.findall(g,teks)
print(cocok)

#nomer2
b = open('Indonesia.txt', 'r')
teks1 = b.read()
b.close()
k = r"di\w+"
string = re.findall(k,teks1)
print(string)

#nomer3
f = open('Indonesia.txt', 'r')
teks2 = f.read()
f.close()
l = r"di\s\w+"
string1 = re.findall(l,teks2)
print(string1)

#nomer4
u = open('KEI.html', 'r', encoding = 'latin1')
teks3 = u.read()
u.close()
pola = r'(\w+)</a></td>'
tampil = re.findall(pola,teks3)
print(tampil)

#nomer4b
p = open('KEI.html','r', encoding='latin1')
teks4 = p.read()
p.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)

