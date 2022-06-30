from tortoise import fields
from tortoise.models import Model


class Dog(Model):
    id_dog = fields.IntField(pk=True)
    name = fields.CharField(max_length=15, description="Dog name")
    picture = fields.CharField(max_length=200, description="Dog picture", null=True)
    is_adopted = fields.BooleanField(default=True)
    create_date = fields.DatetimeField(auto_now_add=True)
    user_id = fields.ForeignKeyField("models.User", related_name="dogs", on_delete="CASCADE")

    class Meta:
        table = "dog"

    def __str__(self):
        return self.name
