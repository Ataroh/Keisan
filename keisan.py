#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import sympify,pprint,Symbol,solve,init_printing,latex
import re

init_printing(use_unicode=True)

def SolveEqua(siki,moji):
    sikis = [siki[i] for i in range(len(siki))]
    que = []
    for s in sikis:
        lr = s.split("=")
        que.append(sympify(lr[0])-sympify(lr[1]))
    ans = solve(que,moji)#リスト、リストで連立になる
    #pprint(ans)
    #print(latex(ans))
    print(str(ans))

def Equation(text,moji):
    SolveEqua(text,moji)

def Math_Checker(t):
    #ゴリ押しリスト化
    t=t.replace(" ","")
    nums = [str(a) for a in range(10)]
    signs = ["+","-","*","/","^","=","(",")","{","}","[","]"]
    syms = ["abcdefghijklmnopqrstuvwxyz_"[i] for i in range(26+1)]

    for i in range(len(t)):
        if not (t[i] in nums or t[i] in signs or t[i] in syms):
            return False 
    b = (t.count("=") == 1 
         and t.count("(") == t.count(")") 
         and t.count("{") == t.count("}") 
         and t.count("[") == t.count("]"))
    return b

def Math_Encode(text):
    #正規表現とかで置き換え
    t = text.replace("^","**")
    #iとlen(t)の関係に注意
    i = 0
    while i < len(t)-1:
        if re.match("[a-z0-9]",t[i]) and (re.match("\(|\{|\[",t[i+1]) or re.match("[a-z]",t[i+1])):
            t = t[0:i+1] + "*" +  t[i+1:]
        i+=1
    #戻り値
    return t

def Toku(inps,nep):
    li = inps
    siki = list()
    for i in range(len(li)):
        siki.append(Math_Encode(li[i]))
    
    moji_s = set()
    for m in nep.split(","):
        moji_s.add(m)
    moji = list(moji_s)

    #print(siki)
    #print(moji)

    #equa = Math_Encode(inp)
    Equation(siki,moji)
    #"(2*x+1)*(x-2)=x**2+3*x"
    #x^3–9x^2+27x–27=0

while True:
    inp = input("数式を入力>>>")
    nep = input("解の文字を入力>>>")
    Toku(inp.split(","),nep)
