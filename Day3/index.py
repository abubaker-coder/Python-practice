# Class method

# class Person:
#     name = "abubaker"

#     @classmethod
#     def change_name(cls, name):
#         cls.name = name

# p1 = Person()
# print(p1.name)  
# p1.change_name("john")
# print(p1.name)  


# property method

# class Marks:
#     def __init__(self, phy, math, chem):
#         self.phy = phy
#         self.math = math
#         self.chem = chem
    
#     @property
#     def total(self):
#         return str((self.phy + self.math + self.chem)/3) + "%"
    
# s1 = Marks(90, 92, 80)
# print(s1.total)

# s1.phy = 80
# print(s1.total)




#  polimorphism

class cal:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return cal(newreal, newimg)

num1 = cal(1, 9)
num1.show()

num2 = cal(2, 3)
num2.show()

num3 = num1 + num2
num3.show()
        