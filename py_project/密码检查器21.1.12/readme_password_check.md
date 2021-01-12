# 密码检查器

## 一、解题思路
 1.我要做什么？<br>
+ 写一个密码检查器  

 2.我要怎么做，分几步？每一步用到哪些语句，方法和对象<br>
>1.写一个固定的密码  
>2.写一个检查密码的函数  
>>* 2.1.密码输入错误等于5次，休眠30秒，继续运行本函数  #1.if语句 2.==比较运算符 3.time.sleep()方法  
>>* 2.2.循环5次 # 1.for循环 2.range()函数  
>>  * 2.2.1.用户输入密码 # 1.input()函数  
>>  * 2.2.2.比较 固定密码 和 用户输入密码 # 1.for循环遍历字符串的索引 2.if语句 3.==比较运算符 4.if-else语句 5.break语句  
>>    * 2.2.2.1输出密码正确或错误 # 1.if-else语句 2.break语句  
         
 3.用代码把思路体现出来<br>
 
## 二、代码及解答
    
    密码检查器
    1.写一个固定的密码
    2.写一个检查密码的函数
        2.1.密码输入错误等于5次，休眠30秒，继续运行本函数  #1.if语句 2.==比较运算符 3.time。sleep()方法
        2.2.循环5次 # 1.for循环 2.range()函数
            2.2.1.用户输入密码 # 1.input()函数
            2.2.2.比较 固定密码 和 用户输入密码 # 1.for循环遍历字符串的索引 2.if语句 3.==比较运算符 4.if-else语句 5.break语句
                2.2.2.1.输出密码正确或错误 # 1.if-else语句 2.break语句
    
    
    import time
    pwd = "wzc1993"
    
    def password_check():
      count1 =0
      for i in range(5):
        a = 0  # a是pwd的长度
        count = 0  # count是user_pwd的长度
        user_pwd = input("请输入密码：")
        for j in range(len(pwd)):  # 以固定密码的长度进行循环
          if user_pwd[j] == pwd[a]:  # 把固定密码的索引给user_pwd
            a += 1  # a是pwd的长度
            count += 1  # count是user_pwd的长度
        if count == len(pwd):  # 如果pwd长度等于user_pwd的长度，就说明密码正确
          print("密码正确")
          break  # 跳出循环
        else:  # 否则密码错误，count1加1
          count1 +=1
          print("密码错误")
      if count1 == 5:  # 如果密码输入错误等于5次，休眠30秒，继续运行本函数
        time.sleep(30)
        password_check()
    
    password_check()
    
## 三、提出问题
 1
 
## 四、强化薄弱的基础知识
 1.if语句  
 2.==比较运算符  
 3.for循环  
 4.range()函数  
 5.input()函数  
 6.if-else语句  
 7.break语句  
 
## 五、重复以上步骤
 1.记录每一次，重复写代码的时间和感悟<br>
 
| 次数 | 时间 | 感悟 |
| :---          |     :---:      |          ---: |
|     |      |     |
|       |        |       |

