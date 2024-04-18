from Utils.crud import read


users: list[dict] = [
    {"name": "Jakub", "surname": "Skrobała", "posts": 20},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 23},
    {"name": "Tymoteusz", "surname": "Miszczak", "posts": 11},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 66},
]
if __name__ == "__main__":

print(f"Witaj {users[0]['name']}!")
while True:
    print("menu:")
    print("0. Zakończ program")
    print("1.Pokaż co u znajomych: ")
    menu_option:str=input("Wybierz dostępną funkcję z menu: ")
    if menu_option == "0":
        break
    if menu_option == "1":
        read(users)