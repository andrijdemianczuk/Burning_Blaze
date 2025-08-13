class SU:
    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        # Expose via property; no setter => read-only
        return self._password


class User(SU):
    __slots__ = ("_name", "_email")  # optional, but tidy

    def __init__(self, name, email, password):
        super().__init__(password)
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    # If you later decide to allow updates, add setters with validation:
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name cannot be empty")
        self._name = value
