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







