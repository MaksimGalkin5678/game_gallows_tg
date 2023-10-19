import sqlite3
from datetime import datetime
import time
from config import PATH_DATABASE

#очищаем текст от HTMl тэгов для корректного отображения пользователя в БД
def clear_html(get_text):
    if get_text is not None:
        if "<" in get_text: get_text = get_text.replace("<", "*")
        if ">" in get_text: get_text = get_text.replace(">", "*")
    return get_text

#Получение текущей даты
def get_date():
    this_date = datetime.today().replace(microsecond=0)
    this_date = this_date.strftime("%d.%m.%Y %H:%M:%S")
    return this_date

#Создание любого словаря (для пользователей, изменений слова)
def dict_factory(cursor, row):
    save_dict = {}
    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]
    return save_dict

#Форматирование запроса в БД без аргументов
def update_format(sql, parameters: dict):
    if "XXX" not in sql: sql += " XXX "
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)
    return sql, list(parameters.values())


#Форматирование запроса в БД с аргументами
def update_format_args(sql, parameters: dict):
    sql = f"{sql} WHERE "
    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])
    return sql, list(parameters.values())

########################################### ЗАПРОСЫ К БД ###########################################
#Добавление пользователя
def add_userx(user_id, user_login, user_name):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        con.execute("INSERT INTO storage_users "
                    "(user_id, user_login, user_name, user_balance, user_win, user_loose ,user_slovo,user_znach,user_wrong ,user_dlina,user_used,user_date) "
                    "VALUES (?, ?, ?, ?, ?, ? ,? , ?, ? ,?,?,?)",
                    [user_id, user_login, user_name, 0, 0, 0, None, None, 0,"➖"," ",get_date()])
        con.commit()

#Получение пользователя
def get_userx(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        sql, parameters = update_format_args(sql, kwargs)
        return con.execute(sql, parameters).fetchone()

#Редактирование пользователя
def update_userx(user_id, **kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = f"UPDATE storage_users SET"
        sql, parameters = update_format(sql, kwargs)
        parameters.append(user_id)
        con.execute(sql + "WHERE user_id = ?", parameters)
        con.commit()

#Изменение слова
def update_slovox(user_id, **kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = f"UPDATE storage_users SET"
        sql, parameters = update_format(sql, kwargs)
        parameters.append(user_id)
        con.execute(sql + "WHERE user_id = ?", parameters)
        con.commit()

#Создание всех таблиц для БД
def create_dbx():
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        #Создание БД с хранением данных пользователей
        if len(con.execute("PRAGMA table_info(storage_users)").fetchall()) == 13:
            print("Таблица юзеров найдена")
        else:
            con.execute("CREATE TABLE storage_users("
                        "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "user_id INTEGER,"
                        "user_login TEXT,"
                        "user_name TEXT,"
                        "user_balance INTEGER,"
                        "user_win INTEGER,"
                        "user_loose INTEGER,"
                        "user_slovo TEXT,"
                        "user_znach TEXT,"
                        "user_wrong INTEGER,"
                        "user_dlina TEXT,"
                        "user_used TEXT,"
                        "user_date TIMESTAMP")
            print("Таблица юзеров создана")
        con.commit()