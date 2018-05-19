import datetime
from json import dumps

from flask import current_app
from sqlalchemy import Column, DateTime, Integer, event
from sqlalchemy_mixins import AllFeaturesMixin

ActiveRecord = AllFeaturesMixin


def serialize(_query):
    indent = None
    separators = (',', ':')

    master = {}
    dict_ = {}
    try:
        for u in _query:
            d = u.__dict__
            for n in d.keys():
                if n != '_sa_instance_state':
                    dict_[n] = d[n]
            x = d['id']
            master[x] = dict_
    except:
        d = _query.__dict__
        for n in d.keys():
            if n != '_sa_instance_state':
                dict_[n] = d[n]
        x = d['id']
        master[x] = dict_

    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] or current_app.debug:
        indent = 2
        separators = (', ', ': ')

    return current_app.response_class(
        dumps(master, indent = indent, separators = separators) + '\n',
        mimetype = current_app.config['JSONIFY_MIMETYPE']
    )


class Timestamp(object):
    """Adds `created_at` and `updated` columns to a derived declarative model.

    The `created_at` column is handled through a default and the `updated_at`
    column is handled through a `before_update` event that propagates
    for all derived declarative models.

    """

    created_at = Column(DateTime, default = datetime.datetime.now(), nullable = True)
    updated_at = Column(DateTime, default = datetime.datetime.now(), nullable = True)


@event.listens_for(Timestamp, 'before_update', propagate = True)
def timestamp_before_update(target):
    # When a model with a timestamp is updated; force update the updated
    # timestamp.
    target.updated_at = datetime.datetime.now()


class IDMixin(Timestamp):
    id: Column = Column(Integer, primary_key = True)
