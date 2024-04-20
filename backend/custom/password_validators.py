import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class NumberValidator(object):
    '''Validator for "at least 1 number"'''
    # RegEx validation:
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                self.get_help_text(),
                code='password_no_number',
            )

    # Help Text:
    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9.")


class UppercaseValidator(object):
    '''Validator for "at least 1 uppercase letter"'''
    # RegEx validation:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                self.get_help_text(),
                code='password_no_upper',
            )

    # Help Text:
    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class SymbolValidator(object):
    '''Validator for "at least 1 symbol"'''
    # RegEx validation:
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                self.get_help_text(),
                code='password_no_symbol',
            )

    # Help Text:
    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
