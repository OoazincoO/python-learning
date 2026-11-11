---
tags:
  - Python
  - Python/异常
---

## 介绍
异常(也称为Bug)就是程序运行过程中出现的错误，它会中断程序的正常执行流程。
作用:
 - 保证数据、逻辑的正确性，避免程序执行混乱
 - 在开发阶段，尽量发现更多的问题，尽早解决问题，保障程序正常执行
 **类型**:==NameError|TypeError|IndexError|KeyError|ValueError==
## 异常处理 
程序运行过程中出现异常,有两种处理方案:
	1.不做处理:整个程序因为一个Bug,中断执行.
	2.捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行.(编写程序时,做好预案,出现异常,按预案处理)
```python
try:
	可能出现异常的业务代码1
	可能出现异常的业务代码2
	...
except[异常类型 as 变量名]: #[]内不填写或异常类型为Exception,则表示捕获所有出现的异常
	出现异常时的预案
finally:
	不管是否出现异常,都会执行的代码#可选

try:
	print("====")
	print(my_name)
	print("====")
except NameError as e:
	print("程序运行报错,错误信息:",e)
finally:
	print("释放资源")
```
## 异常传递
异常如果没有被捕获处理,不会消失,会==沿着[[函数基础|函数]]调用链逐层向上传递==,直到被某层捕获,或一路传到最顶层程序崩溃.
```python
def func1():
	print("func1开始")
	print(1/0)          # ZeroDivisionError,func1 没捕获,向上传递
	print("func1结束")  # 不会执行

def func2():
	print("func2开始")
	func1()             # 异常传进来,自己也没捕获,继续向上传递
	print("func2结束")  # 不会执行

func2()                 # 最外层也没人捕获,打印错误回溯,程序崩溃
```
传递规则:
	1.==try 捕获后异常不再传递==,程序从 except/finally 后继续往下执行
	2.调用链中==任意一层都能捕获==,一旦捕获,更上层不再收到这个异常
	3.一直没人捕获,Python 打印错误回溯(traceback)并终止程序
	4.finally 不拦截异常,只保证自己先执行完,异常继续向上传递
实际开发常用做法:底层函数不写 try,让异常向上传递,由最外层(主函数)统一捕获处理,预案集中、好排查
```python
def input_age():
	age = int(input("请输入年龄:"))   # 输入非数字会抛 ValueError
	if age < 0:
		raise ValueError("年龄不能为负")  # raise 主动抛出,同样按传递规则向上传递
	return age

def main():
	try:
		age = input_age()
	except ValueError as e:
		print("输入有误:",e)

main()
```
> [!tip]
> 想在 except 捕获后继续让异常向上传递,在 except 里写不带参数的 raise,把当前异常原样抛出.

> [!warning]
> 异常传递只沿调用链向上,不会跳到无关的函数;也不要用异常当流程控制,正常业务逻辑该用 [[if条件判断|if 判断]].
