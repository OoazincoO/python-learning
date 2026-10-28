---
tags:
  - Python
  - Python/数据容器
  - Python/字典
---

> [!tip] 实战出口
> 学完字典就能用哈希表重做 [[Two Sum-暴力到哈希的优化|Two Sum]]，把暴力的 O(n²) 优化到 O(n)。横向对比三个维度（是否有序、是否可重复、是否可修改）见 [[概述|数据容器概述]]。

## 介绍
使用键值对(key:value)来存储数据,每一个键都对应一个值,通过键(key)可以快速找到对应的值(value).
### 特点
键值对(key:value)存储,==键(key)不能重复==,可修改.
### 定义
```python
#定义字典
字典名称 = {key:value,key:value,......}
dict1 = {"王林":231,"李木碗":123}
#定义空字典
字典名称 = {}
字典名称 = dict()
dict2 = {}
dict3 = dict()
#根据key获取value
值 = 字典名称[key]
score = dict1["王林"] # 231
```
**字典中的value可以是任何类型的数据,而key==不能为可变类型==(如:不能为 [[列表(list)|列表]]、[[集合(set)|集合]]、字典dict)**

> [!info] 反过来记
> ==[[元组(tuple)|元组]] 可以当 key==（因为不可变），列表、集合、字典都不行。

## 常用操作
### 增删改 #增删改

| 类型     | 操作                  | 含义                          | 样例                        |
| ------ | ------------------- | --------------------------- | ------------------------- |
| **添加** | `字典名称[key] = value` | 往指定字典中添加key-value键值对        | `dict1["涛哥"] = 688`       |
| **删除** | `字典名称.pop(key)`     | 删除字典中指定的key，并返回该key对应的value | `score = dict1.pop("涛哥")` |
| **删除** | `del 字典名称[key]`     | 删除字典中指定的键值对                 | `del dict1["涛哥"]`         |
| **修改** | `字典名称[key] = value` | 修改字典中指定的key对应的值             | `dict1["小智"] = 658`       |
| **查询** | `字典名称[key]`         | 根据key获取value                | `dict1["涛哥"]`             |
| **查询** | `字典名称.get(key)`     | 根据key获取value                | `dict1.get("涛哥")`         |
| **查询** | `字典名称.keys()`       | 获取所有的key                    | `dict1.keys()`            |
| **查询** | `字典名称.values()`     | 获取所有的value                  | `dict1.values()`          |
| **查询** | `字典名称.items()`      | 获取所有的key-value键值对           | `dict1.items()`           |

> [!warning] 取值的两种写法不一样
> `dict1[key]` 的 key 不存在会 ==报 KeyError==，`dict1.get(key)` 则 ==返回 None 不报错==。不确定 key 在不在，用 get()。

### 遍历 #字典遍历
字典是支持遍历的

> [!tip] 遍历三件套
> 配合上面的 keys()、values()、items()：`for k in dict1`、`for v in dict1.values()`、`for k, v in dict1.items()`。

## 案例
### 案例一:
通过控制台菜单与用户交互。具体功能如下:
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
5.退出购物车。
```python
shopping_cart = {}
#1.制作菜单
print('欢迎使用购物车系统')
menu = """
========购物车系统=======
=     1.添加购物车      =
=     2.修改购物车      =
=     3.删除购物车      =
=     4.查询购物车      =
=     5.退出购物车      =
========================
"""
while True:
	print(menu)
	#2.执行的具体操作
	choice = input("请输入要执行的操作(1-5):")
	
	match choice:
		case "1":
			goods_name = input("请输入商品名称:")
			if goods_name in shopping_cart:
				print("商品已存在,请重新选择!")
				continue
			goods_price = float(input("请输入商品价格:"))
			goods_num = int(input("请输入商品数量:"))
			shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
			print("商品添加成功")
			
		case "2":
			goods_name = input("请输入要修改的商品名称:")
			if goods_name not in shopping_cart:
				print("商品不存在,请重新选择")
				continue
			goods_price = float(input("请输入商品最新价格:"))
			goods_num = int(input("请输入商品最新数量:"))
			shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}	
			print("商品修改完毕")	
		case "3":
			goods_name = input("请输入商品名称:")	
			if goods_name not in shopping_cart:
				print("商品不存在,请重新选择")
				continue
			else:
				del shopping_cart[goods_name]
				print("商品删除完毕")
		case "4":
			choice1 = input("查询全部购物车请输入1;查询单个商品请输入2")
			match choice1:
				case "1":
					for goods_name in shopping_cart.keys():
						goods_info = shopping_cart[goods_name]
						print(f"商品名称:{goods_name},商品价格:{goods_info['price']},商品数量:{goods_info['num']}")
				case "2":
					goods_name_choice = input("请输入要查询的商品名称")
					if goods_name_choice not in shopping_cart:
						print("该商品不存在,请重新选择")
						continue
					goods_info = shopping_cart[goods_name_choice]
					print(f"商品名称:{goods_name_choice},商品价格:{goods_info['price']},商品数量:{goods_info['num']}")
		case "5":
			print("bye~")
			break
		case _:
			print("非法操作,不支持")
```