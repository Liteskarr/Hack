import json


class Load:
    """ Интерфейс взаимодействия с файловой системой. """
    @staticmethod
    def load_json(filepath: str) -> dict:
        """ Загружает json из файла. """
        with open(filepath) as file:
            json_str = ''
            for s in file:
                json_str += s
            result = json.loads(json_str)
            return result

    @staticmethod
    def load_file(filepath: str) -> list:
        """ Загружает фойл. """
        with open(filepath) as file:
            return []
