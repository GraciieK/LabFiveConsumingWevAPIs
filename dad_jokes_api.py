import requests

Dad_Jokes_API_URL = 'https://icanhazdadjoke.com/'
Dad_Jokes_Search_URL = f'{Dad_Jokes_API_URL}/search'


def main():
    
    for joke in search_for_dad_jokes('cow'):
        print(joke)
    pass

def get_random_joke():
    """Gets a list of dad jokes that contains a serch term.

    Args:
        search_term (str): Search Term.

    Returns:
        list: List of jokes contaning the search term.
    """

    # Setup the header parameters.
    header_params = {
        'Accept': 'application/json'
    }

    print('Getting a random dad joke...', end='')
 
    resp_msg = requests.get(Dad_Jokes_API_URL, headers=header_params)

    body_dict = resp_msg.json()
    # Check whether the GET request was successful.

    if resp_msg.status_code == requests.codes.ok:
        print('Sucess')
        return body_dict['joke']
    else:
        print('Failed')
        print(f'{resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error:')
        
def search_for_dad_jokes(search_term, page=1, limit=20):

    header_params = {
        'Accept': 'application/json'
    }

    search_params = {
        'page': page,
        'limit': limit,
        'term': search_term
    }

    print(f'Searching for dad jokes contaning {search_term}...',  end=' ')
    resp_msg = requests.get(Dad_Jokes_Search_URL, params=search_params, headers=header_params)
    body_dict = resp_msg.json()

    if resp_msg.ok:
        print('Sucess')
        jokes_list = body_dict['results']

        jokes = []
        for j in jokes_list:
            jokes.append(j['joke'])
        return jokes

    else:
        print('Failed')
        print(f'{resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error: {resp_msg.text}')
    return None



if __name__ == '__main__':
    main()