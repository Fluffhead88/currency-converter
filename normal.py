

class Money:
    def __init__(self, amount, sym):
        self.amount = amount
        self.sym = sym


    def to_usd(self):
        if self.amount != 0:
            return Money(self.amount * 1, "USD")
        else:
            return self

    def to_jpy(self):
        if self.amount != 0:
            return Money(self.amount * 110.272, "JPY")
        else:
            return self


x = Money(2, "JPY")
print(x.to_jpy().amount)
print(x.to_jpy().sym
