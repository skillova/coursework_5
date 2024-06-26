import psycopg2


class DBManager:
    def __init__(self, db_params):
        self.connect = psycopg2.connect(**db_params)
        self.cursor = self.connect.cursor()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        sql = '''SELECT company_name, COUNT(company_name) FROM vacancies
GROUP BY vacancies.company_name'''
        with self.connect:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                return e

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию."""
        sql = '''SELECT company_name, vacancy_name, salary_from, salary_to, url_vacancy FROM vacancies'''
        with self.connect:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                return e

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        sql = '''SELECT AVG(salary_from) AS "Средняя зарплата ОТ", AVG(salary_to) AS "Средняя зарплата ДО" 
        FROM vacancies'''
        with self.connect:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                return e

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        sql = '''SELECT * FROM vacancies WHERE salary_from >(SELECT AVG(salary_from)
        FROM vacancies) AND salary_to > (SELECT AVG(salary_to) FROM vacancies)
        ORDER BY vacancy_id'''
        with self.connect:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                return e

    def get_vacancies_with_keyword(self, keyword_name):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        sql = f"SELECT * FROM vacancies WHERE vacancy_name iLIKE '%{keyword_name}%'"
        with self.connect:
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                return e
