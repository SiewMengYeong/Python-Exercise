#開場白
print('歡迎試玩戰鬥測試!!')
print('請問你要選什麼職業?')
print('1.劍士 2.遊俠 3.術士')
B=0
while B==0:
    JOB=input('請輸入代號:')
    if JOB=='1':
        HP=15
        MP=10
        DEF=2
        HIT=4
        AVO=2
        Skill='"猛擊"MP-3'
        
        B=1
    elif JOB=='2':
        HP=12
        MP=10
        DEF=1
        HIT=6
        AVO=4
        Skill='"二連閃"MP-5'
        
        B=1
    elif JOB=='3':
        HP=10
        MP=30
        DEF=1
        HIT=4
        AVO=2
        Skill='"火球"MP-6'
        
        B=1
    else:
        print('輸入錯誤,請再輸入一次')

#BATTLE
import random
print()
print('敵人"史萊姆A"出現')
EHP=12
EHIT=4
EAVO=1
B=0
C=0
dm=0
while B==0:
    d=1
    h=0
    C=0
    print('主角')
    print('HP:',HP,' MP:',MP,sep='')
    print('=======================')
    print('史萊姆A','HP:',EHP)
    print()
    print('請選擇行動')
    print('1.攻擊 2.防守 3.',Skill,sep='')
    while C==0:
        #主角回合
        A=input('A:')
        if A=='1':
            if JOB=='1':
                h=random.randint(1,20)
                if h>5:
                    a=random.randint(4,6)
                    EHP=EHP-a+dm
                    print('你給史萊姆A',a-dm,'點傷害')
                else:
                    print('你的攻擊未命中')
            elif JOB=='2':
                h=random.randint(1,20)
                if h>3:
                    a=random.randint(3,6)
                    EHP=EHP-a+dm
                    print('你給史萊姆A',a-dm,'點傷害')
                else:
                    print('你的攻擊未命中')
            elif JOB=='3':
                h=random.randint(1,20)
                if h>5:
                    a=random.randint(3,4)
                    EHP=EHP-a+dm
                    print('你給史萊姆A',a-dm,'點傷害')
                else:
                    print('你的攻擊未命中')
            C=1
            dm=0
        elif A=='2':
            print('你採取防禦')
            d=2
            C=1
            dm=0
        elif A=='3':
            if JOB=='1':
                if MP>1:
                    MP=MP-3
                    h=random.randint(1,20)
                    if h>5:
                        a=random.randint(4,6)
                        EHP=EHP-a-2+dm
                        print('你給史萊姆A',a+2-dm,'點傷害')
                    else:
                        print('你的攻擊未命中')
                    C=1
                else:
                    print('MP不足')
                    print('請再輸入一次')
            elif JOB=='2':
                if MP>0:
                    MP=MP-5
                    h=random.randint(1,20)
                    if h>3:
                        a=random.randint(3,6)
                        EHP=EHP-a+dm
                        print('你給史萊姆A',a-dm,'點傷害')
                    else:
                        print('你的攻擊未命中')
                    h=random.randint(1,20)
                    if h>3:
                        a=random.randint(3,6)
                        EHP=EHP-a+dm
                        print('你給史萊姆A',a-dm,'點傷害')
                    else:
                        print('你的攻擊未命中')
                    C=1
                else:
                    print('MP不足')
                    print('請再輸入一次')
            elif JOB=='3':
                if MP>0:
                    MP=MP-6
                    h=random.randint(1,20)
                    if h>5:
                        a=random.randint(3,4)
                        ma=random.randint(2,3)
                        EHP=EHP-a-ma+dm
                        print('你給史萊姆A',a+ma-dm,'點傷害')
                        ma=0
                    else:
                        print('你的攻擊未命中')
                    C=1
                else:
                    print('MP不足')
                    print('請再輸入一次')
            dm=0
        else:
            print('輸入錯誤,請再輸入一次')
    if EHP>0:
        #史萊姆回合
        h=random.randint(1,5)
        if h==1:
            print('史萊姆A防禦')
            dm=3
        else:
            print('史萊姆攻擊')
            h=random.randint(1,20)
            if h>5:
                a=random.randint(4,5)
                HP=HP-a+DEF*d
                print('史萊姆A給你',a-DEF*d,'點傷害')
            else:
                print('史萊姆A的攻擊未命中')
        if HP<=0:
            B=2
            print('主角行動不能')
    else:
        B=1
        print('史萊姆A被擊殺')
    print()
#END
if B==1:
    print('你獲得勝利')
    a=input('請按ENTER鍵使遊戲結束')
elif B==2:
    print('你不幸戰敗')
    a=input('請按ENTER鍵結束遊戲')
