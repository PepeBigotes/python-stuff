def print_pascals_triangle(x: int):

    # Part 1: 2D list of int lists
    ints_triangle = [[1],]
    while len(ints_triangle) < x:
        newrow = []
        last_row = ints_triangle[-1]
        idx1 = -1 ; idx2 = 0
        for i in last_row + [0,]:  # Just to avoid using range(len())
            if idx1 == -1: num1 = 0
            else: num1 = last_row[idx1]
            try: num2 = last_row[idx2]
            except IndexError: num2 = 0
            newrow.append(int(num1 + num2))
            idx1 += 1 ; idx2 += 1
        ints_triangle.append(newrow)

    # Part 2: list of centered strings
    str_triangle = []
    for row in ints_triangle:
        string = ""
        for i in row: string += str(i) + ' '
        str_triangle.append(string)
    bottom_lenght = len(str_triangle[-1])
    for enum in enumerate(str_triangle): str_triangle[enum[0]] = enum[1].center(bottom_lenght)

    # Part 3: actual print
    for row in str_triangle: print(row)


print_pascals_triangle(15)