import requests
s=requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
r=s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)