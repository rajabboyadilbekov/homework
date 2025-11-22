# # №1
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
# ism = str(input("Ism kiriting: "))
# familiya = str(input("Familiya kiriting: "))
# yosh = int(input("Yoshingizni kiriting: "))
# print(user_data(ism, familiya, yosh))
#
# # №2
# def find_max(a, b, c):
#     salom = max(a, b, c)
#     salom1 = []
#     if a == salom:
#         salom1.append("A")
#     if b == salom:
#         salom1.append("B")
#     if c == salom:
#         salom1.append("C")
#     print(f"Eng katta son - {salom1} = {salom}")
# qwe1 = int(input("A ni kiriting: "))
# qwe2 = int(input("B ni kiriting: "))
# qwe3 = int(input("C ni kiriting: "))
# find_max(qwe1, qwe2, qwe3)
#
#
#
# # №4
# def list_sum(myList):
#     qwerty = 0
#     for salom in myList:
#         qwerty += salom
#     print("Listning elementlar yig'indisi =", qwerty)
#
# myList = [1, 9, 12343132, 2]
# list_sum(myList)
#
# # №5
# def daraja(a, b):
#     print(a ** b)
# daraja(2, 3)
#
# # №6
# def daraja4(a, b, c, d):
#     print(a**b, a**c, a**d)
# daraja4(1, 2, 3, 4)
#
# # # №7
#
# # # №8
# def add_right(a, b):
#     """a sonini o'ng tomoniga b sonini birlashtirib, natijani chop etadi."""
#     asd = str(a)
#     asd1 = str(b)
#     asdf = asd + asd1
#     print(asdf)
# add_right(123, 45)
#
# # №9
# def add_right(a, b):
#     """a sonini chap tomoniga b sonini birlashtirib, natijani chop etadi."""
#     asd1 = str(b)
#     asd = str(a)
#     asdf = asd1 + asd
#     print(asdf)
# add_right(123, 45)
#
# # №10
# def work_with_list(a):
#   """a ro'yxatidagi eng kichik sonni topadi,uni har bir elementga ko'paytiradi va yangi ro'yxatni chop etadi.
#   """
#   salom1 = min(a)
#   salom2 = [element * salom1 for element in a]
#   print(salom2)
#
# my_list = [2, 5, 1, 8, 3]
# work_with_list(my_list)
#
# # №11
# def salom123(salom):
#     return max(salom, key=salom.get)
# salom = {
#     "yanvar": 12000,
#     "fevral": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
# print(salom123(salom))
#
# # №12
# def min_max(numbers, max_num, min_num):
#     is_max = (max_num == max(numbers))
#     is_min = (min_num == min(numbers))
#     return is_max, is_min
# min_max(2, 3, 4, )