def rot13(message):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    alpha2 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    message = list(message)
    new_message = []
    for c in message:
        if c in alpha:
            old = alpha.index(c)
            new = old - 13
            if new < 0:
                new = 26 + new
            new_message.append(alpha[new])
        elif c in alpha2:
            old = alpha2.index(c)
            new = old - 13
            if new < 0:
                new = new + 26
            new_message.append(alpha2[new])
        else:
            new_message.append(c)
    return ''.join(new_message)
    
    
if __name__ == '__main__':
    print(rot13("EBG13 rknzcyr"))
