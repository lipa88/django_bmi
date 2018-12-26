from django.db import models


class Bmi(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    height = models.FloatField()
    mass = models.FloatField()
    bmi_value = models.FloatField()
    
    class Meta:
        ordering = ['created'] 

#    @property
#    def bmi_value(self):
#        bmi_v = self.mass / ( self.height ** 2 )
#        return "%.2f" % bmi_v