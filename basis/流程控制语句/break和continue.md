---
tags:
  - Python
  - Python/流程控制
  - Python/循环
---

1.==**break只能够出现在循环中,表示结束,或跳出当前循环**==
==*break跳出循环时,[[while循环|while]]后面的else中的代码不会执行*==
2.==continue执行时循环回到开头==（跳过本次剩余代码，直接下一轮）
## 案例一:登录
*根据输入的用户名密码执行登录操作，具体要求如下:
1.正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666
2、输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录
3.输入的用户名和密码不能为空!
4.登录成功:输出“登录成功，进入B站首页~”
5.登录失败:输出“用户名或密码错误，请重新输入!"

> [!tip] 这个案例是标准模板
> ==`while True` + 成功就 break + 失败/无效就 continue==，"反复重试直到成功"的固定套路，登录、菜单、猜数字都这么写。

```python
while True:
	username = input("请输入正确的用户名:")
	password = input("请输入正确的密码:")
	if username == "" or password == "":
		print("输入的用户名和密码不能为空!请重新输入")
		continue
	if username == "admin" and password == "666888":
		print("登录成功,进入网站首页")
		break
	elif username == "zhangsan" and password == "123456":
		print("登录成功,进入网站首页")
		break
	elif username == "taoge" and password == "888666":
		print("登录成功,进入网站首页")
		break
	else:
		print("用户名或密码错误,请重新输入")
```
