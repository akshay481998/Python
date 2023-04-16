class bank:

    def transactions(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you your account opening status")
    def deposite(self):
        print("This will show you your deposited amount")
    def test(self):
        print("This is the method from bank class")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("This will show you the transactions happened to icici through hdfc")
    def test(self):
        print("This is a method from hdfc bank")


class icici(bank,HDFC_bank):
    pass   # multiple inheritance

i = icici()
i.account_opening()
i.deposite()
i.transactions()
i.hdfc_to_icici()
i.test()