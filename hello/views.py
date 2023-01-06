from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def home(request):
    return render(request , 'home.html',{'name': 'tarun'})

def back(request):
    return render(request, 'home.html')

    
def add(request):
  p = float(request.POST['num1'])
  r = float(request.POST['num2'])
  f1 = request.POST['num3']
  f2 =request.POST['num4']
  l = int(request.POST['num5'])
  loan_date=datetime.strptime(f1,'%Y-%m-%d').date()
  ld=loan_date
  calc_date=datetime.strptime(f2,'%Y-%m-%d').date()

  t1=relativedelta(calc_date,loan_date)
  t=t1.years*12+t1.months
  k=p
  i=0
  #strs=[]
  dates=[]
  interests=[]
  amounts=[]
  for j in range(1,(t//l)+1):
    h=k*l*r/100
    k=k+h
    i=i+h
    loan_date=loan_date+relativedelta(months=+l)

    dates.append(loan_date)
    interests.append(round(h, 2))
    amounts.append(round(k, 2))

  m=((t%l)*r*round(k, 2))/100
  i=i+m
  i=round(i, 2)
  a=round(p+i,2)
  dates.append(calc_date)
  interests.append(m)
  amounts.append(a)
  pds=pd.DataFrame({
  'Date':dates,'Interest':interests,'Amount':amounts
  })
  str=pds.to_html(border=None ,col_space='100')

   
  return render(request,'result.html',{'amount':a, 'interest': i, 'strs': str,'ld': ld,'cd': calc_date })