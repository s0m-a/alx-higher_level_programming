#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        for city in state.cities:
            print("{:d}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
