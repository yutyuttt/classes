def date_of_birth(ssn):
    d = ssn[0:2]
    y = ssn[4:6]

    m = ssn[2:4]
    if m[0] == "0":
        m = m[1]

    if ssn[6] == "A":
        c = "20"
    else:
        c = "19"

    return (c + y, m, d)

print(date_of_birth("140598+abcd"))