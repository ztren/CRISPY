######DICEBOT VER 5.3.1######
##########BY  ZTREN##########
#———————————————————————————#
#MODIIFYING OF THIS FILE IS##
#NOT ADVICED UNLESS YOU KNOW#
######WHAT YOU ARE DOING#####

from wxpy import *
from random import *
from math import *
from time import *
from re import *
from json import *
from copy import *
from threading import *

import os
import WordStr

bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
group = bot.groups().search(WordStr.GroupName)[0]
CRD = ['STR','CON','SIZ','DEX','APP','POW','EXP','INT','EDU','LUK']#人物卡

rpt = False#随机复读开关
pu = []#存放用户PUID
nm = []#存放用户名
pl = []#存放用户人物卡
en = []#存放敌方单位数据
rp = []#存放用户人品
dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')#当前时间
rgnm = False
rgid = -1
ennm = False
enid = -1
Muted = False
TimerOn = False

class pers:
    def __init__(self,STR,CON,SIZ,DEX,APP,POW,INT,EDU,LUK):
        self.STR = STR
        self.CON = CON
        self.DEX = DEX
        self.APP = APP
        self.POW = POW
        self.LUK = LUK
        self.INT = INT
        self.EDU = EDU
        self.SIZ = SIZ
def WakeUp():
    if TimerOn == True:
        if strftime("%H", localtime()) in ['01','04','07']:
            group.send(WordStr.DRM[randint(0,len(WordStr.DRM)-1)] + '#梦话')#1点、4点、7点自动唤醒，避免程序自动睡眠
        Timer(3600,WakeUp).start()

group.send(WordStr.Hello)
@bot.register(group,TEXT)       
def returner(msg):
    global pl,en,rpt,rgnm,rgid,CRD,rp,dt,ennm,enid,Muted
    if (msg.text == '*EXIT*'):#正常退出‘
        TimerOn = False
        group.send(WordStr.Farewell)
        os._exit(0)
    if (msg.text == '*MUTE*'):#静言与解除静言
        Muted = True
        group.send(WordStr.Muted)
    if (msg.text == '*UNMUTE*'):
        Muted = False
        group.send(WordStr.Unmuted)
    if Muted == True:
        return
    if (msg.text == '*TIMER ON*'):#是否开启定时唤醒
        TimerOn = True
        WakeUp()
        group.send(WordStr.TimerOn)
    if (msg.text == '*TIMER OFF*'):
        TimerOn = False
        group.send(WordStr.TimerOff)
    f = ''
    if (msg.text[0:5] == '.help') | (msg.text[0:5] == '。help'):#显示帮助
        if len(msg.text) == 5:
            temp = WordStr.hlp+'ON' if rpt else WordStr.hlp+'OFF'
            group.send(temp)
        else:
            exec('group.send(WordStr.'+msg.text[6:]+'hlp)')
    if msg.member.puid not in pu:#第一次在群中出现的人的初始化
        pu.append(msg.member.puid)
        nm.append(msg.member.name)
        pl.append(pers(-1,-1,-1,-1,-1,-1,-1,-1,-1))
        rp.append(randint(1,100))
    for i in range(0,len(pu)):#群成员指针
        if msg.member.puid == pu[i]:
            tn = nm[i]
            si = i
    if (dt != (strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日'))):#jrrp更新
        for i in range(0,len(pu)):
            rp[i] = randint(1,100)
            dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')
    if (msg.text[0:3] == '.rd') | (msg.text[0:3] == '。rd'):#将rd转化为。r1d
        if (len(msg.text) == 3) | (msg.text[3:4] == ' '):
            f = '.r1d100'+msg.text[3:]
        else:
            f = '.r1d'+msg.text[3:]
    if (randint(1,15) == 1) & (len(msg.text) <= 30) & (rpt == True):#随机复读
        if randint(1,2) == 1:
            group.send(WordStr.Repeat.format(msg.text,tn))
        else:
            group.send(WordStr.DRM[randint(0,len(WordStr.DRM)-1)] + '#梦话')
    if rgnm == True:#人物卡的注册
        if msg.member.puid == pu[rgid]:
            rgnm = False
            try:
                num = findall('\
力量(.+)：(\d+)\n\
体质(.+)：(\d+)\n\
体型(.+)：(\d+)\n\
敏捷(.+)：(\d+)\n\
外貌(.+)：(\d+)\n\
智力(.+)：(\d+)\n\
意志(.+)：(\d+)\n\
教育(.+)：(\d+)\n\
幸运(.+)：(\d+)\
',msg.text)
                for i in range(0,9):
                    exec('pl['+str(rgid)+'].'+num[0][i*2]+'=int('+num[0][i*2+1]+')')
                group.send(WordStr.RegSuc)
            except:
                group.send(WordStr.Err)
            rgid = -1
    elif (msg.text[0:4] == '.reg') | (msg.text[0:4] == '。reg'):#各种。reg
        try:
            x = msg.text[5:]
            if x == '':
                raise Exception
            if x == 'all':
                rgnm = True
                rgid = si
                group.send(WordStr.InputReg)
            elif x == 'del':
                pl[si] = pers(-1,-1,-1,-1,-1,-1,-1,-1,-1)
                group.send(WordStr.DelReg)
            elif x == 'list':
                if pl[si].ORG == -1:
                    group.send(WordStr.NotRegistered.format(tn))
                else:
                    group.send(WordStr.ListCRD.format(tn)+'\n\
力量STR：'+str(pl[si].STR)+'\n\
体质CON：'+str(pl[si].CON)+'\n\
体型SIZ：'+str(pl[si].SIZ)+'\n\
敏捷DEX：'+str(pl[si].DEX)+'\n\
外貌APP：'+str(pl[si].APP)+'\n\
智力INT：'+str(pl[si].INT)+'\n\
意志POW：'+str(pl[si].POW)+'\n\
教育EDU：'+str(pl[si].EDU)+'\n\
幸运LUK：'+str(pl[si].LUK))
            elif msg.text[5:8].upper() in CRD:
                y = msg.text[5:8].upper()
                if len(msg.text) == 8:
                    group.send(WordStr.CRDStatus.format(tn,y,str(eval('pl['+str(si)+'].'+y))))
                elif msg.text[9] == ' ':
                    exec('pl['+str(si)+'].'+y+'=int('+msg.text[9:]+')',globals(),locals())
                    group.send(WordStr.CRDUpd.format(tn,y,str(int(msg.text[9:]))))
                else:
                    exec('pl['+str(si)+'].'+y+'=floor(pl['+str(si)+'].'+msg.text[5:].upper()+')',globals(),locals())
                    group.send(WordStr.CRDUpd.format(tn,y,msg.text[5:].upper(),str(eval('pl['+str(si)+'].'+y))))
        except:
            group.send(WordStr.Err)
    elif (msg.text[0:5] == '.jrrp') | (msg.text[0:5] == '。jrrp'):#显示今日人品
        group.send(WordStr.Jrrp.format(tn,dt,str(rp[si])))
    elif (msg.text[0:3] == '.nn') | (msg.text[0:3] == '。nn'):#更改昵称
        if ' ' in msg.text:
            if len(msg.text[4:]) > 30:
                group.send('@'+tn+' '+WordStr.RCG[randint(0,len(WordStr.RCG)-1)])
            else:
                nm[si] = msg.text[4:]
                group.send(WordStr.NN.format(nm[si]))
        else:
            nm[si] = msg.member.name
            group.send(WordStr.NNForget.format(tn))
    elif (msg.text == '*RPT OFF*'):#开关复读
        rpt = False
        group.send(WordStr.RPT.format('关闭'))
    elif (msg.text == '*RPT ON*'):
        rpt = True
        group.send(WordStr.RPT.format('开启'))
    elif (msg.text[0:3] == '.复读') | (msg.text[0:3] == '。复读'):#手动复读
        if ' ' in msg.text:
            if len(msg.text[4:]) > 50:
                group.send('@'+tn+' '+WordStr.RCG[randint(0,len(WordStr.RCG)-1)])
            else:
                group.send(WordStr.Repeat.format(msg.text[4:],tn))
        else:
            group.send(WordStr.EmptyRpt[randint(0,1)])
    elif (msg.text[0:3] == '.rc') | (msg.text[0:3] == '。rc') | (msg.text[0:3] == '.ra') | (msg.text[0:3] == '。ra'):#检定
        d = randint(1,100)
        k = msg.text[3:] if msg.text[3] != ' ' else msg.text[4:]
        if ' ' in k:
            x,y = k.split(' ')
        else:
            x = k
            y = ''
        try:
            x = int(x)
            if d > 95:
                t = WordStr.LFail
            elif d > x:
                t = WordStr.Fail
            elif d > x // 2:
                t = WordStr.Suc
            elif d > x // 5:
                t = WordStr.HardSuc
            elif d > max(5,x // 5):
                t = WordStr.ExtremeSuc
            else:
                t = WordStr.GSuc
            group.send(WordStr.RC.format(tn,y,d,t))    
        except:
            group.send(WordStr.Err)
    elif (msg.text[0:4] == '.coc') | (msg.text[0:4] == '。coc'):#人物卡生成
        x = 1
        s = WordStr.COC.format(tn)
        if ' ' in msg.text:
            num = findall(msg.text[0:4]+' (\d+)', msg.text)
            x = int(num[0][0])
        for i in range(0,x):
            ax = [((randint(1,6)+randint(1,6)+randint(1,6))*5) for i in range(0,6)]\
                 + [((randint(1,6)+randint(1,6)+6)*5) for i in range (0,3)] + [0,0]
            ax[2],ax[5] = ax[6],ax[8]
            for ii in range(0,9):
                ax[9] += ax[ii]
                if ii != 8:
                    ax[10] += ax[ii]
            s += \
            '力量STR：'+ str(ax[0]) + '\n'\
            '体质CON：'+ str(ax[1]) + '\n'\
            '体型SIZ：'+ str(ax[2]) + '\n'\
            '敏捷DEX：'+ str(ax[3]) + '\n'\
            '外貌APP：'+ str(ax[4]) + '\n'\
            '智力INT：'+ str(ax[5]) + '\n'\
            '意志POW：'+ str(ax[6]) + '\n'\
            '教育EDU：'+ str(ax[7]) + '\n'\
            '幸运LUK：'+ str(ax[8]) + '\n'\
            '总和(不含幸运)SUM：'+ str(ax[9]) + '(' + str(ax[10]) + ')\n'\
            '———————————\n'
        group.send(s)
    elif (msg.text[0:3] == '.rb') | (msg.text[0:3] == '。rb') | (msg.text[0:3] == '.rp') | (msg.text[0:3] == '。rp'):#奖励骰/惩罚骰
        x1 = randint(1,100)
        x2 = []
        y  = ''
        t  = 1
        if len(msg.text) > 3:
            if ' ' in msg.text:
                t = msg.text[3:].split(' ')[0]
                t = 1 if t == '' else int(t)
                if t > 100:
                    group.send('@'+tn+' '+WordStr.RCG[randint(0,len(WordStr.RCG)-1)])
                    t = -1
                y = msg.text[3:].split(' ')[1]
            else:
                t = int(msg.text[3:])
        for i in range(0,t):
            x2.append(randint(0,10))
        x3 = deepcopy(x2)
        x3.append(x1 // 10)
        if msg.text[2] == 'b':
            if x1 % 10 == 0:
                while min(x3) == 0:
                    for i in range(0,len(x3)):
                        x3[i] = 10 if x3[i] == 0 else x3[i]
            x = min(x3) * 10 + x1 % 10
            k = '奖励'
        elif msg.text[2] == 'p':
            if x1 % 10 != 0:
                while max(x3) == 10:
                    for i in range(0,len(x3)):
                        x3[i] = -1 if x3[i] == 10 else x3[i]
            elif min(x3) == 0:
                x3.append(10)
            x = max(x3) * 10 + x1 % 10
            k = '惩罚'
        if y == '':
            group.send(WordStr.RBP.format(tn,msg.text[2].upper(),x1,k,x2,x))
        else:
            group.send(WordStr.RBPn.format(y,tn,msg.text[2].upper(),x1,k,x2,x))
    elif (msg.text[0:4] == '.rhd') | (msg.text[0:4] == '。rhd'):#暗骰
        group.send(WordStr.RHDGroup)
        fr = bot.friends().search('',puid=msg.member.puid)[0]
        if len(msg.text) == 4:
            fr.send(WordStr.RHD.format(randint(1,100)))
        else:
            fr.send(WordStr.RHDn.format(msg.text[6:],randint(1,100)))
        fr.send(WordStr.RHDLine)
    elif (msg.text[0:2] == '.r') | (msg.text[0:2] == "。r"):#普通骰子
        s = ''
        t = ''
        if f == '':
            f = msg.text
        if ' ' in f:
            xx = f.split(' ')[0][2:]
            z = f[len(xx)+3:]
            x,y = xx.split('d')
            if len(y) > 1:
                y,t = findall('(\d+)(.+)',y)[0]
                if len(t) <= 1:
                    y = y+t
                    t = ''
        else:
            x = f.split('d')[0][2:]
            y = f.split('d')[1]
            z = ''
            if len(y) > 1:
                y,t = findall('(\d+)(.+)',y)[0]
                if len(t) <= 1:
                    y = y+t
                    t = ''
        dc = 0
        if (int(x) > 100) | (int(y) > 100000):
            group.send('@'+tn+' '+WordStr.RCG[randint(0,len(WordStr.RCG)-1)])
        else:
            for i in range(1,int(x)+1):
                k = randint(1,int(y))
                s += str(k)
                if i != int(x):
                    s += '+'
                elif int(x) > 1:
                    if t != '':
                        s += ')' + t
                    s += '='
                else:
                    s = ''
                    if t != '':
                        s += str(k) + ')' + t + '='
                dc += k
                if (x == '1') & (y == '100'):
                    rp[si] = rp[si] - 1 if k <= 10 else rp[si]
                    rp[si] = rp[si] + 1 if k >= 90 else rp[si]
                    if (k<=10) | (k>=90):
                        group.send(WordStr.RPChange.format(tn,rp[si]))
            if (t != '') :
                y += t
                s = '(' + s
            if (z == ''):
                group.send(WordStr.ROLL.format(tn,x,y,s,eval('floor('+str(dc)+t+')')))
            else:
                group.send(WordStr.ROLLn.format(z,tn,x,y,s,eval('floor('+str(dc)+t+')')))
        f = ''
    sleep(2)
embed()
