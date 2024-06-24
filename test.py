# # รายการสินค้า
# productList = {
#     1: {
#         'name': "Laptop",
#         'price': 34000,
#         'amountCustomer': 0
#     },
#     2: {
#         'name': "Tablet",
#         'price': 19000,
#         'amountCustomer': 0
#     },
#     3: {
#         'name': "Smartphone",
#         'price': 26000,
#         'amountCustomer': 0
#     }
# }
# if [productInfo['amountCustomer'] for productInfo in productList.values()] == 0:
#     print("[ OK ] ออกจากโปรแกรมเสร็จสิ้น, ขอบคุณสำหรับการใช้บริการ!")
# else:
#     for info in productList.values():
#         if info['amountCustomer'] != 0:
#             print(f"{info['name']}     ต่อเครื่อง    {info['price']} บาท x {info['amountCustomer']}    : {info['price'] * info['amountCustomer']}            บาท")

productsPriceTotal = 200
customerPaid = 0.0

def paymentChecker(allPaid, customerPaidInput, customerPaid):
    try:
        if customerPaid is not None:
            print(f"[ Info ] ยอดที่ต้องชำระเพิ่ม: {allPaid-customerPaid:,.2f} บาท")       
            customerPaid = customerPaid + customerPaidInput
        else:
            print(f"[ Info ] ยอดที่ต้องชำระ: {productsPriceTotal:,.2f} บาท")
    except ValueError:
        print(f"[ Error ] กรุณาป้อนค่าให้ถูกต้อง")

try:
    while productsPriceTotal >= customerPaid:
        customerPaidInput = float(input("ป้อนจำนวนเงินที่ต้องชำระ: "))
        paymentChecker(productsPriceTotal, customerPaidInput, customerPaid)

except KeyboardInterrupt:
    print(customerPaid)