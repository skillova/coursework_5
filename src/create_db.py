import psycopg2


class CreateDB:
    def __init__(self, params, db_name):
        self.db_name = db_name
        with psycopg2.connect(**params) as connection:
            self.cursor = connection.cursor()
            connection.autocommit = True

    def create_db(self):
        self.cursor.execute(f'DROP DATABASE IF EXISTS {self.db_name}')
        sql = f"CREATE DATABASE {self.db_name}"
        self.cursor.execute(sql)

    def create_table_db_from_script(self, script_file):
        with open(script_file, 'r') as file:
            self.cursor.execute(file.read())

    def insert_in_tables(self, data_json):
        for item in data_json:
            line_employers = [item.get('employer').get('name'),
                              item.get('employer').get('alternate_url')]
            self.cursor.execute(
                '''INSERT INTO employers(company_name, url_company) VALUES (%s, %s) RETURNING company_id''',
                line_employers)

            company_id = self.cursor.fetchone()[0]

            if item.get('salary'):
                salary_from = item.get('salary').get('from')
                salary_to = item.get('salary').get('to')
            else:
                salary_from = salary_to = 0
            line_vacancies = [company_id,
                              item.get('name'),
                              item.get('area').get('name'),
                              item.get('published_at'),
                              item.get('employer').get('name'),
                              salary_from,
                              salary_to,
                              item.get('alternate_url')]
            self.cursor.execute(
                '''INSERT INTO vacancies(company_id, vacancy_name, city_name, 
                publish_date, company_name, salary_from, 
                salary_to, url_vacancy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING company_id''',
                line_vacancies)
