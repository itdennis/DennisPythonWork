#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
name=['xiongda', 'xionger','dobi']
for x in name:
    print(x)

#range() function
#list() function
#比如range(5)生成的序列是从0开始小于5的整数,再通过list()函数可以转换为list。
list(range(5))

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
#比如我们要计算100以内所有奇数之和，可以用while循环实现
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print('sum is {0}', sum)

