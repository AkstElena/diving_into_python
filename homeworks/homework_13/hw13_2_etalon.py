class InvalidTextError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid text: {self.text}. Text should be a non-empty string.'


class InvalidNumberError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number: {self.number}. Number should be a positive integer or float.'


class Archive:
    """Документация для класса Архив"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        if not isinstance(text, str) or len(text.strip()) == 0:
            raise InvalidTextError(text)
        if not (isinstance(number, int) or isinstance(number, float)) or number <= 0:
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

if __name__ == '__main__':
    # archive_instance = Archive("Sample text", 42.5)
    # print(archive_instance)
    #
    # invalid_archive_instance = Archive("", -5)
    # print(invalid_archive_instance)

    invalid_archive_instance = Archive("Sample text", -5)
    print(invalid_archive_instance)
