SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


CREATE TABLE employers
(
    company_id   SERIAL PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    url_company  TEXT
);

CREATE TABLE vacancies
(
    vacancy_id   SERIAL PRIMARY KEY,
    company_id   INT REFERENCES employers (company_id),
    vacancy_name VARCHAR(150) NOT NULL,
    city_name    VARCHAR(100),
    publish_date DATE,
    company_name VARCHAR(150) NOT NULL,
    salary_from  INTEGER,
    salary_to    INTEGER,
    url_vacancy  TEXT
);