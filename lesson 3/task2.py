name1 = str(input("Name"))
surname1 = str(input("Surname"))
year1 = str(int(input("Year")))
city1 = str(input("city"))
email1 = str(input("email"))
phone1 = str(input("Phone number"))
def personal_info(name, surname, year, city, email, phone):
    return ' '.join([
        "name: ", name,
        "surname: ", surname,
        "year: ", year,
        "city: ", city,
        "email: ", email,
        "phone: ", phone,
    ])
print(personal_info(name=name1, surname=surname1, year=year1, city=city1, email=email1, phone=phone1))