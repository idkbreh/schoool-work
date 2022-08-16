info_t = input(" ชื่อคุณครู : ")
info_h = input(" จำนวนคาบที่สอน : ")
hour = int(info_h) * 50 // 60
minute = int(info_h) * 50 % 60
print(f"คุณครู{info_t} จำนวนคาบ {info_h} คาบ คิดเป็นเวลา {hour} ชั่วโมง {minute} นาที")