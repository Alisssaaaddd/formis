from django.contrib import admin
from django import forms
from django_jalali.forms import jDateField, jDateInput
from django_jalali.admin.widgets import AdminjDateWidget
from django_jalali.admin.filters import JDateFieldListFilter

from .models import Expense, Income
from django_jalali.db import models as jmodels


class ExpenseForm(forms.ModelForm):
    date = jDateField(widget=AdminjDateWidget) 

    class Meta:
        model = Expense
        fields = '__all__'



class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['text', 'amount', 'date', 'user']
    list_filter = (('date', JDateFieldListFilter),) 
    form = ExpenseForm 


    formfield_overrides = {
        jmodels.jDateField: {'widget': AdminjDateWidget},  
    }


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income)
