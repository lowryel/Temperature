from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


"""
This program sees to convert temperature from Fahrenheit to Degree Celsius and from
Celsius to Kelvin
"""
# The program gets an input from the user in Fahrenheit


def result(request):
    try:
        Tf = request.POST['Fahrenheit']

        Tc = 5 / 9 * (float(Tf) - 32)

        Tk = Tc + 273.15
        context = {
            'fahren': Tf,
            'Celsius': Tc,
            'kelvin': Tk
        }
        return render(request, 'result.html', context)
    except:
        return HttpResponse('<h3>Please enter an integer or a float value</h3>')

#
