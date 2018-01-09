[TOC]


# 1 python虚拟环境
## 1.1 创建
python3可用如下命令：
~~~python
python -m venv ll_env
~~~
## 1.2 激活与停止
### 1.2.1 激活
~~~bash
# Linux
source ll_env/bin/activate
# Windows
ll_env\Scripts\activate
~~~
激活后，命令行提示符变成了：
> **(ll_env)** E:\MyCodes\python\pcc\learning_log>

### 1.2.2 停止
* 方法1：
执行命令：`deactivate`
* 方法2： 关闭运行虚拟环境的终端





# 其他
## 查看Django版本号：
~~~python
python -m django --version
~~~
>E:\MyCodes\python\pcc\MyProj>python -m django --version
1.11.6

## 从给定的数据里面获取随机数
示例:
~~~python
import random
random.choice([1,2,3,4])
~~~
**拓展**：列表里面也可以是字符串:`random.choice(['tom', 'jerry', 'jack', 'maria'])`
## 字符串的格式化
* 方法1：
~~~python
print("%s and %s are good friends." %('Tom.upper', 'Jerry'))
~~~
>>> Tom.upper and Jerry are good friends.

* 方法2
~~~py
print("{0} and {1} are in the same class.".format('Michale', 'Jane'))
print("The first letter is {0} and {4} is the 5th letter.".format('a', 'b', 'c', 'd', 'e') )
~~~

>>> Michale and Jane are in the same class.
The first letter is a and e is the 5th letter.

**小结**：方法2中的{0}，{1}，……，对应的是后面`.format()`内的字符串的序列。




# 经验之谈
注释行长不要超过78个字符。






~~~
                        _ooOoo_
                       o8888888o
                       88" . "88
                       (| -_- |)
                        O\ = /O
                    ____/`---'\____
                  .   ' \\| |// `.
                   / \\||| : |||// \
                 / _||||| -:- |||||- \
                   | | \\\ - /// | |
                 | \_| ''\---/'' | |
                  \ .-\__ `-` ___/-. /
               ___`. .' /--.--\ `. . __
            ."" '< `.___\_<|>_/___.' >'"".
           | | : `- \`.;`\ _ /`;.`/ - ` : | |
             \ \ `-. \_ __\ /__ _/ .-` / /
     ======`-.____`-.___\_____/___.-`____.-'======
                        `=---='

     .............................................
              佛祖镇楼                  BUG辟易
      佛曰:
              写字楼里写字间，写字间里程序员；
              程序人员写程序，又拿程序换酒钱。
              酒醒只在网上坐，酒醉还来网下眠；
              酒醉酒醒日复日，网上网下年复年。
              但愿老死电脑间，不愿鞠躬老板前；
              奔驰宝马贵者趣，公交自行程序员。
              别人笑我忒疯癫，我笑自己命太贱；
              不见满街漂亮妹，哪个归得程序员？
~~~
