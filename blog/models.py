from sqlalchemy import Column,Integer,String

from .database import Base
from sqlalchemy_utils import URLType

class Blog(Base):
  __tablename__='blogs'

  id=Column(Integer,primary_key=True,index=True)
  detail = Column(String)
  url = Column(String)