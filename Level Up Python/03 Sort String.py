def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))

a = input("Enter a list:")
print(sort_words(a))