import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# conn = sqlite3.connect('./contingent.db')
engine = create_engine('sqlite:///database/contingent.db')
session = sessionmaker(bind=engine, autoflush=False)



# conn.commit()
# conn.close()
