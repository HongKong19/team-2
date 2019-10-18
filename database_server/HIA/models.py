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
    
    
    __mapper_args__ = {'concrete': True}
    
    def __repr__(self):
        return '<User %r>' % self.userName

class Heart(Table):
    __tablename__ = 'hearts'

    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    age = db.Column(db.String(16))
    sex = db.Column(db.String(16))
    cp = db.Column(db.String(16))
    trestbps = db.Column(db.String(16))
    chol = db.Column(db.String(16))
    fbs = db.Column(db.String(16))
    restecg = db.Column(db.String(16))
    thalach = db.Column(db.String(16))
    exang = db.Column(db.String(16))
    oldpeak = db.Column(db.String(16))
    slope = db.Column(db.String(16))
    ca = db.Column(db.String(16))
    thal = db.Column(db.String(16))
    is_heart = db.Column(db.String(16))

    __mapper_args__ = {'concrete': True}
    
    # def __repr__(self):
    #     return '<Heart %r>' % self.userName



class Diabete(Table):
    __tablename__ = 'diabetes'


    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    glucose = db.Column(db.String(32))
    blood_presure = db.Column(db.String(32))
    DPF = db.Column(db.String(32))
    age = db.Column(db.String(32))
    is_diabete = db.Column(db.String(4))

    __mapper_args__ = {'concrete': True}
    
    # def __repr__(self):
    #     return '<Diabete %r>' % self.userName


class Admin(Table):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    adminName = db.Column(db.String(32))
    password = db.Column(db.String(32))
    __mapper_args__ = {'concrete': True}