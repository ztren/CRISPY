#—————————————————————————————————————————————————————————————————————————————————————————————————————#
#
###########################################Crispy FUNCTIONS############################################
############################################RELEASE 1.1.0##############################################
#
#—————————————————————————————————————————————————————————————————————————————————————————————————————#
#CRISPY, the Dicebot
#Copyright (C) 2020 by SAIKA
#
#This program is free software: you can redistribute it and/or modify it
#under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with this program. If not, see http://www.gnu.org/licenses/.
#——————————————————————————————————————————————————————————————————————————————————————————————————————#
from random import *
from time import *
from copy import *
import os
import WordStr
import DiceConstant

def init():
    if not os.path.exists('groups/'+WordStr.GroupName):
        os.makedirs('groups/'+WordStr.GroupName)
    try:
        misc = open('groups/'+WordStr.GroupName+'/_misc',mode = 'x')
        initmisc = ['<cmd>\n/\n.\n。\n,\n，\n!\n！\n</cmd>\n',
        '<sep>\n,\n，\n/\n|\n \n</sep>\n'
        '<dt>\n'+strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')+'\n</dt>\n',
        '<rule>\ncocrule 0\nsend off\njrrp on\nrpt off\nmute off\nwelcome off\ndefaultdice 100\n</rule>\n',
        '<members>\n</members>\n<pu>\n</pu>\n<ob>\n</ob>\n']
        misc.writelines(initmisc)
        del initmisc
        misc.close()
    except:
        pass

def readpl(pl):
    pers = open('groups/'+WordStr.GroupName+'/'+pl,mode = 'r')
    a = pers.readlines()
    pers.close()
    return a

def writepl(pl,a):
    pers = open('groups/'+WordStr.GroupName+'/'+pl,mode = 'w')
    pers.writelines(a)
    pers.close()
    return

def readmisc(obj):
    misc = open('groups/'+WordStr.GroupName+'/_misc',mode = 'r')
    a = misc.readlines()
    misc.close()
    flag = False
    if obj == '':
        return a
    b = []
    for i in range(0,len(a)):
        if a[i] == '</'+obj+'>\n':
            flag = False
            return b
        if flag == True:
            b.append(a[i])
        if a[i] == '<'+obj+'>\n':
            flag = True
    raise IndexError

def writemisc(obj):
    misc = open('groups/'+WordStr.GroupName+'/_misc',mode = 'w')
    misc.writelines(obj)
    misc.close()
    return

def changemisc(obj,list):
    a = readmisc('')
    b,e = a.index('<'+obj+'>\n'),a.index('</'+obj+'>\n')
    a[b+1:e] = list
    writemisc(a)
    return

def readrule(obj):
    a = readmisc('rule')
    for i in range(0,len(a)):
        if a[i].split(' ')[0] == obj:
            return a[i][:-1].split(' ')[1]
        if i == len(a)-1:
            raise IndexError
    return

def changerule(obj,str):
    a = readmisc('rule')
    for i in range(0,len(a)):
        if a[i].split(' ')[0] == obj:
            a[i] = obj + ' ' + str + '\n'
            changemisc('rule',a)
            break
        if i == len(a)-1:
            raise IndexError
    return

def st(pl,nam,val):#更改数值
    val = str(val)
    a = readpl(pl)
    for i in range(0,len(a)):
        if a[i] == nam+'\n':
            a[i+1] = val+'\n'
            break
        elif i == len(a)-1:
            a += [nam+'\n',val+'\n']
    a[-1] = a[-1] + '\n' if '\n' not in a[-1] else a[-1]
    writepl(pl,a)
    return

def getvl(pl,nam):#获取数值
    a = readpl(pl)
    for i in range(0,len(a)-1):
        if a[i] == nam+'\n':
            return a[i+1][:-1]
    raise NameError

def syn(nam):
    for i in range(0,len(DiceConstant.syn)):
        if nam.upper() in DiceConstant.syn[i]:
            return DiceConstant.syn[i][0]
    return nam

def cmd(text):
    return text[1:] if text[0] == ' ' else text

def sep(text):
    a = readmisc('sep')
    for i in range(0,len(a)):
        if a[i][:-1] in text:
            return text.split(a[i][:-1])
    raise ValueError

def dice(expr):
    x,y = expr.split('d')
    if (int(x) > 100):
        raise ValueError
    elif (int(y) > 100000):
        raise TypeError
    sum = ''
    for i in range(0,int(x)):
        sum += str(randint(1,int(y))) + '+'
    sum = sum[:-1]
    if int(x) > 1:
        sum = '(' + sum + ')'
    return sum

def jdg(d,val):
    rule = int(readrule('cocrule'))
    t = ''
    if rule == 0:
        if d == 1:
            t = WordStr.GSuc
        elif val < 50:
            if d in range(96,101):
                t = WordStr.LFail
        elif val >= 50:
            if d == 100:
                t = WordStr.LFail
    elif rule == 1:
        if val < 50:
            if d == 1:
                t = WordStr.GSuc
            elif d in range(96,101):
                t = WordStr.LFail
        elif val >= 50:
            if d in range(1,6):
                t = WordStr.GSuc
            if d == 100:
                t = WordStr.LFail
    elif rule == 2:
        if d in range(1,6):
            if d <= val:
                t = WordStr.GSuc
        elif d > 95:
            if d > val:
                t = WordStr.LFail
    elif rule == 3:
        if d in range(1,6):
            t = WordStr.GSuc
        elif d > 95:
            t = WordStr.LFail
    elif rule == 4:
        if d in range(1,6):
            if d <= val // 10:
                t = WordStr.GSuc
        elif val < 50:
            if d >= 96 + val // 10:
                t = WordStr.LFail
        elif val >= 50:
            if d == 100:
                t = WordStr.LFail
    elif rule == 5:
        if d in range(1,3):
            t = WordStr.GSuc
        elif val < 50:
            if d in range(96,101):
                t = WordStr.LFail
        elif val >= 50:
            if d in range(99,101):
                t = WordStr.LFail
    if (t == ''):
        if d > val:
            t = WordStr.Fail
        elif d > val // 2:
            t = WordStr.Suc
        elif d > val // 5:
            t = WordStr.HardSuc
        else:
            t = WordStr.ExtremeSuc
    return t

def rbp(t,type):
    x1 = randint(1,100)
    x2 = []
    if t > 100:
        group.send(WordStr.TooManyDices)
        raise
    for i in range(0,t):
        x2.append(randint(0,9))
    x3 = deepcopy(x2)
    x3.append(x1 // 10)
    if x1 % 10 == 0:
        for i in range(0,len(x3)):
            x3[i] = 10 if x3[i] == 0 else x3[i]
    if type == 'b':
        x = min(x3) * 10 + x1 % 10
        k = '奖励'
    elif type == 'p':
        x = max(x3) * 10 + x1 % 10
        k = '惩罚'
    else:
        raise TypeError
    s = '{0}[{1}骰：{2}]'.format(x1,k,x2)
    return [x,s]

def calc(expr):
    opr = ['+','-','*','/','(',')']
    expr += '*'
    s = ''
    a = []
    li = 0
    for i in range(0,len(expr)):
        if expr[i] in opr:
            a += [expr[li:i],expr[i]]
            li = i + 1
    a.pop()
    for i in range(0,len(a)):
        if 'd' in a[i]:
            a[i] = dice(a[i])
        s += a[i]
    return s
