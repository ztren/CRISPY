####DICEBOT release 1.0.1####
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
from copy import *

import os

from DiceFunctions import *
import WordStr
import DiceConstant
import NameGenerator

if WordStr.GroupName == '':
    raise Exception('Please Input the Name of Your WeChat Group.')

bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
try:
    group = bot.groups().search(WordStr.GroupName)[0]
except:
    print('Can''t find the group. Please pin the group and try again.\n')
    raise
group.send(WordStr.Hello)
init()

@bot.register(group)
def returner(msg):
    dt = strftime("%Y{0}%m{1}%d{2}", localtime()).format('年','月','日')#当前时间
    pu = msg.member.puid
    if not os.path.exists('groups/'+WordStr.GroupName+'/'+pu):#第一次在群中出现的人的初始化
        init = 'wname\n'+msg.member.name+'\nname\n'+msg.member.name+'\nrp\n'+str(randint(1,100))+'\n'
        pers = open('groups/'+WordStr.GroupName+'/'+pu,mode = 'x')
        pers.write(init)
        pers.close()
        changemisc('pu',readmisc('pu')+[pu+'\n'])
    tn = getvl(pu,'name')
    if msg.member.name != getvl(pu,'wname'):#更新群昵称
        st(pu,'wname',msg.member.name)
    if (dt+'\n' != readmisc('dt')[0]):#jrrp更新
        changemisc('dt',dt+'\n')
        for i in range(0,len(readmisc('pu'))):
            st(readmisc('pu')[i][:-1],'rp',randint(1,100))
    if (randint(1,15) == 1) & (len(msg.text) <= 50) & (readrule('rpt') == 'on') & (readrule('mute') == 'off'):#随机复读
        if randint(1,2) == 1:
            group.send(WordStr.Repeat.format(msg.text,tn))
        else:
            group.send(WordStr.DRM[randint(0,len(WordStr.DRM)-1)] + '#bot')
    sleep(0.2)
    if msg.text[0]+'\n' in readmisc('cmd'):#命令列表
        if (msg.text[1:4] == 'bot'):
            if msg.member == group.owner:
                x = cmd(msg.text[4:])
                if (x.lower() == 'on'):
                    changerule('mute','off')
                    group.send(WordStr.Unmuted)
                elif (x.lower() == 'off'):
                    changerule('mute','on')
                    group.send(WordStr.Muted)
            else:
                group.send(WordStr.NotOwner)
        if readrule('mute') == 'on':#被禁言时退出
            return
        if (msg.text[1:4] == 'rpt'):#复读开关
            if msg.member == group.owner:
                x = cmd(msg.text[4:])
                try:
                    if x.lower() == 'off':
                        changerule('rpt','off')
                        group.send(WordStr.FunctionChange.format('随机复读',x))
                    elif x.lower() == 'on':
                        changerule('rpt','on')
                        group.send(WordStr.FunctionChange.format('随机复读',x))
                    else:
                        raise
                except:
                    group.send(WordStr.Err)
            else:
                group.send(WordStr.NotOwner)
        elif (msg.text[1:5] == 'help'):#显示帮助
            if len(msg.text) == 5:
                group.send(WordStr.help.format(readrule('rpt')))
            else:
                x = cmd(msg.text[5:])
                group.send(eval('WordStr.'+x+'help'))
        elif (msg.text[1:5] == 'rules'):#显示房规
            s = readmisc('rule')
            a = 'COC房规：'+WordStr.cocrule.split('######')[int(readrule('cocrule'))]+'其他规则：\n'
            for i in range(1,len(s)):
                a += s[i]
            group.send(WordStr.showrule.format(a))
        elif (msg.text[1:3] == 'st'):#记录数据
            try:
                a = cmd(msg.text[3:])
                if '|' in a:
                    group.send(WordStr.RegSuc)
                    a = a.split('|')
                    for i in range(0,len(a)):
                        nam,val = a[i].split(' ')
                        nam = syn(nam)
                        st(pu,nam,val)
                elif ' ' in a:
                    nam,val = a.split(' ')
                    if nam == 'show':
                        group.send(WordStr.CRDStatus.format(tn,val,getvl(pu,val)))
                    elif nam == 'del':
                        a = readpl(pu)
                        if val == 'all':
                            a = a[0:6]+['\n']
                            group.send(WordStr.DelReg.format(tn,'全部'))
                        else:
                            for i in range(0,len(a)):
                                if a[i] == val+'\n':
                                    a.pop(i)
                                    a.pop(i)
                                    group.send(WordStr.DelReg.format(tn,val))
                                    break
                                if i == len(a)-1:
                                    group.send(NoData.format(val))
                        writepl(pu,a)
                    else:
                        nam = syn(nam)
                        if nam == 'rp':
                            group.send(WordStr.RegDeny)
                        else:
                            val = calc(val)
                            st(pu,nam,val)
                            group.send(WordStr.CRDUpd.format(tn,nam,val))
                else:
                    nam = a
                    opr = ''
                    for i in range(0,len(a)):
                        if a[i] in ['+','-','*','/']:
                            opr = a[i:]
                            nam = a[:i]
                            break
                    nam = syn(nam)
                    if nam == 'rp':
                        group.send(WordStr.RegDeny)
                    else:
                        val = floor(eval(calc(str(getvl(pu,nam))+opr)))
                        if opr == '':
                            group.send(WordStr.CRDStatus.format(tn,nam,val))
                        else:
                            st(pu,nam,val)
                            group.send(WordStr.CRDUpd.format(tn,nam,val))
            except IndexError:
                group.send(WordStr.Err)
            except NameError:
                group.send(WordStr.NoData.format(nam))
        elif (msg.text[1:3] == 'en'):#成长检定
            x = cmd(msg.text[3:])
            try:
                x = x.split(' ')
                nam = syn(x[0])
                if nam == 'rp':
                    group.send(WordStr.RegDeny)
                else:
                    if len(x) == 2:
                        val = int(getvl(pu,nam))
                    elif len(x) == 3:
                        val = int(x[1])
                        st(pu,nam,val)
                    else:
                        raise IndexError
                    r = randint(1,100)
                    if '/' in x[-1]:
                        suc,fail = x[-1].split('/')
                    else:
                        suc,fail = x[-1],'0'
                    if r <= val:
                        a = int(calc(suc))
                        a1 = suc
                        n = '成功'
                    else:
                        a = int(calc(fail))
                        a1 = fail
                        n = '失败'
                    st(pu,nam,val+a)
                    if a1 != str(a):
                        a1 = str(val) + '+' + a1 + '=' + str(val) + '+' + str(a) + '=' + str(val+a)
                    else:
                        a1 = str(val) + '+' + a1 + '=' + str(val+a)
                    group.send(WordStr.EN.format(tn,nam,r,val,n,a1))
            except NameError:
                group.send(WordStr.NoData.format(nam))
            except IndexError:
                group.send(WordStr.Err)
            except ValueError:
                group.send(WordStr.NotInteger.format(nam))
        elif (msg.text[1:7] == 'choose'):#选择
            x = cmd(msg.text[7:])
            try:
                n = 1
                a = []
                x = sep(x)
                if ' ' in x[-1]:
                    n = int(x[-1].split(' ')[1])
                    x[-1] = x[-1].split(' ')[0]
                if (n >= len(x)) | (n > 50):
                    raise ValueError
                while len(a) < n:
                    a.append(x.pop(randint(0,len(x)-1)))
                s = ''
                for i in range(0,len(a)):
                    s += a[i]
                    if i != len(a)-1:
                        s += '+'
                group.send(WordStr.choice.format(s))
            except ValueError:
                group.send(WordStr.nochoice)
        elif (msg.text[1:7] == 'setcoc'):#coc房规
            if msg.member == group.owner:
                x = cmd(msg.text[7:])
                try:
                    x = int(x)
                    if x in range(0,6):
                        changerule('cocrule',str(x))
                        group.send(WordStr.setcoc.format(x,WordStr.cocrule.split('######\n')[x]))
                    else:
                        raise IndexError
                except IndexError:
                    group.send(WordStr.InvalidRule.format('COC'))
                except:
                    group.send(WordStr.Err)
            else:
                group.send(WordStr.NotOwner)
        elif (msg.text[2] == 'i'):#疯狂症状
            r1 = randint(1,10)
            r2 = '1D10 = ' + str(randint(1,10))
            if msg.text[1] == 't':
                a = DiceConstant.ti[r1-1]
                s = '临时'
            elif msg.text[1] == 'l':
                a = DiceConstant.li[r1-1]
                s = '长期'
            if r1 == 9:
                r3 = randint(1,100)
                group.send(WordStr.insanity.format(tn,'临时',r1,a.format(r2,'1D100 = '+str(r3),DiceConstant.fear[r3-1])))
            elif r1 == 10:
                r3 = randint(1,100)
                group.send(WordStr.insanity.format(tn,'临时',r1,a.format(r2,'1D100 = '+str(r3),DiceConstant.panic[r3-1])))
            else:
                group.send(WordStr.insanity.format(tn,'临时',r1,a.format(r2)))
        elif (msg.text[1:5] == 'jrrp'):#显示今日人品
            if msg.text[1:] == 'jrrp':
                if readrule('jrrp') == 'on':
                    group.send(WordStr.Jrrp.format(tn,dt,getvl(pu,'rp')))
                else:
                    group.send(WordStr.JrrpUnavailable)
            else:
                x = cmd(msg.text[5:])
                if x.lower() == 'on' or x.lower() == 'off':
                    if msg.member == group.owner:
                        changerule('jrrp',x.lower())
                        group.send(WordStr.FunctionChange.format('jrrp',x.lower()))
                    else:
                        group.send(WordStr.NotOwner)
        elif (msg.text[1:5] == 'send'):#向骰子拥有者发送消息
            x = cmd(msg.text[5:])
            if x.lower() == 'on' or x.lower() == 'off':
                if msg.member == group.owner:
                    changerule('send',x.lower())
                    group.send(WordStr.FunctionChange.format('send',x.lower()))
                else:
                    group.send(WordStr.NotOwner)
            else:
                if readrule('send') == 'on':
                    group.send(WordStr.Send)
                    bot.file_helper.send(WordStr.Send_msg.format(getvl(pu,'wname'),WordStr.GroupName,x))
                else:
                    group.send(WordStr.SendUnavailable)
        elif (msg.text[1:3] == 'ob'):#旁观
            a = readmisc('ob')
            if pu + '\n' in a:
                a.pop(a.index(pu+'\n'))
                group.send(WordStr.unOB.format(tn))
            else:
                a.append(pu+'\n')
                group.send(WordStr.OB.format(tn))
            changemisc('ob',a)
        elif (msg.text[1:3] == 'nn'):#更改昵称
            if msg.text[3:] == '':
                st(pu,'name',msg.member.name)
                group.send(WordStr.NNForget.format(tn))
            elif msg.text[3] == 'n':
                if msg.text[3:] == 'n':
                    n = NameGenerator.getRandomName('')
                    st(pu,'name',n)
                    group.send(WordStr.NN.format(n))
                else:
                    try:
                        n = NameGenerator.getRandomName(msg.text[-2:].upper())
                        st(pu,'name',n)
                        group.send(WordStr.NN.format(n))
                    except:
                        group.send(WordStr.Err)
            else:
                x = cmd(msg.text[3:])
                if len(x) > 30:
                    group.send('@'+tn+' '+WordStr.RCG[randint(0,len(WordStr.RCG)-1)])
                else:
                    st(pu,'name',x)
                    group.send(WordStr.NN.format(x))
        elif (msg.text[1:3] == '复读'):#手动复读
            if len(msg.text) > 3:
                x = cmd(msg.text[3:])
                if len(x) > 100:
                    group.send('@'+tn+' '+WordStr.RCG[randint(0,len(WordStr.RCG)-1)])
                else:
                    group.send(WordStr.Repeat.format(msg.text[4:],tn))
            else:
                group.send(WordStr.EmptyRpt[randint(0,len(WordStr.EmptyRpt)-1)])
        elif (msg.text[1:9] == 'transfer'):#数据转移
            x = cmd(msg.text[9:])
            if x == 'all':
                group.send(WordStr.Transfering.format('所有用户'))
                a = readmisc('pu')
                b = deepcopy(a)
                ob = readmisc('ob')
                c = []
                for i in range(0,len(a)-1):
                    puSource = a[i][:-1]
                    s = readpl(puSource)
                    ttn = getvl(puSource,'wname')
                    for j in range(i+1,len(a)):
                        puTarget = a[j][:-1]
                        if (getvl(puTarget,'wname') == ttn) & (puSource != puTarget):
                            writepl(puTarget,s)
                            b.pop(i)
                            if a[i] in ob:
                                if a[j] not in ob:
                                    ob[ob.index(a[i])] = a[j]
                                else:
                                    ob.pop(ob.index(a[i]))
                            c.append(getvl(puTarget,'wname'))
                            os.remove('groups/'+WordStr.GroupName+'/'+puSource)
                            break
                changemisc('pu',b)
                changemisc('ob',ob)
                s = ''
                if len(c) > 0:
                    for i in range(0,len(c)):
                        s += c[i] + '\n'
                group.send(WordStr.TransferResult.format(len(c),s))
            else:
                group.send(WordStr.Transfering.format(getvl(pu,'wname')))
                a = readmisc('pu')
                b = deepcopy(a)
                ob = readmisc('ob')
                for i in range(0,len(a)):
                    puSource = a[i][:-1]
                    s = readpl(puSource)
                    ttn = getvl(puSource,'wname')
                    if getvl(pu,'wname') == ttn:
                        if puSource == pu:
                            group.send(WordStr.TransferFailed.format(WordStr.NoUsr))
                            break
                        else:
                            writepl(puTarget,s)
                            b.pop(i)
                            if a[i] in ob:
                                if pu+'\n' not in ob:
                                    ob[ob.index(a[i])] = pu + '\n'
                                else:
                                    ob.pop(ob.index(a[i]))
                            os.remove('groups/'+WordStr.GroupName+'/'+puSource)
                            changemisc('pu',b)
                            changemisc('ob',ob)
                            group.send(WordStr.TransferResult.format(1,getvl(pu,'wname')))
                            break
                    if i == len(a)-1:
                        group.send(WordStr.TransferFailed.format(WordStr.NoUsr))
        elif (msg.text[1:3] == 'rc') | (msg.text[1:3] == 'ra'):#检定
            x = cmd(msg.text[3:])
            try:
                d = randint(1,100)
                if ' ' in x:
                    x,val = x.split(' ')
                    for i in range(0,len(x)):
                        if x[i] in ['+','-','*','/','(',')']:
                            val = eval(val+x[i:])
                            x = x[:i]
                            break
                    val = int(val)
                else:
                    t = ''
                    for i in range(0,len(x)):
                        if x[i] in ['+','-','*','/','(',')']:
                            t = x[i:]
                            x = x[:i]
                            break
                    x = syn(x)
                    val = floor(eval(getvl(pu,x) + t))
                t = ''
                rule = int(readrule('cocrule'))
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
                group.send(WordStr.RC.format(tn,x,d,val,t))
            except NameError:
                group.send(WordStr.NoData.format(x))
            except ValueError:
                group.send(WordStr.NotInteger.format(x))
        elif (msg.text[1:3] == 'sc'):#san check
            x = cmd(msg.text[3:])
            x,y = sep(x)
            x,y = eval(calc(x)),eval(calc(y))
            try:
                r = randint(1,100)
                san = int(getvl(pu,'理智'))
                if r <= san:
                    st(pu,'理智',san-x)
                    group.send(WordStr.SC.format(tn,r,san,WordStr.SCsuc,x,san-x))
                if r > san:
                    st(pu,'理智',san-y)
                    group.send(WordStr.SC.format(tn,r,san,WordStr.SCfail,y,san-y))
            except:
                group.send(WordStr.NoData.format('理智'))
        elif (msg.text[1:4] == 'coc'):#人物卡生成
            try:
                x = 1
                s = WordStr.COC.format(tn)
                if len(msg.text) > 4:
                    x = int(cmd(msg.text[4:]))
                for i in range(0,x):
                    ax = [((randint(1,6)+randint(1,6)+randint(1,6))*5) for i in range(0,6)]\
                         + [((randint(1,6)+randint(1,6)+6)*5) for i in range (0,3)] + [0,0]
                    ax[2],ax[5],ax[6],ax[8] = ax[6],ax[8],ax[2],ax[5]
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
            except ValueError:
                group.send(WordStr.NotInteger.format(''))
        elif (msg.text[1:3] == 'rb') | (msg.text[1:3] == 'rp'):#奖励骰/惩罚骰
            x1 = randint(1,100)
            x2 = []
            y  = ''
            t  = 1
            if len(msg.text) > 3:
                if ' ' in msg.text:
                    t = msg.text[3:].split(' ')[0]
                    t = 1 if t == '' else int(t)
                    if t > 100:
                        group.send(WordStr.TooManyDices)
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
        elif (msg.text[1:4] == 'rhd'):#暗骰
            group.send(WordStr.RHDGroup)
            a = readmisc('ob')
            a = a if pu+'\n' in a else a+[pu+'\n']
            r = randint(1,100)
            for i in range(0,len(a)):
                fr = bot.friends().search('',puid=a[i][:-1])[0]
                fr.send(WordStr.RHD.format(WordStr.GroupName,tn,r))
                fr.send(WordStr.RHDLine)
        elif (msg.text[1] == 'r'):#普通骰子
            try:
                if ' ' in msg.text[2:]:
                    x,z = msg.text[2:].split(' ')
                else:
                    x,z = msg.text[2:],''
                if x[0] == 'd':
                    if x == 'd':
                        x = '1d100'
                    elif x[1] in ['+','-','*','/','(',')']:
                        x = '1d100' + x[1:]
                    else:
                        x = '1' + x
                y = calc(x)
                l = x if str(eval(y)) == y else x + '=' + y
                if (z == ''):
                    group.send(WordStr.ROLL.format(tn,l,floor(eval(y))))
                else:
                    group.send(WordStr.ROLLn.format(z,tn,l,floor(eval(y))))
            except IndexError:
                group.send(WordStr.TooManyFaces)
            except Exception:
                group.send(WordStr.TooManyDices)
embed()
