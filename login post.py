import requests
import random
import string
from urllib.request import Request,urlopen
import time


'''
钓鱼网站垃圾数据提交脚本
作用：给一些盗号网站添加垃圾
'''

#====================================
#         垃圾数据生成函数
#====================================

#生成随机账号
def GetID():
    id = random.randint(100000000, 3000000000)
    return id

# 生成无规律随机密码
def GenPassword(length=8):
    result=''
    chars=string.ascii_letters+string.digits
    for i in range(length):
        result=result+random.choice(chars)
    return result

# 生成规律的随机密码
#电话号码+三个字母
def PhonePassword(Nlen=10,Llen=3):
    num='1'
    ltr=''
    for i in range(Nlen):
        num = num + random.choice(string.digits)
    for i in range(Llen):
        ltr = ltr + random.choice(string.ascii_letters)

    return num + ltr

#生成随机单词
def GetWord():
    with open("words.csv") as file:
        words = file.readlines()
        word = random.choice(words)
        word = word.replace(',\n',' ')
        return word

#生成数字+单词密码
def NumAndWord():
    id = random.randint(10000, 100000000)
    password = GetWord()
    return str(id) + password

#生成以上混合格式密码
def GetAllKindPassword():
    _case = random.randint(1,3)
    if _case ==1:
        return GenPassword()
    if _case ==2:
        return PhonePassword()
    if _case ==3:
        return NumAndWord()

#====================================
#         提交垃圾数据函数
#====================================


#对于低端钓鱼网站
#直接在链接后跟参数的网站
def hahaha(times=10):
    for i in range(times):
        id = GetID()
        password = RegularPassword()
        url = "http://7x24e.com/dnf.php?u="+str(id)+"&p="+password
        response = urlopen(url)
        print(response)
        time.sleep(3)
    
#使用post提交的网站
#开始post 设置 提交次数 默认10此
def StartPost(times=10):
    url ="http://localhost/test.php"
    for i in range(times):
        id = GetID()
        password =  GetAllKindPassword()
        params = {"username":id, "password":password}
        #params = {"u":id,"p":password}
        #params = {"code": "upload "}
        html = requests.post(url,data=params)
        i=i+1
        print(html.text)

#====================================
#          开始提交垃圾数据
#====================================

StartPost(500)


        

