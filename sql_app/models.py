class Item(Base):
    __tablename__ = "items"

    id = Column(integer, primary_key = True, index = True)
    title = Column(String, index = True)
    description= Column(Integer, ForeignKey("users.id"))

    owner= relationshipe("User", back_populates = "items")
    