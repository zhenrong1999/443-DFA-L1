from src.preprocessingJson import isEnglishCharacters


def test_isEnglishCharacters_1():
    assert(isEnglishCharacters('Hello World') is True)


def test_isEnglishCharacters_2():
    assert(isEnglishCharacters('HelloWorld?') is False)


def test_isEnglishCharacters_3():
    assert(isEnglishCharacters('士大夫') is False)
