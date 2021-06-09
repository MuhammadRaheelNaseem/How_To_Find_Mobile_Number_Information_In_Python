# First install this library on your machine
# Then import one by one
import phonenumbers  
from phonenumbers import carrier
from phonenumbers import geocoder

# Make variable for store your phone number here
phone_number = phonenumbers.parse("+923007045699")

# then print all kind of detail in here
print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
