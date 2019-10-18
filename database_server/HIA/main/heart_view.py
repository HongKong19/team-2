from flask import request, session, redirect, url_for, current_app, jsonify, abort
from .. import db
from ..models import Heart
from . import main


@main.route('/hearts', methods=['GET'])
def get_heart():
    allHeart = Heart.query.all()
    data = list()
    for u in allHeart:
        data.append(u.to_dict())
    return jsonify({'heart': data})


@main.route('/heart/create', methods=['POST'])
def create_heart():
    if not request.json:
        abort(400)
    newHeart = Heart(
        user_id = request.json['user_id'], 
        age = request.json['age'], 
        sex = request.json['sex'], 
    	cp = request.json['cp'], 
        trestbps = request.json['trestbps'],
        chol = request.json['chol'], 
        fbs = request.json['fbs'], 
        restecg = request.json['restecg'], 
        thalach = request.json['thalach'], 
        exang = request.json['exang'],
        oldpeak = request.json['oldpeak'],
		sl = request.json['slope'],
		ca = request.json['ca'],
		thal = request.json['thal'],
		is_heart = request.json['is_heart']
        )

    db.session.add(newHeart)
    db.session.commit()
    return jsonify({'heart': newHeart.to_dict()}), 201



