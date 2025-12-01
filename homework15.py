class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def get_info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __repr__(self):
        return self.nomi


class Talaba(Shaxs):
    def __init__(self, ism, yosh):
        super().__init__(ism, yosh)
        self.fanlar = []        # Bo‘sh ro‘yxat

    def fanga_yozil(self, fan_obj):
        self.fanlar.append(fan_obj)

    def remove_fan(self, fan_obj):
        if fan_obj in self.fanlar:
            self.fanlar.remove(fan_obj)
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        fanlar_qwe = ", ".join([fan.nomi for fan in self.fanlar]) or " yo‘q"
        return f"Talaba: {self.ism}, Yosh: {self.yosh}, Fanlar: {fanlar_qwe}"


class Professor(Shaxs):
    def __init__(self, ism, yosh, kafedra):
        super().__init__(ism, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism}, Yosh: {self.yosh}, Kafedra: {self.kafedra}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, username):
        super().__init__(ism, yosh)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.ism}, Username: {self.username}"




fan1 = Fan("Matematika")
fan2 = Fan("Fizika")

talaba = Talaba("suheob", 14)

talaba.fanga_yozil(fan1)
talaba.fanga_yozil(fan2)

print(talaba.get_info())

print(talaba.remove_fan(Fan("Tarix")))
print(talaba.remove_fan(fan1))
print(talaba.get_info())

