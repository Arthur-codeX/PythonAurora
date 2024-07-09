from . import db


class Member(db.Model):
    __tablename__='member'

    id=db.Column(db.BigInteger,primary_key=True)
    alias=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)

    def details(self):
        return {'id':self.id,'alias':self.alias, 'email':self.email}