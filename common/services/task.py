from common.repositories.factory import RepositoryFactory, RepoType
from common.models.task import Task
from app.helpers.exceptions import APIException

from common.services import PersonService


class TaskService:
    def __init__(self, config):
        self.config = config

        self.repository_factory = RepositoryFactory(config)
        self.task_repo = self.repository_factory.get_repository(RepoType.task)

        self.person_service = PersonService(config)

    def save_task(self, task: str, person_id: str)-> Task:

        task = Task(person_id=person_id, title=task, is_completed=False)

        return self.task_repo.save(task)

    def get_all_task(self):
        task = self.task_repo.get_many()
        return task

    def get_task_by_person_id(self, person_id: str):
        task = self.task_repo.get_many({"person_id": person_id})
        return task

    def get_task_by_id(self, entity_id: str):
        task = self.task_repo.get_one({"entity_id": entity_id})
        if not task:
            raise APIException("task does not exist")

        return task

    def delete_task_by_id(self, entity_id: str):
        task = self.get_task_by_id(entity_id)
        return self.task_repo.delete(task)

    def toggle_task(self, entity_id: str):
        task = self.get_task_by_id(entity_id)

        task.is_completed = not task.is_completed

        return self.task_repo.save(task)

    def update_task_by_id(self, entity_id: str, title: str):
        task = self.get_task_by_id(entity_id)

        task.title = title

        return self.task_repo.save(task)

    def set_task_completed(self, task: Task) -> Task:
        task.is_verified = True
        return self.save_task(task)
