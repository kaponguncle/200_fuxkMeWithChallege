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

# ฟังค์ชั่น

def paymentChecker(allPaid, customerPaidInput, customerPaid):
    if customerPaid != 0:
        print(f"[ Info ] ยอดที่ต้องชำระเพิ่ม: {allPaid-customerPaid:,.2f} บาท")       
        customerPaid += customerPaidInput
    else:
        print(f"[ Info ] ยอดที่ต้องชำระ: {productsPriceTotal:,.2f} บาท")
        
def receiptPrint(customerMemberStatus):
    print("***************** CSAI Shop Recipt *****************")
    for info in productList.values():
        if info['amountCustomer'] != 0:
            print(f"{info['name']}     ต่อเครื่อง    {info['price']} บาท x {info['amountCustomer']}    : {info['price'] * info['amountCustomer']} บาท")
    if customerMemberStatus == True:
        print(f"ส่วนลดสมาชิก: {productsPriceTotal * (1 - DISCOUNT_MEMBER):,.2f} บาท")
        if productsPriceTotal > 50000:
            print(f"ส่วนลดเพิ่มเติม: {productsPriceTotal * (1 - DISCOUNT_OVER_50K):,.2f} บาท")
        print(f"ยอดชำระสุทธิ: {productsPriceTotal * (DISCOUNT_MEMBER * DISCOUNT_OVER_50K):,.2f} บาท")
    else:
        if productsPriceTotal > 50000:
            print(f"ส่วนลดเพิ่มเติม: {productsPriceTotal * (1 - DISCOUNT_OVER_50K):,.2f} บาท")
        print(f"ยอดชำระสุทธิ: {productsPriceTotal * (DISCOUNT_MEMBER * DISCOUNT_OVER_50K):,.2f} บาท")
    print("****************************************************")

# โปรแกรม
while True:
    try:
        # แสดงข้อมูลใน productList ที่เก็บข้อมูลของสินค้า
        print("***************** CSAI Shop *****************")
        for product, info in productList.items():
            print(f"{product}. {info['name']} ราคา {info['price']}฿, จำนวนสินค้าที่เลือก {info['amountCustomer']} ชิ้น")
        print("*********************************************")

        # เลือกสินค้า เมื่อเลือกสินค้าเสร็จสิ้น
        selectProductInput = int(input("กรุณาเลือกสินค้า (1-3) เมื่อเลือกสินค้าเสร็จแล้วให้ Ctrl + C เพื่อดำเนินการต่อ: "))

        # ตรวจสอบการเข้ามาของ selectProductInput ให้ตรวจสอบว่าที่ลูกค้าเลือกมีอยู่ใน productList หรือไม่
        if selectProductInput in productList:
            # ถ้าพบรายการแล้วก็จะตรวจสอบว่า product ที่เลือกมานั้นมีสินค้าอยู่หรือไม่ และถ้ายังมีสินค้าอยู่ ก็ให้เพิ่มจากที่มีอยู่เดิม
            productItemInput = int(input("กรุณาระบุจำนวนสินค้าที่ต้องการ หากต้องการลดจำนวนสินค้าใส่เครื่องหมาย - พร้อมกับจำนวนที่ต้องการจะลดได้: "))
            if productList[selectProductInput]['amountCustomer'] != 0:
                # if productList[selectProductInput]['amountCustomer'] == 0:
                
                productList[selectProductInput].update({'amountCustomer': productList[selectProductInput]['amountCustomer']+productItemInput})
                print(f"[ OK ] ได้อัพเดตรายการเพิ่มอีก {productItemInput} เครื่องเรียบร้อยแล้ว ในรายการ {productList[selectProductInput]['name']}")
            
            else:
                if productItemInput < 0:
                    print(f"[ Error ] เนื่องจาก {productList[selectProductInput]['name']} ไม่ได้ใส่จำนวนไว้ จึงไม่สามารถลดจำนวนสินค้าลงได้")
                else:
                    productList[selectProductInput].update({'amountCustomer': productItemInput})
                    print(f"[ OK ] ได้เพิ่มรายการเรียบร้อยแล้ว ใน {productList[selectProductInput]['name']} จำนวน {productList[selectProductInput]['amountCustomer']} เครื่อง")
        else:
            print("[ Error ] ไม่พบสินค้าที่คุณเลือก, กรุณาเลือกใหม่อีกครั้ง")

    except IndexError:
        print("[ Error ] ไม่พบค่าที่คุณป้อน! กรุณาลองอีกครั้ง")

    except ValueError:
        print("[ Error ] คุณป้อนนั้นไม่ถูกต้อง! กรุณาลองอีกครั้ง")
    
    except KeyboardInterrupt:
        # Maintenance Mode... <start>
        
        checkAmount = [productInfo['amountCustomer'] for productInfo in productList.values()]
        if checkAmount == 0:
            print("\n[ OK ] ออกจากโปรแกรมเสร็จสิ้น, ขอบคุณสำหรับการใช้บริการ!")
            exit()
        else:
            laptopTotal = productList[1]['price'] * productList[1]['amountCustomer']
            tabletTotal = productList[2]['price'] * productList[2]['amountCustomer']
            phoneTotal = productList[3]['price'] * productList[3]['amountCustomer']

            productsPriceTotal = laptopTotal + tabletTotal + phoneTotal

            customerMemberInput = str(input("\n[ Prompt ] คุณเป็นสมาชิกหรือไม่ (Y/N): ")).strip()
            if customerMemberInput == "Y" or customerMemberInput == "y":
                
                customerMemberStatus = True
                print("[ Info ] คุณเป็นสมาชิกร้านค้า CSAI Shop")
                # print(f"[ Info ] รายการสินค้าที่เลือก\n{productList}")
                
                # เนื่องจากเป็นสมาชิกอยู่แล้วจึงได้นับส่วนลด 5% และถ้าลดราคาแล้วยังเกิน 50,000 บาทอยู่รับส่วนลดเพิ่มอีก 10%
                productsPriceTotal *= DISCOUNT_MEMBER
                if productsPriceTotal > 50000:
                    productsPriceTotal *= DISCOUNT_OVER_50K

                # ตรวจสอบการจ่ายเงิน
                # ถ้าจ่ายครบให้ไปที่ใบเสร็จ หากไม่ครบหรือไม่ใช่
                while customerPaid >= productsPriceTotal:
                    print(f"[ Info ] จำนวนเงินที่ต้องชำระ {productsPriceTotal:,.2f} บาท")
                    customerPaidInput = float(input("ป้อนจำนวนเงินที่ต้องชำระ: ")).strip()
                    if customerPaid != 0:
                        print(f"[ Info ] ยอดที่ต้องชำระเพิ่ม: {productsPriceTotal-customerPaid:,.2f} บาท")       
                        customerPaid += customerPaidInput
                    else:
                        print(f"[ Info ] ยอดที่ต้องชำระ: {productsPriceTotal:,.2f} บาท")
                receiptPrint(customerMemberStatus)
                exit()
            elif customerMemberInput == "N" or customerMemberInput == "n":
                customerMemberStatus = False
                print("[ Info ] คุณไม่ได้เป็นสมาชิกร้านค้า CSAI Shop")
                # print(f"[ Info ] รายการสินค้าที่สั่งซื้อ\n{productList}")
                
                # เนื่องจากเป็นสมาชิกอยู่แล้วจึงได้นับส่วนลด 5% และถ้าลดราคาแล้วยังเกิน 50,000 บาทอยู่รับส่วนลดเพิ่มอีก 10%
                productsPriceTotal *= DISCOUNT_MEMBER
                if productsPriceTotal > 50000:
                    productsPriceTotal *= DISCOUNT_OVER_50K

                # ตรวจสอบการจ่ายเงิน
                # ถ้าจ่ายครบให้ไปที่ใบเสร็จ หากไม่ครบหรือไม่ใช่
                while customerPaid >= productsPriceTotal:
                    print(f"[ Info ] จำนวนเงินที่ต้องชำระ {productsPriceTotal:,.2f} บาท")
                    customerPaidInput = float(input("ป้อนจำนวนเงินที่ต้องชำระ: ")).strip()
                    if customerPaid != 0:
                        print(f"[ Info ] ยอดที่ต้องชำระเพิ่ม: {productsPriceTotal-customerPaid:,.2f} บาท")       
                        customerPaid += customerPaidInput
                    else:
                        print(f"[ Info ] ยอดที่ต้องชำระ: {productsPriceTotal:,.2f} บาท")
                receiptPrint(customerMemberStatus)
                exit()
            else:
                print("[ Error ] คุณป้อนค่าไม่ถูกต้อง! กรุณาลองอีกครั้ง")
            # Maintenance Mode... <end>
    
    except Exception as error:
    # ถ้าพบ Error ให้แสดงผลออกมา และออกจากโปรแกรมทันที
        print(f"[ Error ] โปรแกรมพบข้อผิดพลาด:\n{error}")
        exit()