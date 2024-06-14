notebook = 34000
tablet = 19000
smartphone = 26000
discountCustomer = 0.05
discountOver50k = 0.1

customerStatus = str(input("คุณได้เป็นสมาชิกหรือไม่ (Y/N): "))

print(f"""
******************** รายการสินค้า ********************
1. Notebook     {notebook} บาท
2. Tablet       {tablet} บาท
3. Smartphone   {smartphone} บาท
****************************************************
""")

amountNotebook = int(input("จำนวนโน๊ตบุ๊คที่ต้องการซื้อ: "))
amountTablet = int(input("จำนวนแท็บเล็ตที่ต้องการซื้อ: "))
amountSmartphone = int(input("จำนวนสมาร์ทโฟนที่ต้องการซื้อ: "))

priceAllNotebook = notebook * amountNotebook
priceAllTablet = tablet * amountTablet
priceAllSmartphone = smartphone * amountSmartphone

priceAll = priceAllNotebook + priceAllTablet + priceAllSmartphone

if customerStatus == "Y" or customerStatus == "Yes" or customerStatus == "y" or customerStatus == "yes":
    withDiscountForCustomer = priceAll - (priceAll*discountCustomer)
    if withDiscountForCustomer > 50000:
        priceWithDiscount10per = withDiscountForCustomer - (withDiscountForCustomer*discountOver50k)
        print(f"รายการที่ต้องชำระ: {priceWithDiscount10per} บาท")
        while True:
            paymentInput = float(input("กรอกจำนวนเงินที่ต้องชำระ: "))
            if priceWithDiscount10per > paymentInput or paymentInput == '' or paymentInput == 0 or paymentInput == 0.0:
                print("[ Error ] จำนวนเงินของคุณไม่เพียงพอ")
            else:
                print("[ OK ] ขอบคุณสำหรับการชำระเงิน")
                print(f"[ INFO ] จำนวนเงินทอน {paymentInput-priceWithDiscount10per} บาท")
                print(f"""
******************** ใบเสร็จ ********************
1. Notebook     ต่อเครื่อง    {notebook} บาท x {amountNotebook}    : {priceAllNotebook}            บาท
2. Tablet       ต่อเครื่อง      {tablet} บาท x {amountTablet}      : {priceAllTablet}              บาท
3. Smartphone   ต่อเครื่อง  {smartphone} บาท x {amountSmartphone}  : {priceAllSmartphone}          บาท
                                                รวมทั้งสิ้น (ก่อนลด) : {priceAll}                    บาท
                                                    ส่วนลดสมาชิก  : {priceAll*discountCustomer}   บาท
                                                    ส่วนลดเพิ่มเติม : {withDiscountForCustomer*discountOver50k} บาท
                                                    ราคาสุทธิ     : {withDiscountForCustomer - (withDiscountForCustomer*discountOver50k)} บาท
************************************************
""")
                exit()
    else:
        print(f"รายการที่ต้องชำระ: {withDiscountForCustomer} บาท")
        while True:
            paymentInput = float(input("กรอกจำนวนเงินที่ต้องชำระ: "))
            if withDiscountForCustomer > paymentInput or paymentInput == '' or paymentInput == 0 or paymentInput == 0.0:
                print("[ Error ] จำนวนเงินของคุณไม่เพียงพอ")
            else:
                print("[ OK ] ขอบคุณสำหรับการชำระเงิน")
                print(f"[ INFO ] จำนวนเงินทอน {paymentInput-withDiscountForCustomer} บาท")
                print(f"""
******************** ใบเสร็จ ********************
1. Notebook     ต่อเครื่อง    {notebook} บาท x {amountNotebook}    : {priceAllNotebook}            บาท
2. Tablet       ต่อเครื่อง      {tablet} บาท x {amountTablet}      : {priceAllTablet}              บาท
3. Smartphone   ต่อเครื่อง  {smartphone} บาท x {amountSmartphone}  : {priceAllSmartphone}          บาท
                                                รวมทั้งสิ้น (ก่อนลด) : {priceAll}                    บาท
                                                    ส่วนลดสมาชิก  : {priceAll*discountCustomer}   บาท
                                                    ราคาสุทธิ     : {withDiscountForCustomer} บาท
************************************************
""")
                exit()
else:
    if priceAll > 50000:
        priceWithDiscount10per = priceAll - (priceAll*discountOver50k)
        print(f"รายการที่ต้องชำระ: {priceWithDiscount10per} บาท")
        while True:
            paymentInput = float(input("กรอกจำนวนเงินที่ต้องชำระ: "))
            if priceWithDiscount10per > paymentInput or paymentInput == '' or paymentInput == 0 or paymentInput == 0.0:
                print("[ Error ] จำนวนเงินของคุณไม่เพียงพอ")
            else:
                print("[ OK ] ขอบคุณสำหรับการชำระเงิน")
                print(f"[ INFO ] จำนวนเงินทอน {paymentInput-priceWithDiscount10per} บาท")
                print(f"""
******************** ใบเสร็จ ********************
1. Notebook     ต่อเครื่อง    {notebook} บาท x {amountNotebook}    : {priceAllNotebook}            บาท
2. Tablet       ต่อเครื่อง      {tablet} บาท x {amountTablet}      : {priceAllTablet}              บาท
3. Smartphone   ต่อเครื่อง  {smartphone} บาท x {amountSmartphone}  : {priceAllSmartphone}          บาท
                                                รวมทั้งสิ้น (ก่อนลด) : {priceAll}                    บาท
                                                    ส่วนลด       : {priceAll*discountOver50k}   บาท
                                                    ราคาสุทธิ     : {priceWithDiscount10per} บาท
************************************************
""")
                exit()
    else:
        print(f"รายการที่ต้องชำระ: {priceAll} บาท")
        while True:
            paymentInput = float(input("กรอกจำนวนเงินที่ต้องชำระ: "))
            if priceAll > paymentInput or paymentInput == '' or paymentInput == 0 or paymentInput == 0.0:
                print("[ Error ] จำนวนเงินของคุณไม่เพียงพอ")
            else:
                print("[ OK ] ขอบคุณสำหรับการชำระเงิน")
                print(f"[ INFO ] จำนวนเงินทอน {paymentInput-priceAll} บาท")
                print(f"""
******************** ใบเสร็จ ********************
1. Notebook     ต่อเครื่อง    {notebook} บาท x {amountNotebook}    : {priceAllNotebook}            บาท
2. Tablet       ต่อเครื่อง      {tablet} บาท x {amountTablet}      : {priceAllTablet}              บาท
3. Smartphone   ต่อเครื่อง  {smartphone} บาท x {amountSmartphone}  : {priceAllSmartphone}          บาท
                                                รวมทั้งสิ้น (ก่อนลด) : {priceAll}                    บาท
                                                        ราคาสุทธิ : {priceAll}                    บาท
************************************************
""")
                exit()