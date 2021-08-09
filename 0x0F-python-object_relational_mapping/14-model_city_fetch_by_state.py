#!/usr/bin/python3
"""all states via SQLAlchemy"""

import sys
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, passwd, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).\
        order_by(City.id)

    records = query.all()

    for record in records:
        print("{:s}: ({:d}) {:s}".format(*record))

    session.close()
