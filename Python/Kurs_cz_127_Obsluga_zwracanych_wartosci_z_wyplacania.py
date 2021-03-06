class Result:
    def __init__(self, isSuccess, message, value = None):
        self.isSuccess = isSuccess 
        self.message = message
        self.value = value

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            print("[try_withdraw] Wypłacono", amount)
            return True, "[True] Wypłacono", amount
        print("[try_withdraw] Za mało pieniędzy")
        return False, "[False] Za mało pieniędzy", amount
    def __str__(self):
        return str(self.balance) # Rzutowanie na typ string
    def try_withdraw_with_tuple(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            print("[try_withdraw] Wypłacono", amount)
            return (True, "[True] Wypłacono", amount)
        print("[try_withdraw] Za mało pieniędzy")
        return (False, "[False] Za mało pieniędzy", amount)
    def try_withdraw_with_dict(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            print("[try_withdraw] Wypłacono", amount)
            return {"isSuccess": True, "message": "[True] Wypłacono", "value": amount}
        print("[try_withdraw] Za mało pieniędzy")
        return {"isSuccess": False, "message": "[False] Za mało pieniędzy", "value": amount}
    def try_withdraw_with_result_class(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            print("[try_withdraw] Wypłacono", amount)
            return Result(True,"[True] Wypłacono",amount)
        print("[try_withdraw] Za mało pieniędzy")
        return Result(False,"[False] Za mało pieniędzy",amount)