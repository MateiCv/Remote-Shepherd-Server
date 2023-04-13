#supabase= Clientul din app.py pe care il fac pentru supabase


def update_collar(id,lat,lon,supabase):#location update for collar 
    data = supabase.table("collars").update({"location_x": lat, "location_y": lon}).eq("id", id).execute()
