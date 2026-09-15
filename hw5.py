while (expr := input("Enter an expression: ")) != "":
    (a, op, b) = expr.split()
    a, b = float(a), float(b)

    match op:
        case "+":
            res = a + b
        case "-":
            res = a - b
        case "*":
            res = a * b
        case "/": # because why not
            if b == 0.0:
                res = "undefined"
            else:
                res = a / b
        case _:
            res = "invalid"

    print(res)
