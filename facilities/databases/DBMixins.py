import datetime

from sqlalchemy import Column, DateTime, Integer, event
from sqlalchemy.ext.declarative import DeclarativeMeta


class OutputMixin(object):
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel: object = None, backref: object = None) -> object:
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref = self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref = self.__table__)
                                         for i in value]
        return res

    # def to_json(self, rel = None):
    #     def extended_encoder(x):
    #         if isinstance(x, datetime.datetime):
    #             return x.isoformat()
    #     #     if isinstance(x, UUID):
    #     #         return str(x)
    #
    #     if rel is None:
    #         rel = self.RELATIONSHIPS_TO_DICT
    #     return json.dumps(self.to_dict(rel), default = extended_encoder)


class Timestamp():
    """Adds `created_at` and `updated` columns to a derived declarative model.

    The `created_at` column is handled through a default and the `updated_at`
    column is handled through a `before_update` event that propagates
    for all derived declarative models.

    """

    created_at = Column(DateTime, default = datetime.datetime.now())
    updated_at = Column(DateTime, onupdate = datetime.datetime.utcnow())


@event.listens_for(Timestamp, 'before_update', propagate = True)
def timestamp_before_update(target):
    # When a model with a timestamp is updated; force update the updated
    # timestamp.
    target.updated_at = datetime.datetime.now()


class IDMixin(Timestamp, OutputMixin):
    id: Column = Column(Integer, primary_key = True)


# ---------------------------------------------------------

class UserMixin:
    """
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        """
        Checks the equality of two `UserMixin` objects using `get_id`.
        """
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        """
        Checks the inequality of two `UserMixin` objects using `get_id`.
        """
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


class AnonymousUserMixin:
    """
    This is the default object for representing an anonymous user.
    """

    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return


class Serialize:
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
