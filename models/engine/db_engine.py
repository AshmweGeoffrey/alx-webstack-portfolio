#!/usr/bin/python3
from sqlalchemy import create_engine, text  # Import text for raw SQL
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


# DBStorage class initializes the database connection and provides methods to interact with the database[SqlAlchemy[sql]]
class DBStorage:
    engine = None
    session = None

    def __init__(self, db_name):
        self.connect(db_name)

    def connect(self, db_name):
        if self.session:
            self.session.close()  # Close the existing session if any
        if self.engine:
            self.engine.dispose()  # Dispose of the old engine
        
        self.engine = create_engine(
            'mysql+mysqldb://root:Ashimwe#001@localhost:3306/{}'.format(db_name), 
            pool_pre_ping=True,
            echo=True  # Enable SQL logging
        )
        
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def all(self, cls):
        return self.session.query(cls).all()

    def new(self, obj):
        self.session.add(obj)

    def save(self):
        self.session.commit()

    def delete(self, obj=None):
        if obj:
            self.session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # Use text() for raw SQL commands
    def command(self, command):
        with self.engine.connect() as connection:
            result = connection.execute(text(command))  # Wrap command in text()
            return result

    def close(self):
        self.session.close()