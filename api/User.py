import flask_praetorian
from flask import request
from flask_classful import FlaskView as Resource, route
from flask_orator import jsonify

from config.settings import guard
from models.User import User


class UserView(Resource):

    @route('login', methods = ['POST'])
    def login(self):
        """
        Logs a user in by parsing a POST request containing user credentials and
        issuing a JWT token.

        .. example::
           $ curl http://localhost:5000/login -X POST \
             -d '{"username":"Walter","password":"calmerthanyouare"}'
        """
        req = request.get_json(force = True)
        username = req.get('username', None)
        password = req.get('password', None)
        user = guard.authenticate(username, password)
        ret = {'access_token': guard.encode_jwt_token(user)}
        return jsonify(ret), 200

    @route('protected', methods = ['GET'])
    @flask_praetorian.auth_required
    def protected(self):
        """
        A protected endpoint. The auth_required decorator will require a header
        containing a valid JWT

        .. example::
           $ curl http://localhost:5000/protected -X GET \
             -H "Authorization: Bearer <your_token>"
        """
        return jsonify(f'protected endpoint (allowed user {flask_praetorian.current_user().username})')

    @route('protected_admin_required')
    @flask_praetorian.auth_required
    @flask_praetorian.roles_required('can_nothing')
    def protected_admin_required(self):
        """
        A protected endpoint that requires a role. The roles_required decorator
        will require that the supplied JWT includes the required roles

        .. example::
           $ curl http://localhost:5000/protected_admin_required -X GET \
              -H "Authorization: Bearer <your_token>"
        """
        return jsonify(
            f'protected_admin_required endpoint (allowed user {flask_praetorian.current_user().username})'
        )

    @route('protected_operator_accepted')
    @flask_praetorian.auth_required
    @flask_praetorian.roles_accepted('can_nothing', 'admin')
    def protected_operator_accepted(self):
        """
        A protected endpoint that accepts any of the listed roles. The
        roles_accepted decorator will require that the supplied JWT includes at
        least one of th accepted roles

        .. example::
           $ curl http://localhost/protected_operator_accepted -X GET \
             -H "Authorization: Bearer <your_token>"
        """
        return jsonify(
            f'protected_operator_accepted endpoint (allowed usr {flask_praetorian.current_user().username})'
        )

    @route('refresh', methods=['GET'])
    def refresh(self):
        """
        Refreshes an existing JWT by creating a new one that is a copy of the old
        except that it has a refreshed access expiration.

        .. example::
           $ curl http://localhost:5000/refresh -X GET \
             -H "Authorization: Bearer <your_token>"
        """
        old_token = guard.read_token_from_header()
        new_token = guard.refresh_jwt_token(old_token)
        ret = {'access_token': new_token}
        return jsonify(ret), 200

    @route('disable_user', methods = ['POST'])
    @flask_praetorian.auth_required
    @flask_praetorian.roles_required('can_nothing')
    def disable_user(self):
        """
        Disables a user in the data store

        .. example::
            $ curl http://localhost:5000/disable_user -X POST \
              -H "Authorization: Bearer <your_token>" \
              -d '{"username":"Walter"}'
        """
        req = request.get_json(force = True)
        usr = User.query().where('username', req.get('username', None)).first()
        return jsonify(f'disabled user {usr.username}')


# # Blacklist example
# blacklist = set()
#
#
# def is_blacklisted(jti):
#     return jti in blacklist
#
# # Initialize the flask-praetorian instance for the app with is_blacklisted
# guard.init_app(app, User, is_blacklisted=is_blacklisted)
#
# @app.route('/blacklist_token', methods=['POST'])
# @flask_praetorian.auth_required
# @flask_praetorian.roles_required('admin')
# def blacklist_token():
#     """
#     Blacklists an existing JWT by registering its jti claim in the blacklist.
#
#     .. example::
#        $ curl http://localhost:5000/blacklist_token -X POST \
#          -d '{"token":"<your_token>"}'
#     """
#     req = flask.request.get_json(force=True)
#     data = guard.extract_jwt_token(req['token'])
#     blacklist.add(data['jti'])
#     return flask.jsonify(message='token blacklisted ({})'.format(req['token']))
