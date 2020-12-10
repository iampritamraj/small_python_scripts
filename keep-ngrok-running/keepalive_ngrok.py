
import json
import subprocess
import time
from pathlib import Path
import atexit
import boto3
import requests
import datetime

#path where you have extracted ngrok execution file. Follow readme file to install on Pi
ngrokDir="/home/pi" 
#change the port which you want to tunnel through ngrok
port='5000'

#set it False if you don't want to update ngrok url to dynamoDB
#you don't need any of below variables in that case 
#also comment out updateDynamoDB function
useDynamo=True 
dynamodb = boto3.resource('dynamodb') 
dbPiNgRok = dynamodb.Table('PiNgrok')
deviceId="mypi"





localhost_url = "http://localhost:4040/api/tunnels"  # Url with tunnel details

def updateDynamoDB(ngrok_address):
    dbPiNgRok.update_item(
        Key ={
            'deviceId': deviceId
        },
        UpdateExpression='SET address = :address, createdOn=:createdOn',
        ExpressionAttributeValues={
            ':address': ngrok_address,
            ':createdOn': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        }
    )

def is_running():
    try:
        ngrok_req = requests.get(localhost_url).text
        ngrok_address = get_ngrok_url(ngrok_req)
        print("ngrok is already running {ngrok_address}".format(ngrok_address=ngrok_address))
        #check if expired
        r=requests.get(ngrok_address)
        if r.status_code == 402:
            return _run_ngrok()
        return ngrok_address
    except Exception as e: 
        print("exception",e)
        return _run_ngrok()

def get_ngrok_url(ngrok_req):
    j = json.loads(ngrok_req)
    tunnel_url = j['tunnels'][len(j['tunnels'])-1]['public_url']  # Do the parsing of the get
    #tunnel_url = tunnel_url.replace("http", "https")
    return tunnel_url


def _run_ngrok():
    global ngrokDir
    command = "ngrok"
    executable = str(Path(ngrokDir, command))
    ngrok = subprocess.Popen([executable, 'http', '-inspect=false','-bind-tls=true', port])
    atexit.register(ngrok.terminate)
    time.sleep(3)
    tunnel_url = requests.get(localhost_url).text  # Get the tunnel information
    ngrok_address =get_ngrok_url(tunnel_url)
    print("ngrok created  {ngrok_address}".format(ngrok_address=ngrok_address))
    #at this point you have new ngrok url. Do whatever you want. I used to store it in 
    #dynamodb so that I can use that data somewhere else where I need
    updateDynamoDB(ngrok_address)
    # keep the process running for 3450 seconds
    # You should adjust this time as you need. I have cron job on Pi which runs this 
    # python every hour (3600 seconds). So this script will treminate just 60 seconds
    # before cron executes again. Make sure to terminate this script before cron executes
    # next time. Otherwise you may have multiple ngrok listening to same port and lead to 
    # some inconsistent behavior
    time.sleep(3540) 
    return ngrok_address



is_running()
