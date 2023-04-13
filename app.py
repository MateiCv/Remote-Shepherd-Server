from dotenv import load_dotenv
load_dotenv()
from flaskr.utils.collar_logic import *
from flaskr.utils.cow_logic import *
from flaskr.utils.perimeter_logic import *
import os
from supabase import create_client
from flask import Flask, request

#app setup
app= Flask(__name__)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


@app.route('/locations',methods=['POST'])
def default():
   try:  
    #request parcing 
    data= request.get_json()# requestul 
    lat= data['lat']
    lon= data['lon']
    id= data['collarId'] # collar id

    #performing actions 
    update_cow_location(id,lat,lon,supabase)
    update_collar(id,lat,lon,supabase)
    
    return in_perimeter(id,lat,lon,supabase)
   
   except Exception as e:
    return str(e)



if __name__== "__main__":
    app.run(debug=True)

