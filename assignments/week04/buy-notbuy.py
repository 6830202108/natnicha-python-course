# Assignment 2.2 : buy-notbuy.py
# โปรแกรมช่วยตัดสินใจเลือกซื้อสินค้าภายใต้งบประมาณรวม

# สร้าง list สำหรับเก็บราคาสินค้า
prices = []

# รับราคาสินค้า 6 รายการ
print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)

# รับงบประมาณรวม
budget = int(input("\nEnter total budget: "))

# ตัวแปรเก็บยอดใช้จ่าย และรายการสินค้าที่ซื้อได้
total = 0
buy_list = []

print()

# ตรวจสอบสินค้าทีละรายการ
for i in range(6):

    # ถ้าซื้อแล้วไม่เกินงบประมาณ
    if total + prices[i] <= budget:
        print(f"Item {i+1} = {prices[i]} -> buy")

        total += prices[i]          # เพิ่มยอดใช้จ่าย
        buy_list.append(prices[i])  # เก็บรายการที่ซื้อได้

    else:
        print(f"Item {i+1} = {prices[i]} -> cannot buy")

    print(f"Current total = {total}\n")

# แสดงผลลัพธ์
print(f"Bought items: {buy_list}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget-total}")