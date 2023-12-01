def getchars(line):
    for char in line:
        if char.isdigit():
            forward_digit = char
            break
    for char in reversed(line):
        if char.isdigit():
            back_digit = char
            break
    result = int(forward_digit + back_digit)

    return result 





def Trebuchet():
    total = 0
    file = open("file.txt","r")
    for line in file:
        print("\n", line)
        total += getchars(line)
        print(getchars(line))
    print("THE TOTAL: ",  total)






Trebuchet()
