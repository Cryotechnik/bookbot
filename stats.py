def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count