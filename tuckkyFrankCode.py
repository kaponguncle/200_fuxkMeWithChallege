class CSALShop:
    def __init__(self):
        # กำหนดราคาของสินค้าแต่ละชนิด
        self.prices = {'notebook': 34000, 'tablet': 19000, 'mobile': 26000}
        self.notebook_qty = 0
        self.tablet_qty = 0
        self.mobile_qty = 0
        self.is_member = False
        self.total_price = 0
        self.payment = 0

    def get_user_input(self):
        # รับข้อมูลจากผู้ใช้ว่าลูกค้าเป็นสมาชิกหรือไม่
        while True:
            member_input = input("คุณเป็นสมาชิกหรือไม่ (ใช่/ไม่): ").strip().lower()
            if member_input == "ใช่":
                self.is_member = True
                break
            elif member_input == "ไม่":
                self.is_member = False
                break
            else:
                print("ข้อมูลไม่ถูกต้อง กรุณาป้อน 'ใช่' หรือ 'ไม่'.")

        # รับข้อมูลจำนวนสินค้าที่ลูกค้าต้องการซื้อ
        self.notebook_qty = self.get_positive_integer("รับ Notebook กี่เครื่อง: ")
        self.tablet_qty = self.get_positive_integer("รับ Tablet กี่เครื่อง: ")
        self.mobile_qty = self.get_positive_integer("รับ Mobile กี่เครื่อง: ")

    def get_positive_integer(self, prompt):
        # ฟังก์ชันเพื่อรับจำนวนเต็มบวกจากผู้ใช้
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("กรุณาป้อนจำนวนเต็มบวก.")
            except ValueError:
                print("ข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลข.")

    def calculate_price(self):
        # คำนวณราคาสินค้าทั้งหมดก่อนหักส่วนลด
        original_price = (
            self.notebook_qty * self.prices['notebook'] +
            self.tablet_qty * self.prices['tablet'] +
            self.mobile_qty * self.prices['mobile']
        )

        self.total_price = original_price

        # หักส่วนลด 5% สำหรับสมาชิก
        if self.is_member:
            self.total_price *= 0.95

        # หักส่วนลด 10% ถ้ายอดรวมมากกว่า 50,000 บาท
        if self.total_price > 50000:
            self.total_price *= 0.90

        # คำนวณส่วนลดทั้งหมด
        self.discount_amount = original_price - self.total_price

    def process_payment(self):
        # รับเงินจากลูกค้าและตรวจสอบว่าจ่ายเงินพอหรือไม่
        while True:
            try:
                self.payment = float(input("กรุณากรอกจำนวนเงินที่จะชำระ: "))
                if self.payment >= self.total_price:
                    break
                else:
                    shortfall = self.total_price - self.payment
                    print(f"จำนวนเงินไม่เพียงพอ ขาดอีก {shortfall:.2f} บาท")
                    # ถ้าจ่ายไม่พอ ให้ลูกค้าจ่ายเพิ่ม
                    while self.payment < self.total_price:
                        try:
                            additional_payment = float(input(f"กรุณากรอกจำนวนเงินที่จะเพิ่มเพื่อชำระที่ขาดอีก {self.total_price - self.payment:.2f} บาท: "))
                            self.payment += additional_payment
                        except ValueError:
                            print("ข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลข.")
                    break
            except ValueError:
                print("ข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลข.")

    def print_receipt(self):
        # พิมพ์ใบเสร็จรับเงิน
        print("************************** ใบเสร็จ *************************************\n")
        if self.notebook_qty > 0:
            print(f"Notebook {self.notebook_qty} เครื่อง ราคา {self.notebook_qty * self.prices['notebook']:.2f} บาท")
        if self.tablet_qty > 0:
            print(f"Tablet {self.tablet_qty} เครื่อง ราคา {self.tablet_qty * self.prices['tablet']:.2f} บาท")
        if self.mobile_qty > 0:
            print(f"Mobile {self.mobile_qty} เครื่อง ราคา {self.mobile_qty * self.prices['mobile']:.2f} บาท")
        print(f"ราคารวมหลังหักส่วนลด: {self.total_price:.2f} บาท")
        print(f"ยอดส่วนลด: {self.discount_amount:.2f} บาท")  # แสดงยอดส่วนลดที่คำนวณได้
        print(f"จำนวนเงินที่ชำระ: {self.payment:.2f} บาท")
        print(f"เงินทอน: {self.payment - self.total_price:.2f} บาท")
        print("***************************************************************************\n")

    def run(self):
        self.get_user_input()
        self.calculate_price()
        print(f"ยอดรวมที่ต้องชำระ: {self.total_price:.2f} บาท")
        self.process_payment()
        self.print_receipt()

# สร้างวัตถุของคลาสและเรียกใช้โปรแกรม
CSALShop().run()