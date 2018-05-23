




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

    def to_eur(self):
        if self.amount != 0:
            return Money(self.amount * 0.856046, "EUR")
        else:
            return self

    def to_btc(self):
        if self.amount != 0:
            return Money(self.amount * 0.000132802, "BTC")
        else:
            return self

t = Money(100.00, "USD") + Money(56.32, "EUR")
print(t.to_usd().amount)
print(t.to_usd().sym)

"""x = Money(2, "JPY")
print(x.to_jpy().amount)
print(x.to_jpy().sym)

y = Money(2, "EUR")
print(y.to_eur().amount)
print(y.to_eur().sym)

z = Money(2, "BTC")
print(z.to_btc().amount)
print(z.to_btc().sym)"""
