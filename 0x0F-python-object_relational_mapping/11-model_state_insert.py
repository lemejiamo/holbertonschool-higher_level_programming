#!/usr/bin/python3
"""all states via SQLAlchemy"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state = "Louisiana"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, passwd, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    add_state = State(name=state)
    session.add(add_state)
    session.commit()

    print(add_state.id)

    session.close()
