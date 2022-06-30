# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

import inspect

def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass

def print_func_data(func):
    name = func.__name__
    args  = str(inspect.signature(func))
    print(f"Имя: {name}")
    # if the args are only ()
    if len(args) == 2:
        print("Аргументов нет")
    else:
        print(f"Аргументы: {args}")

print_func_data(find_registration_button_on_login_page)

for func in [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]:
    print_func_data(func)
