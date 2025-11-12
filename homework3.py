#add () to'plamga element qo'shadi
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
car={"bmw","mersders benz","gelik"}
car.add("jiguli")
print(car)
# clear () to'plamdagi barcha elementlarni olib tashlaydi
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
car={"bmw","mersders benz","gelik"}
car.clear()
print(car)
#copy () to'plam nusxasini qaytaradi
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
car={"bmw","mersders benz","gelik"}
c=car.copy()
print(c)
#farq() - Ikki yoki undan ortiq to'plamlar orasidagi farqni o'z ichiga olgan to'plamni qaradi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
a={"bmw","mersders benz","gelik"}
b={"mersders benz","apple","goggles"}
c = a.difference(b)
print(c)
#different_update() -= Ushbu to'plamdagi boshqa, belgilangan to'plamga kiritilgan narsalarni o'chiradi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
a={"bmw","mersders benz","gelik"}
b={"mersders benz","apple","goggles"}
a.difference_update(b)
print(a)
#discard() Belgilangan elementni olib tashlang
fruits = {"apple", "banana", "cherry"}

fruits.discard("apple")

print(fruits)
worlds=b={"mersders benz","apple","goggles"}
worlds.discard("apple")
#intersection() & To'plamni qaytaradi, ya'ni boshqa ikkita to'plamning kesishishi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
a={"bmw","mersders benz","gelik"}
q={"mersders benz","apple","goggles"}
g = a.intersection(q)
print(g)
#intersection_update() &= Ushbu to'plamdagi boshqa belgilangan to'plam(lar)da mavjud bo'lmagan elementlarni o'chiradi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
a={"bmw","mersders benz","gelik"}
q={"mersders benz","apple","goggles"}
g.intersection_update(q)
print(g)
#isdisjoint() Ikki toʻplamning kesishishi bor yoki yoʻqligini qaytaradi
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
w={"bmw","mersders benz","gelik"}
q={"mersders benz","apple","goggles"}
h=w.isdisjoint(q)
print(h)
# barcha elementlari boshqa to'plamda mavjud bo'lsa, True qiymatini#issubset() <= Agar ushbu to'plamnin qaytaradi
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
w={"a","r","b","j"}
y={"h","y","g","h","i","y","t"}
z = x.issuperset(y)
print(z)