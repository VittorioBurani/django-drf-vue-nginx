import abc
from typing import Any
from django.core.exceptions import ValidationError as ViewValidationError
from rest_framework.serializers import ValidationError as APIValidationError


##################
### Interfaces ###
##################

class ViewAPIFieldValidator(abc.ABC):
    '''Interface for View/API single field validators'''
    error_code:str

    def __init__(self, api:bool) -> None:
        '''Common constructor for all validators'''
        self.validation_error = APIValidationError if api else ViewValidationError

    @abc.abstractmethod
    def get_help_text(self) -> str:
        '''Return error string for validation error'''
        pass

    @abc.abstractmethod
    def validate(self, field:Any) -> None:
        '''Validation method for a single field'''
        pass

    def raise_error(self) -> None:
        '''Raise validation error'''
        raise self.validation_error(self.get_help_text(), self.__class__.error_code)


class ViewAPIMultiFieldValidator(abc.ABC):
    '''Interface for View/API single field validators'''
    error_code:str

    def __init__(self, api:bool, *args, **kwargs) -> None:
        '''Common constructor for all validators'''
        self.validation_error = APIValidationError if api else ViewValidationError

    @abc.abstractmethod
    def get_help_text(self) -> str:
        '''Return error string for validation error'''
        pass

    @abc.abstractmethod
    def validate(self, *args, **kwargs) -> None:
        '''Validation method for multiple fields'''
        pass

    def raise_error(self) -> None:
        '''Raise validation error'''
        raise self.validation_error(self.get_help_text(), self.__class__.error_code)
