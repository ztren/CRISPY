# COCdicebot
CRISPY, the COC7 Dicebot, by ZTREN
## 概述
CRISPY是基于COC7的跑团规则，由ZTREN独立编写的微信dicebot，旨在成为溯洄骰的微信版替代品。目前已经复刻了溯洄骰的除黑白名单、draw以及me之外的几乎所有功能。
## 安装
### 1.安装python3
**注意：本程序并不兼容python2。**\
官网链接如下。\
https://www.python.org/downloads/
### 2.安装wxpy
**WINDOWS用户需要安装pip。** \
运行init文件夹中的
OSX、LINUX：
```
pip install wxpy
```
或者按照以下链接安装wxpy源代码。\
https://pypi.org/project/wxpy/
### 3.下载DICEBOT
https://github.com/ztren/COC7dicebot/releases \
点击最新版本的zip下载并解压。
### 4.运行DICEBOT
用命令行或终端运行**DICE.py**，并根据提示操作。\
若扫描二维码之后未报错并出现">>>"字样（不含双引号）（linux系统显示为In [1]:），即说明登陆成功，可以使用。\
**注：wxpy并不会响应bot自身所在微信号发送的消息。**
## 功能介绍
.rules：规则速查\
.rd [text]：[因为text]投掷1D100的一颗骰子\
.rXdY [text]：[因为text]投掷XDY的一颗骰子\
.rb/rp[n] [text]：[因为text]投掷n个奖励骰/惩罚骰（默认为1）\
.ra/rc <text> [x]：投掷text检定（优先使用x数据，若x为空则采用.st注册过的的数据\
.rhd：暗骰1D100\
.sc <x/y>：理智检定，若成功则减少x点理智，失败则减少y点理智\
.coc [n]：生成n张COC人物卡（默认为1）\
.nn [name]：将自己在骰子中显示的昵称改为name（长度限制30），若name为空则改为群昵称\
.nnn [lang]：随机生成人名（lang支持CN,JP,EN）\
.ob：设置旁观模式\
.复读 [msg]：让骰子复读你的话（长度限制100）\
.jrrp：今日人品（1d100到10以下-1，90以上+1，不包含加减）\
.send：向dice拥有者的文件传输助手发送消息\
.choose <xx/yy/zz>（或<xx yy zz>）从选项中选择一个，选恐助手\
.st <XXX> <数据> 人物卡数据填写（如STR 65）\
.st <XXX+表达式> 人物卡数据改变（如STR+5，san+1d6）\
.st [show] <XXX> 显示你人物卡中的某项数据（有无show均视为该命令）\
.st del <XXX> 删除人物卡中的某项数据（若XXX为'all'则删除所有数据）\
.transfer <XXX> 将原群昵称为XXX的用户数据转移到你的数据下\
.transfer all 将群内所有人的原先的用户数据转移到现在的表单中\
群主指令：\
.bot on(off) 将本bot禁言或解除禁言\
.rpt/jrrp/send on(off) 开启或关闭随机复读/今日人品/发送消息功能\
注：由于技术限制，微信群管理员无法使用此命令。多有不便，敬请谅解。\
注：[]内为选填，<>内为必填\
视为bot指令的提示符为：'.' '。' '/' '!' '！'
## 常见问题解答
### 1、使用微信登陆失败，如何解决？
请进入[网页版微信网址](https://web.weixin.qq.com)并尝试登录网页版微信，检查自己的微信号是否可以使用网页版微信。若提示无法登录网页版微信，则需要更换使用时间更长，微信安全等级更高的微信号登录。
### 2、打开程序时显示IndexError: list index out of range错误，如何解决
在需要绑定骰子的群聊中发送几条消息并将其置顶再运行程序。等程序运行之后可以将其取消置顶。多次尝试即可。
### 3、我该如何修改dicebot所说的台词？
修改WordStr文件即可。
