"""Case-study #4 Парсинг web-страниц
Разработчики:
Овечкин А.С. Потапович С.А.

"""
import urllib.request
url = 'http://www.nfl.com/player/mattmoore/2507282/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]
print(name)

TOTAL = text.find('TOTAL')
num = text[TOTAL:text.find("<td>66</td>")]


a = num.replace('t','')
b = a.replace('d', '')
c = b.replace('n', '')
e = c.replace("\\", "")
k = e.replace('/','')
g = k.replace('<>'," ")
f = g.replace('TOTAL', '')
j = f.replace('  ', ' ')
t = j.replace(',', '')
print(t)
h = ''
p = 0
for i in range(11):
    qwe = t[t.find(" ")+1:t.find(" ", t.find(" ")+2)]
    t = t[len(qwe)+1:]
    if str(i) in '01356':
        h += str(qwe) + ' '
    if i == 0:
        comp = int(qwe)
    if i == 1:
        att = int(qwe)
    if i == 3:
        yds = int(qwe)
    if i == 5:
        td = int(qwe)
    if i == 6:
        int = int(qwe)

print(h)
print(comp*3)

print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}'.format(name, comp, att, yds, td, int))