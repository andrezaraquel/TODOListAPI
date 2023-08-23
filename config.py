from dotenv import load_dotenv, dotenv_values

class Config:
    load_dotenv()
    config = dotenv_values()

