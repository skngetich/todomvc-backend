from dataclasses import dataclass, field
from typing import Optional
import string

from rococo.models import VersionedModel


@dataclass
class Task(VersionedModel):
    """ Task method model """ 
    person_id: str = None
    title: str = None
    is_completed: Optional[bool] = False
