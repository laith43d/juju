from functools import wraps

from flask import Response, jsonify, redirect, request

from .helpers import json_value
from .response import make_json_response


def jsonapi(f):
	""" Declare the view as a JSON API method
		This converts view return value into a :cls:JsonResponse.
		The following return types are supported:
			- tuple: a tuple of (response, status, headers)
			- any other object is converted to JSON
	"""

	@wraps(f)
	def wrapper(*args, **kwargs):
		rv = f(*args, **kwargs)
		return make_json_response(rv)

	return wrapper


def ssl_required(f):
	"""Force requests to be secured with SSL. Must set the `SSL` config parameter to `True`

	:param f: function
	"""

	@wraps(f)
	def wrapper(*args, **kwargs):
		from flask import current_app as app

		if app.config.get("SSL"):
			if request.is_secure:
				return f(*args, **kwargs)
			else:
				return redirect(request.url.replace("http://", "https://"))
		return f(*args, **kwargs)

	return wrapper


def as_json(f):
	"""Return result as a JSON response.

	Responses of type :class:`flask.wrappers.Response` are returned as is.
	Responses of type :class:`dict` are serialized to JSON.
	All other response types are serialized to JSON and returned
	in an object with key `result` such as: {'result': True}

	:param f: function
	"""

	@wraps(f)
	def wrapper(*args, **kwargs):
		response = f(*args, **kwargs)
		if response is None:
			raise Exception("Cannot serialize None to JSON")
		if isinstance(response, Response):
			return response
		if not callable(response):
			response = json_value(response)
		if isinstance(response, dict):
			return jsonify(**response)
		else:
			return jsonify(result = response)

	return wrapper
