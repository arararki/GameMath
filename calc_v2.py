def f21(x):
    if x[0] == 1972:
        if x[3] == 2015:
            if x[2] == 'rebol':
                return 0
            if x[2] == 'ampl':
                return 1
        if x[3] == 1992:
            if x[4] == 'r':
                if x[1] == 1984:
                    return 2
                if x[1] == 2017:
                    return 3
                if x[1] == 2004:
                    return 4
            if x[4] == 'ston':
                if x[2] == 'rebol':
                    return 5
                if x[2] == 'ampl':
                    return 6
            if x[4] == 'http':
                return 7
    if x[0] == 1969:
        if x[1] == 1984:
            return 8
        if x[1] == 2004:
            return 11
        if x[1] == 2017:
            if x[3] == 2015:
                return 9
            if x[3] == 1992:
                return 10
    if x[0] == 1985:
        return 12




def f22(x):
    temp_ = bin(x)
    temp = (str(temp_[2:]))
    if len(temp) == 29:
        temp = '000' + temp
    if len(temp) == 30:
        temp = '00' + temp
    if len(temp) == 31:
        temp = '0' + temp
    e_ = temp[0:1]
    d_ = temp[1:7]
    c_ = temp[7:11]
    b_ = temp[11:24]
    a_ = temp[24:32]
    new_temp = '0b' + d_ + b_ + a_ + c_ + e_
    new_x = int(new_temp,2)
    s = hex(new_x)
    s_ = int(s, 16)
    return s_

def trans(new_tabl,new_tabl_):
    for i in range(len(new_tabl[0])):
        row = []
        for item in new_tabl:
            row.append(item[i])
        new_tabl_.append(row)
    return new_tabl_

x = [1972, 2004, 'ampl', 1992, 'r']
f21(x)

x = 0x3799ec28
f22(x)