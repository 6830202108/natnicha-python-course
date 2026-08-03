# Assignment 2.1 : exam-score.py
# โปรแกรมตรวจสอบผลการสอบของนักเรียน

scores = []  # สร้าง list สำหรับเก็บคะแนนนักเรียนทั้ง 5 คน

# รับคะแนนของนักเรียนทั้ง 5 คน
for i in range(5):
    score = int(input(f"Enter score of student {i+1}: "))
    scores.append(score)

print()

# ตรวจสอบผลสอบของนักเรียนแต่ละคน
for i in range(5):
    if scores[i] >= 50:
        print(f"Student {i+1}: {scores[i]} -> ผ่าน")
    else:
        print(f"Student {i+1}: {scores[i]} -> ไม่ผ่าน")