
# 类，  70亿，抽象
class Person:

    def intoSeft(self):
        print("我是父类")


class Man(Person):
    sex = "男"

    def intoSeft(self):
        print("我是男的")

class Woman(Person):
    sex = "女"

    def intoSeft(self):
        print("我是女的")