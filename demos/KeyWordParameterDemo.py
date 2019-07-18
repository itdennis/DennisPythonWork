# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'others: ', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('dennis', 28, **extra)

# 下面是命名关键字参数, named keyword parameter实例
# 比如你想将关键字参数中只接受某些固定的参数 你的函数可以这样写
def person2(name,age,*,city,job):
    print(name, age, city, job)
# 这样写,将一个*作为分隔符,*之后的将作为关键字参数的名字, 我们看一下调用效果
person2('Jack', 24, city='Beijing', job='Engineer')