# Simple if statement
age = int(input("Enter your age: "))
if age >= 18: # ใส่อะไรก็ได้หลัง if ที่เป็น จริง กับ เท็จ
    print("You are an adult") # ใช้เว้นวรรค 4 space หรือ tab 1 ครั้ง

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else statement
score = 85
if score >= 90: # ใช้โคลอน (:) หลัง if, elif, else เสมอ
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
