
chat_id = 881200429
token = "6486146762:AAH0l7IvOLHfWvEw3JYtybiNbov-e3ai0Es"
PATH_DATABASE = "database.db"


def get_admins():
    admin = chat_id
    if admin >= 1:
        admin = [admin]
    else:
        admin = []

    admin = list(map(int, admin))

    return admin
