# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def forget_acc_pass(self):
#         print("your account password is:", self.__acc_pass)

# acc1 = Account(123456, 'john@123')
# print(acc1.acc_no)
# print(acc1.forget_acc_pass())





# class student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

# s1 = student("john", 20, 85)
# print(s1.name, s1.age, s1.marks)
# del s1.marks
# print(s1.name, s1.age, s1.marks)


# Single inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car started ...")
#     @staticmethod
#     def stop():
#         print("car stopped ...")

# class toyota(car):
#     def __init__(self, name):
#         self.name = name

# t1 = toyota("innova")
# print(t1.start())



#  multiple-level inheritance


# class car:
#     @staticmethod
#     def start():
#         print("started ...")
#     @staticmethod
#     def stop():
#         print("stopped ...")

# class toyota(car):
#     def __init__(self, name):
#         self.name = name

# class bike(toyota):
#     def __init__(self, name):
#         self.name = name

# b1 = bike("kawasaki ninja zx-10r")
# print(b1.name)
# b1.start()
# b1.stop()





# multi inheritance


class A:
    var1 =   "welcome var1"

class B:
    var2 = "walcome var2"

class C(A, B):
    var3 = "welcome var3"

c1 = C()
print(c1.var1)
print(c1.var2)
print(c1.var3)