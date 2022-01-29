import PersonTest


# # 类的实例，类的对象，具体的东西
# lgh = PersonTest.Person('林国辉',8)
# lgh.intoSeft()

# 定义的时候，是父类，执行的时候是子类

def Inro(Person):
    Person.intoSeft()


man = PersonTest.Man()
woman = PersonTest.Woman()
Inro(woman)