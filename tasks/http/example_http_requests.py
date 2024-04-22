import requests

response = requests.get('https://example.com')
print(response.status_code)
print(response.reason)
print(response.headers)
print(response.headers['Content-Type'])
