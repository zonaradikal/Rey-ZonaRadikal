import re


# === POLA VALIDASI === #
USERNAME_PATTERN = r"[A-Za-z0-9_]+"
PASSWORD_PATTERN = r"[A-Za-z0-9]+"


# === VALIDASI NAMA LENGKAP === #
def validate_full_name(full_name):
    if not full_name or not full_name.strip():
        return "Nama lengkap wajib diisi."

    return None


# === VALIDASI USERNAME === #
def validate_username(username):
    if not username or not username.strip():
        return "Username wajib diisi."

    username = username.strip()
    if len(username) < 4:
        return "Username minimal 4 karakter."
    if " " in username:
        return "Username tidak boleh mengandung spasi."
    if not re.fullmatch(USERNAME_PATTERN, username):
        return "Username hanya boleh huruf, angka, dan underscore."

    return None


# === VALIDASI PASSWORD === #
def validate_password(password):
    if not password:
        return "Password wajib diisi."
    password = password.strip()
    if len(password) < 8:
        return "Password minimal 8 karakter."
    if " " in password:
        return "Password tidak boleh mengandung spasi."

    if not re.search(r"[A-Za-z]", password):
        return "Password wajib mengandung huruf."
    if not re.search(r"[0-9]", password):
        return "Password wajib mengandung angka."
    if not re.fullmatch(PASSWORD_PATTERN, password):
        return "Password tidak boleh mengandung karakter khusus."

    return None


# === VALIDASI KONFIRMASI PASSWORD === #
def validate_confirm_password(password, confirm_password):
    if not confirm_password:
        return "Konfirmasi password wajib diisi."
    if password != confirm_password:
        return "Konfirmasi password tidak cocok."
    
    return None