import socket


def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    parse_content = lines[empty_index+1:]
    return int(status_code), headers, parse_content


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_item = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_item)
print('----HTTP MESSAGE----')
print(content)
print('----END OF MESSAGE----')
sock.send(content.encode('utf-8'))
result = sock.recv(10024)
status_code1, headers1, parse_content1 = parse_http_response(result.decode('utf-8'))
print("Status Code:", status_code1)
print("Headers:", headers1)
print("Content:", parse_content1)
