class Payment:
    def __init__(self, payment_id, amount, date):
        self.Payment_ID = payment_id
        self.Amount = amount
        self.Date = date

    def Process_Payment(self):
        print(f"Payment processed for Payment ID: {self.Payment_ID}")

    def Generate_Receipt(self):
        print(f"Receipt generated for Payment ID: {self.Payment_ID}")

    def Cancel_Payment(self):        
        print(f"Payment canceled for Payment ID: {self.Payment_ID}")

# cara penggunaannya
# Membuat objek Payment
payment = Payment("S1", 100, "2024-04-20")

# Memanggil metode Process_Payment
payment.Process_Payment()

# Memanggil metode Generate_Receipt
payment.Generate_Receipt()

# Memanggil metode Cancel_Payment
payment.Cancel_Payment()

