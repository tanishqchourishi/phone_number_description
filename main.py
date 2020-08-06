import phonenumbers
# from test import numbers
from phonenumbers import geocoder
from phonenumbers import carrier

user_input=input("Enter a phone number with country code:")

ch_number=phonenumbers.parse(user_input,'CH')
print(geocoder.description_for_number(ch_number,"en")) #you can write any language here

service_number=phonenumbers.parse(user_input,"RO")
print(carrier.name_for_number(service_number,"en"))
