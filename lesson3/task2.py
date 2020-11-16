# Task 2 User data output
def user_data(**kwargs):
    return kwargs

print(user_data(
    name=input('Name: '), surname=input('Surname: '), birthday=input('Birthday: '),
    city=input('City: '), email=input('Email: '), phone=input('Phone: '),
))