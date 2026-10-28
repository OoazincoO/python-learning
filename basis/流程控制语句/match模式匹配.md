---
tags:
  - Python
  - Python/流程控制
  - Python/模式匹配
---

> [!info] 版本要求
> match...case 是 ==Python 3.10+== 的新语法，作用类似 [[if条件判断]] 的多分支，但更适合"按值分发"的场景。

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
> [!tip] 三个语法点
> ==`"6"|"7"` 是"或"模式==（任一匹配即可），==`case _` 是兜底分支==（相当于 else，必须放最后）。

## 基于match.... case 实现计算器功能实现简单加减乘除 #守卫条件
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
> [!warning] case 后面的 if 是守卫条件
> ==`case "/" if num2 != 0:` 只有 if 成立才真正匹配==；守卫不成立会继续往下找其他分支（最后落到 `case _`），这是 match 和普通 if 最大的不同。
