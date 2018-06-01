import datetime

from sqlalchemy import Column, DateTime, Integer, inspect


class Timestamp():
    """Adds `created_at` and `updated_at` columns to a derived declarative model.

    The `created_at` column is handled through a default and the `updated_at`
    column is handled through a onupdate event trigger.

    """

    created_at = Column(DateTime, default = datetime.datetime.now())
    updated_at = Column(DateTime, onupdate = datetime.datetime.utcnow())


class IDMixin(Timestamp):
    id: Column = Column(Integer, primary_key = True)

    def as_dict(self):
        basic_object = {c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs}
        return {**basic_object}

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
