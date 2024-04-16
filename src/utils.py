def get_data_for_tables(data_json):
    """Извлекаем данные по ключам, помещаем в словарь словарей для каждой таблицы"""
    data = {'employers': [], 'vacancies': []}
    for employee in data_json:
        data['employers'].append([employee.get('employer').get('name'),
                                  employee.get('employer').get('alternate_url')])

        if employee.get('salary'):
            salary_from = employee.get('salary').get('from')
            salary_to = employee.get('salary').get('to')
        else:
            salary_from = salary_to = 0
        data['vacancies'].append([employee.get('employer').get('name'),
                                  employee.get('name'),
                                  salary_from,
                                  salary_to,
                                  employee.get('area').get('name'),
                                  employee.get('published_at'),
                                  employee.get('alternate_url')])
    return data
