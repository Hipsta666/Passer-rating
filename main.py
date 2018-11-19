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

        # Clear the text of unnecessary characters
        change_1 = num.replace('t', '')
        change_2 = change_1.replace('d', '')
        change_3 = change_2.replace('n', '')
        change_4 = change_3.replace('\\', '')
        change_5 = change_4.replace('/', '')
        change_6 = change_5.replace('<>', ' ')
        change_7 = change_6.replace('TOTAL', '')
        change_8 = change_7.replace('  ', ' ')
        change_10 = change_8.replace(',', '')
        change_11 = change_10.replace('>', '')
        new_text = change_11[:41]

        # Choose the numbers we need from the resulting string
        for char in range(10):
            number = new_text[new_text.find(" ") + 1:new_text.find(" ", new_text.find(" ") + 2)]
            new_text = new_text[len(number) + 1:]

            if char == 0:
                comp = int(number)
            if char == 1:
                att = int(number)
            if char == 3:
                yds = int(number)
            if char == 5:
                td = int(number)
            if char == 6:
                INT = int(number)

        rate = ((((comp / att - .3) * 5) +
                 ((yds / att - 3) * .25) + ((td / att) * 20) +
                 (2.375 - (INT / att * 25))) / 6) * 100

        # write the resulting numbers to the output.txt file
        print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7.2f}'.format(name, comp, att, yds, td, INT, rate), file=f_out)
f_out.close()