def send_email(message, recipient,sender =  "university.help@gmail.com"):
    if (("@" and (".com" or".ru" or".net")) not in (recipient) or ("@" or (".ru" or ".com" or".net"))
            not in (sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com" :
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи','vasyok1337@gmail.com',
           "university.help@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           "university.help@gmail.com")
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', "university.help@gmail.com",
           "university.help@gmail.com")