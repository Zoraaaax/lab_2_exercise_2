def cube_elements(array):
    for number in array:
        print(number ** 3)


try:
    size = int(input("Enter the size of the array: "))
    elements = list(map(int, input("Enter the elements separated by space: ").split()))

    if len(elements) != size:
        print(f"Please enter exactly {size} elements.")
    else:
        cube_elements(elements)

except ValueError:
    print("Please enter valid numbers")
