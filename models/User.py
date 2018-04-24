from config.settings import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True, nullable = False)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(128))
    password_again = db.Column(db.String(128))
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default = True, server_default = 'true')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username = username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        if not self.is_active:
            raise Exception("user has been disabled")

# Seed DB -------------------------------------------------

# Add users for the example
# with app.app_context():
#     db.create_all()
#     db.session.add(User(
#         username='TheDude',
#         password=guard.encrypt_password('abides'),
#     ))
#     db.session.add(User(
#         username='Walter',
#         password=guard.encrypt_password('calmerthanyouare'),
#         roles='admin'
#     ))
#     db.session.add(User(
#         username='Donnie',
#         password=guard.encrypt_password('iamthewalrus'),
#         roles='operator'
#     ))
#     db.session.add(User(
#         username='Maude',
#         password=guard.encrypt_password('andthorough'),
#         roles='operator,admin'
#     ))
#     db.session.commit()

#
# Set up some routes for the example ----------------------
#
# # curl http://localhost:5000/login -X POST \
# #   -d '{"username":"Walter","password":"calmerthanyouare"}'
# @app.route('/login', methods=['POST'])
# def login():
#     req = flask.request.get_json(force=True)
#     username = req.get('username', None)
#     password = req.get('password', None)
#     user = guard.authenticate(username, password)
#     ret = {'access_token': guard.encode_jwt_token(user)}
#     return flask.jsonify(ret), 200
#
#
# # curl http://localhost:5000/refresh -X GET \
# #   -H "Authorization: Bearer <your_token>"
# @app.route('/refresh', methods=['GET'])
# def refresh():
#     old_token = guard.read_token_from_header()
#     new_token = guard.refresh_jwt_token(old_token)
#     ret = {'access_token': new_token}
#     return flask.jsonify(ret), 200
#
#
# @app.route('/')
# def root():
#     return flask.jsonify(message='root endpoint')
#
#
# # curl http://localhost:5000/protected -X GET \
# #   -H "Authorization: Bearer <your_token>"
# @app.route('/protected')
# @flask_praetorian.auth_required
# def protected():
#     return flask.jsonify(message='protected endpoint (allowed user {})'.format(
#         flask_praetorian.current_user().username,
#     ))
#
#
# # curl http://localhost:5000/protected_admin_required -X GET \
# #   -H "Authorization: Bearer <your_token>"
# @app.route('/protected_admin_required')
# @flask_praetorian.auth_required
# @flask_praetorian.roles_required('admin')
# def protected_admin_required():
#     return flask.jsonify(
#         message='protected_admin_required endpoint (allowed user {})'.format(
#             flask_praetorian.current_user().username,
#         )
#     )
#
#
# # curl http://localhost/protected_operator_accepted -X GET \
# #   -H "Authorization: Bearer <your_token>"
# @app.route('/protected_operator_accepted')
# @flask_praetorian.auth_required
# @flask_praetorian.roles_accepted('operator', 'admin')
# def protected_operator_accepted():
#     return flask.jsonify(
#         message='protected_operator_accepted endpoint (allowed usr {})'.format(
#             flask_praetorian.current_user().username,
#         )
#     )
