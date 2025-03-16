from mimesis import Locale, Person


class FakeData:
    def __init__(self, lang: str = "en"):
        if lang == "en":
            self._LOCALE = Locale.EN
        if lang == "ru":
            self._LOCALE = Locale.RU
        self.person = Person(self._LOCALE)

    @property
    def username(self):
        return self.person.username()

    @property
    def full_name(self):
        return self.person.full_name()

    @property
    def email(self):
        return self.person.email(domains=["google.com"])

    @property
    def password(self):
        return self.person.password()
