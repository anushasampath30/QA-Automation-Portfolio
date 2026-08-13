class LoginService:
    def __init__(self, valid_users : dict[str,str]):
        self.valid_users = valid_users
    def login(self, username:str, password: str) -> bool:
        return self.valid_users.get(username) == password