def cvs_export(id: int, date: float, title: str, note: str) -> None:
    """
    Записывает в файл введённую заметку
    :param id: идентификатор заметки
    :param date: дата создания или редактирования заметки
    :param title: заголовок заметки
    :param note: текст заметки
    :return: None
    """
    with open('DataBase/csvDB.csv', 'a+', encoding='utf-8') as file:
        file.write('{};{};{};{}\n'.format(id, date, title.upper(), note))
