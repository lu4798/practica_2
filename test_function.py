from PruebaListas import function
import pytest

def test_argument_not_string():
    with pytest.raises(TypeError):
        function(5)

def test_two_same_words():
    assert function("hola hola")==[["hola", 2]]

def test_with_numbers():
    assert function("ho1a ho1a 5 5 7")==[["ho1a", 2],["5",2],["7",1]]

def test_stop_words():
    assert function("de")==[]

def test_two_equal_words_and_stopwords():
    assert function("hola de hola")==[["hola", 2]]

def test_two_equal_words_and_two_stopwords():
    assert function("hola de a hola") == [["hola", 2]]

def test_two_pairs_of_equal_words():
    assert function("hola adios adios hola")==[["hola", 2],["adios", 2]]

def test_two_words_capitalize_difference():
    assert function("HoLa hola")==[["hola", 2]]

def test_not_letter_simbols():
    assert function(". ,-´")==[]

def test_all_different_words_with_stopwords():
    assert function("hola adios que tal como va")==[["hola",1],["adios",1],["tal",1]]

def test_english_stopwords():
    assert function("The rain is in the su'n Sun thE Rain RAIN the In")==[["rain",3],["sun",2]]

def test_arabic_stopwords():
    assert function("عليه منزل منزل ذلك ذلك منزل ايضا كلب")==[["منزل",3],["كلب",1]]

def test_bulgarian_stopwords():
    assert function("къде тогава котка всяка котка куче това ")==[["котка",2],["куче",1]]

def test_czech_stopwords():
    assert function("pokuD déšť Déšť naproti kočka")==[["déšť",2],["pokud",1],["kočka", 1]]

def test_all_different_words_with_stopwords_from_different_languages():
    assert function("hola adios que tal como va naproti това عليه")==[["hola",1],["adios",1],["tal",1]]


