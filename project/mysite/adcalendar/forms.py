from django import forms
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminDateWidget

class viewForm(forms.Form):
    case_number = forms.IntegerField(label=mark_safe('<br />case_number'))

class addCaseForm(forms.Form):
    case_number = forms.IntegerField(label=mark_safe('<br />case_number'))
    ad_name = forms.CharField(label=mark_safe('<br />ad_name'))
    start_date = forms.DateField(label=mark_safe('<br />start_date' ) , widget = AdminDateWidget)
    end_date = forms.DateField(label=mark_safe('<br />end_date') , widget = AdminDateWidget)
    remarks = forms.CharField(label=mark_safe('<br />remarks'))

class updateIfExist(forms.Form):
    case_number = forms.IntegerField(label=mark_safe('<br />case_number'))
	
class updateForm(forms.Form):
    case_number = forms.IntegerField(label=mark_safe('<br />case_number'))
    ad_name = forms.CharField(label=mark_safe('<br />ad_name'))
    start_date = forms.DateField(label=mark_safe('<br />start_date' ) , widget = AdminDateWidget)
    end_date = forms.DateField(label=mark_safe('<br />end_date') , widget = AdminDateWidget)
    remarks = forms.CharField(label=mark_safe('<br />remarks'))