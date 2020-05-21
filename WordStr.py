#———————————————————————————#
####WordStr release 1.0.2####
##########BY  ZTREN##########
#———————————————————————————#
#####FEEL FREE TO MODIFY#####
##########THIS FILE##########
############ENJOY!###########
#———————————————————————————#

GroupName = ''#跑团群群名，初次使用需要修改！
RCG = \
['爬','给爷爬','你说你马呢？','输的啥心里没丶ACD数？','8太行嗷']#复读/nn长度过长
DRM = \
['昂？','爷佛了','啥啊','这是ao的','啊？','#¥…#¥!@#','搜到有','爬']#随机复读

help = \
'''——CRISPY使用指南——
CRISPY release 1.0.2
已经开发的功能有：
.rules：规则速查
.rd [text]：[因为text]投掷1D100的一颗骰子
.rXdY [text]：[因为text]投掷XDY的一颗骰子
.rb/rp[n] [text]：[因为text]投掷n个奖励骰/惩罚骰（默认为1）
.ra/rc <text> [x]：投掷text检定（优先使用x数据，若x为空则采用.st注册过的的数据）
.rhd：暗骰1D100
.sc <x/y>：理智检定，若成功则减少x点理智，失败则减少y点理智
.coc [n]：生成n张COC人物卡（默认为1）
.nn [name]：将自己在骰子中显示的昵称改为name（长度限制30），若name为空则改为群昵称
.nnn [lang]：随机生成人名（lang支持CN,JP,EN）
.ob：设置旁观模式
.复读 [msg]：让骰子复读你的话（长度限制100）
.jrrp：显示今日人品
.send：向dice拥有者的文件传输助手发送消息
.choose <xx/yy/zz> [n]从选项中选择n个(默认为1)，选恐助手
.st：详细见 .help st
.trasnfer：详细见 .help transfer
群主指令：详细见.help cmd
注：[]内为选填，<>内为必填
目前随机复读状态为：{0}
视为bot指令的提示符为：'.' '。' '/' '!' '！' ',' '，'
视为分割线的提示符为：',' '，' '/' '|' ' '
提示符可在groups/群名/_misc文件中修改
'''
cmdhelp = \
'''群主指令列表：
.bot on(off) 将本bot禁言或解除禁言
.rpt/jrrp/send on(off) 开启或关闭随机复读/今日人品/发送消息功能
注：由于技术限制，微信群管理员无法使用此命令。多有不便，敬请谅解。
'''
sthelp = \
'''——ST功能使用指南——
.st <XXX> <数据> 人物卡数据填写（如STR 65）
.st <XXX+表达式> 人物卡数据改变（如STR+5，san+1d6）
.st [show] <XXX> 显示你人物卡中的某项数据（有无show均视为该命令）
.st del <XXX> 删除人物卡中的某项数据（若XXX为'all'则删除所有数据）
'''
transferhelp = \
'''——transfer功能使用指南——
.transfer <XXX> 将原群昵称为XXX的用户数据转移到你的数据下
.transfer all 将群内所有人的原先的用户数据转移到现在的表单中
'''
#各种帮助文本
cocrule = \
'''0 规则书
出1大成功
不满50出96 - 100大失败，满50出100大失败
######
1
不满50出1大成功，满50出1 - 5大成功
不满50出96 - 100大失败，满50出100大失败
######
2
出1 - 5且 <= 成功率大成功
出100或出96 - 99且 > 成功率大失败
######
3
出1 - 5大成功
出96 - 100大失败
######
4
出1 - 5且 <= 十分之一大成功
不满50出 >= 96 + 十分之一大失败，满50出100大失败
######
5
出1 - 2且 < 五分之一大成功
不满50出96 - 100大失败，满50出99 - 100大失败
'''
#coc房规设置
setcochelp = \
'为每个群设置COC房规，如.setcoc 1（可选：0-5）\n'+cocrule
#房规设置帮助
NotOwner = \
'你并不是群主，无法使用此命令~'
#不是群主提示
NotInteger = \
'你输入的{0}数值好像并不是一个整数x'
#输入数值非数字提示
TooManyDices = \
'扔的骰子太多啦 CRISPY也算不过来啦x'
#骰子数量太多
TooManyFaces = \
'这是几面骰？不是一个球吗'
#骰子面数太多
MemberExit = \
'有人退出群聊了哦..'
#有人退出群聊提示
MemberWelcome = \
'''欢迎新人加入本群！
输入.help查看CRISPY食用方法～
提示：请勿发送太多次以防刷屏
'''
#加入群聊提示
showrule = \
'以下是你群规则一览表：\n{0}'
#房规速查
setcoc = \
'COC房规已被设置为第{0}条啦w：\n{1}'
#房规设置
Transfering = \
'正在转移{0}的数据……'
#数据转移中
TransferResult = \
'''数据转移结果：
{0}人转移成功，群昵称为：
{1}转移失败的原因可能是bot掉线时更改了群昵称。
'''
#数据转移结果
TransferFailed = \
'转移失败，原因是{0}'
#数据转移失败
NoUsr = \
'未找到名为该群昵称的用户'
#找不到用户
RegSuc = \
'人物卡信息录入成功！'
#信息录入成功
RegDeny = \
'RP值可不能随便乱改哦\\(ﾟwﾟ)/'
#禁止更改rp
DelReg = \
'{0}的{1}数值被清空了！'
#清空人物卡数据
NoData = \
'你似乎并没有注册「{0}」的值(ﾉﾟ▽ﾟ)ﾉ'
#人物卡数值未注册
CRDStatus = \
'{0}，你的{1}目前的数值为：{2}'
#显示人物卡数值
CRDUpd = \
'{0}的{1}数值已经更新为{2}啦_(:з」∠)_'
#更新人物卡数值
EN = \
'''{0}想要通过骰点来获得一些{1}上的成长？来，让我们看看——
1D100 = {2}/{3} {4}
{1}的数值变化：{5}
'''
#成长检定
choice = \
'当然是选择{0}啦'
#选项
nochoice = \
'你这样写让我怎么选嘛'
#choose命令格式错误
OB = \
'{0}已经成功更改为旁观者模式(￣▽￣)／'
#进入ob位
unOB = \
'{0}已离开观众席(￣▽￣)／'
#离开ob位
FunctionChange = \
'{0}功能的状态已经更改为{1}～'
#功能开关
Jrrp = \
'{0}，你在{1}的人品为：{2}！'
#今日人品
JrrpUnavailable = \
'Jrrp功能暂不可用～'
#今日人品不可用
Send = \
'已向骰子主人的文件传输助手发送了这条消息～看不到可不怪我哦'
#发送信息
Send_msg = \
'''{0}在{1}群中向你发送了信息：
{2}'''
#发送信息的格式
SendUnavailable = \
'Send功能暂不可用～'
#发送信息不可用
NN = \
'啊，那之后就把你叫做 {0} 了昂'
#自定义名称
StrError = \
'CRISPY并没有看懂你再说什么x'
#输入错误
NNForget = \
'让我忘掉 {0} 这个称号？好啊'
#忘掉自定义名称
RPT = \
'已{0}随机对话！'
#开/关随机对话
EmptyRpt = \
['耍我啊？','干啥啊']
#。复读内容为空
COC = \
'{0}酱，这是新的调查员数据\n'
#roll人物卡数据
SC = \
'''{0}的San Check:
D100 = {1}/{2}
{3}
你的San值减少{4}点，当前剩余{5}点。祝你好运。
'''
#san check
SCsuc = \
'你的意志足够扛下这一击了。'
#sc成功
SCfail = \
'看来你被震慑住了。'
#sc失败
insanity = \
'''{0}的{1}疯狂症状：
1D10 = {2}
症状：{3}
'''
#疯狂症状
RBP = \
'{0} 骰出了 {1}={2}[{3}骰：{4}]={5}'
#奖励骰/惩罚骰
RBPn = \
'因为{0}检定，{1} 骰出了 {2}={3}[{4}骰：{5}]={6}'
#由于某检定而进行的奖励骰/惩罚骰
RHDGroup = \
'CRISPY正在暗骰……'
#暗骰时在群中的提示
RHD = \
'在群{0}中{1}的暗骰结果是：{2}'
#暗骰结果
RHDLine = \
'——[Doge]——'
#暗骰分割线，用于遮挡微信主界面显示的数据。若不需要则填''
NotFriend = \
'（部分用户似乎没有加CRISPY好友呢，这样是无法收到暗骰结果的）'
#部分ob列表中的好友或暗骰者非骰娘好友
ROLL = \
'{0} 骰出了 {1}={2}'
#骰子
ROLLn = \
'由于 {0} 检定，{1}骰出了 {2}={3}'
#由于某检定而进行的骰子
Repeat = \
'{0}\n——{1}'
#复读
RC = \
'{0}似乎想要通过{1}检定来解决问题呢：\nD100 = {2}/{3}\n{4}'
#检定
Suc = \
'成功了呢，祝贺'
#成功提示
HardSuc = \
'困难成功，今天的运气不错哦？'
#困难成功提示
ExtremeSuc = \
'极难成功，期待你的表现~'
#极难成功提示
GSuc = \
'是大成功？？真令人难以置信，不愧是你'
#大成功提示
Fail = \
'失败了的说，抱歉哦'
#失败提示
LFail = \
'是大失败哦？生死有命富贵在天啊'
#大失败提示
Muted = \
'嗯？好的，那我就不说话了'
#禁言
Unmuted = \
'可以说话了？好的哦'
#解除禁言
Hello = \
''
#开启程序时的问候语
Farewell = \
'那么，晚安'
#关闭程序时的问候语
Err = \
'输入格式好像不太对的说'
#输入有误
InvalidRule = \
'是CRISPY没听说过的{0}房规呢'
#房规输入错误
