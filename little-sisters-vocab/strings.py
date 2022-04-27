"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un'+word


def make_word_groups(vocab_words):
    return (' :: ' + vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word):
    return word[:-5] + "y" if word.endswith("iness") else word[:-4]


def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip(".") + "en"

