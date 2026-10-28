---
tags:
  - Python
  - Python/流程控制
  - Python/循环
---

==*本质是一种轮询遍历机制,对一批内容逐个处理.*==
语法结构
```
for 元素 in 待处理数据集:
	循环体代码(对元素进行处理)
else:  #可选
	循环结束时,实行代码
```
# range语句 #range
## 作用:生成指定规则的数字序列
> [!warning] range 包头不包尾
> ==所有 range 都不含 end 本身==，和切片一个脾气（见 [[列表(list)|列表]] 的切片）。

### 用法一: 
`range(end)`    ***获取一个从0开始到end结束的数字序列(不含end本身)***
`range(5)`*获得的序列为 0,1,2,3,4*

### 用法二:
`range(start,end)`  ***获取一个从start开始到end结束的数字序列(不含end本身)***
`range(3,9)`*获得的数字序列为3,4,5,6,7,8*

### 用法三:
`range(start,end,step)` ***获取一个从start开始到end结束的数字序列,step步长(不含end本身)***

`range(4,20,5)`*获得的数字序列为4,9,14,19*

> [!info] 对比着记
> for 配 range 用（知道次数），while 配条件用（不知道次数），见 [[while循环]]。
