import socket
from views import index, blog, error

URLS = {
    '/': index,
    '/blog': blog
}


def generate_body(status_code, url):
    if status_code == 405:
        return '<h1>405</h1><h3>Method not allowed</h3>'
        # return error()
    if status_code == 404:
        return '<h1>404</h1><h3>Not Found</h3>'
        # return error()
    return URLS[url]()


def generate_headers(method, url):
    if not method == 'GET':
        return 'HTTP/1.1 405 Method not allowed\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Not Found\n\n', 404
    return 'HTTP/1.1 200 OK\n\n', 200


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_response(request):
    method, url = parse_request(request)
    headers, status_code = generate_headers(method, url)
    body = generate_body(status_code, url)
    print((headers + body).encode())
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 7000))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024)
        request = request.decode('utf-8')
        print(address)
        print(request)

        response = generate_response(request)

        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()