from qhue import Bridge

b = Bridge("$Bridge_IP_Address", '$Bridge_API_username')

lights  = b.lights


#Updated with the number of the light in question
b.lights[$SpecifcLightNumber].state(on=True, bri=200)

