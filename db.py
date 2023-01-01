import os
import sqlalchemy
from sqlalchemy import create_engine

def write(sql, val):
    engine = create_engine(f'mysql+mysqlconnector://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_IP")}/responses', echo=False)
    db = engine.connect()
    db.execute(sql, val)