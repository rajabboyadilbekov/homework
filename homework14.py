#1,2
class user:
    def __init__(self,name,age,user_name,email):
        self.name = name
        self.user_name=user_name
        self.email=email
        self.age=age

    def get_info(self):
        print(f"foydalanuvchi>>> {self.user_name} ismi>>> {self.name}.gmail>>> {self.email} ")

user1=user("suhrob","14","the.a11aberganov.cds_","sukhrob@gmail.com")

print(user1.name)
print(user1.age)
print(user1.user_name)
print(user1.email)
user1.get_info()

