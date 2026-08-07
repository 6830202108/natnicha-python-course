def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area."""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area: {length} x {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_triangle_area(height, base):
    """Calculates and displays triangle area."""
    area = 0.5 * height * base
    print(f"Triangle with height {height} and width {base}")
    print(f"Area: {height} x {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)