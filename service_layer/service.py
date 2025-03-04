from flask import Blueprint, request, abort, render_template, redirect, url_for
from werkzeug.exceptions import HTTPException, BadRequest
import json
from service_layer.models import LeaveRequestForm, User
import logging as log

leave_request = Blueprint('leave_request', __name__, url_prefix='/api/v1/leave-requests/')

@leave_request.route('', methods=['POST'])
def create_leave_request():
    try:
        leave_form = LeaveRequestForm(request.form)
        if request.method == 'POST' and leave_form.validate():
            payload = request.form
            payload = json.loads(payload)
            start_date = payload['start_date']
            end_date = payload['end_date']
           
            if start_date > end_date:
                raise BadRequest('Start date cannot be greater than end date')

        else:
            raise BadRequest('Invalid form data')    
        
        number_of_leave_days = (end_date - start_date).days + 1
        # check for any overlapping leave requests
        """
        * from sql get all leave requests for the employee using select query to get all leave requests for the employee
        * check if the applied leave request overlapps with any leave request
        * if yes then raise BadRequest('Leave request overlaps with existing leave request')
        """
        
        if number_of_leave_days > 14:
            raise BadRequest('Maximum consecutive leave days is 14')
        
    except BadRequest as e:
        log.error(e)
        abort(400)
    except HTTPException as e:
        log.error(e)
        abort(500)

@leave_request.route('<employee_id>', methods=['GET'])
def get_leave_requests(employee_id):
    try:
        render_template('leave_requests.html')
    except HTTPException as e:
        log.error(e)
        abort(500)