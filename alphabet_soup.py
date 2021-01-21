import re


def create_message(message_, bowl_letters):
    """ remove special characters, spaces and lowercase every letter """
    new_message = re.sub('[^A-Za-z0-9]+', '', message_).lower()
    return search_bowl(new_message, bowl_letters)


def search_bowl(letters, bowl):
    """ using recursion to search the bowl """
    if len(letters) == 0:
        return True

    if letters[0] not in bowl:
        return False
    else:
        bowl.index(letters[0])
        remaining = letters[1:]
        """ recalling the function by removing the already checked letters """
        return search_bowl(remaining, bowl)


if __name__ == '__main__':
    message = 'raven pack'
    # soup_letters = ['r', 'z', 'r', 'p', 'l', 'o', 'q', 'u', 'n', 'c', 'l', 'o', 'c', 't', 'a', ]  # FALSE

    soup_letters = ['w', 'r', 'a', 'w', 's', 'r', 'e', 'i', 'v', 'p', 'd', 'o', 'i', 'j', 'g', 't', 'o', 'm', 'o', 'r',
                    'r', 'c', 'h', 'm', 'o', 'r', 'x', 'i', 'n', 'g', 'z', 'a', 'l', 'k']  # TRUE

    # soup_letters = ['p'] # FALSE

    func = create_message(message, soup_letters)
    print(func)
