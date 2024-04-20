def interface(obj, answer):
    """Вернуть запрашиваемую информации методами dbmanager"""
    if answer == '1':
        result = (obj.get_companies_and_vacancies_count())
    if answer == '2':
        result = (obj.get_all_vacancies())
    if answer == '3':
        result = (obj.get_avg_salary())
    if answer == '4':
        result = (obj.get_vacancies_with_higher_salary())
    if answer == '5':
        keyword = input('Введите ключевое слово для поиска\n')
        result = (obj.get_vacancies_with_keyword(keyword))

    return result
