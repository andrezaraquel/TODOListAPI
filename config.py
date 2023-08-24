from dotenv import load_dotenv, dotenv_values
import random
import string

class Config:

    load_dotenv()
    config = dotenv_values()

    def __init__(self):
        random_str = string.ascii_letters + string.digits + string.ascii_uppercase
        key = ''.join(random.choice(random_str) for i in range(12))
        self.config['SECRET_KEY'] = key

config = Config().config
