"""
Name: frede
Filename: attendance.py
Date: 8/8/2021
"""
STRING = '''DENON CHONG CHENG ZONG
ROY TAN WEI MING
TEO XU KAI
TANG SIU YUEN ENOCH 
ONG ZI XUAN, MAX
LIM SING THAI TIGER
LIM ZHI HAO DARIUS
V. S. ASHOK BALAJI
LIM WEI WEN 
MANT KOH EN WEI
TOK VALENTINO
LEE JUN LIANG
PEH BOON WAH
ALOYSIUS TAY HUI MING
WONG WEI HAN
KENNETH WANG YONG QI
TEO YOU XIANG 
JOEL LOH KONG JANN
TAN JING HAN CHAD
HO SHANG WEE
BRYAN GOH WEI HAO
BECKHAM LEE WEN JIE
CHIA MING JIU
ANG JING LIANG
DERRICK LIM KAH HAO
CLEON TAY SHI HONG
ONG JUN HENG, JAMES
DARRYL DAN WAH PING
REYNALDI CHEOK
FREDERICK LIAU YAN CHUEN
GARETH YEO WEI JUN
ERIC KOH MENG HWAN
CHESTON LEE MING XUAN
KIEFER KOH KANG REI
ALVIN YEO ZONG HENG
AARON JOEL TAN TZE ERN
TAY SHAO AN JONATHAN
ANAKIN
JIA YANG
ADWIN
'''

def main(string):
    lst = string.split('\n')
    print(len(lst))
    while True:
        user_input = input("name").upper()[4:]
        for name in lst:
            if user_input == 'QUIT':
                print(lst)
                break
            if user_input in name:
                lst.remove(name)



if __name__ == '__main__':
    main(STRING)
