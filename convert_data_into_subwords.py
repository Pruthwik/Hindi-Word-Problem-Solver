"""Create subword data for any language."""
from bpemb import BPEmb
from sys import argv
from re import search


number_pattern = '\d*[,\/\.]?\d+'
hindi_subword_model = BPEmb(lang='hi', dim=300, vs=200000)


def find_number_in_text(text):
    """Find numbers in the text."""
    return search(number_pattern, text)


def convert_numbers_into_special_tokens(text):
    """Convert actual numbers into special tokens."""
    index = 0
    updated_tokens = list()
    dict_special_actual_nums = dict()
    for token in text.split():
        if find_number_in_text(token):
            updated_tokens.append(chr(ord('p') + index))
            dict_special_actual_nums[chr(ord('p') + index)] = token
            index += 1
        else:
            updated_tokens.append(token)
    return ' '.join(updated_tokens), dict_special_actual_nums


def convert_text_into_subwords(text):
    """Convert lines into subwords using subword model, we will convert numbers into single symbol literals like p, q, r, and so on."""
    text, dict_special_actual_nums = convert_numbers_into_special_tokens(text)
    subwords_in_text = hindi_subword_model.encode(text)
    return ' '.join(subwords_in_text), dict_special_actual_nums


def main():
    """Pass arguments and call functions here."""
    pass


if __name__ == '__main__':
    main()
