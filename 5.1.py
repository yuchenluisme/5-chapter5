#if else语句
name=input('what is your name')
if name.endswith('gumby'):
     print('hi')
else:print('bye')

#必须把需要用的变量定义为整型
grade=int(input("please type your grade："))
if grade > 60: print('you are qualified')
else :print('you still have to work hard')

#==检查是否相等； is检查是否相同。del删除这个值，括号里是删除的值。
x=[1,2,3]
y=[1,2]
x is not y
True
del x[2]
x
[1, 2]
x==y
True
x is y
False

#assert充当检察官。
assert 0<age<100