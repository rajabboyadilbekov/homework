#1
def kopaytma(*sonlar):
    kopaytr = 1
    for son in sonlar:
        kopaytr *= son
    return kopaytr
print(kopaytma(11,54,))
#2
def talabalar(ism,kurs,**malumotlar):
    malumotlar["ism"]=ism
    malumotlar["kurs"]=kurs
    return malumotlar
talaba_1=talabalar("suhrob",2,yil=2011,yashash_manzil="urganch")
talaba_2=talabalar("akrom",3,yil=2010,yashash_manzil="urganch")
print(talaba_1,talaba_2)
#math.prod()

