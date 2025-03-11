class Payment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата карткою {amount}{self.currency}")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплата PayPal {amount}{self.currency}")

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount}{self.currency}")

def create_payment():
    print("Оберіть тип платежу:")
    print("1 - CreditCardPayment")
    print("2 - PayPalPayment")
    print("3 - CryptoPayment")
    
    choice = input("Ваш вибір: ").strip()
    currency = input("Введіть валюту: ").strip()

    if choice == "1":
        return CreditCardPayment(currency)
    elif choice == "2":
        return PayPalPayment(currency)
    elif choice == "3":
        return CryptoPayment(currency)
    else:
        print("Невірний вибір! Спробуйте ще раз.")
        return create_payment()

payments = []

for _ in range(3):  
    payment = create_payment()
    payments.append(payment)

for i, payment in enumerate(payments, start=1):
    amount = float(input(f"Введіть суму для платежу #{i}: "))
    payment.pay(amount)
