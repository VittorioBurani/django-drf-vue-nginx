from knox.models import AuthToken
from accounts.models import CustomUser


def delete_user_tokens(user:CustomUser):
    AuthToken.objects.filter(user=user).delete()
