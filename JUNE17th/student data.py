
class Student:
    def __init__(self, name, rno, maths, physics, chemistry):
        self.name = name
        self.rno = rno
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
    def calculation(self):
        if(self.maths>=40 and self.physics>=40 and self.chemistry>=40):
            total=self.maths+self.physics+self.chemistry
            average=total/3
            print(total)
            print(average)
            if(self.maths>=75 and self.physics>=75) or (self.physics>=75 and self.chemistry>=75) or (self.maths>=75 and self.chemistry>=75):
                print("admission is confirmed")
            else:
                print("admission not confirmed")
        else:
            print("FAIL")
s1=Student("kiran",501,74,85,85)
s1.calculation()
