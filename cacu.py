def add(x,y,z):
    return x+y+z


def sub(x,y,z):
    return x-y-z


def multi(x,y,z):
    return x*y*z


def prompts():
    print("1. additon")
    print("2. subtraction")
    print("3. nultiplication")
prompts()    

pr = input("choose number: ")




num = float((input("input first digit: ")))
num1 = float((input ("input second digit: ")))
num2 = float((input("input third digit: ")))

if pr == "1":
    print("results: ", add(num, num1, num2))
elif pr == "2":
    print("results: ", sub(num, num1, num2))
elif pr == "3":
        print("results: ", multi(num, num1, num2)) 
