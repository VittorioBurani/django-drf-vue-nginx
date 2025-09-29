from typing import Any
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
from custom.abc_field_validator import ViewAPIFieldValidator


class IntegerRangeValidator(ViewAPIFieldValidator):
    error_code = 'invalid_integer_range'

    def __init__(self, min_value=None, max_value=None, api:bool=False) -> None:
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(api)

    def get_help_text(self) -> str:
        '''Return error string for validation error'''
        return f"Value must be between {self.min_value} and {self.max_value}"

    def validate(self, field:Any) -> None:
        '''Validation method for a single field'''
        if not (self.min_value <= field <= self.max_value):
            self.raise_error()


semver_validator = RegexValidator(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$",
    _("Your string should be a valid SemVer.")
)
