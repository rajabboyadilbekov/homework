jura_1 = {'ism':'ALI', 't_yil':2011, 't_vil':'Xorazm', 'sev_taomi':'osh'}
jura_2 = {'ism':'Vali', 't_yil':2009, 't_vil':'Samarqand', 'sev_taomi':'manti'}
jura_3 = {'ism':'Jasur', 't_yil':2010, 't_vil':'Toshkent', 'sev_taomi':'somsa'}
print(f"1-jo'ramning ismi {jura_1['ism']},\
 u {jura_1['t_yil']}- yilda \
{jura_1['t_vil']}  viloyatida tug'ilgan")

print(f"2-jo'ramning ismi {jura_2['ism']}, \
 va u {jura_2['t_yil']}- yilda,\
{jura_2['t_vil']} viloyatida tug'ilgan")

print(f"3-jo'ramning ismi {jura_3['ism']}, va u esa {jura_3['t_yil']}- yilda, {jura_3['t_vil']} viloyatida tug'ilgan")

#2

print(f"Alining sevimli taomi {jura_1['sev_taomi']}")
print(f"Valining sevimli taomi {jura_2['sev_taomi']}")
print(f"Jasurning sevimli taomi {jura_3['sev_taomi']}")

#3

atamalar = {'int':'butun son', 'float':'haqiqiy son', 'str':'matn',
            'list':'ruyxat', 'tuple':'ozgarmas ruyxat', 'ValueError':'notugri qiymat',
            'TypeError':'mos kelmaydigan tur', 'IndexError':'notugri index',
            'SyntaxError':'yozilish qoidasi buzilganda sodir buladigan xato',
            'Input':'foydalanuvchidan malumot olish funksiyasi'}
print(f"Integer: {atamalar['int']}")
print(f"Float: {atamalar['float']}")
print(f"Str: {atamalar['str']}")
print(f"List: {atamalar['list']}")
print(f"Tuple: {atamalar['tuple']}")
print(f"ValueError: {atamalar['ValueError']}")
print(f"TypeError: {atamalar['TypeError']}")
print(f"IndexError: {atamalar['IndexError']}")
print(f"SyntaxError: {atamalar['SyntaxError']}")
print(f"Input: {atamalar['Input']}")

#4
soz = input("kalit so'z kiriting: ")
if soz in atamalar:
    print(atamalar[soz])
else:
    print("bunday so'z mavjud emas!")

#5

if soz in atamalar:
    print(f"{soz} so'zi {atamalar[soz]} dep tarjima qilinadi")
else:
    print("bunday so'z mavjud emas!")




