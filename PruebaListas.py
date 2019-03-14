import re

from stop_words import get_stop_words


def function(array):
    acceptable_languages = ['arabic', 'bulgarian', 'catalan', 'czech', 'danish', 'dutch', 'english', 'finnish',
                            'french', 'german', 'hungarian', 'indonesian', 'italian',
                            'norwegian', 'polish', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish',
                            'ukrainian']
    if not isinstance(array,str):
        raise TypeError

    forbidden_words = []
    for language in acceptable_languages:
        forbidden_words.append(get_stop_words(language))
    list_aux = re.sub("[^\w]", " ", array.lower()).split()
    string_list_lowercase = []
    final_list = []
    for x in list_aux:
        if x not in forbidden_words:
            string_list_lowercase.append(x)
    while len(string_list_lowercase) > 0:
        current_word = string_list_lowercase[0]
        counter = string_list_lowercase.count(current_word)
        while current_word in string_list_lowercase:
            string_list_lowercase.remove(current_word)
        final_list.append([current_word,counter])
    return sorted(final_list, key=lambda x: x[1],reverse=True)
