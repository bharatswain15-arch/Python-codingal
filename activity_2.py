amount = int(input("please enter amount for whithdraw: "))
note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = (amount % 100 % 50) // 10

print("notes of hundred rupees ",note_1)
print("notes of fifty rupees ",note_2)
print("notes of ten rupees ",note_3)