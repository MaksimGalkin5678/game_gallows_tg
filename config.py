chat_id = 881200429 #Id админа 
token = "6486146762:AAH0l7IvOLHfWvEw3JYtybiNbov-e3ai0Es" #токен бота
PATH_DATABASE = "database.db" #База данных
#Для получения админки
def get_admins():
    admin = chat_id
    if admin >= 1:
        admin = [admin]
    else:
        admin = []
    admin = list(map(int, admin))
    return admin
