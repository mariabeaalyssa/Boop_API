import uuid

from app.main import db
from app.main.models.specie import Specie
from app.main.services.help import Helper

def new_specie(data):
    new_public_id = str(uuid.uuid4())

    new_specie = Specie(
        public_id = new_public_id,
        specie_name = data["specieName"]
    )

    Helper.save_changes(new_specie)

    return Helper.generate_token("Specie", new_specie)

def get_all_species():
    return Specie.query.all()

def get_a_specie(public_id):
    return Specie.query.filter_by(public_id=public_id).first()

def delete_specie(public_id):
    specie = Specie.query.filter_by(public_id=public_id).first()

    if specie:
        db.session.delete(specie)

        db.session.commit()

        return Helper.return_resp_obj("success", "Specie delete successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No specie found.", None, 409)

def edit_specie(public_id, data):
    specie = Specie.query.filter_by(public_id=public_id).first()

    if specie:
        specie.specie_name = data["specieName"]

        db.session.commit()

        return Helper.return_resp_obj("success", "Specie updated successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No specie found.", None, 409)