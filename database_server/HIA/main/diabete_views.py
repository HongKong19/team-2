from flask import request, session, redirect, url_for, current_app, jsonify, abort
from .. import db
from ..models import Diabete
from . import main

@main.route('/diabete', methods=['GET'])
def get_diabete():
    allDiabete = diabete.query.all()
    data = list()
    for u in allDiabete:
        data.append(u.to_dict())
    return jsonify({'diabete': data})


@main.route('/diabete/create', methods=['POST'])
def create_diabete():
    if not request.json:
        abort(400)

    newDiabete = diabete(
        user_id = request.json['user_id'], 
        glucose = request.json['glucose'], 
        blood_pressure = request.json['blood_pressure'], 
    	DPF = request.json['DPF'], 
        age = request.json['age'],
        is_diabete = request.json['is_diabete'], 
        )

    db.session.add(newDiabete)
    db.session.commit()
    return jsonify({'diabete': newDiabete.to_dict()}), 201
