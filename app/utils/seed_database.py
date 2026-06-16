from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db
from app.models import (Radioisotop, Perisai, SatuanKonversi, Panduan, FAQ,)
from app.data import (RADIOISOTOP_DATA, PERISAI_DATA, SATUAN_DATA, PANDUAN_DATA, FAQ_DATA,)


# === HELPER FUNCTION === #
def clean_data(model, data):
    columns = model.__table__.columns.keys()
    return {
        key: value
        for key, value in data.items()
        if key in columns and key != "id"
    }
def update_existing(existing, data, exclude_fields=None):
    if exclude_fields is None:
        exclude_fields = []
    for key, value in data.items():
        if key not in exclude_fields:
            setattr(existing, key, value)


# === SEED RADIOISOTOP === #
def seed_radioisotop():
    for data in RADIOISOTOP_DATA:
        data = clean_data(Radioisotop, data)
        existing = Radioisotop.query.filter_by(
            radioisotop=data["radioisotop"]
        ).first()

        if existing is None:
            db.session.add(Radioisotop(**data))
        else:
            update_existing(
                existing=existing,
                data=data,
                exclude_fields=["radioisotop"]
            )


# === SEED PERISAI === #
def seed_perisai():
    for data in PERISAI_DATA:
        data = clean_data(Perisai, data)
        existing = Perisai.query.filter_by(
            radioisotop=data["radioisotop"],
            material_perisai=data["material_perisai"]
        ).first()

        if existing is None:
            db.session.add(Perisai(**data))
        else:
            update_existing(
                existing=existing,
                data=data,
                exclude_fields=[
                    "radioisotop",
                    "material_perisai"
                ]
            )


# === SEED SATUAN KONVERSI === #
def seed_satuan():
    for data in SATUAN_DATA:
        data = clean_data(SatuanKonversi, data)
        existing = SatuanKonversi.query.filter_by(
            jenis_besaran=data["jenis_besaran"],
            satuan_asal=data["satuan_asal"],
            satuan_tujuan=data["satuan_tujuan"]
        ).first()

        if existing is None:
            db.session.add(SatuanKonversi(**data))
        else:
            update_existing(
                existing=existing,
                data=data,
                exclude_fields=[
                    "jenis_besaran",
                    "satuan_asal",
                    "satuan_tujuan"
                ]
            )


# === SEED PANDUAN === #
def seed_panduan():
    for data in PANDUAN_DATA:
        data = clean_data(Panduan, data)
        existing = Panduan.query.filter_by(
            kategori=data["kategori"],
            judul=data["judul"]
        ).first()

        if existing is None:
            db.session.add(Panduan(**data))
        else:
            update_existing(
                existing=existing,
                data=data,
                exclude_fields=[
                    "kategori",
                    "judul"
                ]
            )


# === SEED FAQ === #
def seed_faq():
    for data in FAQ_DATA:
        data = clean_data(FAQ, data)
        existing = FAQ.query.filter_by(
            kategori=data["kategori"],
            pertanyaan=data["pertanyaan"]
        ).first()

        if existing is None:
            db.session.add(FAQ(**data))
        else:
            update_existing(
                existing=existing,
                data=data,
                exclude_fields=[
                    "kategori",
                    "pertanyaan"
                ]
            )


# === SEED DATABASE === #
def seed_database():
    try:
        seed_radioisotop()
        seed_perisai()
        seed_satuan()
        seed_panduan()
        seed_faq()

        db.session.commit()

    except SQLAlchemyError:
        db.session.rollback()
        raise