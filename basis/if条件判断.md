```python
point = 405  
if point > 400:  
     print("欢迎")  
if point <400 :  
     print("抱歉")
```

## 案例,登录网站  
numbers= "18888888888"  
password = "666888"

```python
innumbers = input("请输入账号:")  
inpassword = input("请输入密码:")  
if numbers == innumbers and password == inpassword:  
    print("登录成功")  
    print("欢迎")    
if numbers != innumbers or password != inpassword:  
    print("登录失败")  
    print("账号或密码错误")  
  
  
if numbers == innumbers and password == inpassword:  
    print("登录成功")  
    print("欢迎")  
else :  
    print("登陆失败")  
    print("账号或密码错误")
```
## 案例:判断为闰年或平年
```python
year = int(input("请输入年份:"))  
  
#如果是非整百年份,且能被4整除或为整百年份,能被400整除则为闰年  
  
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  
    print(f"{year}为闰年")  
else :  
    print(f"{year}是平年")
```
## 需求1判断数字奇偶
```python
num = int(input("请输入一个整数"))  
if num % 2 == 0 :  
    print(f"{num}为偶数")  
else :  
    print(f"{num}为奇数")
```
## 需求2判断该数字为正数or负数or0
```python
num = float(input("请输入一个数字"))  
  
if num == 0 :  
    print(f"{num}为0")  
elif num > 0 :  
    print(f"{num}为正数")  
else :  
    print(f"{num}为负数")
    
```
## 案例3:根据输入用户名,密码进行登录系统
admin/888888   root/123123   zhangsan/333333
```python
username = input("请输入用户名:")  
password = input("请输入密码:")  
  
if username == "admin" and password == "888888":  
    print("登录成功")  
elif username == "root" and password == "123123":  
    print("登录成功")  
elif username == "zhangsan" and password == "333333":  
    print("登录成功")  
else :  
    print("登录失败,账号或密码错误")
```
## 案例:三角形类型判断:根据输入的三个边的边长,判定是等边三角形,等腰三角形,普通三角形,还是不能构成三角形
1.构成三角形的条件:两边之和大于第三边  
2.三角形判定规则:  
    三个边都相等:等边三角形  
    两个边相等:等腰三角形  
    三个边不相等:普通三角形
```python
a= input("请输入a的值")  
b= input("请输入b的值")  
c= input("请输入c的值")  
if a+b<c or a+c<b or b+c<a :  
    print("不能构成三角形")  
elif a == b and b == c :  
    print("该三角形为等边三角形")  
elif a==b or b==c or a==c:  
    print("该三角形为等腰三角形")  
else :  
    print("该三角形为普通三角形")  
  
  
if a+b>c and a+c>b and b+c>a :  
    if a == b and b == c :  
        print("该三角形为等边三角形")  
    elif a == b or b == c or a == c:  
        print("该三角形为等腰三角形")  
    else:  
        print("该三角形为普通三角形")  
else :  
    print("不能构成三角形")
```
