




class Money:
    def __init__(self, amount, sym):
        self.amount = amount
        self.sym = sym


    def to_usd(self):
        if self.amount != 0:
            return Money(self.amount * 1, self.sym)
        else:
            return self

    def to_jpy(self):
        if self.amount != 0:
            return Money(self.amount * 110.084, self.sym)
        else:
            return self

    def to_eur(self):
        if self.amount != 0:
            return Money(self.amount * 0.854739, self.sym)
        else:
            return self

    def to_xbt(self):
        if self.amount != 0:
            return Money(self.amount * 0.000133278, self.sym)
        else:
            return self

    def to_symbol(self):
        if to_usd():
            self.sym = "USD"
        if to_jpy():
            self.sym = "JPY"
        if to_eur():
            self.sym = "EUR"
        if to_xbt():
            self.sym = "XBT"


x = Money(1, "JPY")
print(x.to_jpy().amount, x.to_jpy().sym)


y = Money(1, "EUR")
print(y.to_eur().amount, y.to_eur().sym)


z = Money(1, "XBT")
print(z.to_xbt().amount, z.to_xbt().sym)
