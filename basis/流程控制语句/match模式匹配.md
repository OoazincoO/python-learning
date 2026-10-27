---
tags:
  - Python
  - Python/流程控制
  - Python/模式匹配
---

```python
day = input("请输入星期几(1-9):")  
  
match day :  
    case "1":  
        print("周一:工作会议日")  
    case "2":  
        print("周二:学习日")  
    case "3":  
        print("周三:项目开发日")  
    case "4":  
        print("周四:代码审查日")  
    case "5":  
        print("周五:总结日")  
    case "6"|"7":  
        print("周末:休息日")  
    case _ :  
        print("error")
```

## 基于match.... case 实现计算器功能实现简单加减乘除
```python
num1 = float(input("请输入第一个数字"))  
num2 = float(input("请输入第二个数字"))  
oper = input("请输入运算符(+-*/)")  
  
match oper:  
    case "+":  
        print(f"{num1}+{num2}={num1+num2}")  
    case "-":  
        print(f"{num1}-{num2}={num1-num2}")  
    case "*":  
        print(f"{num1}*{num2}={num1*num2}")  
    case "/" if num2 != 0:  #if 条件成立,才匹配这个case  
        print(f"{num1}/{num2}={num1/num2}")  
    case _:  
        print("操作不支持!")  
  
  
  
inkey = input("请输入操作指令:")  
  
match inkey:  
    case "上" :  
        print("角色向上移动")  
    case "w" :  
        print("角色向上移动")  
    case "W" :  
        print("角色向上移动")
```
