# รายการสินค้า
productList = {
    1: {
        "name": "Notebook",
        "price": 34000,
        "amountCustomer": 0
    },
    2: {
        "name": "Tablet",
        "price": 19000,
        "amountCustomer": 0
    },
    3: {
        "name": "Mobile cs Phone",
        "price": 26000,
        "amountCustomer": 0
    }
}

# ส่วนลดต่าง ๆ
discountMember = 0.05
discountOver50k = 0.1

# ฟังค์ชั่น
def discounter(allPay):
    if allPay > 50000:
        return allPay * discountOver50k

def paymentChecker(allPay, customerPay):
    if allPay < customerPay:
        return False
    else:
        return True

def printReceipt(memberStatus, notebookAmount, tabletAmount, phoneAmount, allPay):
    pass

while True:
    try:
        # แสดงรายการสินค้า
        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 CSAI Shop 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
        for productName, productInfo in productList.items():
            print(f"{productName} - {productInfo["name"]}       {productInfo["price"]}฿")
        print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")

        # รับค่าเพื่อเลือกสินค้า
        selectItemInput = int(input("เลือกรายการสินค้า (1-3), Ctrl + C เพื่อดำเนินการต่อ: "))
        amountSelectItemInput = int(input("จำนวนสินค้าที่ต้องการ: "))

        # ถ้า amountCustomer ไม่เท่ากับ 0 ให้เพิ่มข้อมูล
        if productList[selectItemInput]["amountCustomer"] != 0:
            productList[selectItemInput].update({"amountCustomer": productList[selectItemInput]["amountCustomer"]+amountSelectItemInput})
        else:
            productList[selectItemInput].update({"amountCustomer": amountSelectItemInput})
    
    except IndexError:
        print(f"\n[ Error ] ไม่พบรายการที่คุณป้อนเข้ามาในระบบ, กรุณาลองอีกครั้ง!")

    except KeyboardInterrupt:
        # Debug Mode (Please remove before present!!!)
        print(f"\n[ Info ] รายการที่ถูกสั่ง: {productInfo}")

        # เตรียมค่าต่าง ๆ ให้พร้อมใช้งาน
        notebookAmount = productList[1]["price"] * productList[1]["amountCustomer"]
        tabletAmount = productList[2]["price"] * productList[2]["amountCustomer"]
        phoneAmount = productList[3]["price"] * productList[3]["amountCustomer"]
        allPay = notebookAmount + tabletAmount + phoneAmount

        # ลูกค้าเป็นสมาชิกหรือไม่
        memberCheckInput = str(input("คุณเป็นสมาชิกหรือไม่ (Y/N): "))

        # หากใช่, ได้รับส่วนลด 5% 
        if memberCheckInput == "Y" or memberCheckInput == "y":
            discountMember5per = allPay - (allPay*discountMember)
            if discountMember5per > 50000:
                discountMember10per = discountMember5per - (discountMember5per*discountOver50k)
                # แล้วถ้าลดแล้วเกิน 50,000฿ ได้ลดเพิ่มอีก 10%
                # while paymentChecker(discountMember5per, customerPayInput) == False:
                #     print("[ Warning ] คุณชำระเงินไม่ครบ, กรุณาชำระเงินให้ครบยอดชำระ!")
                while True:
                    customerPayInput = float(input("กรุณาชำระเงิน: "))
                    if discountMember10per > customerPayInput or customerPayInput == None or customerPayInput == '' or customerPayInput == 0 or customerPayInput == 0.0:
                        print("[ Warning ] คุณชำระเงินไม่ครบ, กรุณาชำระเงินให้ครบยอดชำระ!")
                    else:
                        print("[ Error ] ขอบคุณสำหรับการชำระเงิน")
                        print(f"[ Info ] จำนวนเงินทอน {customerPayInput-discountMember10per} ฿")
                        print("[ Info ] รายการสั่งซื้อ")
                        print(printReceipt())

            else:
               while True:
                    customerPayInput = float(input("กรุณาชำระเงิน: "))
                    if discountMember5per > customerPayInput or customerPayInput == None or customerPayInput == '' or customerPayInput == 0 or customerPayInput == 0.0:
                        print("[ Warning ] คุณชำระเงินไม่ครบ, กรุณาชำระเงินให้ครบยอดชำระ!")
                    else:
                        print("[ Error ] ขอบคุณสำหรับการชำระเงิน")
                        print(f"[ Info ] จำนวนเงินทอน {customerPayInput-discountMember5per} ฿")
                        print("[ Info ] รายการสั่งซื้อ")
                        print(printReceipt())

        elif memberCheckInput == "N" or memberCheckInput == "n":
            pass

        else:
            print("[ Error ] กรุณาป้อนค่าให้ถูกต้อง!")

        exit()
    
    except Exception as error:
        print(f"\n[ Error ] พบปัญหาในการทำงาน: {error}")
        exit()