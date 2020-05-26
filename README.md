# CRISPY
CRISPY, the Dicebot, by SAIKA
## 概述
CRISPY是saika独立编写的微信dicebot，旨在成为溯洄骰的微信版替代品。目前已经复刻了溯洄骰的除黑白名单、draw以及me之外的几乎所有功能。\
开发中的功能：dnd，黑白名单系统
## 安装
### 1.安装python3
**注意：本程序并不兼容python2。**\
官网链接如下。\
https://www.python.org/downloads/
### 2.安装wxpy
**WINDOWS：**\
用管理员模式运行init文件夹中的setup.cmd文件来安装pip和wxpy。\
注：由于Windows的不稳定性，**不建议**使用Windows来运行bot。\
**OSX、LINUX：**
```
pip install wxpy
```
或者按照以下链接安装wxpy源代码。\
https://pypi.org/project/wxpy/
### 3.下载DICEBOT
https://github.com/ztren/COC7dicebot/releases \
点击最新版本的zip下载并解压。
### 4.运行DICEBOT
**初次运行请修改WordStr.py中的GroupName参数，使单引号中的内容与需要使用骰子的群名一致**\
用命令行或终端运行**DICE.py**，并根据提示操作。\
若扫描二维码之后未报错并出现">>>"字样（不含双引号）（linux系统显示为In [1]:），即说明登陆成功，可以使用。\
**注：wxpy并不会响应bot自身所在微信号发送的消息。**
## 常见问题解答
### 1、使用微信登陆失败，如何解决？
请进入[网页版微信网址](https://web.weixin.qq.com)并尝试登录网页版微信，检查自己的微信号是否可以使用网页版微信。若提示无法登录网页版微信，则需要更换注册使用时间更长，微信安全等级更高的微信号登录。
### 2、打开程序时显示IndexError: list index out of range错误，如何解决
首先在WordStr.py的GroupName变量中填入需要绑定的微信群，并在群聊中发送几条消息然后将其置顶，再运行程序。等程序运行之后可以将其取消置顶。多次尝试即可。若多次尝试还是无法成功，可以试试退出网页版微信再登陆重试。
### 3、我该如何修改dicebot所说的台词？
修改WordStr.py文件即可。
### 4、若群名更改，我该如何转移数据？
修改WordStr.py的GroupName变量使其和新群对应，然后将groups目录下名为[原微信群群名]的文件夹修改为[现有微信群群名]然后再重新启动bot。
### 5、我可以在不同群聊同时开启bot吗？
可以。有两种方案：\
1、在开启一个bot之后修改GroupName并使其与另一个群的GroupName一致。\
2、将不同的bot放在不同文件夹，然后将已登陆网页版微信的bot文件夹中的wxpy.pkl和wxpy_puid.pkl复制到其他bot所在文件夹。
### 6、我的网页版微信因为意外/手动/断网或其他情况而自动退出了，我该如何操作？
重新开启bot，并使用.transfer all命令来转移在bot开启到你输入命令之前发言过的所有用户的数据。
