#1
ismlar =["ali","vali","xasan","xusan","olim"]
for ism in ismlar:
    print(f"salom {ism}")
print(f'Kod {len(ismlar)} marta takrorlandi')
#2
sonlar = list(range(11,100))
for son in sonlar:
    print(f"{son*son*son}")
#3
dostlar = []
print("sevimli kinolaringizni kriting?:")
for n in range(5):
    dostlar.append(input(f"{n + 1}-sevimli kinoyingizni kriting? :"))
print(dostlar)
#4
dostlar = []
print("Bugun nechta odam bilan suhbatlashdingiz?")
for n in range(3):
    dostlar.append(input(f"{n + 1}-suhbat qigan odamingiz kim edi? :"))
print(dostlar)
