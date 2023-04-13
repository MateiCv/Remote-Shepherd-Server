#supabase= Clientul din app.py pe care il fac pentru supabase
import json
import geopy.distance
from flaskr.utils.cow_logic import *



def get_perimeter_id(id,supabase):

    cowId=get_cow_id(id,supabase)

    #select perimeter_id field from cow with cowId as a json 
    cowInstance= supabase.table("cows").select("perimeter_id").eq("id",cowId).execute()
    #parce json
    perimeter_data_json= json.loads(cowInstance.json())
    perimeter_id= perimeter_data_json['data'][0]['perimeter_id']

    return perimeter_id



def get_perimeter_data(id,supabase):
    perimeter_id=get_perimeter_id(id,supabase)
    
    #parce json 
    perimeter_instance= supabase.table("perimeters").select("radius","center_x","center_y").eq("id",perimeter_id).execute()
    perimeter_data_json= json.loads(perimeter_instance.json())

    return ( perimeter_data_json['data'][0]['radius'],perimeter_data_json['data'][0]['center_x'],perimeter_data_json['data'][0]['center_y'])
 


def in_perimeter(id,lat,lon,supabase):
    geo_data= get_perimeter_data(id,supabase)

    radius= geo_data[0]
    center_x= geo_data[1]
    center_y= geo_data[2]


    center_coordonates = (center_x, center_y)
    cow_coordonates = (lat, lon)
    distance = geopy.distance.geodesic(center_coordonates, cow_coordonates).m # distanta in metri


    if distance>=radius:
        update_cow_status(id,supabase,False)
        return 'outside_perimeter'
    else:
        update_cow_status(id,supabase,True)
        return 'inside_perimeter'
    
    

