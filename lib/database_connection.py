import psycopg
from psycopg.rows import dict_row
import os

class DatabaseConnection:

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "book_store"
    )

    DATABASE_HOST = os.getenv(
        "DATABASE_HOST",
        "book_store_db"
)
    # old one:
    # DATABASE_HOST = os.getenv(
    #     "DATABASE_HOST",
    #     "localhost"
    # )

    DATABASE_USER = os.getenv(
        "DATABASE_USER",
        "yuhan"
    )

    DATABASE_PASSWORD = os.getenv(
        "DATABASE_PASSWORD",
        ""
    )

    def __init__(self):
        self.connection = None

    def connect(self):

        connection_string = (
            f"postgresql://{self.DATABASE_USER}"
        )

        if self.DATABASE_PASSWORD != "":
            connection_string += f":{self.DATABASE_PASSWORD}"

        connection_string += (
            f"@{self.DATABASE_HOST}/{self.DATABASE_NAME}"
        )

        self.connection = psycopg.connect(
            connection_string,
            row_factory=dict_row
        )