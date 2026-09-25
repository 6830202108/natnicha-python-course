"""
2 types of programming
1) structured programming ==> การเขียนโปรแกรมแบบมีโครงสร้าง > c, js, python
2) object-oriented programming (OOP) ==> การเขียนโปรแกรมเชิงวัตถุ > java, c#, python
"""

# วิธีแก้ป้ญการปัญหา เป็ฯแค่แนวทาง template แม่แบบ เป็นเหมือนตรายาง
class ClassName:
    """Class docstring"""

    # ข้อมูลที่ต้องใช้ในการแก้ปัญหา ระบุไว้ใน constructor method
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value

    # การกระทำ ==> method
    def method_name(self): # ทุก constructor จะต้องมี self เป็น parameter ตัวแรก
        # Instance method
        return something

    def method_name2(self): # สมมติว่ามี method อีกตัว
        pass

# การสร้างวัตถุจากคลาส ==> เอาคลาสมาใช้สร้างวัตถุ (object) เพื่อแก้ปัญหา
myObj = ClassName(parameters)

# ใช้งานวัตถุจากคลาส
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method_name2() # เรียกใช้งาน method อีกตัว เป็นการเรียกใช้งาน method ของวัตถุ myObj

myObj2 = ClassName(parameters) # สร้างวัตถุอีกตัวจากคลาสเดียวกัน
print(myObj2.attribute)
print(myObj2.method_name())
myObj2.method_name2() # เรียกใช้งาน method อีกตัว เป็นการเรียกใช้งาน method ของวัตถุ myObj2

# อยากใช้อีกวัตถุจากคลาสเดียวกัน ก็สามารถสร้างได้เรื่อยๆ