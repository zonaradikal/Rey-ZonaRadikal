from flask import (Blueprint, render_template, request, redirect, url_for, flash, session,)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import User, UserSession
from app.models.user import waktu_indonesia
from app.utils import (
    validate_full_name,
    validate_username,
    validate_password,
    validate_confirm_password,
)

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# === KONSTANTA === #
LOGIN_TEMPLATE = "auth/login.html"
REGISTER_TEMPLATE = "auth/register.html"

# === HELPER === #
def redirect_if_logged_in():
    if session.get("user_id"):
        return redirect(url_for("main.beranda"))
    return None

def flash_and_render(message, category, template):
    flash(message, category)
    return render_template(template)

def login_failed():
    return flash_and_render(
        "Username atau password salah. Silakan coba lagi.",
        "error",
        LOGIN_TEMPLATE
    )


# === ROUTE LOGIN === #
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    # === CEK LOGIN === #
    redirect_response = redirect_if_logged_in()
    if redirect_response:
        return redirect_response

    # === PROSES LOGIN === #
    if request.method == "POST":
        login_id = request.form.get("login_id", "").strip().lower()
        password = request.form.get("password", "")

        # === VALIDASI INPUT === #
        if not login_id or not password:
            return login_failed()

        # === CARI USER === #
        user = User.query.filter_by(username=login_id).first()

        # === VALIDASI USER === #
        if not user or not check_password_hash(user.password_hash, password):
            return login_failed()
        if user.status != "active":
            return flash_and_render(
                "Akun masih menunggu verifikasi admin.",
                "error",
                LOGIN_TEMPLATE
            )

        # === BUAT SESSION === #
        session.clear()
        session.permanent = True
        session["user_id"] = user.id
        session["username"] = user.username
        session["full_name"] = user.full_name
        session["role"] = user.role

        session_log = UserSession(
            user_id=user.id,
            ip_address=request.remote_addr,
            user_agent=request.headers.get("User-Agent")
        )

        db.session.add(session_log)
        db.session.commit()
        session["session_log_id"] = session_log.id
        return redirect(url_for("main.beranda"))

    # === RENDER PAGE === #
    return render_template(LOGIN_TEMPLATE)


# === ROUTE REGISTER === #
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    # === CEK LOGIN === #
    redirect_response = redirect_if_logged_in()
    if redirect_response:
        return redirect_response

    # === PROSES REGISTER === #
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        username = request.form.get("username", "").strip().lower()
        no_sertifikat_ppr = request.form.get("no_sertifikat_ppr", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        # === VALIDASI INPUT === #
        validation_errors = [
            validate_full_name(full_name),
            validate_username(username),
            validate_password(password),
            validate_confirm_password(password, confirm_password),
        ]
        for error in validation_errors:
            if error:
                return flash_and_render(error, "error", REGISTER_TEMPLATE)

        # === CEK DUPLIKAT USER === #
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            if existing_user.username == username:
                message = "Username sudah digunakan. Silakan gunakan username lain."

            return flash_and_render(message, "error", REGISTER_TEMPLATE)
        
        if no_sertifikat_ppr.lower() != "admin":
            existing_ppr = User.query.filter_by(no_sertifikat_ppr=no_sertifikat_ppr).first()
            if no_sertifikat_ppr and existing_ppr:
                
                return flash_and_render(
                    "Nomor Sertifikat PPR sudah digunakan.",
                    "error",
                    REGISTER_TEMPLATE
                )

        # === BUAT USER === #
        role = "admin" if no_sertifikat_ppr.lower() == "admin" else "user"
        new_user = User(
            full_name=full_name,
            username=username,
            no_sertifikat_ppr=no_sertifikat_ppr or None,
            password_hash=generate_password_hash(password),
            status="pending",
            role=role
        )

        try:
            # === SIMPAN USER === #
            db.session.add(new_user)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()

            return flash_and_render(
                "Data sudah digunakan oleh pengguna lain.",
                "error",
                REGISTER_TEMPLATE
            )

        except Exception:
            db.session.rollback()
            return flash_and_render(
                "Registrasi gagal. Silakan coba lagi.",
                "error",
                REGISTER_TEMPLATE
            )

        # === FLASH SUCCESS === #
        flash("Registrasi berhasil. Akun Anda sedang menunggu verifikasi admin.", "success")
        return redirect(url_for("auth.login"))

    # === RENDER PAGE === #
    return render_template(REGISTER_TEMPLATE)


# === ROUTE LOGOUT === #
@auth_bp.route("/logout", methods=["POST"])
def logout():

    session_log_id = session.get("session_log_id")
    if session_log_id:

        session_log = db.session.get(
            UserSession,
            session_log_id
        )

        if session_log:
            session_log.logout_at = waktu_indonesia()
            session_log.is_online = False
            db.session.commit()

    # === HAPUS SESSION === #
    session.clear()
    
    # === REDIRECT LOGIN === #
    return redirect(url_for("auth.login"))