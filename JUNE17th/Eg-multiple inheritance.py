#MULTIPLE INHERITANCE

class dance:
    def dancing(self):
        print("I can Dance")
class fly:
    def flying(self):
        print("I can Fly also")
class peacock(dance,fly):
    def sound(self):
        print('I had a good sound too')

p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
