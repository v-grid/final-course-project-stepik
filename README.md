# final-course-project-stepik
Final course project stepik 

Команда запуска теста "pytest -v --tb=line --language=en test_main_page.py"
base_page.py - базовая страница, от которой унаследованы все остальные классы. В ней мы описаны вспомогательные методы для работы с драйвером.

Методы:
__init__ - метод, который вызывается, когда мы создаем объект (в качестве параметров мы передаем экземпляр драйвера и url адрес).
open - метод открывает нужную страницу в браузере, используя метод get().

