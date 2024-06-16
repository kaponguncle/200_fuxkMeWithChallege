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
discountCustomer = 0.05
discountOver50k = 0.1

while True:
    try:
        # แสดงรายการสินค้า
        print("**************** CSAI Shop ****************")
        for productName, productInfo in productList.items():
            print(f"{productName} - {productInfo}")
        print("*******************************************")

        # รับค่าเพื่อเลือกสินค้า
        selectItemInput = int(input("เลือกรายการสินค้า (1-3): "))
        amountSelectItemInput = int(input("จำนวนสินค้าที่ต้องการ: "))

        # ถ้า amountCustomer ไม่เท่ากับ 0 ให้เพิ่มข้อมูล
        if productList[selectItemInput]["amountCustomer"] != 0:
            productList[selectItemInput].update({"amountCustomer": productList[selectItemInput]["amountCustomer"]+amountSelectItemInput})
        else:
            productList[selectItemInput].update({"amountCustomer": amountSelectItemInput})
    
    except IndexError:
        print("[ Error ] ไม่พบรายการที่คุณป้อนเข้ามาในระบบ, กรุณาลองอีกครั้ง")

    except KeyboardInterrupt:
        print(f"\n[ Info ] รายการที่ถูกสั่ง: {productInfo}")
        exit()
    
    except Exception as error:
        print(f"\n[ Error ] พบปัญหาในการทำงาน: {error}")