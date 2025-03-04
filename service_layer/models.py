from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, validators

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database.db"

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "Leave_Request"
    employee_id = Column(String(50), primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    leave_type = Column(String(50))
    reason = Column(String(50))

# Create the table in the database
Base.metadata.create_all(engine)


class LeaveRequestForm(FlaskForm):
    employee_id = StringField('Employee ID', [validators.DataRequired()])
    start_date = DateField('Start Date', [validators.DataRequired()])
    end_date = DateField('End Date', [validators.DataRequired()])
    leave_type = StringField('Leave Type', [validators.DataRequired('ANNUAL', 'SICK', 'PERSONAL')]) 
    reason = StringField('Reason', [validators.DataRequired(), validators.Length(min=10)])
    submit = SubmitField('Submit')

class LeaveRequest(leave.Model):
    employee_id = leave.Column(leave.String(50), primary_key=True)
    start_date = leave.Column(leave.Date, primary_key=True)
    end_date = leave.Column(leave.Date, primary_key=True)
    leave_type = leave.Column(leave.String(50), primary_key=True)
    reason = leave.Column(leave.String(50), primary_key=True)
    # number_of_leave_days = leave.Column(leave.Integer)
    
    def __init__(self, employee_id, start_date, end_date, leave_type, reason):
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.leave_type = leave_type
        self.reason = reason
        # self.number_of_leave_days = (end_date - start_date).days + 1