#List: Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmetes=['master','dobi']
print(classmetes)

print("func: len()")
print(len(classmetes))

#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print("test: index of list")
print("test: classmetes[0]")
print(classmetes[0])
print("test: classmetes[-1]")
print(classmetes[-1])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
print("func: append()")
print("test: classmetes.append('Bear big')")
classmetes.append("Bear big")
print(classmetes)

print("func: insert()")
print("test: classmetes.insert(2,'Bear 2')")
classmetes.insert(2,"Bear 2")
print(classmetes)

#要删除list末尾的元素，用pop()方法：
print("func: pop()")
print("test: classmetes.pop()")
classmetes.pop()
print(classmetes)

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
print("test: classmetes.pop(1)")
classmetes.pop(1)
print(classmetes)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmetes[1]='Bear big'
print(classmetes)

#list里面的元素的数据类型也可以不同,也可以是另一个list
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
#要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

