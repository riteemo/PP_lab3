from typing import List

from regexp import find_tandem_words_in_text
from requests import get
from requests.exceptions import MissingSchema


# Класс для поиска регулярных выражений
class RegexpFinder:
    def __init__(self, regexp: str):
        self.regexp = regexp

    def find_in_string(self, input_txt: str) -> list[str]:
        return find_tandem_words_in_text(input_txt, self.regexp)

    def find_on_page(self, url: str) -> list[str] | str:
        try:
            res = get(url).text
            return find_tandem_words_in_text(res, self.regexp)
        except MissingSchema:
            return "Wrong URL"

    def find_in_file(self, filename: str) -> list[str] | str:
        try:
            with open(filename) as file:
                text = file.read()
                return find_tandem_words_in_text(text, self.regexp)
        except (FileNotFoundError, OSError):
            return "File not found"
