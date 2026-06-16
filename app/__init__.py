from flask import Flask
from app.config import Config
from app.extensions import db, migrate

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.admin_routes import admin_bp
    from app.routes.auth_routes import auth_bp
    from app.routes import register_main_routes
    from app.routes.helpers import update_session_activity

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    register_main_routes(app)

    @app.before_request
    def before_request():
        update_session_activity()

    return app