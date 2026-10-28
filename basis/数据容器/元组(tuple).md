---
tags:
  - Python
  - Python/数据容器
  - Python/元组
---

## 介绍:
元组是**不可变**的序列,类似于[[列表(list)|列表]],但创建后不可修改.

> [!warning] 坑：不可变的是"元素引用"
> 如果元组里装了一个列表，==那个列表本身是能改的==。元组锁住的是"装什么"，锁不住"里面的东西自己变"。

### 特点:
- 可以存储不同类型的元素
- ==元素可以重复,有序,不可以修改==(支持索引访问,切片)
### 与列表的区别:
- 列表中的元素是可重复,有序,可以修改的
- 而元组定义完成后,是不可修改的
- 元组定义的时候用的是小括号()而列表为中括号\[]
### 定义:
```
#定义元组
元组名称 = (元素1,元素2,.....)
t1 = (5,7,8,2,3,4,6,121323,44,123)

#定义空元组
元组名称 = ()
元组名称 = tuple()
t2 = ()
t3 = tuple()
```

### 方法:
- count():统计某元素在元组中出现的次数
- index():查找某个元素在元组中的索引位置(第一次出现的位置)
## 元组操作

### 索引访问
与列表一致

```python
t1 = (23,42,314,123,5,1,2,3,42,51)

print(t1[0])  # 输出结果为23
print(t1[-1])  #输出结果为51
```
### 切片 #切片
与列表一致

```python
t1 = (23,42,314,123,5,1,2,3,42,51)

print(t1[0:5:1])

```
### 统计元素的个数
```python
print(t1.count(42)) # 输出的结果为2
```

### 获取元素的索引(第一个元素的位置)
```python
print(t1.index(314)) #输出结果为2
```

### 定义单元素元组 #单元素元组
==如果定义单元素的元组,须在元素后加个逗号","==
```python
t2 = (100,)
```
> [!warning] 最容易忘的逗号
> `(100)` 只是普通数字 100，==必须写成 `(100,)`== 才是元组。

### 组包(packing) #组包
将多个值合并到一个容器(元组,列表)中.
**也就是定义时可以省略括号**
```python
#定义元组,解包
t1 = (5,4,7,6)
t2 = 5,4,7,6
```
### 解包(unpacking) #解包
将容器(元组,列表)解开成独立的元素,分别赋值给多个[[字面量与变量|变量]].
==**在元组解包时,\*表示收集剩余的所有元素**==,允许我们处理不确定数量的元素(生成列表,与便于可以进行进一步的处理).
```python
#基础解包
a,b,c,d = t1

#(*)扩展解包
x,*y,z = t2  #x为5,y为[4,7],z为6
s,*o = t2  #s为5,o为[4,7,6]
*o,e = t2  #o为[5,4,7],e为6
```

## 案例
### 案例一:
现有两个变量，分别为:a=10，b=20，现需要将这两个变量值交换，然后输出到控制台。
```python
a = 10
b = 20

a,b = b,a   #b,a为组包操作 a,b为解包操作(意会一下)
print(a) #20
print(b) #10
```
> [!tip] 变量交换
> ==a,b = b,a 是 Python 的经典写法==，不用中间变量，右边先组包、左边再解包。

### 案例二:
现有三个变量，分别为:a=100.b=200.c=300，现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b，并将其输出到控制台。
```python
a =100
b =200
c =300

a,b,c = b,c,a
print(a) #200
print(b) #300
print(c) #100
```
### 案例三:
根据如下提供的学生成绩单，完成如下需求:
1.计算每个学生的总分、各科平均分，然后一并输出出来。
2.统计各科成绩的最低分、最高分、平均分，并输出。
3.查找成绩优秀(平均分大于90)的学生，并输出。

| 学号   | 姓名  | 语文  | 数学  | 英语  |
| :--- | :-- | :-- | :-- | :-- |
| S001 | 王林  | 85  | 92  | 78  |
| S002 | 李慕婉 | 92  | 88  | 95  |
| S003 | 十三  | 78  | 85  | 82  |
| S004 | 曾牛  | 88  | 79  | 91  |
| S005 | 周轶  | 95  | 96  | 89  |
| S006 | 王卓  | 76  | 82  | 77  |
| S007 | 红蝶  | 89  | 91  | 94  |
| S008 | 徐立国 | 75  | 69  | 82  |
| S009 | 许木  | 86  | 89  | 98  |
| S010 | 遁天  | 66  | 59  | 72  |

#### 方式一:
```python
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
#1.计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students: #("S001","王林",85,92,78)
	total = s[2]+s[3]+s[4]
	avg = total/3
	print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{avg:.1f}")
#2.1获取到各科成绩列表
Chinese_scores = [s[2] for s in students]
Math_scores = [s[3] for s in students]
English_scores = [s[4] for s in students]
#2.2统计各科成绩的最高分,最低分,平均分,并输出.
print(f"语文最低分:{min(Chinese_scores)},最高分{max(Chinese_scores)},平均分{sum(Chinese_scores)/len(Chinese_scores)}")
print(f"数学最低分:{min(Math_scores)},最高分{max(Math_scores)},平均分{sum(Math_scores)/len(Math_scores)}")
print(f"英语最低分:{min(English_scores)},最高分{max(English_scores)},平均分{sum(English_scores)/len(English_scores)}")
#3.查找成绩优异(平均分大于90的学生),并输出.
print("优秀学生(平均分大于90的学生)名单")
for s in students:
	total = s[2] + s[3] + s[4]
	avg = total / 3
	if avg > 90:
		print(f"学号:{s[0]}\t姓名:{s[1]}\t平均分{avg:.1f}")
	
```
#### 方式二:part1中可用元组解包
```python
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
#1.计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id,name,chinese,math,english in students: #("S001","王林",85,92,78)
	total = chinese + math + english
	avg = total/3
	print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")
#2.1获取到各科成绩列表
Chinese_scores = [s[2] for s in students]
Math_scores = [s[3] for s in students]
English_scores = [s[4] for s in students]
#2.2统计各科成绩的最高分,最低分,平均分,并输出.
print(f"语文最低分:{min(Chinese_scores)},最高分{max(Chinese_scores)},平均分{sum(Chinese_scores)/len(Chinese_scores)}")
print(f"数学最低分:{min(Math_scores)},最高分{max(Math_scores)},平均分{sum(Math_scores)/len(Math_scores)}")
print(f"英语最低分:{min(English_scores)},最高分{max(English_scores)},平均分{sum(English_scores)/len(English_scores)}")
#3.查找成绩优异(平均分大于90的学生),并输出.
print("优秀学生(平均分大于90的学生)名单")
for id,name,chinese,math,english in students: 
	total = chinese + math + english
	avg = total/3
	if avg > 90:
		print(f"学号:{id}\t姓名:{name}\t平均分{avg:.1f}")
	
```
