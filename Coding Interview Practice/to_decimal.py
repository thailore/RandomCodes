def to_decimal(num):
    binary = list(num)
    binary = binary[::-1]
    for index, val in enumerate(binary):
        if int(val) != 1 and int(val) != 0:
            return "Not a binary"
    decimal = 0
    if num == 0:
        return 0
    for index, val in enumerate(binary):
        if int(val) == 1:
            decimal += 2**(index)
    return decimal


if __name__ == '__main__':
	num = input("Enter number to be switched to decimal: ")
	print(to_decimal(num))
