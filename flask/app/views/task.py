from flask_restx import Namespace, Resource
from flask import request
from app.helpers.response import (
    get_success_response,
    parse_request_body,
    validate_required_fields,
)
from app.helpers.decorators import login_required
from common.app_config import config
from common.services import AuthService, TaskService


# Create the task blueprint
task_api = Namespace("task", description="Task-related APIs")


@task_api.route("")
class TaskList(Resource):
    @login_required()
    def get(self, person):

        task_service = TaskService(config)
        tasks = task_service.get_task_by_person_id(person.entity_id)

        return get_success_response(tasks=tasks)


    @task_api.expect(
        {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
            },
        }
    )
    @login_required()
    def post(self, person):
        parsed_body = parse_request_body(request, ["title"])
        validate_required_fields(parsed_body)

        task_service = TaskService(config)

        task = task_service.save_task(
            task=parsed_body["title"],
            person_id=person.entity_id,
        )

        return get_success_response(task=task)


    @task_api.expect(
        {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "entity_id": {"type": "string"},
            },
        }
    )
    @login_required()
    def put(self):
        parsed_body = parse_request_body(request, ["entity_id", "title"])
        validate_required_fields(parsed_body)

        task_service = TaskService(config)

        person_obj = task_service.update_task_by_id(
            entity_id=parsed_body["entity_id"], title=parsed_body["title"]
        )
        return get_success_response(person=person_obj)


@task_api.route(
    "/<string:entity_id>", doc=dict(description="Delete task by id")
)
class TaskItem(Resource):
    @login_required()
    def delete(self, entity_id):
        task_service = TaskService(config)

        deleted_task_obj = task_service.delete_task_by_id(entity_id)
        return get_success_response(
            message=f"task with id: { deleted_task_obj.entity_id} deleted"
        )


@task_api.route(
    "/<string:entity_id>/toggle", doc=dict(description="toggle task to complete or incomplete")
)
class ToggleTask(Resource):
    @login_required()
    def put(self, entity_id):
        task_service = TaskService(config)

        task_service.toggle_task(entity_id)
        return get_success_response(message="task status changed")
