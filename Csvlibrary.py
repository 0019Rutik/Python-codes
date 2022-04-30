import csv
from gmplot import gmplot

# with open ('Route.csv','r')as f:
#     reader = csv.reader(f)

#     for row in reader:
#         lat = float(row[0])
#         long = float(row[1])
#         print(lat)
#         print(long)
#         print(lat+long)

gmp = gmplot.GoogleMapPlotter(28.689169,77.3224448,17)

#gmp.coloricon = "http://www.googlemapsmarker.com/v1/%s/"

with open('route.csv','r') as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        #  print(lat)
        #  print(long)
        #  print(lat+long)

        if (  k == 0):
            gmp.marker(lat,long,'yellow')
            k = 1
        else:
            gmp.marker(lat,long,'blue')
        
gmp.marker(lat,long,'red')

gmp.draw(("mymap.html"))

        
        