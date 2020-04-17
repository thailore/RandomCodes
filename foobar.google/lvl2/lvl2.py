def solution(n, b):
    seenNumbers = []
    while True:
        x = int("".join(sorted(str(n), reverse=True)))
        y = int("".join(sorted(str(n))))
        z = getDiff(x, y, b)

        lenX = len(str(x))
        lenZ = len(str(z))
        if lenZ != lenX:
            z = int(z) * (10 ** (lenX - lenZ))
        
        for index, item in enumerate(seenNumbers):
          if item == z:
            return index + 1
        seenNumbers = [z] + seenNumbers
        n = z


def getDiff(x, y, base):
    if base == 10:
        return x - y
    x = convertToDecimal(x, base)
    y = convertToDecimal(y, base)
    return convertToBase(x - y, base)


def convertToBase(decimalNumber, base):
    digits = []
    while decimalNumber > 0:
        digits.insert(0, str(decimalNumber % base))
        decimalNumber = decimalNumber // base
    return "".join(digits)


def convertToDecimal(number, base):
    num = 0
    for digit in str(number):
        num = base * num + int(digit)
    return num

