#!/usr/bin/env python3

import sys

yanglao_bx = 0.08
yiliao_bx = 0.02
shiye_bx = 0.005
gongshang_bx = 0
shengyu_bx = 0
gongjijin = 0.06
wuxianyijin = yanglao_bx + yiliao_bx + shiye_bx + gongshang_bx + shengyu_bx + gongjijin

def jisuan_ynse(ynssdr):
    if ynssdr > 80000:
        ynse = ynssdr * 0.45 -13505
    elif ynssdr > 55000:
        ynse = ynssdr * 0.35 - 5505
    elif ynssdr > 35000:
        ynse = ynssdr * 0.30 -2755
    elif ynssdr > 9000:
        ynse = ynssdr * 0.25 -1005
    elif ynssdr > 4500:
        ynse = ynssdr * 0.20 -555
    elif ynssdr > 1500:
        ynse = ynssdr * 0.10 -105
    elif ynssdr > 0:
        ynse = ynssdr * 0.03
    else:
        ynse = 0
    return ynse
    


try:
    alist = sys.argv[1:]
    for i in alist:
        gonghao = i.split(":")[0]
        #print(gonghao)
        gzje = int(float(i.split(":")[1]))
        gzje = gzje * (1 - wuxianyijin)
        ynssdr = gzje - 3500
        #print(gzje)
        ynse = jisuan_ynse(ynssdr)
        #print(ynse)
        print('{} : {:.2f}'.format(gonghao,(gzje - ynse )))
except:
    print("Parameter Error")
    

