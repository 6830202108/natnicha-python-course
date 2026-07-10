print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

radius = float(input("Radius: ")) # สำหรับบแบบรวบรัดในอัดเดียว ฟังก์ชันเดียวมีหน้าที่หลายตัว

# input
radius = input("Radius: ")
radius = float(radius)

# process
area = 3.14159 * float(radius) ** 2
circumference = 2 * 3.14159 * radius

# output
print("Area of this circle =", area)
print("Circumference of this circle =" + str(circumference))