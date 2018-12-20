from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger
from .forms import DetailsForm

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context=context)

def flight(request, flight_id):
    try :
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does npot exist")
    context = {
        "flight": flight,
        "passengers" : flight.Passenger.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context=context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    #Key error is when we use GET request or the form details aree not complete
    except KeyError:
        return render(request, "flights/error.html", {"message": "No Selection"})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger."})
    
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

def details(request):
    if request.method=="POST":
        form = DetailsForm(request.POST)
        if form.is_valid:
            details = form.save(commit=False)
            return HttpResponseRedirect('abcde', pk="xyz")
        #..........#   
        # we will use {% if user.is_authenticated %} bla-bla-bla {% endif %}
        # in html to check if the user is authenticated or not. 
    form = DetailsForm()
    return render(request, 'flights/details.html', {'form': form})