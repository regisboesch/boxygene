from django.db import models

class Contacts(models.Model):
    title = models.ForeignKey('Titles', models.DO_NOTHING, blank=True, null=True)
    lastname = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    birthdaydate = models.DateField()
    weight = models.IntegerField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=45, blank=True, null=True)
    adress1 = models.CharField(db_column='Adress1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adress2 = models.CharField(db_column='Adress2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    np = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'contacts'


class Countries(models.Model):
    description = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return self.description	

class Titles(models.Model):
    description = models.CharField(max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'titles'
