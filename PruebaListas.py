import re
from stop_words import get_stop_words

def word_counter(array):
    acceptable_languages = ['arabic', 'bulgarian', 'catalan', 'czech', 'danish', 'dutch', 'english','finnish', 'french', 'german', 'hungarian', 'indonesian', 'italian',
                            'norwegian', 'polish', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish', 'ukrainian']

    if not isinstance(array,str):
        raise TypeError

    string_list_lowercase = []
    final_list = []
    list_aux = []
    forbidden_words = []

    for language in acceptable_languages:
        forbidden_words.append(get_stop_words(language))

    word_list = (array.lower()).split()

    for word in word_list:
        is_stopword = 0
        for forbidden in forbidden_words:

            if word in forbidden and is_stopword == 0:
                is_stopword = 1

        if is_stopword == 0:
            list_aux.append(word)

    for x in list_aux:
        reemplazo = re.sub("[^\w]", "", x)
        if reemplazo != '':
            string_list_lowercase.append(re.sub("[^\w]", "", x))

    while len(string_list_lowercase) > 0:
        current_word = string_list_lowercase[0]
        counter = string_list_lowercase.count(current_word)
        while current_word in string_list_lowercase:
            string_list_lowercase.remove(current_word)

        final_list.append([current_word,counter])
        
    return sorted(final_list ,key= lambda x : x[1],reverse=True)
