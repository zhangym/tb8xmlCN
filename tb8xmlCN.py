# -*- coding: UTF-8 -*-

import sys, re

def func(m):
    return chr(int(m.group(1).title()))

if len(sys.argv) != 2:
        print("Usage：python tb8xmlCN <inputFile>")
else:
    strfin =  sys.argv[1] + ".xml"
    strfout = sys.argv[1] + "_out.xml"
    fin = open(strfin, 'r')
    fout = open(strfout, 'w', encoding='utf-8')
    key = fin.read()
    
    p1 = r"&amp;#(\d{5});"  # 这是我们写的正则表达式规则
    pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
    res = pattern1.findall(key)
    newKey = re.sub(p1, func, key)
    fout.write(newKey)
    fin.close()
    fout.close()
    print("\nOK, Success!.\n")




