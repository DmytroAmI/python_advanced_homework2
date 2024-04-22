from urllib import request

response = request.urlopen('https://example.com/')
print(response)

print(response.status)
print(response.getcode())

print(response.msg)
print(response.reason)

print(response.headers)
print(response.getheaders())

print(response.headers['Content-Type'])
print(response.headers.get('content-type'))
print(response.getheader('content-type'))
