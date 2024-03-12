import logging

logging.basicConfig(filename='Log/log_2.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'аргументы функции: {args}, результат функции: {result}')
        return result

    return wrapper


@decor
def power(x, y):
    return x ** y


print(power(2, 10))
print(power(5, 3))
