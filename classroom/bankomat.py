i = int(input("vvedite chislo: "))
a5000 = divmod(i, 5000)
a2000 = divmod(a5000[1], 2000)
a1000 = divmod(a2000[1], 1000)
a500 = divmod(a1000[1], 500)
a200 = divmod(a500[1], 200)
a100 = divmod(a200[1], 100)
a50 = divmod(a100[1], 50)
a10 = divmod(a50[1], 10)
a5 = divmod(a10[1], 5)
a3 = divmod(a5[1], 3)
a1 = divmod(a3[1], 1)
print(f" 5000 - {a5000[0]}, 2000 - {a2000[0]}, 1000 - {a1000[0]}, 500 - {a500[0]}, 200 - {a200[0]}, 100 - {a100[0]}, 50 - {a50[0]}, 10 - {a10[0]}, 5 - {a5[0]}, 3 - {a3[0]}, 1 - {a1[0]}")