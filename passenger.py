class PassengerAccount:
    def __init__(self, name):
        self.name = name
        self.__wallet_balance = 0.0

    def top_up_wallet(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        self.__wallet_balance += amount
        print(f"New balance: P{self.__wallet_balance:.2f}")

    def pay_for_ride(self, fare_amount):
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")

        self.__wallet_balance -= fare_amount
        print(f"Payment successful! Remaining balance: P{self.__wallet_balance:.2f}")
