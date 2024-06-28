# รายการสินค้า
productList = {
    1: {
        'name': "Laptop",
        'price': 34000,
        'amountCustomer': 0
    },
    2: {
        'name': "Tablet",
        'price': 19000,
        'amountCustomer': 0
    },
    3: {
        'name': "Smartphone",
        'price': 26000,
        'amountCustomer': 0
    }
}

# ส่วนลดต่าง ๆ
DISCOUNT_MEMBER = 0.95
DISCOUNT_OVER_50K = 0.9

# สถานะของลูกค้า
customerMemberStatus = False
productsPriceTotal = 0.0
customerPaid = 0.0

# ฟังก์ชัน

def paymentChecker(allPaid, customerPaidInput, customerPaid):
    if customerPaid != 0:
        print(f"[ Info ] ยอดที่ต้องชำระเพิ่ม: {allPaid - customerPaid:,.2f} บาท")
        customerPaid += customerPaidInput
    else:
        print(f"[ Info ] ยอดที่ต้องชำระ: {productsPriceTotal:,.2f} บาท")
        customerPaid = customerPaidInput
    return customerPaid

def receiptPrint(customerMemberStatus):
    print("***************** CSAI Shop Receipt *****************")
    for info in productList.values():
        if info['amountCustomer'] != 0:
            print(f"{info['name']}     ต่อเครื่อง    {info['price']} บาท x {info['amountCustomer']}    : {float(info['price'] * info['amountCustomer']):,.2f} บาท")
    if customerMemberStatus:
        member_discount = productsPriceTotal * (1 - DISCOUNT_MEMBER)
        if productsPriceTotal > 50000:
            additional_discount = productsPriceTotal * (1 - DISCOUNT_OVER_50K) - member_discount
            print(f"ส่วนลดสมาชิก: {member_discount:,.2f} บาท")
            print(f"ส่วนลดเพิ่มเติม: {additional_discount:,.2f} บาท")
            print(f"ยอดชำระสุทธิ: {productsPriceTotal - member_discount - additional_discount:,.2f} บาท")
        else:
            print(f"ส่วนลดสมาชิก: {member_discount:,.2f} บาท")
            print(f"ยอดชำระสุทธิ: {productsPriceTotal - member_discount:,.2f} บาท")
    else:
        if productsPriceTotal > 50000:
            additional_discount = productsPriceTotal * (1 - DISCOUNT_OVER_50K)
            print(f"ส่วนลดเพิ่มเติม: {additional_discount:,.2f} บาท")
            print(f"ยอดชำระสุทธิ: {productsPriceTotal - additional_discount:,.2f} บาท")
        else:
            print(f"ยอดชำระสุทธิ: {productsPriceTotal:,.2f} บาท")
    print("****************************************************")

# โปรแกรม
while True:
    try:
        print("***************** CSAI Shop *****************")
        for product, info in productList.items():
            print(f"{product}. {info['name']} ราคา {float(info['price']):,.2f} ฿ จำนวนสินค้าที่เลือก {info['amountCustomer']} ชิ้น")
        print("*********************************************")

        selectProductInput = int(input("กรุณาเลือกสินค้า (1-3) เพื่อเลือกสินค้าเสร็จแล้วกด Enter: "))

        if selectProductInput in productList:
            productItemInput = int(input("กรุณาระบุจำนวนสินค้าที่ต้องการ: "))
            if productList[selectProductInput]['amountCustomer'] != 0:
                productList[selectProductInput]['amountCustomer'] += productItemInput
                print(f"[ OK ] ได้อัพเดตรายการเพิ่มอีก {productItemInput} เครื่องเรียบร้อยแล้ว ในรายการ {productList[selectProductInput]['name']}")
            else:
                if productItemInput < 0:
                    print(f"[ Error ] เนื่องจาก {productList[selectProductInput]['name']} ไม่มีสินค้า จึงไม่สามารถลดจำนวนสินค้าได้")
                else:
                    productList[selectProductInput]['amountCustomer'] = productItemInput
                    print(f"[ OK ] ได้เพิ่มรายการเรียบร้อยแล้ว ใน {productList[selectProductInput]['name']} จำนวน {productList[selectProductInput]['amountCustomer']} เครื่อง")
        else:
            print("[ Error ] ไม่พบสินค้าที่คุณเลือก, กรุณาเลือกใหม่อีกครั้ง")

    except ValueError:
        print("[ Error ] คุณป้อนค่าที่ไม่ถูกต้อง! กรุณาลองใหม่อีกครั้ง")

    except KeyboardInterrupt:
        try:
            checkAmount = [productInfo['amountCustomer'] for productInfo in productList.values()]
            if sum(checkAmount) == 0:
                print("\n[ OK ] ออกจากโปรแกรมเรียบร้อยแล้ว, ขอบคุณที่ใช้บริการ!")
                break
            else:
                laptopTotal = productList[1]['price'] * productList[1]['amountCustomer']
                tabletTotal = productList[2]['price'] * productList[2]['amountCustomer']
                phoneTotal = productList[3]['price'] * productList[3]['amountCustomer']

                productsPriceTotal = laptopTotal + tabletTotal + phoneTotal

                customerMemberInput = input("\n[ Prompt ] คุณเป็นสมาชิกหรือไม่ (Y/N): ").strip()

                if customerMemberInput == "Y" or customerMemberInput == "y":
                    customerMemberStatus = True
                    print("[ Info ] คุณเป็นสมาชิกร้านค้า CSAI Shop")
                elif customerMemberInput == "N" or customerMemberInput == "n":
                    customerMemberStatus = False
                    print("[ Info ] คุณไม่ได้เป็นสมาชิกร้านค้า CSAI Shop")
                else:
                    print("[ Error ] คุณป้อนค่าไม่ถูกต้อง! กรุณาลองอีกครั้ง")

                while True:
                    print(f"[ Info ] จำนวนเงินที่ต้องชำระ {productsPriceTotal:,.2f} บาท")
                    customerPaidInput = float(input("ป้อนจำนวนเงินที่ต้องชำระ: "))
                    customerPaid = paymentChecker(productsPriceTotal, customerPaidInput, customerPaid)
                    if customerPaid >= productsPriceTotal:
                        print(f"[ OK ] ชำระเงินเสร็จสิ้น, เงินทอน {customerPaid - productsPriceTotal:,.2f} บาท")
                        receiptPrint(customerMemberStatus)
                        break
                    else:
                        print(f"[ Info ] ยอดที่ต้องชำระเพิ่ม: {productsPriceTotal - customerPaid:,.2f} บาท")

        except KeyboardInterrupt:
            print("\n[ OK ] ออกจากโปรแกรมเรียบร้อยแล้ว, ขอบคุณที่ใช้บริการ!")
            break

        except Exception as error:
            print(f"[ Error ] เกิดข้อผิดพลาด: {error}")
