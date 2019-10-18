from HIA import db


class Table(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        dicttem = dict(self.__dict__)
        dicttem.pop('_sa_instance_state', None)
        if self.id != None:
            dicttem['id'] = self.id
        return dicttem

    
    
class User(Table):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64))
    phone = db.Column(db.String(32), unique=True, index=True)
    age = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    height = db.Column(db.String(32))
    weight = db.Column(db.String(32))
    smoking = db.Column(db.String(6))
    alcohol = db.Column(db.String(32))
    pulse = db.Column(db.String(32))
    disease = db.Column(db.String(128))
    occupation = db.Column(db.String(32))
    ethnicity = db.Column(db.String(32))
    blood_sugar = db.Column(db.String(32))
    family_id = db.Column(db.Integer, db.ForeignKey('families.id'))
    __mapper_args__ = {'concrete': True}
    
    def __repr__(self):
        return '<User %r>' % self.userName

class Family(Table):
    __tablename__ = 'families'


    id = db.Column(db.Integer, primary_key=True)
    
    income = db.Column(db.String(64))
    food_choice = db.Column(db.String(32))
    family_information = db.Column(db.String(128))

    __mapper_args__ = {'concrete': True}
    
    def __repr__(self):
        return '<User %r>' % self.userName


class Admin(Table):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    adminName = db.Column(db.String(32))
    password = db.Column(db.String(32))
    __mapper_args__ = {'concrete': True}