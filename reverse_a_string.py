#input() gives you int type return,and raw_input gives you string return

#这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）且均将输入当成字符串。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 
s=raw_input("enter a string:")
print("input s is:",s)
a=s[len(s)-1]   #the last letter in the string
for i in range(len(s)-1,0,-1):
	a=a+s[i-1]
s=a
print("reversed s is:",s)
'''
s=raw_input("input:")
input:123

In [42]: s
Out[42]: '123'

s=input("input:")
input:123

In [40]: s
Out[40]: 123

s=input("input:")
input:'123'

In [38]: s
Out[38]: '123'
'''
