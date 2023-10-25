import geocoder

def get_ip_geolocation():
    g = geocoder.ip('me')
    latlng = g.latlng
    return latlng

def main():
    latlng = get_ip_geolocation()

    print("IP Geolocation")
    print("---------------")
    print(f"Latitude: {latlng[0]}")
    print(f"Longitude: {latlng[1]}")

if __name__ == "__main__":
    main()
