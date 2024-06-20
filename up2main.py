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
# customerMemberStatus = False
customerPaid = 0

# ฟังค์ชั่น
def paymentChecker(allPaid, customerPaid):
    while customerPaid >= allPaid:
       return True
    

def receiptPrint():
    pass

# โปรแกรม
while True:
    try:
        # แสดงข้อมูลใน productList ที่เก็บข้อมูลของสินค้า
        print("***************** CSAI Shop *****************")
        for product, info in productList.items():
            print(f"{product}. {info["name"]} ราคา {info["price"]}฿, จำนวนสินค้าที่เลือก {info["amountCustomer"]} ชิ้น")
        print("*********************************************")

        selectProductInput = int(input("กรุณาเลือกสินค้า (1-3) เมื่อเลือกสินค้าเสร็จแล้วให้ Ctrl + C เพื่อดำเนินการต่อ: "))

        if selectProductInput in productList:
            productItemInput = int(input("กรุณาระบุจำนวนสินค้าที่ต้องการ หากต้องการลดจำนวนสินค้าใส่เครื่องหมาย - พร้อมกับจำนวนที่ต้องการจะลดได้: "))
            if productList[selectProductInput] != 0:
                productList[selectProductInput].update({"amountCustomer": productList[selectProductInput]["amountCustomer"]+productItemInput})
                print(f"[ OK ] ได้อัพเดตรายการเพิ่มอีก {productItemInput} เครื่องเรียบร้อยแล้ว ในรายการ {productList[selectProductInput]["name"]}")
            else:
                productList[selectProductInput].update({"amountCustomer": productList[selectProductInput]})
                print(f"[ OK ] ได้เพิ่มรายการเรียบร้อยแล้ว ใน {productList[selectProductInput]["name"]} จำนวน {productList[selectProductInput]["amountCustomer"]} เครื่อง")
        else:
            print("[ Error ] ไม่พบสินค้าที่คุณเลือก, กรุณาเลือกใหม่อีกครั้ง")

    except IndexError:
        print("[ Error ] ไม่พบค่าที่คุณป้อน! กรุณาลองอีกครั้ง")

    except ValueError:
        print("[ Error ] คุณป้อนนั้นไม่ถูกต้อง! กรุณาลองอีกครั้ง")
    
    except KeyboardInterrupt:
        # Maintenance Mode... <start>
        customerMemberInput = str(input("\n[ Prompt ] คุณเป็นสมาชิกหรือไม่ (Y/N): ")).strip()
        if customerMemberInput == "Y" or customerMemberInput == "y":
            print("[ Info ] คุณไม่ได้เป็นสมาชิกร้านค้า CSAI Shop")
            print(f"[ Info ] ราการสินค้าที่เลือก\n{productList}")
            exit()
        elif customerMemberInput == "N" or customerMemberInput == "n":
            customerMemberStatus = True
            print("[ Info ] คุณเป็นสมาชิกร้านค้า CSAI Shop")
            print(f"[ Info ] รายการสินค้าที่สั่งซื้อ\n{productList}")
            exit()
        else:
            print("[ Error ] คุณป้อนค่าไม่ถูกต้อง! กรุณาลองอีกครั้ง")
            # Maintenance Mode... <end>
        # print(f"\n[ OK ] ออกจากโปรแกรมเสร็จสิ้น, ขอบคุณสำหรับการใช้บริการ!")
        # exit()

    except Exception as error:
    # ถ้าพบ Error ให้แสดงผลออกมา และออกจากโปรแกรมทันที
        print(f"[ Error ] โปรแกรมพบข้อผิดพลาด:\n{error}")
        exit()