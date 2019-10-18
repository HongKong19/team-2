from flask import request, session, redirect, url_for, current_app, jsonify, abort
from .. import db
from ..models import User
from . import main



@main.route('/users', methods=['GET'])
def get_users():
    allUser = User.query.all()
    data = list()
    for u in allUser:
        data.append(u.to_dict())
    return jsonify({'users': data})


@main.route('/user/id/<int:user_id>', methods=['GET'])
def get_user_byID(user_id: int):
    targetUser = User.query.get_or_404(user_id)
    return jsonify({'user': targetUser.to_dict()}), 201




@main.route('/user', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)

    newUser = User(
        userName = request.json['userName'], 
        phone = request.json['phone'], 
        gender = request.json['gender'], 
    	height = request.json['height'], 
        weight = request.json['weight'],
        smoking = request.json['smoking'], 
        alcohol = request.json['alcohol'], 
        pulse = request.json['pulse'], 
        occupation = request.json['occupation'], 
        ethnicity = request.json['ethnicity'],
        blood_sugar = request.json['blood_sugar']

        )

    db.session.add(newUser)
    db.session.commit()
    return jsonify({'user': newUser.to_dict()}), 201




@main.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    if not request.json:
        abort(400)

    targetUser = User.query.get_or_404(user_id)

    updateDict = dict(request.json)
    if 'userName' in updateDict:
        targetUser.userName = updateDict['userName']
    if  'phone'in updateDict:
        targetUser.phone = updateDict['phone']
    if  'gender'in updateDict:
        targetUser.gender = updateDict['gender']
    if  'height'in updateDict:
        targetUser.height = updateDict['height']
    if  'weight'in updateDict:
        targetUser.weight = updateDict['weight']
    if  'smoking'in updateDict:
        targetUser.smoking = updateDict['smoking']
    if 'alcohol' in updateDict:
        targetUser.alcohol = updateDict['alcohol']
    if  'pulse'in updateDict:
        targetUser.pulse = updateDict['pulse']
    if  'disease'in updateDict:
        targetUser.disease = updateDict['disease']
    if  'occupation'in updateDict:
        targetUser.occupation = updateDict['occupation']
    if  'ethnicity'in updateDict:
        targetUser.ethnicity = updateDict['ethnicity']
    if  'blood_sugar'in updateDict:
        targetUser.blood_sugar = updateDict['blood_sugar']
    
    db.session.add(targetUser)
    db.session.commit()
    return jsonify({'user': targetUser.to_dict()}), 201


@main.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    targetUser = User.query.get_or_404(user_id)
    targetDict = targetUser.to_dict()
    db.session.delete(targetUser)
    db.session.commit()

    return jsonify({'user': targetDict}), 201


