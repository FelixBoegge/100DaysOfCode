import collections


def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    char_frequency_for_letter = collections.Counter(letter_text)
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True
    return not char_frequency_for_letter


def is_letter_constructible_form_magazine_pythonic(letter_text: str, magazine_text: str) -> bool:
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

