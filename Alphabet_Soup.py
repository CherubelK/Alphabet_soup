# Alphabet Soup Problem

def Alphabet_Soup(s):

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



print(Alphabet_Soup("ABCDEFGHIJKLMAAAAAAaaaaaaaaNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
