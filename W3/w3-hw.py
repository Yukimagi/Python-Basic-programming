import math
#工作量、體重(變數定義)
low_low_kcal=35
mid_low_kcal=40
high_low_kcal=45

low_mid_kcal=30
mid_mid_kcal=35
high_mid_kcal=40

low_high_kcal=25
mid_high_kcal=30
high_high_kcal=35
#每日熱量
print('每日熱量建議')
#體重過輕者
print('-----------------')
print('體重過輕者所需熱量:')
print('輕度工作: '+str(low_low_kcal)+' kcal')
print('中度工作: '+str(mid_low_kcal)+' kcal')
print('重度工作: '+str(high_low_kcal)+' kcal')
#體重正常者
print('-----------------')
print('體重正常者所需熱量:')
print('輕度工作: '+str(low_mid_kcal)+' kcal')
print('中度工作: '+str(mid_mid_kcal)+' kcal')
print('重度工作: '+str(high_mid_kcal)+' kcal')
#體重過重者
print('-----------------')
print('體重過重者所需熱量:')
print('輕度工作: '+str(low_high_kcal)+' kcal')
print('中度工作: '+str(mid_high_kcal)+' kcal')
print('重度工作: '+str(high_high_kcal)+' kcal')
print('-----------------')
#顯示我的熱量計算
print('我的體重:49kg')
w=49
print('我的身高:158cm')
h=158
print('我的工作量:正常')
print('我的bmi:正常')
print('我所需的熱量:'+str(mid_mid_kcal*w))
print('-----------------')
#顯示我的每日飲食建議量
#使用變數，可幫助之後有其他大卡的數據可以直接修正
a=3
b=5
c=1.5
d=3
e=2
f=5
print('由於我是1715大卡\n(因此我大約需要1800大卡):')
print('全榖雜糧類:'+str(a)+'份')
print('豆魚蛋肉類:'+str(b)+'份')
print('乳品類    :'+str(c)+'份')
print('蔬菜類    :'+str(d)+'份')
print('水果類    :'+str(e)+'份')
print('油脂類    :'+str(f)+'份')
print('total     :'+str(a+b+c+d+e+f)+'份')
print('-----------------')
print('以下為每日餐盤建議')
print('每天早晚一杯奶\n')
print('每餐水果拳頭大\n')
print('菜比水果多一點\n')
print('飯跟蔬菜一樣多\n')
print('豆魚蛋肉一掌心\n')
print('堅果種子一茶匙\n')
print('-----------------')
