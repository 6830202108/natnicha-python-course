# Assignment-3 : Function + try-except
# Name : Natnicha Buddaduang
# Student ID : 6830202108

def deposit(money):
    balance = 1000

    try:
        money = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))

        if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

    except ValueError as e:
        print("เกิดข้อผิดพลาด:", e)

    else:
        balance = balance + money
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")

    finally:
        print("สิ้นสุดรายการฝากเงิน")


print("ยอดเงินเริ่มต้น: 1000 บาท")
deposit(0)
