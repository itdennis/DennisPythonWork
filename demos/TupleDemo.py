#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
classmates = ('bear big', 'bear 2', 'master')
print(classmates)

#要定义一个只有1个元素的tuple时必须加一个逗号',', 来消除歧义
t=(1,)
print(t)