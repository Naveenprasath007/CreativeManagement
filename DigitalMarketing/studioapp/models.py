from django.db import models


class ssScriptdetails(models.Model):
    UserID = models.CharField(db_column='userid', primary_key=True, max_length=255)  # Field name made lowercase.
    prompt = models.TextField(db_column='prompt')   # Field name made lowercase.
    script1 = models.TextField(db_column='script1')   # Field name made lowercase.
    script2 = models.TextField(db_column='script2')   # Field name made lowercase.
    script3 = models.TextField(db_column='script3')   # Field name made lowercase.
    script4 = models.TextField(db_column='script4')   # Field name made lowercase.
    script5 = models.TextField(db_column='script5')   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ss_scriptdetails'


