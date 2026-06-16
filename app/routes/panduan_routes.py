from flask import render_template, redirect, url_for, session

from app.models import Panduan, FAQ
from app.routes.main_bp import main_bp
from app.routes.helpers import get_current_user, get_sidebar_riwayat


# === ROUTE PANDUAN === #
@main_bp.route("/panduan")
def panduan():

    # === CEK LOGIN === #
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))
    user = get_current_user()
    if not user:
        session.clear()
        return redirect(url_for("auth.login"))

    # === DATA AWAL === #
    daftar_panduan = Panduan.query.filter_by(is_active=True).order_by(
        Panduan.kategori.asc(), Panduan.urutan.asc()
    ).all()
    daftar_faq = FAQ.query.filter_by(is_active=True).order_by(
        FAQ.kategori.asc(), FAQ.urutan.asc()
    ).all()

    sidebar_riwayat = get_sidebar_riwayat(user.id)


    # === RENDER PAGE === #
    return render_template(
        "pages/panduan.html",
        user=user,
        username=user.username,
        full_name=user.full_name,
        daftar_panduan=daftar_panduan,
        daftar_faq=daftar_faq,
        sidebar_riwayat=sidebar_riwayat,
    )