import doctest


def reverse_words(text):
    """
    1. тільки букви (одне слово)
    >>> reverse_words("hello")
    'olleh'

    2. тільки букви (два слова)
    >>> reverse_words("abcd efgh")
    'dcba hgfe'

    3. порожня строка
    >>> reverse_words("")
    ''

    4. букви і небукви (два слова)
    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'

    5. число
    >>> reverse_words(123)
    Аргумент має бути string
    """

    if not isinstance(text, str):
        print("Аргумент має бути string")
        return None

    reversed_text = ""

    for word in text.split(' '):
        word_chars = list(word)
        left_idx = 0
        right_idx = len(word_chars) - 1

        while left_idx < right_idx:
            if not word_chars[left_idx].isalpha():
                left_idx += 1
            elif not word_chars[right_idx].isalpha():
                right_idx -= 1
            else:
                word_chars[left_idx], word_chars[right_idx] = word_chars[right_idx], word_chars[left_idx]
                left_idx += 1
                right_idx -= 1

        reversed_text += "".join(word_chars) + " "

    return reversed_text[:-1]


def run():
    in_str = input("Введіть рядок\n")
    result = reverse_words(in_str)
    if result is not None:
        print(result)


if __name__ == '__main__':
    doctest.testmod(verbose=True)