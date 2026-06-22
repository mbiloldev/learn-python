balance = 1000
try:
 money = int(input("Pul yechish: "))
 if money > balance:
 print("Yetarli mablag‘ yo‘q")
 else:
 balance -= money
 print("Qoldiq:", balance)
except ValueError:
 print("Faqat son kiriting")
