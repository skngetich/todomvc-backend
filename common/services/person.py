from common.repositories.factory import RepositoryFactory, RepoType
from common.models.person import Person
from common.app_logger import logger
from app.helpers.exceptions import InputValidationError, APIException


class PersonService:

    def __init__(self, config):
        self.config = config

        from common.services import EmailService
        self.email_service = EmailService(config)

        self.repository_factory = RepositoryFactory(config)
        self.person_repo = self.repository_factory.get_repository(RepoType.PERSON)

    def save_person(self, person: Person):
        person = self.person_repo.save(person)
        return person

    def get_person_by_email_address(self, email_address: str):
        email_obj = self.email_service.get_email_by_email_address(email_address)
        if not email_obj:
            return
        
        person = self.person_repo.get_one({"entity_id": email_obj.person_id})
        return person

    def get_person_by_id(self, entity_id: str):
        person = self.person_repo.get_one({"entity_id": entity_id})
        return person
    def update_person_name_by_id(self, entitiy_id: str, first_name:str, last_name:str)-> Person:
        person_obj: Person = self.get_person_by_id(entity_id=entitiy_id)
        if not person_obj:
            raise APIException("User does not exist") 
        
        person_obj.first_name = first_name
        person_obj.last_name = last_name

        return self.person_repo.save(person_obj)
        