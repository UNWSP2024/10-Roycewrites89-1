#Royce Daniel 4/10/2026 "Two students"
class student:
    def check_pass_fail(self):
        if self.score >= 60:
            return True
        else:
         return False

    def __init__(self,name,score):
     self.name = name
     self.score = score

Student1 = student("Chuck", 99)
Student2 = student("Mico", 12)
print(Student1.name,Student1.score)
print(Student2.name,Student2.score)
didpass=Student1.check_pass_fail()
print(didpass)
did_pass=Student2.check_pass_fail()
print(did_pass)