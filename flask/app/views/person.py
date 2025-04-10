from flask_restx import Namespace, Resource
from flask import request
from app.helpers.response import get_success_response, parse_request_body, validate_required_fields
from app.helpers.decorators import login_required
from common.app_config import config 
from common.services import AuthService, PersonService



# Create the organization blueprint
person_api = Namespace('person', description="Person-related APIs")


@person_api.route('/me')
class Me(Resource):
    
    @login_required()
    def get(self, person):
        return get_success_response(person=person)

@person_api.route('/change_name',
                  doc=dict(description="Update Person first name and last name "))
class UpdateName(Resource):
    @person_api.expect(
        {'type': 'object', 'properties': {
            'entity_id': {'type': 'string'},
            'first_name': {'type': 'string'},
            'last_name': {'type': 'string'},
        }}
    )
    @login_required()
    def put(self):
        parsed_body = parse_request_body(request, ['entity_id','first_name', 'last_name'])
        validate_required_fields(parsed_body)

        person_service = PersonService(config)

        person_obj = person_service.update_person_name_by_id(parsed_body["entity_id"], parsed_body["first_name"], parsed_body["last_name"])
        return get_success_response(person=person_obj)
