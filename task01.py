def qosh(a ,b):
    natija = a + b
    return natija
def ayirish (a ,b):
    natija = a - b
    return natija
def kopayt (a, b):
    natija = a * b
    return natija
def bol(a, b):
    natija = a / b
    return natija
def kamanda():
    a = int(input("son kiriting: "))
    b = int(input("2 chi sonni kirting: "))
    amal = input("Qaysi belgidan foydalanasiz (+ , - , * , / ): ")
    if amal == "+":
        print(qosh(a, b))
        
    elif amal == "-":
        print(ayirish(a, b))
        
    elif amal == "*":
        print(kopayt(a, b))
    
    elif amal == "/":
        print(bol(a, b))
kamanda()