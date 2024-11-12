from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///data/duombaze.db', echo=False) # No need of "echo=Flase" as this is default
Base = declarative_base()

class nereceptiniai_vaistai(Base):
    __tablename__ = 'nereceptiniai_vaistai'
    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String, primary_key=True, nullable=False)
    price = Column("price", Float, primary_key=True, nullable=False)
    discount = Column("discount", String, primary_key=True)

Session = sessionmaker(bind=engine)
session = Session()

all_nereceptiniai_vaistai = session.query(nereceptiniai_vaistai).all()

for vaistas in all_nereceptiniai_vaistai:
    print(f"ID: {vaistas.id}, Name: {vaistas.name}, Price: {vaistas.price}, Discount: {vaistas.discount}")

def search_nereceptiniai_vaistai_by_id(id: Integer):
    print(session.query(nereceptiniai_vaistai).filter_by(id=id).first().name)

search_nereceptiniai_vaistai_by_id(4)