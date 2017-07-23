# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import *


from .models import Cases
from .forms import *


def index(request):
    return render(request, 'adcalendar/index.html')

def addCase(request):
    if request.method == 'POST':
        form = addCaseForm(request.POST)      
        print form.is_valid()
        if form.is_valid():
            caseNumber = request.POST.get('case_number','')
            adName = request.POST.get('ad_name','')
            startDate = request.POST.get('start_date','')
            endDate = request.POST.get('end_date','')
            remarks = request.POST.get('remarks','')
            if Cases.objects.filter(case_number=caseNumber).exists():
			  form = addCaseForm()
			  return render(request , 'adcalendar/addCase.html' , {'exists':True,'form':form} )
                          
        
        obj = Cases(case_number = caseNumber, ad_name = adName, start_date = startDate, end_date = endDate, remarks=remarks  )
        obj.save()
        form = addCaseForm()
        return render(request , 'adcalendar/addCase.html' , {'is_added':True,'form':form} )
           
      
    else:
        form = addCaseForm()
		
    return render(request, 'adcalendar/addCase.html', {'form': form})	

def update(request):
    if request.method == 'POST':
        form = updateIfExist(request.POST)      
        print form.is_valid()
        if form.is_valid():
            caseNumber = request.POST.get('case_number','')
            
            if Cases.objects.filter(case_number=caseNumber).exists():
			    obj = Cases.objects.get(case_number=caseNumber)
			    case_number = obj.case_number
			    start_date = obj.start_date
			    end_date = obj.end_date
			    ad_name = obj.ad_name
			    remarks = obj.remarks
			    form = updateForm(initial={'case_number': caseNumber,'start_date': end_date,'ad_name':ad_name,'remarks':remarks})
			    return render(request , 'adcalendar/update.html' , {'is_exists':True,'form':form} )
            else:
                form = updateIfExist()
                return render(request, 'adcalendar/update.html', {'not_exists':True,'form':form} )
    else:
        form = updateIfExist()
    return render(request, 'adcalendar/update.html', {'form': form})	
	
	
def updateCase(request):
    if request.method == 'POST':
        form = updateForm(request.POST)      
        print "in update case view"
        if form.is_valid():
            caseNumber = request.POST.get('case_number','')
            adName = request.POST.get('ad_name','')
            startDate = request.POST.get('start_date','')
            endDate = request.POST.get('end_date','')
            remarks = request.POST.get('remarks','')             
            print "Is Valid"   
		
		
        obj = Cases(case_number = caseNumber, ad_name = adName, start_date = startDate, end_date = endDate, remarks=remarks  )
        obj.save()
        form = updateIfExist()
        return render(request , 'adcalendar/update.html' , {'is_updated':True,'form':form} )
	
def viewCase(request):
    if request.method == 'POST':
        form = viewForm(request.POST)      
        print form.is_valid()
        if form.is_valid():
            caseNumber = request.POST.get('case_number','')
            
            if Cases.objects.filter(case_number=caseNumber).exists():
                obj = Cases.objects.get(case_number=caseNumber)
                case_number = obj.case_number
                start_date = obj.start_date
                end_date = obj.end_date
                ad_name = obj.ad_name
                remarks = obj.remarks
				
                context = {'case' : obj}
			    
                return render(request , 'adcalendar/viewCase.html' , context )
            else:
                form = viewForm()
                return render(request, 'adcalendar/viewCase.html', {'not_exists':True,'form':form} )
    else:
        form = viewForm()
    return render(request, 'adcalendar/viewCase.html', {'form': form , 'first':True})
	
	