def index():
    with open('templates/home.html') as file:
        return file.read()


def blog():
    with open('templates/blog.html') as file:
        return file.read()


def error():
    with open('templates/error/error.html') as file:
        return file.read()