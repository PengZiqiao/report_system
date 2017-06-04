from flask_script import Manager
from app import create_app
import config
from livereload import Server

app = create_app(config.Development)
manager = Manager(app)


@manager.command
def dev():
    server = Server(app.wsgi_app)
    server.serve(open_url_delay=True)


if __name__ == '__main__':
    manager.run()
