
def to_binary(num):
    num = int(num)
    binary = []
    if num == 0:
        return 0
    while num >= 1:
        binary.append(num%2)
        num = num // 2
    binary = [str(i) for i in binary]
    binary = ''.join(binary)
    return binary[::-1]


if __name__ == '__main__':
	num = input("Enter number to be switched to binary: ")
	print(to_binary(num))
