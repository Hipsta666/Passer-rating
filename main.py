"""Case-study #4 Парсинг web-страниц
Разработчики:
Овечкин А.С. Потапович С.А.

"""
import urllib.request

l = 0
f_out = open("output.txt", "w")
print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}'.format("Name", "COMP", "ATT", "YDS", "TD", "INT", "RATE"), file=f_out)
print("-"*60, file=f_out)
with open("input.txt", "r") as f_input:
    f_text = f_input.readlines()
    for line in range(len(f_text)):

        url = f_text[line]

        f = urllib.request.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find("player-name")
        name = text[text.find('>', part_name) + 1:text.find('&', part_name)]

        TOTAL = text.find("TOTAL")
        num = text[text.find('/td', TOTAL) + 1:text.find('/tr', TOTAL)]

        a = num.replace('t', '')
        b = a.replace('d', '')
        c = b.replace('n', '')
        e = c.replace('\\', '')
        k = e.replace('/', '')
        g = k.replace('<>', ' ')
        ff = g.replace('TOTAL', '')
        j = ff.replace('  ', ' ')
        t = j.replace(',', '')
        y = t.replace('>', '')
        tt = y[:41]


        for i in range(10):
            qwe = tt[tt.find(" ") + 1:tt.find(" ", tt.find(" ") + 2)]
            tt = tt[len(qwe) + 1:]

            if i == 0:
                comp = int(qwe)
            if i == 1:
                att = int(qwe)
            if i == 3:
                yds = int(qwe)
            if i == 5:
                td = int(qwe)
            if i == 6:
                INT = int(qwe)

        rate = ((((comp / att - .3) * 5) +
                 ((yds / att - 3) * .25) + ((td / att) * 20) +
                 (2.375 - (INT / att * 25))) / 6) * 100

        print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7.2f}'.format(name, comp, att, yds, td, INT, rate), file=f_out)
f_out.close()