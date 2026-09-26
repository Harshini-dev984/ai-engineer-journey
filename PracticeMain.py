import requests
try:
    response=requests.get(
        url="https://open.er-api.com/v6/latest/USD", timeout=5,
        params={
            'base_code': 'USD',
            'time_last_update_utc': 'Fri, 25 Sep 2026 00:02:31 +0000'
        }
    )
except requests.exceptions.ConnectionError:
    print('Error: could not connect to the API.')

try:
    data=response.json()
    print(response.text)
except(KeyError, ValueError):
    print("Error: unexpected response format from API.")