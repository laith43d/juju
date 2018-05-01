import datetime

from sqlalchemy import Column, DateTime, Integer, event
from sqlalchemy_mixins import AllFeaturesMixin

BaseModel = AllFeaturesMixin


class Timestamp(object):
    """Adds `created_at` and `updated` columns to a derived declarative model.

    The `created_at` column is handled through a default and the `updated_at`
    column is handled through a `before_update` event that propagates
    for all derived declarative models.

    """

    created_at = Column(DateTime, default = datetime.datetime.now, nullable = False)
    updated_at = Column(DateTime, default = datetime.datetime.now, nullable = False)


@event.listens_for(Timestamp, 'before_update', propagate = True)
def timestamp_before_update(mapper, connection, target):
    # When a model with a timestamp is updated; force update the updated
    # timestamp.
    target.updated_at = datetime.datetime.now()


class IdTimestampMixin(Timestamp):
    id: Column = Column(Integer, primary_key = True)
