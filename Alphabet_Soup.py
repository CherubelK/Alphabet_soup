# Question 10

def ele_func(s):

    up = []
    lo = []
    for i in sorted(s):
        if i == i.upper():
            up.append(i)
        else:
            lo.append(i)
    upco = 0
    loco = 0
    out = []
    for null in range(len(up)+len(lo)):
        if upco == len(up):
            out.extend(lo[loco:])
            break
        elif loco == len(lo):
            out.extend(up[upco:])
            break
        else:
            if up[upco].lower() == lo[loco] or up[upco].lower() < lo[loco]:
                out.append(up[upco])
                upco += 1
            else:
                out.append(lo[loco])
                loco += 1

    return ''.join(out)




def alphabetSoup2(str):
    sorted_list_string = sorted(list(str)) # Convert the string to a list so you can sort it.
    sorted_list_string_lower = sorted(list(str.lower())) # Convert the string to a list so you can sort it.

    caps = []
    for char in sorted_list_string:
        if char.isupper():
            caps.append(char)

    newString = ''
    for letter in sorted_list_string_lower:
        if caps.count(letter.upper()) != 0:
            newString += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            newString += letter
    return newString

print(alphabetSoup2("ABCDEFGHIJKLMAAAAAAaaaaaaaaNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
