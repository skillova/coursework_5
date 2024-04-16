import os
from pprint import pprint

from src.parsing_cfg import get_cfg
from src.create_db import CreateDB
from parser_HH import Parser
from utils import get_data_for_tables

if __name__ == '__main__':
    # Объявляем переменные для базы данных
    filename_ini = "cfg.ini"
    section = "postgresql"
    db_name = 'my_db'
    file_ini = os.path.join(os.path.dirname(__file__), filename_ini)
    db_param = get_cfg(file_ini, section)

    # Объявляем переменные для фарсера HH.ru
    url = 'https://api.hh.ru/vacancies'
    employers = [1473866, 78638, 493586, 4181, 85339]
    page = 0
    per_page = 1

    # Парсим HH.ru, получаем json
    obj_json = Parser(url, employers, page, per_page=100)
    all_data_employers = obj_json.get_vacancies()

    # Создаем базу 'my_db' данных и таблицы 'employers', 'vacancies'
    CreateDB(db_param, db_name).create_db()
    db_param.update({'dbname': f'{db_name}'})
    CreateDB(db_param, db_name).create_table_db_from_script('script_create_db.sql')

    # Наполняем таблицы базы данных
    CreateDB(db_param, db_name).insert_in_tables(all_data_employers)




