#supabase= Clientul din app.py pe care il fac pentru supabase
import json

def get_cow_id(id,supabase):
   #parce json
   collarInstance= supabase.table("collars").select("cow_id").eq("id",id).execute()
   data_json = json.loads(collarInstance.json())
   return data_json['data'][0]['cow_id']

def update_cow_location(id,lat,lon,supabase):
    
    cowId=get_cow_id(id,supabase)
    data = supabase.table("cows").update({"location_x": lat, "location_y": lon}).eq("id", cowId).execute()


def update_cow_status(id,supabase,inside):#inside or outside perimeter
    
    cow_id=get_cow_id(id,supabase)
    data = supabase.table("cows").update({"in_perimeter":inside}).eq("id", cow_id).execute()