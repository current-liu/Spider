# coding=utf-8

# 查看python的默认工作目录
print(os.getcwd())
# 修改工作目录
os.chdir('D:\LiuChao\PycharmProjects')
print(os.getcwd())
if True:
    print "true"

# 等待用户输入
raw_input("\n\nPress the enter key to exit")

# 不换行输出
print "a"
print "b"
print "c",
print "d"

a = 0
if a > 0:
    print "a>0"
elif a < 0:
    print "a<0"
else:
    print "a=0"
