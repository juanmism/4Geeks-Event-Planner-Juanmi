from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# USER

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# EVENTS

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(360), nullable=False)
    location = db.Column(db.String(240), nullable=False)
    guests = db.Column(db.String(240), nullable=False)
    image = db.Column(db.String(360), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)


    
    def __repr__(self):
        return f'<Events {self.id}>'  

    def serialize(self):
        return {
        "id": self.id,
        "title": self.title,
        "date": self.date,
        "time": self.time,
        "description": self.description,
        "location": self.location,
        "guests": self.guests,
        "image": self.image,
        "user_id": self.user_id,
    }

# CONTACTS

class Contacts(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __repr__(self):
        return f'<Contacts {self.id}>'  

    def serialize(self):
        return {
        "id": self.id,
        "email": self.email,
        "user_id": self.user_id,
    } 

#EVENT_GUESTS

class Event_Guests(db.Model):
    __tablename__ = 'event_guests'
    id = db.Column(db.Integer, primary_key=True)
    contact_email = db.Column(db.String(120), db.ForeignKey('contacts.email'), unique=True, nullable=False)
    contact = db.relationship(Contacts)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship(Events)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  
    user = db.relationship(User)

    def __repr__(self):
        return f'<Event_Guests {self.id}>'  

    def serialize(self):
        return {
        "id": self.id,
        "contact_email": self.contact_email,
        "contact": self.contact,
        "event_id": self.event_id,
        "event": self.event,
        "user_id": self.user_id,
    }