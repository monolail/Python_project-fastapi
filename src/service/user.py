import random
import datetime
import time
from datetime import timedelta,datetime

import bcrypt
from jose import jwt

class UserService :
    encoding : str = "UTF-8"
    secret_key : str = "9031083a2c9b45954faa15dbd86bfcaeda21e99b7a942ca8b9b1333b37d60c9c"
    jwt_algorithm:str = "HS256"

    def hash_password(self, plain_password: str) -> str :
        hashed_password : bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding),
            salt = bcrypt.gensalt()
        )
        return hash.decode("UTF-8")

    def verify_password(
            self, plain_password : str, hashed_password:str
    )-> bool:

        return bcrypt.checkpw(
            plain_password.encode(self.encoding),
            hashed_password.encode(self.encoding)
        )

    def create_jwt(self, username : str)->str:
        return jwt.encode(
            {
                "sub" : username, # unique한 식별자
                "exp" : datetime.now()+timedelta(days=1),
            },
            self.secret_key,
            algorithm=self.jwt_algorithm),

    def decode_jwt(self,access_token:str) -> str:
        payload: dict = jwt.decode(
            access_token, self.secret_key, algorithms=[self.jwt_algorithm]
        )
        # expire
        return payload["sub"] # username

    @staticmethod
    def create_otp(self) -> int :
        return random.randint(1000,9999)

    @staticmethod
    def send_email_to_user( email:str)->None:
        time.sleep(10)
        print(f"sending email to {email}!")