import requests



class Parser:
    """Класс для работы с API hh.ru"""

    def __init__(self, url: str, employer: str, page: int = 0, per_page: int = 10) -> None:
        """Инициализация класса"""
        self.__url: str = url
        self.employer_id: list = employer
        self.page: int = int(page)
        self.per_page: int = int(per_page)

    def get_params(self, *args) -> dict:
        """
        Создание параметров для запроса к сервису
        :return: возвращает словарь ключей
        """
        params: dict = {
            "employer_id": self.employer_id,
            "page": self.page,
            "per_page": self.per_page
        }
        return params

    def get_vacancies(self) -> list:
        """
        Метод для получения вакансий
        :param params: параметры поиска вакансий
        :return: список словарей найденных вакансий
        """
        # Объявляем список для добавления найденных вакансий
        vacancies_list: list = []
        # Парсим 20 страниц циклом for (20 стр х 100 вакансий = 2000 вакансий),
        # возвращаем найденные вакансии в формате json по ключу <"items">,
        # после каждой итерации добавляем вакансии в список vacancies_list,
        # метод возвращает список вакансий <[{vacancy}, {vacancy}, {vacancy}...]>
        for page in range(0, 20):
            self.page = page
            params = self.get_params(self.page)
            response = requests.get(url=self.__url, params=params)
            result: list = response.json()['items']
            vacancies_list.extend(result)
        return vacancies_list