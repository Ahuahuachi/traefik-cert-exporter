class Model:
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"


class Registration(Model):
    def __init__(self, body: dict, uri: str):
        self.body = body
        self.uri = uri

    def __str__(self) -> str:
        return f"body={self.body}, uri={self.uri}"


class Account(Model):
    def __init__(self, email: str, registration: dict, private_key: str, key_type: str):
        self.email = email
        self.registration = Registration(**registration)
        self.private_key = private_key
        self.key_type = key_type

    def __str__(self) -> str:
        return self.email

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        return cls(
            email=data["Email"],
            registration=data["Registration"],
            private_key=data["PrivateKey"],
            key_type=data["KeyType"],
        )
