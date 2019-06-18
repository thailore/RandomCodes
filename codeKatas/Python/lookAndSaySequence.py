def lookAndSaySequenceNextElement(element):
    total = []
    look = list(element)
    i = 0
    while i<len(look):
        search = []
        j = 0
        while look[i] == look[i+j]:
            search.append(look[i+j])
            j+=1
            if i+j == len(look):
                break
        total.append(str(search.count(look[i])))
        total.append(str(look[i]))
        i+=j
    answer = "".join(total)
    return answer
            

"""
Look and say sequence generated as follows.

the second term is 11, generated by reading the first term as "One 1" (There is one 1 in previous term);
the third term is 21, generated by reading the second term as "Two 1";
the fourth term is 1211, generated by reading the third term as "One 2 One 1";

For element = "1", the output should be
lookAndSaySequenceNextElement(element) = "11"; meaning "there is one 1"
For element = "1211", the output should be
lookAndSaySequenceNextElement(element) = "111221" meaning "there is one 1, one 2, and 2 ones"
"""