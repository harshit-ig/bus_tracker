import time
from threading import Thread
import requests
import os
from flask import Flask
from multiprocessing import Process


phone = os.environ['phone']
schoolcode = os.environ['schoolcode']

link = ''
app = Flask('')

@app.route('/')
def home():
    global link
    returnlink = f'''
    <head><title>Bus Tracker(S9)</title><meta name='theme-color' content= '#101010'></head>
    
    
    
    <style>
html,
body {{
    margin: 0;
    padding: 0;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    background: #101010;
    z-index: 0;
}}

.glow-on-hover {{
    width: 220px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
}}

.glow-on-hover:before {{
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}}

.glow-on-hover:active {{
    color: #000
}}

.glow-on-hover:active:after {{
    background: transparent;
}}

.glow-on-hover:hover:before {{
    opacity: 1;
}}

.glow-on-hover:after {{
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}}

@keyframes glowing {{
    0% {{ background-position: 0 0; }}
    50% {{ background-position: 400% 0; }}
    100% {{ background-position: 0 0; }}
}}

#button{{height:70px;
width:210px;}}



	.light-background{{
			width: 400px;
    		height: 200px;
   			margin: auto;
   			background-color: black;
   			position: relative;
		}}
		.breath-light{{
			width: 400px;
		    height: 20px;
		    position: absolute;
    		opacity: 0.3;
    		
		}}
		.star-breath{{
			opacity: 0.1;
			animation:breath 3s ease-in-out infinite;/* IE10, Firefox and Opera, IE9 and earlier versions do not support*/
			-webkit-animation:breath 3s ease-in-out infinite;/*Safari and Chrome*/
		}}
		@keyframes breath {{
		    from {{opacity: 0.3;}}/* The opacity when the animation starts*/
		    50% {{opacity: 1;}}/* The opacity of the animation at 50%*/
		    to {{opacity: 0.3;}}/* The opacity at the end of the animation*/   
		}}
		 
		@-webkit-keyframes breath {{
		    from {{opacity: 0.3;}}/* The opacity when the animation starts*/
		    50% {{opacity: 1;}}/* The opacity of the animation at 50%*/
		    to {{opacity: 0.3;}}/* The opacity at the end of the animation*/
		}}
.bottomright {{ position: fixed; bottom: 5px; right: 5px; text-align: right; color:#00FF78;  }}

.mainmap{{
 margin-top: 5em;

    background-color: #fff;

    box-shadow: 0px 0px 50px 10px #202020;
}}


.block {{
  position: relative;
  margin: 70px auto 0;
  background: linear-gradient(0deg, #000, #272727);
}}

.block:before, .block:after {{
  content: '';
  position: absolute;
  left: -2px;
  top: -2px;
  background: linear-gradient(45deg, #fb0094, #0000ff, #00ff00,#ffff00, #ff0000, #fb0094, 
    #0000ff, #00ff00,#ffff00, #ff0000);
  background-size: 400%;
  width: calc(100% + 4px);
  height: calc(100% + 4px);
  z-index: -1;
  animation: steam 20s linear infinite;
}}

@keyframes steam {{
  0% {{
    background-position: 0 0;
  }}
  50% {{
    background-position: 400% 0;
  }}
  100% {{
    background-position: 0 0;
  }}
}}

.block:after {{
  filter: blur(20px);
}}





</style>
<script> 
function refreshPage(){{
    window.location.reload();
}}
  </script>




<center>
<div class='block'>
<div class="mapouter"><div class="gmap_canvas"><iframe width="800" height="800" id="gmap_canvas" src="{link}&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://fmovies-online.net">fmovies</a><br><style>.mapouter{{position:relative;text-align:right;height:800px;width:800px;}}</style><a href="https://www.embedgooglemap.net">how to copy and paste google maps</a><style>.gmap_canvas {{overflow:hidden;background:none!important;height:800px;width:800px;}}</style></div></div>

</div>

<br><br>
<br><br><button id= 'button' class="glow-on-hover" type="button" onClick="refreshPage()"><h1>REFRESH</h1></button></center> 

			<div class="breath-light star-breath bottomright">
   Website Developed By Harshit Singh
			</div>
	

'''
    return (returnlink)

def run():
    app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
    t = Process(target = run())
    while True:
        t.start()
        time.sleep(30)
        t.terminate()
        t.join()

url = "http://parentgenericappws.xitixworld.com/app_json_param.asmx?op=GetRouteMap_JSON"


headers = {'content-type': 'text/xml'}
    
body = f'<?xml version="1.0" encoding="UTF-8"?><v:Envelope xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:d="http://www.w3.org/2001/XMLSchema" xmlns:c="http://schemas.xmlsoap.org/soap/encoding/" xmlns:v="http://schemas.xmlsoap.org/soap/envelope/"><v:Header /><v:Body><GetRouteMap_JSON xmlns="http://tempuri.org/" id="o0" c:root="1"><jsonString i:type="d:string">{{MobileNo:"{phone}",SchoolCode:"{schoolcode}"}}</jsonString></GetRouteMap_JSON></v:Body></v:Envelope>'

alive = Thread(target=keep_alive)
alive.start()
while True:
    response = requests.post(url,data=body,headers=headers)

    
    textval = response.text.strip()
    ptn = textval.split("\n")
    ptn = ptn[4:-3]
    dic = {}

    for i in ptn:
        a, b = i.split(":",1)
        a, b = a.strip('" '), b.strip(' ", \r')
        dic[a] = b
        
    coordinates = str(dic.get("pickupbuslocation"))
    link = f'https://maps.google.com/maps?q={coordinates}'
    time.sleep(10)