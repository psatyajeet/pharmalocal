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
from pygeocoder import Geocoder
import simplejson, urllib
#from django.contrib.gis.utils import GeoIP
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
    key = 'AIzaSyBOebFrowSFSnB7V4zeNGagd9hTG4ydq8M'
    # Find these values at https://twilio.com/user/account
    account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
    auth_token = "423fb88dee17931cdb345671ed665069"
    client = TwilioRestClient(account_sid, auth_token)
    
    order=Order.objects.get(pk=100)

    ids=request.GET.lists()[0][1]
    results=[]
    for id in ids:
        referencenum=id
        URL= 'https://maps.googleapis.com/maps/api/place/details/json?reference='+ referencenum+ '&sensor=true&key='+ key
        results.append(simplejson.load(urllib.urlopen(URL)))
    make_call(results[0]['result']['formatted_phone_number'], order)
    return render_to_response('orders/confirm.html', {'results': results})
    
def show_nearby(order):

    key = 'AIzaSyBOebFrowSFSnB7V4zeNGagd9hTG4ydq8M'
    gmaps = GoogleMaps(key)
    address = order.zipcode
    lat, lng= (40.337904,-74.587335)
    lat, lng=Geocoder.geocode(address)[0].coordinates
    #lat, lng = gmaps.address_to_latlng(address)
    
    radius = '5000'
    
    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) + ',' + str(lng) + '&radius=' + radius + '&types=pharmacy&sensor=false&key=' + key

    #print URL
    #r=requests.get(URL)
    #r.json()
    
    result = simplejson.load(urllib.urlopen(URL))
    return (result, lat, lng)

    
def make_call(number, order):
    # Get these credentials from http://twilio.com/user/account
    account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
    auth_token = "423fb88dee17931cdb345671ed665069"
    client = TwilioRestClient(account_sid, auth_token)
 
    # Make the call
    number="+16099370216"
    firstname=order.first_name
    myurl="http://twimlets.com/menu?Message=This%20is%20a%20call%20from%20pharma%20save.%20The%20customers%20last%20name%20is%20"+order.last_name+"%20and%20the%20first%20name%20is%20"+order.first_name+".%20The%20order%20date%20is%20April%202nd%202013.%20The%20customer's%20phone%20number%20is%20i"+str(order.phone_number)+"%20.Their%20medication%20is%20"+order.medication+".%20Their%20prescriber's%20name%20is%20Shiwei%20Tong.%20The%20prescriber's%20phone%20number%20is%20i"+str(order.prescriber_phone_number)+".%20Press%201%20to%20repeat%20the%20order.%20Press%202%20to%20confirm%20the%20order.%20&Options%5B1%5D=%2FAC4f13c39e2e5b0cf1fd1017be8fd944a7%2Ffirsttry&Options%5B2%5D=%2FAC4f13c39e2e5b0cf1fd1017be8fd944a7%2Fconfirm&"
    call = client.calls.create(to=number,  # Any phone number
                               from_="+19173380736", # Must be a valid Twilio number
                               url=myurl)
    #print call.sid
    
def send_text(number):
    # Find these values at https://twilio.com/user/account
    account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
    auth_token = "423fb88dee17931cdb345671ed665069"
    client = TwilioRestClient(account_sid, auth_token)
    
    print number
    message = client.sms.messages.create(to="+16099370216", from_="+19173380736",
                                         body="Take it easy boys!")
