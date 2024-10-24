from re import findall, fullmatch


regexp = r"\b(\w+)\1\b"

def word_is_tandem(word: str, regexp: str) -> bool:
    return fullmatch(regexp, word) is not None

def find_tandem_words_in_text(text: str, regexp: str) -> list[str]:
    return list(map(lambda x: x + x, findall(regexp, text)))
