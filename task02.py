def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"Yangi balans: {balance:,.2f} so'm")
    else:
        print("Iltimos, musbat miqdor kiriting.")
    return balance   
def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(f" Yangi balans: {balance:,.2f} so'm")
    else:
        print("Iltimos, to'g'ri miqdor kiriting.")
    return balance
def check_balance(balance):
    print(f"Joriy balans: {balance:,.2f} so'm")
    return balance
def main():
    balance = 100000  
    while True:
        print("\n=== Bank Dasturi ===")
        print("1. Pul qo'yish ")
        print("2. Pul yechish ")
        print("3. Balansni ko'rish")
        print("4. Chiqish ")
        amal = input("Qaysi amalni bajarishni xohlaysiz? (1/2/3/4): ").strip()
        if amal == "1":
            try:
                miqdor = float(input(" Qo'yiladigan miqdorni kiriting: "))
                balance = deposit(balance, miqdor)
            except ValueError:
                print(" Iltimos, raqam kiriting.")
        elif amal == "2":
            try:
                miqdor = float(input(" Yechiladigan miqdorni kiriting: "))
                balance = withdraw(balance, miqdor)
            except ValueError:
                print(" Iltimos, raqam kiriting.")
        elif amal == "3":
            check_balance(balance)
        elif amal == "4":
            print(" Dasturdan chiqildi. Xayr!")
            break
        else:
            print(" Noto'g'ri amal tanlandi. Qaytadan urinib ko'ring.")
main()
