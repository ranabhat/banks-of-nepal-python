from app import db

class Bank(db.Model):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    bankHeadAddress = db.Column(db.String())
    bankUrl = db.Column(db.String())
    bankSwiftCode= db.Column(db.String())

    def __init__(self, name, bankHeadAddress, bankUrl, bankSwiftCode):
        self.name = name
        self.bankHeadAddress = bankHeadAddress
        self.bankUrl = bankUrl
        self.bankSwiftCode = bankSwiftCode

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'bankHeadAddress': self.bankHeadAddress,
            'bankUrl': self.bankUrl,
            'bankSwiftCode': self.bankSwiftCode
}