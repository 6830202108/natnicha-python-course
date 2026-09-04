# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร

# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not strong!

# Insert your password: Test@123
# Your password is strong

password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')

if len(words):
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left and right:
    print("Your password is strong!")
else:
    print("Your password is not strong!")