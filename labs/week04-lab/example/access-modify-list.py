# access คือการเข้าถึงข้อมูลใน list โดยใช้ index ของ list
# modify คือการแก้ไขข้อมูลใน list โดยใช้ index ของ list

fruits = ["apple", "banana", "orange", "grape", "kiwi"] # index ของ list เริ่มจาก 0 ถึง 4
# ถ้าติดลบ จะนับจากด้านหลังของ list เช่น -1 คือ index ของ kiwi, -2 คือ index ของ grape

# Positive indexing (0-based)
print(f"First fruit: {fruits[0]}")      # apple
print(f"Second fruit: {fruits[1]}")     # banana
print(f"Last fruit: {fruits[4]}")       # kiwi

# Negative indexing
print(f"Last fruit: {fruits[-1]}")      # kiwi
print(f"Second last: {fruits[-2]}")     # grape

# List slicing
print(f"First 3 fruits: {fruits[0:3]}")     # ['apple', 'banana', 'orange']
# เฉือนเบอร์ 0 ถึง 2 (ไม่รวม index 3) จะได้ ['apple', 'banana', 'orange']
print(f"From index 2: {fruits[2:]}")        # ['orange', 'grape', 'kiwi']
# เฉือนจาก index 2 ถึง index สุดท้าย จะได้ ['orange', 'grape', 'kiwi']
print(f"Last 2 fruits: {fruits[-2:]}")      # ['grape', 'kiwi']
# เฉือนจาก index -2 ถึง index สุดท้าย จะได้ ['grape', 'kiwi']
print(f"Every 2nd fruit: {fruits[::2]}")    # ['apple', 'orange', 'kiwi']
# เฉือนตั้งแต่ตัวแรกและโดดทุกๆ 2 index จะได้ ['apple', 'orange', 'kiwi']
print(f"Reverse list: {fruits[::-1]}")      # ['kiwi', 'grape', 'orange', 'banana', 'apple']
# เฉือนตั้งแต่ตัวแรกและโดดทุกๆ 1 index แต่กลับด้าน จะได้ ['kiwi', 'grape', 'orange', 'banana', 'apple']

# Changing single elements
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'orange']

# Changing multiple elements
fruits[0:2] = ["pear", "cherry"]
# เฉือน index 0 ถึง 1 (ไม่รวม index 2) แล้วแทนที่ด้วย ["pear", "cherry"]
print(fruits)  # ['pear', 'cherry', 'orange']

# Adding elements
fruits.append("grape")           # Add to end
print(fruits)  # ['pear', 'cherry', 'orange', 'grape']
# append() คือการเพิ่ม element เข้าไปที่ท้าย

fruits.insert(1, "banana")       # Insert at specific position
print(fruits)  # ['pear', 'banana', 'cherry', 'orange', 'grape']
# insert() คือการเพิ่ม element เข้าไปที่ตำแหน่งที่กำหนด โดย index 1 คือ banana จะอยู่ระหว่าง pear และ cherry

fruits.extend(["kiwi", "apple"]) # Add multiple elements
print(fruits)  # ['pear', 'banana', 'cherry', 'orange', 'grape', 'kiwi', 'apple']
# extend() คือการเพิ่มหลายๆ element เข้าไปที่ท้าย list โดย ["kiwi", "apple"] จะถูกเพิ่มเข้าไปที่ท้าย list fruits

# Removing elements
fruits.remove("banana")          # Remove first occurrence
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi', 'apple']
# remove() คือการลบ element ตัวแรกที่เจอจาก list โดย "banana" จะถูกลบออกจาก list fruits

removed_fruit = fruits.pop()     # Remove and return last element
print(f"Removed: {removed_fruit}")  # apple
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi']
# pop() คือการลบ element ตัวสุดท้ายออกจาก list และ return

removed_fruit = fruits.pop(1)    # Remove and return element at index 1
print(f"Removed: {removed_fruit}")  # cherry
print(fruits)  # ['pear', 'orange', 'grape', 'kiwi']
# pop(index) คือการลบ element ที่มี index ตรงกับที่ระบุ และ return ค่า element นั้น

del fruits[0]                    # Delete element at index 0
print(fruits)  # ['orange', 'grape', 'kiwi']

fruits.clear()                   # Remove all elements
print(fruits)  # []