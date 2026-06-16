from flask import render_template, redirect, url_for, session

from app.routes.main_bp import main_bp
from app.routes.helpers import get_current_user, get_sidebar_riwayat

# === ROUTE INDEX === #
@main_bp.route("/")
def index():

    # === CEK LOGIN === #
    if session.get("user_id"):
        return redirect(url_for("main.beranda"))

    # === REDIRECT LOGIN === #
    return redirect(url_for("auth.login"))


# === ROUTE BERANDA === #
@main_bp.route("/beranda")
def beranda():

    # === CEK LOGIN === #
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))
    user = get_current_user()
    if not user:
        session.clear()
        return redirect(url_for("auth.login"))

    # === DATA AWAL === #
    sidebar_riwayat = get_sidebar_riwayat(user.id)

    # === RENDER PAGE === #
    return render_template(
        "pages/beranda.html",
        user=user,
        username=user.username,
        full_name=user.full_name,
        sidebar_riwayat=sidebar_riwayat
    )