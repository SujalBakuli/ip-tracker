#!/bin/bash/python

#IMEI number
#Google map

try:
    from ip2geotools.databases.noncommercial import DbIpCity
    from sys import argv
    import ipaddress
    import socket
    #import googlemaps
    from gmplot import gmplot
    from webbrowser import open_new_tab
    from pyfiglet import figlet_format
except:
    print('[+] Module Not Found!')


def loadingscreen():
    print(figlet_format('IP-Tracker'))

def marking_the_area(lat,lng):
    
    gmap = gmplot.GoogleMapPlotter(lat, lng, 10) 
    gmap.marker(lat, lng, 'red')
    gmap.draw("user_location_map.html")

    #opening in browser
    open_new_tab("user_location_map.html")

def ip_info(ipaddr):

    try:

        #converting domain -> ip (if domain is provided )
        ipaddr=socket.gethostbyname(ipaddr)
        
        if ipaddress.ip_address(ipaddr):

            #fetching the informations
            response=DbIpCity.get(ipaddr, api_key='free')

            #informations
            print(f'[+] ip-type: {type(ipaddress.ip_address(ipaddr))}')
            print(f'[+] ip_address: {response.ip_address}')
            print(f'[+] city: {response.city}')
            print(f'[+] region: {response.region}')
            print(f'[+] country: {response.country}')
            print(f'[+] latitude: {response.latitude}')
            print(f'[+] longitude: {response.longitude}')

            return response.latitude,response.longitude
        
    except:
        print('[+] Check the IP Address!')



if __name__=='__main__':
    loadingscreen()
    lat,lng=ip_info(str(argv[1]))   #to get basic info about the ipaddress/domain
    marking_the_area(lat,lng)
