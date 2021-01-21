from __future__ import print_function
from alphabet_soup import create_message


message = 'raven pack'
soup_letters_false = ['s', 'z', 'r', 'p', 'l', 'o', 'q', 'u', 'n', 'c', 'l', 'o', 'c', 't', 'a', ]  # FALSE

soup_letters = ['w', 'r', 'a', 'w', 's', 'r', 'e', 'i', 'v', 'p', 'd', 'o', 'i', 'j', 'g', 't', 'o', 'm', 'o', 'r',
                'r', 'c', 'h', 'm', 'o', 'r', 'x', 'i', 'n', 'g', 'z', 'a', 'l', 'k']  # TRUE


def test_alphabet_soup():
    """ Test for True cases """
    assert create_message(message, soup_letters)


def test_alphabet_soup_false():
    """Test for False cases"""
    assert create_message(message, soup_letters_false) == False
