import requests

Developer_Key = 'HeUEb1_7oeFxNqtuAuv5SIKHrqZJXu60'
Paste_Bin_API_URL = 'https://pastebin.com/api/api_post.php'



def main():
    url = post_new_paste("This is a title.", "This is the body.", '1H', True)
    print(f'New paste URL: {url}')


def post_new_paste(title, body_text, expiration='10', listed=False):
    """Posts a new public paste to PasteBin

    Args:
        title (str): Paste Title
        body_text (str): Paste Body Type
        expiration (str, optional): Expration Date of Paste (N = Never, 10M = Minutes, 1H, 1S, 1W, 2W, 1M, 6M, 1Y). Default
        listed (bool, optional): Whether paste is publicly listed (True) or not (False). Defaults to False.

    Returns:
        _type_: _description_
    """
    # Setup the parameters for the request.

    paste_params = {
        'api_dev_key': Developer_Key,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date':  expiration,
        'api_paste_private': 0 if listed else 1
    }

    # Send the POST request to the PasteBin API.
    print('Sending POST request to PastBin API...', end='')
    resp_msg = requests.post(Paste_Bin_API_URL, data=paste_params)

    if resp_msg.ok:
        print('Sucess')
        return resp_msg.text
    else:
        print('Failed')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')
  

if __name__ == '__main__':
    main()