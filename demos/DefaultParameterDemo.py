def add_end(L=[]):
    L.append('End')
    return L

#定义默认参数要牢记一点：默认参数必须指向不变对象！ 
print(add_end())
print(add_end())
print(add_end())

#['End']
#['End', 'End']
#['End', 'End', 'End']

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2())
print(add_end2())
print(add_end2())