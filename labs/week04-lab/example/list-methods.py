# Sample data
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
fruits = ["apple", "banana", "apple", "orange"]

# Length and counting
print(f"Length: {len(numbers)}")           # 9 บอกตำแหน่งของจำนวนใน list
print(f"Count of 1: {numbers.count(1)}")   # 2
print(f"Count of apple: {fruits.count('apple')}")  # 2

# Finding elements
print(f"Index of 4: {numbers.index(4)}")   # 2
print(f"Index of banana: {fruits.index('banana')}")  # 1

# ถึงจะผสมกันแต่ก็แยกได้ ตัวเลขมาก่อนตัวอักษร ประโยชน์ของการ sort คือการจัดลำดับให้เรียงกัน
# number_copy คือเหมือนทำสำเนาของ list numbers
# Sorting
numbers_copy = numbers.copy()
numbers_copy.sort()                         # Sort in place
print(f"Sorted: {numbers_copy}")           # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numbers_copy.sort(reverse=True)             # Sort descending
print(f"Reverse sorted: {numbers_copy}")   # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# ตัวแปร sorted ต้องมีตัวแปรมารองรับ เพราะ sorted() จะ return ค่าเป็น list ใหม่ ไม่ได้เปลี่ยน list เดิม
# sorted() function - returns new list
sorted_numbers = sorted(numbers)
print(f"Original: {numbers}")              # [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"New sorted: {sorted_numbers}")     # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Reversing
fruits.reverse()
print(f"Reversed fruits: {fruits}")        # ['orange', 'apple', 'banana', 'apple']

# Min, max, sum (for numeric lists)
print(f"Min: {min(numbers)}")              # 1
print(f"Max: {max(numbers)}")              # 9
print(f"Sum: {sum(numbers)}")              # 36

# min คือหาค่าต่ำสุด max คือหาค่าสูงสุด sum คือหาผลรวมของ list

# แล้วค่าเฉลี่ยล่ะ numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# average = sum(numbers) / len(numbers)