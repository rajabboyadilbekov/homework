class Shaxs:
    def __init__(self, ism, yosh):
        self.__ism = ism
        self.__yosh = yosh

    def get_ism(self):
        return self.__ism,
    def get_yosh(self):
        return self.__yosh
inson = Shaxs ("akrom","15")

print(inson.get_ism())
print(inson.get_yosh())
class maxsulot:
    def __init__(self,nomi,narx,yil,rangi):
        self.__nomi = nomi
        self.__narx = narx
        self.__yil = yil
        self.__rangi = rangi
    def get_maxsulot(self):
        return self.__nomi
    def get_narx(self):
        return self.__narx
    def get_yil(self):
        return self.__yil
    def get_rangi(self):
        return self.__rangi
mol =maxsulot("cola","12000","2025","qora")
print(mol.get_maxsulot())
print(mol.get_narx())
print(mol.get_yil())
print(mol.get_rangi())
