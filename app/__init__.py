from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # 注册蓝图
    from .main import main
    app.register_blueprint(main)
    from .weekly import weekly
    app.register_blueprint(weekly)

    return app
