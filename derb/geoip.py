import requests
import json

print(f"""
████████╗██████╗  █████╗  ██████╗██╗  ██╗        ██╗██████╗     
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝        ██║██╔══██╗    
   ██║   ██████╔╝███████║██║     █████╔╝         ██║██████╔╝    
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗         ██║██╔═══╝     
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║██║         
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝         
                                                                
=============================================================
Github: https://github.com/bimasena321
Youtube: bima020
created by: bima020
""")

i = input(f"Masukan ip addres: ")
key = '1a9dea3fe1404a4e920b79b3bd83bbff'
url = f'https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={i}'
url_requests = requests.get(f"{url}")
if url_requests.status_code == 200:
    data = json.loads(url_requests.text)
    print(f"ip: ",data['ip'])
    print(f"negara: ", data['country_name'])
    print(f"ibukota: ", data['country_capital'])
    print(f"kecamatan: ", data['district'])
    print(f"provinsi: ", data['state_prov'])
    print(f"kota: ", data['city'])
    print(f"zip_code: ", data['zipcode'])
    print(f"latitude && logtitude: ", data['latitude'],",", data['longitude'])
    print(f"kode_telpon: ", data['calling_code'])
    print(f"kode_internet: ", data['country_tld'])
    print(f"isp: ", data['isp'])
    print(f"mata uang: ",data[f'currency'])
    print(f"zona waktu: ",data['time_zone'])
    print(f"kontinen: ",data['continent_code'])