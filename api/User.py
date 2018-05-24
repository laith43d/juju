from flask import request
from flask_classful import FlaskView as Resource, route
from flask_orator import jsonify

from models.User import User


class UserView(Resource):

    @route('', methods = ['POST'])
    def add(self):
        print(request.get_json())
        User.create(**request.get_json())
        return jsonify({'message': 'success'})

    @route('/usernames', methods = ['GET'])
    def get_ordered_desc(self):
        users = User.select('id', 'username').order_by('created_at', 'desc').get().all()
        result = [user.to_json() for user in users]
        return jsonify(result)

    @route('', methods = ['GET'])
    def get_all(self):
        return jsonify(User.all().to_json())

