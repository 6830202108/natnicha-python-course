print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

# input
second = int(input("Input seconds: "))

# process
hours = second // 3600
second_remain = second % 3600

minutes = second_remain // 60
second_remain = minutes % 60

# output
print(f"{second} seconds = {hours} hour, {minutes} minute, {second_remain} second")