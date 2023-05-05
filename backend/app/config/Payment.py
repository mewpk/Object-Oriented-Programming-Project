class PaymentCollection():
    def __init__(self):
        self.__payment_method = ["ATM","Debit","Wallet"]
        self.__payment = []
    
    @property
    def payment_method(self):
        return self.__payment_method
    @property
    def payment(self):
        return self.__payment
    
    def add_payment_method(self,payment):
        self.payment.append(payment)

    def get_payment_method(self,type,name):
        for payment in  self.payment:
            if payment.type == type and payment.name == name:
                return payment