import requests


def find_avatar(user):
    """
    Find a user's avatar on github

    :param user: str with a user's name on github
    :return: str with avatar's link
    """

    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(find_avatar('dubergonzoni'))
