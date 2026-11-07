def word_tokenize(text):
    if not text:
        return []
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text.split()