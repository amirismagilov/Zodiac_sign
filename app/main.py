from lib import zodiac_sign_calculation


date = '21.01.1994'
date = date.split('.')
# print(date)

mouth = int(date[1])
day = int(date[0])
sign = zodiac_sign_calculation(mouth, day)
print(sign)

link_part1 = "www.google.ru/search?newwindow=1&ei=HpByXMboM_LOrgT9xZyoAQ&q=гороскоп+"
link_part2 = "&oq=гороскоп+"
link_part3 = "&gs_l=psy-ab.3..0i203l10.5721.6984..7540...0.0..0.143.888.2j6......0....1..gws-wiz.......0i71.xiZCPVOXPUg"

link = link_part1 + sign + link_part2 + sign + link_part3
print("узнайте свой гороскоп по ссылке", link)