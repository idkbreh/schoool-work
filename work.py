user = input(" ชื่อลูกค้า >>: ")
Total_spend = input(" ซื้อสินค้าทั้งหมดกี่บาท >>: ")
member = input(" เป็นสมาชิกหรือไม่ [ Y / N ] ? >>: ")
print(" ")
print("********************************************")
answer = member.lower() //high accurate
if answer == "y":
    print(" ")
    if int(Total_spend) >= 10000:
        final_price = int(Total_spend) * 90 //100
        point = int(final_price) * 1
        print(f"คุณ{user} เป็นสมาชิก ซื้อสินค้า {Total_spend} จะได้รับส่วนลด 10% ลดเหลือ {final_price} ได้เเต้มสะสม {point} เเต้ม")
    elif int(Total_spend) < 10000:
        final_price = int(Total_spend) * 95 //100
        point = int(final_price) * 0.75
        print(f"คุณ{user} เป็นสมาชิก ซื้อสินค้า {Total_spend} จะได้รับส่วนลด 5% ลดเหลือ {final_price} ได้เเต้มสะสม {point} เเต้ม")
if answer == "n" :
    print(" ")
    final_price = int(Total_spend) * 95 //100
    point = int(final_price) // 2
    print(f"คุณ{user} ไม่ได้เป็นสมาชิก ซื้อสินค้า {Total_spend} จะได้รับส่วนลด 5% ลดเหลือ {final_price} ได้เเต้มสะสม {point} เเต้ม")
