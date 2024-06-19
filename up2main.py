# รายการสินค้า
productList = {
    1: {
        "name": "Laptop",
        "price": 34000,
        "amountCustomer": 0
    },
    2: {
        "name": "Tablet",
        "price": 19000,
        "amountCustomer": 0
    },
    3: {
        "name": "Smartphone",
        "price": 26000,
        "amountCustomer": 0
    }
}

# ส่วนลดต่าง ๆ
DISCOUNT_MEMBER = 0.95
DISCOUNT_OVER_50K = 0.9

# สถานะของลูกค้า
customerMemberStatus = False
customerPaid = 0

# ฟังค์ชั่น
def discounter(allPaid, memberStatus): # เอาไว้ตรวจสอบการลดราคา
    if allPaid > 50000 and memberStatus == True:
        return True
    elif allPaid > 50000 and memberStatus == False:
        return True
    else:
        return False
    
def paymentChecker(allPaid, customerStatus):
    if allPaid > customerStatus:
        return False
    else:
        return True

def receiptPrint():
    pass

# โปรแกรม
while True:
    try:
        # แสดงข้อมูลใน productList ที่เก็บข้อมูลของสินค้า
        print("***************** CSAI Shop *****************")
        for product in productList:
            print(f"{productList.index(product)+1}. {product["name"]} ราคา {product["price"]}฿ ,จำนวนสินค้าที่เลือก {product["amountCustomer"]} ชิ้น")
        print("*********************************************")

        # เมื่อ **Feature กำลังดำเนินการพัฒนา... 
        selectProductInput = input("กรุณาเลือกสินค้า (1-3) เมื่อเลือกสินค้าเสร็จแล้วให้พิมพ์ ok หรือ OK เพื่อดำเนินการต่อ: ").strip()

        # เมื่อเลือกเสร็จแล้ว ก็ให้ผู้ใช้งานพิมพ์ ok หรือ OK (ตัวใหญ่) เพื่อดำเนินการต่อ
        if selectProductInput == "ok" or selectProductInput == "OK":
            customerMemberInput = str(input("[ Prompt ] คุณเป็นสมาชิกหรือไม่ (Y/N): "))
            if customerMemberStatus:
                print("")
            else:
                customerMemberStatus = True
                print("")
        else:
            # โดยแปลง selectProductInput ให้สามารถเลือกข้อมูลใน productList ได้
            if selectProductInput in productList:
                productItemInput = int(input("กรุณาระบุจำนวนสินค้าที่ต้องการ หากต้องการลดจำนวนสินค้าใส่เครื่องหมาย - พร้อมกับจำนวนที่ต้องการจะลดได้: "))
                if productList[selectProductInput] != 0:
                    productList[selectProductInput].update({"amountCustomer": productList[selectProductInput]["amountCustomer"]+productItemInput})
                    print(f"[ OK ] ได้อัพเดตรายการเพิ่มอีก {productItemInput} เครื่องเรียบร้อยแล้ว ในรายการ {productList[selectProductInput]["name"]}")
                else:
                    productList[selectProductInput].update({"amountCustomer": productList[selectProductInput]})
                    print(f"[ OK ] ได้เพิ่มรายการเรียบร้อยแล้ว ใน {productList[selectProductInput]["name"]} จำนวน {productList[selectProductInput]["amountCustomer"]} เครื่อง")

    except ValueError:
        print(f"[ Error ] ไม่พบข้อมูลที่เลือก!")
    
    except KeyboardInterrupt:
        print(f"[ OK ] ออกจากโปรแกรมเสร็จสิ้น, ขอบคุณสำหรับการใช้บริการ!")
        exit()

    except Exception as error:
    # ถ้าพบ Error ให้แสดงผลออกมา และออกจากโปรแกรมทันที
        print(f"[ Error ] โปรแกรมพบข้อผิดพลาด:\n{error}")
        exit()


    