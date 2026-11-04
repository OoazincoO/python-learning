下面列常见模块（不是全部，完整列表见文末方法）。

|分类|模块名|主要用途|
|---|---|---|
|系统/运行时|`sys`|解释器、命令行参数、路径等|
||`os`|操作系统接口、环境变量、进程等|
||`platform`|获取系统/平台信息|
||`builtins`|内置函数和异常|
||`gc`|垃圾回收控制|
||`signal`|信号处理|
||`errno`|系统错误码|
||`importlib`|动态导入模块|
||`pkgutil`|包/模块遍历|
||`warnings`|警告控制|
||`traceback`|异常堆栈信息|
|数学/数值|`math`|数学函数|
||`cmath`|复数数学函数|
||`random`|随机数|
||`decimal`|高精度十进制|
||`fractions`|分数|
||`statistics`|统计函数|
||`array`|紧凑数组|
|日期时间|`time`|时间、睡眠、时间戳|
||`datetime`|日期时间处理|
||`calendar`|日历相关|
|文本/正则|`re`|正则表达式|
||`string`|字符串常量和模板|
||`textwrap`|文本换行/缩进|
||`difflib`|文本差异比较|
|数据结构/函数式|`collections`|容器数据类型|
||`itertools`|迭代器工具|
||`functools`|高阶函数工具|
||`operator`|运算符函数形式|
||`heapq`|堆队列算法|
||`bisect`|有序列表二分|
||`copy`|浅拷贝/深拷贝|
||`pprint`|美化打印|
|序列化/数据|`json`|JSON 编解码|
||`pickle`|Python 对象序列化|
||`csv`|CSV 读写|
||`struct`|二进制打包/解包|
||`configparser`|INI 配置文件|
|文件/路径/IO|`io`|流式 IO|
||`pathlib`|面向对象路径操作|
||`os.path`|路径操作|
||`tempfile`|临时文件和目录|
||`shutil`|文件/目录高级操作|
||`glob`|通配符文件匹配|
||`fnmatch`|文件名模式匹配|
||`fileinput`|多文件逐行读取|
|压缩/归档|`gzip`|gzip 压缩|
||`bz2`|bzip2 压缩|
||`lzma`|LZMA 压缩|
||`zlib`|zlib 压缩|
||`zipfile`|ZIP 归档|
||`tarfile`|TAR 归档|
|加密/编码|`hashlib`|哈希算法|
||`hmac`|HMAC 签名|
||`secrets`|安全随机数/令牌|
||`base64`|Base64 编解码|
||`binascii`|二进制/ASCII 转换|
|并发/异步|`threading`|线程|
||`multiprocessing`|多进程|
||`concurrent.futures`|线程/进程池|
||`asyncio`|异步 IO|
||`queue`|线程安全队列|
||`subprocess`|启动子进程|
|网络/互联网|`socket`|底层网络通信|
||`ssl`|TLS/SSL|
||`select`|IO 多路复用|
||`http`|HTTP 相关包|
||`urllib`|URL 和网络请求|
||`smtplib`|发送邮件|
||`imaplib`|IMAP 邮件|
||`poplib`|POP3 邮件|
||`ftplib`|FTP 客户端|
|Web/解析|`html`|HTML 转义/解析|
||`xml`|XML 处理|
||`email`|邮件消息解析|
|数据库|`sqlite3`|SQLite 数据库|
|开发/测试|`argparse`|命令行参数解析|
||`logging`|日志|
||`unittest`|单元测试|
||`doctest`|文档测试|
||`pdb`|调试器|
||`timeit`|代码计时|
||`profile` / `cProfile`|性能分析|
|类型/面向对象|`typing`|类型注解|
||`dataclasses`|数据类|
||`enum`|枚举|
||`abc`|抽象基类|
||`contextlib`|上下文管理器工具|

查看你当前 Python 自带的全部标准库模块：
```python
import sys

# Python 3.10+ 可直接查看标准库模块名集合
print(sorted(sys.stdlib_module_names))

# 查看内置模块（C 实现、编译进解释器的模块）
print(sys.builtin_module_names)
```