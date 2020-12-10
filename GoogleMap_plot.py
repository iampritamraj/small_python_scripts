def mapplot():
    """
    plot google map based on given latitude and longitude
    """
    from os import system as terminal
    import os 
    try:
        import gmplot 
        print("Enter latitude and longitude to print html Or Press Enter to use default")
        lat = input("latitude:")
        longitude = input("longitude:")
        if len(lat) == 0 and len(longitude) == 0:
        # Passing the center latitude and longitude
            gmap = gmplot.GoogleMapPlotter(13.0826802,80.2707184, 13)
        else:
            gmap = gmplot.GoogleMapPlotter(float(lat),float(longitude), 13)
        #save file in html formet
        filename = "plottedlocation.html"
        completename = os.path.join(os.path.expanduser('~'),'Desktop',filename)
        gmap.draw(completename)
        print("your file saved on desktop named as 'plottedlocation.html'")
    except ImportError:
        terminal("pip install gmplot")
        import gmplot 
        print("Enter latitude and longitude to print html Or Press Enter to use default")
        lat = input("latitude:")
        longitude = input("longitude:")
        if len(lat) and len(longitude) == 0:
        # Passing the center latitude and longitude
            gmap = gmplot.GoogleMapPlotter(13.0826802,80.2707184, 13)
        else:
            gmap = gmplot.GoogleMapPlotter(float(lat),float(longitude), 13)
        #save file in html formet
        filename = "plottedlocation.html"
        completename = os.path.join(os.path.expanduser('~'),'Desktop',filename)
        gmap.draw(completename)
        print("your file saved on desktop named as 'plottedlocation.html'")
    except Exception as err_msg:
        print("something went wrong:",err_msg)
if __name__ == "__main__":
    mapplot()