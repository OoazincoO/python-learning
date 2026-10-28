---
tags:
  - Python
  - Python/流程控制
  - Python/循环
---

```python
i=0
while i<10:
	print("人生苦短")
	i+=1
else:
	print("循环正常结束,执行完毕")
```
==while语句中当条件表达式中为True,则继续循环,当表达式为False时跳出循环或进入else==

> [!warning] 两个必查点
> 1. 循环体里==必须有改变条件的语句==（如 `i+=1`），否则死循环
> 2. while 也有 else，==只有循环正常结束才执行==，被 [[break和continue|break]] 跳出就不执行

> [!tip] 不知道循环几次时用 while
> 对比 [[for循环]]：for 是"轮询遍历"（次数确定），while 是"条件成立就继续"（次数不确定，比如登录重试）。
