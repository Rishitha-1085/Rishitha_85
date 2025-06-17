'''
a.REPRESENT name,rno,3 subject marks of student -using class
b. The 3 subjects are maths,physics,chemistry
c. First verify whether the student is pass or fail
if passed in all 3 subjects then cal and print the :
1.total
2. average
3. admission is confirmed in engineering or not
condition for admission conformation in engineering:
out of 3 subjects in any 2 subjects the score should be >75 otherwise print a message as fail
'''


class Student:
    def __init__(self, name, rno, maths, physics, chemistry):
        self.name = name
        self.rno = rno
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def is_pass(self):
        # Check if passed in all 3 subjects (assuming pass mark is 35)
        return self.maths >= 35 and self.physics >= 35 and self.chemistry >= 35

    def total_and_average(self):
        total = self.maths + self.physics + self.chemistry
        average = total / 3
        return total, average

    def admission_confirmed(self):
        # Admission confirmed if marks in any 2 subjects > 75
        scores = [self.maths, self.physics, self.chemistry]
        count = sum(1 for score in scores if score > 75)
        return count >= 2

    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rno}")

        if self.is_pass():
            total, avg = self.total_and_average()
            print("Status: Passed in all subjects")
            print(f"Total Marks: {total}")
            print(f"Average Marks: {avg:.2f}")
            if self.admission_confirmed():
                print("Admission Confirmed in Engineering")
            else:
                print("Admission Not Confirmed: Less than two subjects have marks > 75")
        else:
            print("Status: Fail (Did not pass all subjects)")

# Example usage
student = Student("John Doe", 12, 80, 40, 35)
student.display_result()
