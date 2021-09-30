import socket
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    my_host = "127.0.0.1"
    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind((my_host, 0))
    free_socket.listen(5)
    free_port = free_socket.getsockname()[1]
    free_socket.close()

    # BLUEPRINTS
    from users.views import users_blueprint
    from blog.views import blog_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(blog_blueprint)

    app.run(host=my_host, port=free_port, debug=True)



@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')
