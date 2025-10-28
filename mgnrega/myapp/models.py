from django.db import models

# Create your models here.
class MgnregaRecord(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    total_individuals_worked = models.IntegerField()
    total_households_worked = models.IntegerField()
    average_days_of_employment_provided_per_Household = models.IntegerField()
    average_wage_rate_per_day_per_person = models.DecimalField(max_digits=10, decimal_places=8)
    number_of_completed_works = models.IntegerField()
    number_of_ongoing_works = models.IntegerField()
    women_persondays = models.IntegerField()
    sc_persondays = models.IntegerField()
    st_persondays = models.IntegerField()
    wages = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.state} - {self.district}"