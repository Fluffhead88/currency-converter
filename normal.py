

class Money:
    def __init__(self, amount, sym):
        self.amount = amount
        self.sym = sym


    def to_usd(self):
        if self.sym == "USD":
            return Money(self.amount * 1, self.sym)
        if self.sym == "JPY":
            self.sym = "USD"
            return Money(self.amount * 0.00909426, self.sym)
        if self.sym == "EUR":
            self.sym = "USD"
            return Money(self.amount * 1.17024, self.sym)
        if self.sym == "XBT":
            self.sym = "USD"
            return Money(self.amount * 7569.11, self.sym)

    def to_jpy(self):
        if self.sym == "USD":
            self.sym = "JPY"
            return Money(self.amount * 1, self.sym)
        if self.sym == "JPY":
            return Money(self.amount * 109.958, self.sym)
        if self.sym == "EUR":
            self.sym = "JPY"
            return Money(self.amount * 128.699, self.sym)
        if self.sym == "XBT":
            self.sym = "JPY"
            return Money(self.amount * 836610.69, self.sym)

    def to_eur(self):
        if self.sym == "USD":
            self.sym = "EUR"
            return Money(self.amount * 0.854388, self.sym)
        if self.sym == "JPY":
            self.sym = "EUR"
            return Money(self.amount * 0.00777060, self.sym)
        if self.sym == "EUR":
            return Money(self.amount * 1, self.sym)
        if self.sym == "XBT":
            self.sym = "EUR"
            return Money(self.amount * 6500.82, self.sym)

    def to_xbt(self):
        if self.sym == "USD":
            self.sym = "XBT"
            return Money(self.amount * 0.000131307, self.sym)
        if self.sym == "JPY":
            self.sym = "XBT"
            return Money(self.amount * 0.00000119429, self.sym)
        if self.sym == "EUR":
            self.sym = "XBT"
            return Money(self.amount * 0.000153687, self.sym)
        if self.sym == "XBT":
            return Money(self.amount * 1, self.sym)




x = Money(1, "USD")
print(x.to_xbt().amount, x.to_xbt().sym)
