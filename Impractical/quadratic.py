import math


def quadr():
    while True:
        a = int(input("\nPlease Enter the value of a:"))
        b = int(input("\nPlease Enter the value of b:"))
        c = int(input("\nPlease Enter the value of c:"))

        x1 = (-b + math.sqrt(b**2 + 4*a*c)) / 2*a
        x2 = (-b - math.sqrt(b**2 + 4*a*c)) / 2*a

        answers = [x1, x2]

        print_answer = print("The answer is: " +
                             str(answers[0]) + " or " + str(answers[1]))

        try_again = input("\nAny more questions? (y/n)")
        if try_again == "n":
            break
    return print_answer


quadr()
