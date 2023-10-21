from django.db import models


class OtherDB(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'otherdb'
        app_label = 'myapp'


def create_entry():
    print("-------------------")
    instance = OtherDB(name="Bruce")
    instance.save(using='other_database')


# try:
#     create_entry()
# except Exception:
#     print("尚未創建table")
