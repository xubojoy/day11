#Author:xubojoy
import time,sys,os
user_file=open("user_file",'r+',encoding='utf-8')#打开用户列表文件
#with open('user_file.txt','r+',encoding='utf-8') as user_file:
user_list=eval(user_file.readline())#转换用户文件中的字符串  user_list:注册用户列表
lock_name=open('lock_name','r+',encoding='utf-8')#打开锁定用户列表文件
lock_list=eval(lock_name.readline())#转换锁定用户文件中的字符串


def regis():
    while True:
        name=input("请输入您要注册的用户名：")
        if name not in user_list:
            print("恭喜！该用户名可以被注册！>>>")
            password=input('请输入密码：')
            password2=input('请再次确认密码：')
            if password==password2:
                name_infor='''恭喜您用户注册成功！
                    用户名：{name}
                    密  码：{password}
                    请牢记您的用户名与密码
                '''
                print(name_infor.format(name=name,password=password2))
                user_list[name]=password2#增加注册用户到字典中
                user_file.seek(0)#称到最前
                user_file.write(str(user_list))#写入文件
                user_file.flush()#即可保存

                #confirm()
                break
        else:
            print("该用户名已经被注册啦！请重新来过<<<")
            confirm()#是否退出
            continue



def userchar(_user_name):#检测用户名的函数
    while True:
        if _user_name in user_list and _user_name not in lock_list:#判断用户是否存在并正常
            return True#存在返回真
        elif _user_name in user_list and _user_name  in lock_list:#判断用户是否被锁定
            print('您的用户已经被锁定，请联系商家解锁！')
            break
        else:
            reg=input('您输入用户不存在，请先注册！按\033[31;1m Q/q\033[0m 直接退出  \033[31;1m Y/y\033[0m 确定注册，其它键返回！')
            if reg=='y' or reg=='Y':
                regis()#用户注册函数
                print('是否直接退出商城？')
                break
            elif  reg=='q' or reg=='Q':
                print("您已经退出！" )
                exit()
            else :
                break

def confirm():#退出确认函数
    qu=input("是否退出！按\033[31;1mY/y\033[0m退出？ 按其它键返回<<<")
    if qu=='Y'or qu=='y':
        print("您已经退出！" )
        exit()#退出程序
    else :
        pass

def user_pass():
    bool=True#定义退出循环条件变量
    while bool:
        print("用户登陆".center(30,'-'))
        _user_name=(input('请输入用户名：'))
        if userchar(_user_name.strip()):#运行检测用户名的函数判断，去除两边空格
            count=3#定义锁次数
            while count>0 :#如果密码错误次数超过退出密码输入
                #password=getpass.getpass('请输入密码:')
                password=input('请输入密码:')
                if password==user_list[_user_name]:#密码通过验证结束循环
                    print("密码通过验证")
                    bool=False
                    print("欢迎您  \033[32;1m%s\033[0m  您已经登陆成功！" % _user_name)
                    return _user_name#返回用户名
                else:
                    count -=1#次数减少
                    print("密码错误请重试，剩余:\033[31;1m%s\033[0m次! "% count)
                    pass
            else:
                print("\033[31;1m超出所试次数，账户已锁定！请联系商家！\033[0m")
                lock_list.append(_user_name)#将用户名加出锁定列表
                lock_name.seek(0)#指针移动到开头，以免产生多个元组
                lock_name.write(str(lock_list))#写入锁定用户文件
                lock_name.tell()#获取当前指针,以免产生多个元组
                lock_name.close()#关闭锁定用户文件
                confirm()#退出确认函数
                #continue#退回到输入用户名的位置
        else:#如果用户名出错新来过
            confirm()
            pass

def infor():#打开用户信息函数
    with open('user_infor','r+',encoding='utf-8') as user_infor:#打开用户购物信息文件
        infor_list=eval(user_infor.readline())#转换文件的字符串
    return infor_list

def history_user():#用户购物历史记录函数
    with open('history','r',encoding="utf-8") as user_history:#读取用户文件
        history_list=eval(user_history.readline())#用户购物信息
    return history_list

def history():#用户消费记录函数
    history_list=history_user()#用户购物历史记录
    history=history_list[_user_name]#用户购物记录信息
    print('您的购物记录如下:')
    for k,v in history.items():#转为列表进行输出
        print(k,v)#输出购物记录
    choose_index=input("请选择您想要的操作:按\033[32;1mq/Q\033[0m直接退出商城！其它键返回！")
    if choose_index=='Q' or choose_index=='q' :
        choo=input('''>>>>>\033[42;1m您确定出退商城吗？\033[0m
                    如果您已经添加商品，此操作将不进行结算，
                    您就无法将心爱的东东买回家了，按\033[31;1my/Y\033[0m确定直接退出！''')
        if choo=='y'or choo=='Y':
            print("您已经出退商城！")
            exit()
    else:
        pass
#程序开始：
if os.path.exists('history'):#确认文件是否存在
    pass
else:
    with open('history','w',encoding='utf-8') as user_history:#创建一个用户帐户购物记录文件
        user_history.write('{}')#写入空值
    pass

if os.path.exists('user_infor'):#确认文件是否存在
    pass
else:
    with open('user_infor','w',encoding='utf-8') as user_infor:#创建一个用户帐户信息记录文件
        user_infor.write('{}')#写入空值
    pass

print("欢迎来到\033[31;1mpython\033[0m购物商城！")

time_format='%y-%m-%d %X'#定义时间格式
times=time.strftime(time_format)#定义时间
_user_name= user_pass()#将通过验证的用户名赋于变量

if _user_name in infor():#如果用户信息存在记录就跳过
    pass
else:
    while True:
        name_char=input("首次登陆，请输入工资（购物资金）：")#用户输入工资（购物资金）
        if  name_char.isdigit():#检测输入是否为整数
            name_char=int(name_char)#转为int
            with open('history','r+',encoding='utf-8') as user_history:#打开用户帐户购物记录文件
                history_list=eval(user_history.readline())#将文本读为字典
                history_list[_user_name]={}#创建用户购物记录
                user_history.seek(0)#移到开头
                user_history.write(str(history_list))#写入文件
            with open('user_infor','r+',encoding='utf-8') as user_infor:
                infor_list=eval(user_infor.readline())#转换首登用户文件中的字符串
                infor_list[_user_name]={"金额":name_char}
                user_infor.seek(0)
                user_infor.write(str(infor_list))#写入用户信息
            print("充值成功，充值金额：\033[32;1m%s\033[0m元."% name_char)
            break
        else:
            print('金额不能为0或负数请正确输入金额！')
            continue

#再次登陆直接显示用户信息
infor_list=infor()#使用用户信息函数 获取用户信息字典
name_char=int(infor_list[_user_name]['金额'])#获取余额
print("\n您的帐户信息：")
print('用户名:\033[32;1m%s\033[0m:'%_user_name)#输出用户信息
print('您的余额:\033[31;1m%s\033[0m元.:'%name_char)
while True:
    print('''您可以进行以下相关操作:\n
            按 1 >>>查询购物记录。
            按 2 >>>显示商品列表开始购物！
            按 3 >>>直接出退商城！
    ''')
    choose=input("请选择您所要的功能：")#请用户可以查询
    if choose=='1':
        history()#查询消费记录
    elif choose=='2':
        ###进入商品列表###
        shoplist=[]#购物车列表
        shop_count=0#购物金额统计
        goodsname=[]#定义商品列表
        print('加载商品列表：')
        for i in range(40):#加载动画
            sys.stdout.write('#')
            sys.stdout.flush()
            time.sleep(0.05)
        print('\n')
        with open('goodslist.txt','r',encoding='utf-8') as f:#打开商品列表文件
            for line in f:
                a=line.find(',')#定位分割符的索引进行分割
                goodsname.append((line[0:a],int(line[a+1:])))#元组模式追加到列表,价格转为整数
        while True:
            print("商品列表".center(50,'='))
            for index,p_item in enumerate(goodsname):#取出下标输出 商品列表
                print(index,p_item)#输出商品列表
            print("列表底部".center(50,'='))
            user_index=input('请输入商品编号添加你所在购买的商品,按\033[31;1mc/C\033[0m>> 查看当前购物清单, \033[31;1mh/H\033[0m查看消费记录 \033[31;1mq/Q\033[0m结算商品退出>>>:')
            if user_index.isdigit():#判断是否为整数
                user_index=int(user_index)#转为数字
                if user_index < len(goodsname) and user_index>=0:#判断所选商品编号在在列表
                    p_item=goodsname[user_index]#读取下标所在（元素）商品
                    if p_item[1]<=name_char:#余额是否足够
                        shoplist.append(p_item)#添加到购物车
                        name_char-=p_item[1]#扣除金额
                        shop_count+=p_item[1]#累加购物金额
                        print("添加 \033[32;1m%s\033[0m 到购物车，价格： \033[32;1m%s\033[0m 元"% p_item)
                        print("你的购物金额余: \033[31;1m%s\033[0m 元"% name_char)
                    else:
                        print("你的购物金额余: \033[41;1m%s\033[0m 元,无法购买该商品!" % name_char)
                else:
                     print('输入错误，该编号 \033[41;1m%s\033[0m 的商品不存在!'%user_index)
            elif user_index=='q'or user_index=='Q':
                print('你的购物清单：')
                for up in shoplist:#打印购物清单
                    print(up)
                print("你的购物总金额为：\033[32;1m%s\033[0m 元!"% shop_count)
                print("你的购物金额余： \033[31;1m%s\033[0m 元!" % name_char)
                while True:
                    confirm=input("你是否确定结算商品并退出商城？\033[31;1m Y/y\033[0m是, \033[31;1mN/n\033[0m否:")
                    if confirm== 'Y'or confirm== 'y' :
                        infor_list[_user_name]['金额']=name_char#修改用户金额（购物后）
                        shoplist.append(('总额:',shop_count))#列表加入总额
                        history_list=history_user()#用户消费记录函数
                        history_list[_user_name][times+'购物清单:']=shoplist#添加时间:清单
                        with open('user_infor','w',encoding="utf-8") as user_infor:#写入文件用户信息
                            user_infor.seek(0)#移到最前
                            user_infor.write(str(infor_list))#写入
                        with open('history','r+',encoding='utf-8') as user_history:#购物信息写入文件
                            user_history.seek(0)#移到最前
                            user_history.write(str(history_list))#写入
                        exit(print("谢谢!\033[31;1mpython\033[0m 商城欢迎您再次光临！"))
                    elif confirm=='N'or confirm== 'n' :
                        break
                    else:
                        print("输入错误！请按提示输入！")
                        continue
            elif user_index=='h'or user_index=='H':
                history()#查消费记录
            elif user_index=='c'or user_index=='C':
                print("当前购物清单：")
                for up in shoplist:#打印购物清单
                    print(up)
                print("总金额：\033[32;1m%s\033[0m"%shop_count)
                continue
            else:
                print('\033[41;1m输入商品编号错误，请重新输入！\033[0m')

    elif choose=='3':
        print("您已经出退商城！")
        exit()#退出商城
    else:
        print("\033[31;1m输入有误，请重新输入！\033[0m")
        continue