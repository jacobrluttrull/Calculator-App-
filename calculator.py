import math 

menu = print('Welcome to the Area Calculator!')
print('1. Square')
print('2. Rectangle')
print('3. Triangle')
print('4. Circle')
print('5. Quit')

choice = int(input('Please select an option (1-5): '))

while choice != 5:
    if choice == 1:
        side = float(input('Enter the length of the side of the square: '))
        area = side ** 2
        print(f'The area of the square is: {area}')
    elif choice == 2:
        length = float(input('Enter the length of the rectangle: '))
        width = float(input('Enter the width of the rectangle: '))
        area = length * width
        print(f'The area of the rectangle is: {area}')
    elif choice == 3:
        base = float(input('Enter the base of the triangle: '))
        height = float(input('Enter the height of the triangle: '))
        area = 0.5 * base * height
        print(f'The area of the triangle is: {area}')
    elif choice == 4:
        radius = float(input('Enter the radius of the circle: '))
        area = math.pi * radius ** 2
        print(f'The area of the circle is: {area}')
    else:
        print('Invalid choice, please try again.')

    print('\n1. Square')
    print('2. Rectangle')
    print('3. Triangle')
    print('4. Circle')
    print('5. Quit')
    
    choice = int(input('Please select an option (1-5): '))


