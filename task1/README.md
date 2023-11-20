# Task1 pytest

На сайте https://en.wikipedia.org/wiki/Programming_languages_used_in_most _popular_websites 
есть таблица «Programming languages used in most popular websites» 
Необходимо реализовать параметризованный тест, проверяющий, что в этой таблице нет строк, у которых значение в столбце «Popularity(unique visitors per month)» меньше передаваемого в качестве параметра в тест значения. 
Если такие строки в таблице есть, тест выводит сообщение об ошибке, перечисляя строки с ошибками в виде, пример: 
“Wikipedia (Frontend:JavaScript|Backend:PHP) has 475 000 000 unique visitors per month. (Expected more than 500 000 000)”
Тест должен запускаться для значений: [10^7, 1.5 * 10^7, 5 * 10^7, 10^8, 5 * 10^8, 10^9, 1.5 * 10^9] 
При реализации теста необходимо учитывать, что данные из этой таблицы могут понадобиться и в других тестах. Будет плюсом реализовать хранение данных из таблицы в виде датаклассов. 


## Precondition
To install dependencies, run the following command:
python version: 3.9.8
```bash
pip install -r requirements.txt

if the selenium has not been set ->  pip install selenium {must have the latest version of Selenium webdriver}


## To run tests use

pytest -s -v
