from stats import word_count, char_count, sort_by_value
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    
    return contents

def main(path):
    get_content = get_book_text(path)
    
    return get_content

def print_report(content_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {content_path}")
    print("----------- Word Count ----------")
    wc = word_count(main(content_path))
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    char_dictionary = sort_by_value(char_count(main(content_path)))
    for key, value in char_dictionary:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

try:
    content_path = sys.argv[1]
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
print_report(content_path)