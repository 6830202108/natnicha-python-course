# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a, e, i, o, u)

# แสดงตัวอย่างหน้าจอ
# what is your name? Natnicha
# your text have 3 vowels.

# test
name = input("What is your name? ")
letters = list(name)
print(letters)

a = letters.count("a")
e = letters.count("e")
i = letters.count("i")
o = letters.count("o")
u = letters.count("u")

A = letters.count("A")
E = letters.count("E")
I = letters.count("I")
O = letters.count("O")
U = letters.count("U")

count = a + e + i + o + u + A + E + I + O + U
print("Your text have", count, "vowels.")

# สมมติว่าถ้าชื่อ mamuamg จะได้ count = 3 เพราะมี a, u, a เป็นสระทั้งหมด 3 ตัว

"""
name = input("What is your name? ")
count = 0
for letter in name:
    if letter == "a" or letter == "A":
       count + 1
    elif letter == "e" or letter == "E":
       count + 1
    elif letter == "i" or letter == "I":
       count + 1
    elif letter == "o" or letter == "O":
       count + 1
    elif letter == "u" or letter == "U":
       count + 1
"""

"""
name = input("What is your name? ")
count = 0
for letter in name:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
           count + 1
"""

    

# print(f"ตัวอักษร: {letters}")
# print("Your text have", count, "vowels.")