from collections import Counter
def wordCount():
        with open("/Users/jeremyfoxx/workspace/github.com/mobius29er/bookbot/books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            print(len(words))

def characterCount():
        with open("/Users/jeremyfoxx/workspace/github.com/mobius29er/bookbot/books/frankenstein.txt") as f:
            count_contents = f.read()
            lowered_contents = count_contents.lower()
            characters = Counter(lowered_contents)
            print("--- Begin report of books/frankenstein.txt ---")
            for character in sorted(characters):
                if character.isalpha():
                    print(f"The '{character}' was found {characters[character]} times")
            print("--- End report ---")

wordCount()
characterCount()