from tortoise import fields
from tortoise.models import Model


class User(Model):
    id_user = fields.IntField(pk=True)
    name = fields.CharField(max_length=15, description="User name")
    last_name = fields.CharField(max_length=15, description="User last name")
    email = fields.CharField(max_length=25, description="User email")
    username = fields.CharField(max_length=20, null=True)
    hashed_password = fields.CharField(max_length=200, null=True)

    class Meta:
        table = "user"

    def __str__(self):
        return self.name
