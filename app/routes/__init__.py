from app.routes.main_bp import main_bp


def register_main_routes(app):
    from app.routes import beranda_routes
    from app.routes import aktivitas_routes
    from app.routes import paparan_routes
    from app.routes import daerah_routes
    from app.routes import riwayat_routes
    from app.routes import panduan_routes
    from app.routes import bantuan_routes

    app.register_blueprint(main_bp)