class People():
    def eat(self,ids):
        print("{}吃饭".format(ids))
# class Students(People):
#     def study(self):
#         print("学习")
#
# s = Students()
# s.eat("学生")
# s.study()
#
# print('===========')
class Students(People):
    def __init__(self):
        super().__init__()
    def study(self,ids):
        print("学习")
        super().eat(ids)
    def eat(self,ids):
        if ids == "学生":
            print("当前吃饭的角色是学生")
        else:
            print("当前学生并没有吃饭")
s = Students()
s.study("学生")