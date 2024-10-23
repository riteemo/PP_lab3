from re import findall, fullmatch


regexp = r"\b(\w+)\1\b"

def word_is_tandem(word: str) -> bool:
    return fullmatch(regexp, word) is not None

def text_has_tandem_words(text: str) -> list[str]:
    return list(map(lambda x: x + x, findall(regexp, text)))
