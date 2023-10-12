from config import get_admins
from sql import *
from main import bot

#Удаление отступов у текста (когда бот отправляет сообщение)
def ded(get_text: str):
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []
        for text in split_text:
            while text.startswith(" "):
                text = text[1:]
            save_text.append(text)
        get_text = "\n".join(save_text)
    return get_text

# Открытие своего профиля
def open_profile_user(user_id):
    get_user = get_userx(user_id=user_id)
    return ded(f"""
           <b>👻 Ваш профиль:</b>
           
           🏆 Твои баллы: <code>{get_user['user_balance']} очков</code>
           🤘 Угадано слов: <code>{get_user['user_win']}</code>
           ☠️ Проигрышей: <code>{get_user['user_loose']}</code>
           """)

