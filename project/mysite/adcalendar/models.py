# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

  
class Cases(models.Model):
    case_number = models.IntegerField(primary_key = True)
    ad_name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    remarks = models.TextField()

