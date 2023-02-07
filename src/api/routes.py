"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Events
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# USERS

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    results = [user.serialize() for user in users]
    response_body = {'message': 'OK',
                     'total_records': len(results),
                     'results': results}
    return jsonify(response_body), 200

@api.route('/user/<user_id>', methods=['GET'])
def handle_hello(user_id):
    print(user_id)
    user = User.query.get(user_id)
    print(user)
    return jsonify(user.serialize()), 200

@api.route('/user/register', methods=['POST'])
def create_user():
    body = request.get_json()
    new_user = User(email=body["email"], password=body["password"], is_active=True)
    print(body)
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 200

@api.route('/users/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)

    user.email = request.json.get('email', user.email)
    user.password = request.json.get('password', user.password)
    user.is_active = request.json.get('is_active', user.is_active)
    db.session.commit()

    response_body = {'email': user.email,
                     'password': user.password,
                     'is_active': user.is_active}

    return jsonify(response_body), 200

@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user)
    db.session.commit()
    response_body = {
        "message": "User deleted correctly"}    
    return jsonify(response_body), 200

# EVENTS

@api.route('events', methods=['GET'])
def get_all_events():
    events = Events.query.all()
    results = [event.serialize() for event in events]
    response_body = {'message': 'OK',
                     'total_records': len(results),
                     'results': results}
    return jsonify(response_body), 200

@api.route('/event/<event_id>', methods=['GET'])
def get_event_by_id(event_id):
    print(event_id)
    event = Events.query.get(event_id)
    print(event)
    return jsonify(event.serialize()), 200

@api.route('/event/register', methods=['POST'])
def create_event():
    body = request.get_json()
    new_event = Events(title=body["title"], date=body["date"], time=body["time"], description=body["description"], location=body["location"], guests=body["guests"], image=body["image"], user_id=body["user_id"] )
    print(body)
    print(new_event)
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.serialize()), 200

@api.route('/events/<int:event_id>', methods=['PUT'])
def modify_event(event_id):
    event = Events.query.get(event_id)
    if event is None:
        raise APIException('Event not found', status_code=404)

    event.title = request.json.get('title', event.title)
    event.date = request.json.get('date', event.date)
    event.time = request.json.get('time', event.time)
    event.description = request.json.get('description', event.description)
    event.location = request.json.get('location', event.location)
    event.guests = request.json.get('guests', event.guests)
    event.image = request.json.get('image', event.image)
    event.user_id = request.json.get('user_id', event.user_id)
    db.session.commit()

    response_body = {'title': event.title,
                     'date': event.date,
                     'time': event.time,
                     'description': event.description,
                     'location': event.location,
                     'guests': event.guests,
                     'image': event.image,
                     'user_id': event.user_id
                     }

    return jsonify(response_body), 200

@api.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Events.query.get(event_id)
    if event is None:
        raise APIException('Event not found', status_code=404)
    db.session.delete(event)
    db.session.commit()
    response_body = {
        "message": "Event deleted correctly"}    
    return jsonify(response_body), 200
