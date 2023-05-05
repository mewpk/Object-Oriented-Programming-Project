class PaymentCollection():
    def __init__(self):
        self.__payment_method = ["ATM","Debit","Wallet"]
    
    @property
    def payment_method(self):
        return self.__payment_method