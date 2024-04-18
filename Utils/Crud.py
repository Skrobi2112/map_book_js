

def read(users: list[dict]) ->None:
    for user in users[1:]:
         print(f"twój znajomy {user['name']}: {user['surname']} opublikował: {user['posts']}")

read(users)