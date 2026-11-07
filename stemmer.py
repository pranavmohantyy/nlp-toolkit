def porter_stem(word):
    suffixes = ['ing', 'ed', 'ness', 'ly', 's', 'es']
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

