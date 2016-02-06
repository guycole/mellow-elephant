#
# Title:sql_table.py
# Description: SQLAlchemy adapter
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import uuid

from sqlalchemy import Column
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Installation(Base):
    __tablename__ = 'installation'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean)
    receiver = Column(String)
    antenna = Column(String)
    loc_latitude = Column(Float)
    loc_longitude = Column(Float)
    name = Column(String)
    create_time = Column(DateTime, default=datetime.datetime.utcnow)
    installation_uuid = Column(String)
    note = Column(String)

    def __init__(self, receiver, antenna, name):
        self.active = True
        self.receiver = receiver
        self.antenna = antenna
        self.loc_latitude = 0
        self.loc_longitude = 0
        self.name = name
#        self.create_time = datetime.datetime.utcnow
        self.installation_uuid = uuid.uuid4()
        self.note = 'No Note'

    def __repr__(self):
        return "<installation(%d, %s)>" % (self.id, self.name)

class Sortie(Base):
    __tablename__ = 'sortie'

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String)
    sortie_uuid = Column(String)
    installation_uuid = Column(String)
    note = Column(String)

    def __init__(self, installation_uuid):
        self.name = 'No Name'
        self.installation_uuid = installation_uuid
        self.sortie_uuid = uuid.uuid4()
        self.note = 'No Note'

    def __repr__(self):
        return "<sortie(%d, %s)>" % (self.id, self.name)

class Observation(Base):
    __tablename__ = 'observation'

    id = Column(BigInteger, primary_key=True)
    band = Column(String)
    frequency = Column(Integer)
    sample = Column(Integer)
    sortie_uuid = Column(String)
    time_stamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, band, frequency, sample, sortie_uuid, time_stamp):
        self.band = band
        self.frequency = frequency
        self.sample = sample
        self.sortie_uuid = sortie_uuid
        self.time_stamp = time_stamp

    def __repr__(self):
        return "<observation(%d, %d)>" % (self.id, self.frequency)