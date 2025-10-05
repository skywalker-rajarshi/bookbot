def word_count(content):
    wc = len(content.split())
    
    return wc

def char_count(content):
    char_dictionary = {}
    for ch in content:
        char_dictionary[ch.lower()] = char_dictionary.get(ch.lower(), 0) + 1
    
    return char_dictionary

def sort_by_value(dictionary):
    return sorted(dictionary.items(), key=lambda tuple:tuple[1], reverse=True)
