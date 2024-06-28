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
DISCOUNT_MEMBER = 0.05
DISCOUNT_OVER_50K = 0.1

# สถานะของลูกค้า
customerMemberStatus = False
productsPriceTotal = 0.0
productsDis5per = 0.0
productsDis10per = 0.0
customerPaid = 0.0

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

while True:
    try:
        # แสดงรายการสินค้า
        print("************************ CSAI Shop ************************")
        for product, info in productList.items():
            print(f"{product}. {info['name']}  ราคา {float(info['price']):,.2f} บาท   จำนวนที่สั่งซื้อ {info['amountCustomer']} ชิ้น" )
        print("***********************************************************")
    
        # เลือกสินค้า
        productSelectInput = int(input("[ Prompt ] เลือกสินค้า 1-3 ถ้าทำรายการเสร็จแล้วกด Ctrl - C บนคีย์บอร์ด: "))
        
        # Checking productSelectInput in productList if found it, continue checking amountCustomer in dictionary
        if productSelectInput in productList:
            amountItemsCustomer = int(input("[ Prompt ] กรุณาป้อนจำนวนสินค้าที่ต้องการ หากต้องการลินค้าป้อน - พร้อมกับจำนวนที่ต้องการลดสินค้า: "))
            if productList[productSelectInput]['amountCustomer'] != 0:
                productList[productSelectInput].update({'amountCustomer': productList[productSelectInput]['amountCustomer']+amountItemsCustomer})
                print(f"[ OK ] ได้ทำการอัพเดตใน {productList[productSelectInput]['name']} เรียบร้อย, คงเหลือ {productList[productSelectInput]['amountCustomer']} ชิ้น")
            elif productList[productSelectInput]['amountCustomer'] == 0:
                if amountItemsCustomer < 0:
                    print("[ Error ] สินค้าที่คุณเลือกมีจำนวนไม่พอต่อการลดสินค้าที่ต้องการ")
                else:
                    productList[productSelectInput].update({'amountCustomer': productList[productSelectInput]['amountCustomer']+amountItemsCustomer})
                    print(f"[ OK ] ได้ทำการอัพเดตใน {productList[productSelectInput]['name']} เรียบร้อย, คงเหลือ {productList[productSelectInput]['amountCustomer']} ชิ้น")
            else:
                print("[ Error ] กรุณาตรวจสอบค่าที่คุณเพิ่มอีกครั้ง")
        else:
            print("[ Error ] ไม่พบรายการที่คุณเลือก กรุณาลองใหม่อีกครั้ง")
    
    except KeyboardInterrupt:
        # ก่อนที่จะชำระเงินตัวโปรแกรมจะเช็คข้อมูลใน Dictionary ก่อนที่จะคำนวณ ถ้าทั้งหมดมีค่าเป็น 0 จะบังคับออกจากโปรแกรมทันที
        if all(productInfo['amountCustomer'] == 0 for productInfo in productList.values()) :
            print("\n[ Warning ] เนื่องจากคุณไม่เลือกสินค้าโปรแกรมจะจบการทำงานทันที, ขอบคุณสำหรับการใช้บริการ")
            exit()
        else:
            productsPriceTotal = sum(productInfo['price']*productInfo['amountCustomer'] for productInfo in productList.values())
            statusMemberInput = str(input("\n[ Prompt ] คุณเป็นสมาชิกหรือไม่ (Y/N): ")).strip()
            if statusMemberInput == 'Y' or statusMemberInput == 'y':
                # จะทำการ Set Status ทันที
                customerMemberStatus = True
                productsDis5per = productsPriceTotal * DISCOUNT_MEMBER
                # ถ้ายังยังลดแล้วยังเกิน 50,000 ก็จะได้รับเพิ่มอีก 10%
                if productsPriceTotal - productsDis5per > 50000:
                    productsDis10per = (productsPriceTotal-productsDis5per) * DISCOUNT_OVER_50K
                while customerPaid < productsPriceTotal:
                    try:
                        print(f"[ Info ] ยอดที่ต้องชำระ {abs((productsPriceTotal-productsDis5per-productsDis10per) - customerPaid):,.2f} บาท")
                        customerPaidInput = float(input("[ Prompt ] กรุณาป้อนจำนวนเงิน: "))
                        # ถ้าป้อนจำนวนติดลบลงไป จะแสดง Error ขึ้นมา
                        if customerPaidInput < 0:
                            print("[ Error ] ป้อนค่าไม่ถูกต้อง กรุณาป้อนใหม่อีกครั้ง")
                            continue
                        customerPaid += customerPaidInput
                    except ValueError:
                        print("[ Error ] กรุณาป้อนค่าให้ถูกต้อง")
                print(f"[ OK ] ชำระเงินเสร็จสิ้น, ทอนเงิน {abs((productsPriceTotal-productsDis5per-productsDis10per) - customerPaid):,.2f} บาท")
                exit()
            elif statusMemberInput == 'N' or statusMemberInput == 'n':
                customerMemberStatus = False
                if productsPriceTotal - productsDis5per > 50000:
                    productsDis10per = (productsPriceTotal-productsDis5per) * DISCOUNT_OVER_50K
                # while customerPaid < productsPriceTotal:
                #     try:
                #         print(f"[ Info ] ยอดที่ต้องชำระ {abs((productsPriceTotal-productsDis5per-productsDis10per) - customerPaid):,.2f} บาท")
                #         customerPaidInput = float(input("[ Prompt ] กรุณาป้อนจำนวนเงิน:"))
                #         if customerPaidInput < 0:
                #             print("[ Error ] ป้อนค่าไม่ถูกต้อง กรุณาป้อนใหม่อีกครั้ง")
                #             continue
                #         customerPaid += customerPaidInput
                #     except ValueError:
                #         print("[ Error ] กรุณาป้อนค่าให้ถูกต้อง")
                # print(f"[ OK ] ชำระเงินเสร็จสิ้น, ทอนเงิน {abs((productsPriceTotal-productsDis5per-productsDis10per) - customerPaid):,.2f} บาท")
                # exit()
                while customerPaid < productsPriceTotal:
                    try:
                        print(f"[ Info ] ยอดที่ต้องชำระ {abs((productsPriceTotal-productsDis5per-productsDis10per) - customerPaid):,.2f} บาท")
                        customerPaidInput = float(input("[ Prompt ] กรุณาป้อนจำนวนเงิน: "))
                        # ถ้าป้อนจำนวนติดลบลงไป จะแสดง Error ขึ้นมา
                        if customerPaidInput < 0:
                            print("[ Error ] ป้อนค่าไม่ถูกต้อง กรุณาป้อนใหม่อีกครั้ง")
                            continue
                        customerPaid += customerPaidInput
                    except ValueError:
                        print("[ Error ] กรุณาป้อนค่าให้ถูกต้อง")
                print(f"[ OK ] ชำระเงินเสร็จสิ้น, ทอนเงิน {abs((productsPriceTotal-productsDis5per-productsDis10per) - customerPaid):,.2f} บาท")
                exit()
            else:
                print("[ Error ] กรุณาป้อนค่าใหม่อีกครั้ง!")
    except IndexError:
        print("[ Error ] ไม่พบค่าที่คุณป้อน กรุณาลองอีกครั้ง")
    except ValueError:
        print("[ Error ] ป้อนค่าไม่ถูกต้อง กรุณาลองอีกครั้ง")        
    except Exception as error:
        print(f"[ Error ] พบข้อผิดพลาด \n{error}")
        exit()