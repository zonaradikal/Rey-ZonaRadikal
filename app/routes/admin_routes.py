from flask import Blueprint, render_template, redirect, url_for, flash

from app.extensions import db
from app.models import User, UserSession
from app.utils import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# === HALAMAN ADMIN === #
@admin_bp.route("/")
@admin_required
def index():

    total_users = User.query.count()
    pending_count = User.query.filter_by(status="pending").count()
    active_count = User.query.filter_by(status="active").count()
    rejected_count = User.query.filter_by(status="rejected").count()
    admin_count = User.query.filter_by(role="admin").count()

    pending_users = User.query.filter_by(status="pending").order_by(User.created_at.desc()).all()
    all_users = User.query.order_by(User.created_at.desc()).all()
    sessions = UserSession.query.order_by(UserSession.login_at.desc()).limit(50).all()

    return render_template(
        "pages/admin.html",
        total_users=total_users,
        pending_count=pending_count,
        active_count=active_count,
        rejected_count=rejected_count,
        admin_count=admin_count,
        pending_users=pending_users,
        all_users=all_users,
        sessions=sessions
    )


# === UBAH STATUS USER === #
@admin_bp.route("/status/<int:user_id>/<status>", methods=["POST"])
@admin_required
def change_status(user_id, status):

    user = User.query.get_or_404(user_id)
    if user.role == "admin":
        flash("Status admin tidak dapat diubah.", "warning")
        return redirect(url_for("admin.index"))

    if status not in ["active", "rejected"]:
        flash("Status tidak valid.", "error")
        return redirect(url_for("admin.index"))

    user.status = status
    db.session.commit()

    flash(
        f"Status '{user.username}' berhasil diubah menjadi {status}.",
        "success"
    )

    return redirect(url_for("admin.index"))