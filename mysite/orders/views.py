# Create your views here.
from django.template import Context, loader, RequestContext
from orders.models import Order, OrderForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from twilio.rest import TwilioRestClient
from googlemaps import GoogleMaps
import simplejson, urllib

import requests

def index(request):
    return render_to_response('orders/index.html')

def new_prescription(request):
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            (places, lat, lng)=show_nearby(order)
            
            return render_to_response('orders/choose.html', {'form': form, 'places': places, 'lat': lat, 'lng': lng})
        else:
            return render_to_response('orders/new.html', {
            'form': form, },context_instance=RequestContext(request))
            
        #return render_to_response('orders/index.html') # Redirect after POST
    else:
        form = OrderForm() # An unbound form
    
    return render_to_response('orders/new.html', {
            'form': form, },context_instance=RequestContext(request))
            
def choose_location(request):
    
    
    # Find these values at https://twilio.com/user/account
    account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
    auth_token = "423fb88dee17931cdb345671ed665069"
    client = TwilioRestClient(account_sid, auth_token)
    
    
    return HttpResponse(request.GET.lists())
    
    #message = client.sms.messages.create(to=order.phone_number, from_="+19173380736", body=order.medication)
    #return render_to_response('orders/confirm.html', {'form': form, 'places': places, 'lat': lat, 'lng': lng})
    
def show_nearby(order):

    key = 'AIzaSyBOebFrowSFSnB7V4zeNGagd9hTG4ydq8M'
    gmaps = GoogleMaps(key)
    address = order.zipcode
    lat, lng= (40.337904,-74.587335)
    #lat, lng = gmaps.address_to_latlng(address)
    
    radius = '5000'

    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) + ',' + str(lng) + '&radius=' + radius + '&types=pharmacy&sensor=false&key=' + key

    #print URL
    r=requests.get(URL)
    r.json()
    
    result = simplejson.load(urllib.urlopen(URL))
 
    return (result, lat, lng)

    
def make_call(order):
    # Get these credentials from http://twilio.com/user/account
    account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
    auth_token = "423fb88dee17931cdb345671ed665069"
    client = TwilioRestClient(account_sid, auth_token)
 
    # Make the call
    call = client.calls.create(to="+19178265606",  # Any phone number
                               from_="+19173380736", # Must be a valid Twilio number
                               url="http://twimlets.com/message?Message%5B0%5D=Are%20you%20from%20Columbia%3F%20If%20yes%20press%201&Message%5B1%5D=Awesome!!%20%20%20")
    print call.sid
