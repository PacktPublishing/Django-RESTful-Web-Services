from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Replace user01 with the name you configured for this user
user = User.objects.get(username="user01")
token = Token.objects.create(user=user)
print(token.key)
