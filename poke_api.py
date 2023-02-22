import requests

poke_api_URL = 'https://pokeapi.co/'


def main():  
    pokemon = search_for_pokemon()
    print(pokemon) 
    
        
def search_for_pokemon(search_term):

    poke_Search_URL = f'https://pokeapi.co/api/v2/pokemon/{search_term}'


    header_params = {
        'Accept': 'application/json'
    }

    print(f'Getting information for {search_term}...',  end=' ')
    resp_msg = requests.get(poke_Search_URL, headers=header_params)
    

    if resp_msg.ok:
        print('Success')
        body_dict = resp_msg.json()
        poke_list = [p['ability']['name']for p in body_dict['abilities']]
        return poke_list

    else:
        print('Failed')
        print(f'{resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error: {resp_msg.text}')
    return None



if __name__ == '__main__':
    main()