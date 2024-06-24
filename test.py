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

def receiptPrint(customerMemberStatus):
    global productsPriceTotal
    print("***************** CSAI Shop Receipt *****************")
    for info in productList.values():
        if info['amountCustomer'] != 0:
            print(f"{info['name']}    {info['price']} บาท x {info['amountCustomer']}    : {float(info['price'] * info['amountCustomer']):,.2f} บาท")
    if customerMemberStatus:
        member_discount = productsPriceTotal * (1 - DISCOUNT_MEMBER)
        if productsPriceTotal > 50000:
            additional_discount = (productsPriceTotal-member_discount) * (1-DISCOUNT_OVER_50K)
            print(f"ส่วนลดสมาชิก: {member_discount:,.2f} บาท")
            print(f"ส่วนลดเพิ่มเติม: {additional_discount:,.2f} บาท")
            print(f"ยอดชำระสุทธิ: {productsPriceTotal - (member_discount + additional_discount):,.2f} บาท")
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
        # แสดงรายการสินค้า
        print("***************** CSAI Shop *****************")
        for product, info in productList.items():
            print(f"{product}. {info['name']} ราคา {info['price']:,.2f} บาท จำนวนที่เลือก {info['amountCustomer']} ชิ้น")
        print("*********************************************")

        # เลือกสินค้า
        selectProductInput = int(input("กรุณาเลือกสินค้า (1-3) หรือกด Ctrl + C เพื่อชำระเงิน: "))

        # ตรวจสอบสินค้า
        if selectProductInput in productList:
            productItemInput = int(input(f"กรุณาระบุจำนวนสินค้าที่ต้องการเพิ่มหรือลด ({productList[selectProductInput]['name']}) : "))
            if productList[selectProductInput]['amountCustomer'] + productItemInput < 0:
                print("[ Error ] ไม่สามารถลดจำนวนสินค้าได้เนื่องจากไม่มีสินค้าในรายการ")
            else:
                productList[selectProductInput]['amountCustomer'] += productItemInput
                print(f"[ OK ] จำนวนสินค้า {productList[selectProductInput]['name']} คือ {productList[selectProductInput]['amountCustomer']}")
        else:
            print("[ Error ] ไม่พบสินค้าที่เลือก กรุณาลองอีกครั้ง")

    except KeyboardInterrupt:
        # คำนวณยอดชำระ
        productsPriceTotal = sum(product['price'] * product['amountCustomer'] for product in productList.values())
        print(f"\n[ Prompt ] คุณเป็นสมาชิกหรือไม่ (Y/N): ", end='')
        customerMemberInput = input().strip().lower()
        
        # ตรวจสอบสถานะสมาชิก
        if customerMemberInput == "y":
            customerMemberStatus = True
            productsPriceTotal *= DISCOUNT_MEMBER
            if productsPriceTotal > 50000:
                productsPriceTotal *= DISCOUNT_OVER_50K
        elif customerMemberInput == "n":
            customerMemberStatus = False
            if productsPriceTotal > 50000:
                productsPriceTotal *= DISCOUNT_OVER_50K
        else:
            print("[ Error ] ป้อนค่าไม่ถูกต้อง! กรุณาลองอีกครั้ง")
            continue
        
        # จ่ายเงิน
        while customerPaid < productsPriceTotal:
            try:
                print(f"[ Info ] จำนวนเงินที่ต้องชำระ: {productsPriceTotal - customerPaid:,.2f} บาท")
                customerPaidInput = float(input("ป้อนจำนวนเงินที่ชำระ: "))
                if customerPaidInput < 0:
                    print("[ Error ] ป้อนจำนวนเงินไม่ถูกต้อง! กรุณาลองอีกครั้ง")
                    continue
                customerPaid += customerPaidInput
            except ValueError:
                print("[ Error ] ป้อนค่าไม่ถูกต้อง! กรุณาลองอีกครั้ง")

        # พิมพ์ใบเสร็จ
        change = customerPaid - productsPriceTotal
        print(f"[ OK ] ชำระเงินเสร็จสิ้น, เงินทอน {change:,.2f} บาท")
        receiptPrint(customerMemberStatus)
        break

    except ValueError:
        print("[ Error ] ป้อนค่าไม่ถูกต้อง! กรุณาลองอีกครั้ง")
    except Exception as e:
        print(f"[ Error ] เกิดข้อผิดพลาด: {e}")
