from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from datetime import timedelta

from app.extensions import db
from app.models import User, UserSession
from app.models.user import waktu_indonesia
from app.routes.helpers import normalize_datetime
from app.utils import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# === HALAMAN ADMIN === #
@admin_bp.route("/")
@admin_required
def index():

    sekarang = waktu_indonesia()
    batas = sekarang - timedelta(days=30)
    user_filter = request.args.get("user_filter", "all")
    user_page = request.args.get("user_page", 1, type=int)
    session_filter = request.args.get("session_filter", "all")
    session_period = request.args.get("session_period", "30")
    session_page = request.args.get("session_page", 1, type=int)

    total_users = User.query.count()
    pending_count = User.query.filter_by(status="pending").count()
    active_count = User.query.filter_by(status="active").count()
    session_active_count = UserSession.query.filter(
        UserSession.logout_at.is_(None),
        UserSession.last_activity_at >= sekarang - timedelta(hours=3)
    ).count()

    
    all_users_query = User.query
    
    if user_filter == "pending":
        all_users_query = all_users_query.filter_by(status="pending")
    elif user_filter == "active":
        all_users_query = all_users_query.filter_by(status="active")
    elif user_filter == "rejected":
        all_users_query = all_users_query.filter_by(status="rejected")
    elif user_filter == "admin":
        all_users_query = all_users_query.filter_by(role="admin")
    elif user_filter == "user":
        all_users_query = all_users_query.filter_by(role="user")
    
    all_users = all_users_query.order_by(User.created_at.desc()).paginate(
        page=user_page, per_page=10, error_out=False)
    
    
    sessions_query = UserSession.query
    
    if session_period == "1":
        batas = sekarang - timedelta(days=1)
    elif session_period == "7":
        batas = sekarang - timedelta(days=7)
    else:
        batas = sekarang - timedelta(days=30)
    sessions_query = sessions_query.filter(UserSession.login_at >= batas)

    if session_filter == "active":
        sessions_query = sessions_query.filter(
            UserSession.logout_at.is_(None),
            UserSession.last_activity_at >= sekarang - timedelta(hours=3)
        )
    elif session_filter == "logout":
        sessions_query = sessions_query.filter(
            UserSession.logout_at.is_not(None)
        )
    
    sessions = sessions_query.order_by(UserSession.login_at.desc()).paginate(
        page=session_page, per_page=10, error_out=False)
    
    for session_item in sessions.items:
        sekarang_normal = normalize_datetime(sekarang)
        last_activity = normalize_datetime(session_item.last_activity_at)

        session_item.is_active_now = (
            session_item.logout_at is None and
            last_activity is not None and
            (sekarang_normal - last_activity).total_seconds() <= 10800
        )


    return render_template(
        "pages/admin.html",
        user_filter=user_filter,
        user_page=user_page,
        session_filter=session_filter,
        session_period=session_period,
        session_page=session_page,

        total_users=total_users,
        pending_count=pending_count,
        active_count=active_count,
        session_active_count=session_active_count,

        all_users=all_users,
        sessions=sessions
    )


# === DATA STATISTIK === #
@admin_bp.route("/stats")
@admin_required
def stats():

    sekarang = waktu_indonesia()

    pending_count = User.query.filter_by(
        status="pending"
    ).count()

    session_active_count = UserSession.query.filter(
        UserSession.logout_at.is_(None),
        UserSession.last_activity_at >= sekarang - timedelta(hours=3)
    ).count()

    return jsonify({
        "pending_count": pending_count,
        "session_active_count": session_active_count
    })


# === CHECK UPDATE === #
@admin_bp.route("/check-updates")
@admin_required
def check_updates():

    latest_user = User.query.order_by(
        User.created_at.desc()
    ).first()

    latest_session = UserSession.query.order_by(
        UserSession.login_at.desc()
    ).first()

    return jsonify({
        "latest_user": (
            latest_user.created_at.timestamp()
            if latest_user else 0
        ),
        "latest_session": (
            latest_session.login_at.timestamp()
            if latest_session else 0
        )
    })


# === PENDING USER COUNT === #
@admin_bp.route("/pending-count")
@admin_required
def pending_count():

    count = User.query.filter_by(
        status="pending"
    ).count()
    return jsonify({
        "count": count
    })


# === UBAH STATUS USER === #
@admin_bp.route("/status/<int:user_id>/<status>", methods=["POST"])
@admin_required
def change_status(user_id, status):

    user = User.query.get_or_404(user_id)
    if user.role == "admin" and user.status == "active":
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