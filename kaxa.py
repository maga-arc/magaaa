def main(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b ==0:
                return "Делить на 0 нельзя"
            return a / b

        case _:
            return "Неизвестная операция"


print(main(3, 2, "*"))