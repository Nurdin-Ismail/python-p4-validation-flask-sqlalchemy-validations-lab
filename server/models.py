from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('name')
    def validate_name(self, key, name):
        if len(name) == 0:
            raise ValueError("Name must have a value")
        author = Author.query.filter_by(name=name).first()
        if author:
            raise ValueError("Author name not unique")
        return name

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone_number should contain exactly 10 digits")
        else:
            return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    
    
    
    @validates("content")
    def validate_content(self, key, content):
        if not len(content) >= 250:
            raise ValueError("Post content is at least 250 characters long.")
        else:
            return content

    @validates("summary")
    def validate_summary(self, key, summary):
        if not len(summary) < 250:
            raise ValueError("Post summary is a maximum of 250 characters.")
        else:
            return summary

    @validates("category")
    def validate_category(self, key, category):
        if not category in ("Fiction", "Non-Fiction"):
            raise ValueError("Post category is either Fiction or Non-Fiction.")
        else:
            return category
        
        
    @validates('title')
    def is_clickbait_title(self, key, title):
       good_titles =  ["Won't Believe", "Secret", "Top", "Guess"]
       for good_title in good_titles:
           if good_title not in title:
               raise ValueError('Make it clickable')
        
        
    
   


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
