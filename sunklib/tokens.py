import json
from pathlib import Path
from pydantic import BaseModel

from sunklib.util.io import open_toml, save_toml
from sunklib.env import FILE_CREDENTIALS


class Credentials:
    @property
    def data(self) -> dict:
        return open_toml(FILE_CREDENTIALS)

    @property
    def tokens(self) -> list[str]:
        return list(self.data.keys())

    def exists(self, name: str) -> bool:
        return name in self.tokens

    def check(self, name) -> None:
        if not self.exists(name):
            raise ValueError("key does not exist")

    def get(self, name: str) -> str:
        self.check(name)
        return self.data[name]

    def save(self, name: str, token: str) -> None:
        creds = self.data
        creds[name] = token
        save_toml(creds, FILE_CREDENTIALS)

    def delete(self, name: str) -> None:
        self.check(name)
        creds = self.data
        del creds[name]
        save_toml(creds, FILE_CREDENTIALS)


creds = Credentials()

# PATH_HOME = Path.home()
# PATH_CACHE = PATH_HOME / ".sunkcosts"
# PATH_CREDENTIALS = PATH_CACHE / "credentials.json"


# def get_token(name: str) -> str:
#     with open(PATH_CREDENTIALS) as cf:
#         data = json.loads(cf.read())
#         if name not in data.keys():
#             raise ValueError("token does not exist")
#         else:
#             key = data[name]
#     cf.close()
#     return key


# def add_token(name: str, key: str) -> None:
#     with open(PATH_CREDENTIALS) as cf:
#         data = json.loads(cf.read())
#     cf.close()
#     data[name] = key
#     with open(PATH_CREDENTIALS, "w") as cf:
#         cf.write(json.dumps(data))
#     cf.close()


# def del_token(name: str) -> None:
#     with open(PATH_CREDENTIALS) as cf:
#         data = json.loads(cf.read())
#         if name not in data.keys():
#             raise ValueError("token does not exist")
#         else:
#             del data[name]
#     cf.close()
#     with open(PATH_CREDENTIALS, "w") as cf:
#         cf.write(json.dumps(data))
#     cf.close()
#     cf.close()


# class Token(BaseModel):
#     name: str

#     def add_token(self, key: str):
#         add_token(self.name, key)

#     def get_token(self) -> str:
#         return get_token(self.name)

#     def del_token(self, name: str) -> None:
#         del_token(self.name)


# class Credentials:
#     def __init__(self) -> None:
#         self.mapbox_pub = Token(name="mapbox_pub")
#         self.mapbox_dev = Token(name="mapbox_dev")


# creds = Credentials()
