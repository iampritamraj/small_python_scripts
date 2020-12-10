# Keep ngrok running forever on Raspberry Pi
Keep ngrok running forever on Raspberry Pi. If you are not a paid user of ngrok then 
your ngrok session expires in 8 hours. You need to restart the ngrok process to obtain 
new address. Here I am going to show you how you can keep your ngrok session running 
forever. 

**Please note, this is a hack and probably you should be good if you are prototyping something 
for your own such as home automation etc. Please consider paid subscription of ngrok if you are
thinking to use it in production environment or commercial use.**

![iot](https://user-images.githubusercontent.com/9275193/51857830-3ef9ab80-2301-11e9-955f-96a706c52380.png)


### Install ngrok on Raspberry Pi

SSH into your Raspberry Pi or open terminal on your Raspberry pi.

```
cd /home/pi

sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip unzip ngrok-stable-linux-arm.zip
sudo chmod +x ./ngrok
./ngrok help
```
If everything goes fine, you should see ngrok help instruction printed on your terminal.

Copy both keepalive_ngrok.py and keepalive_ngrok.sh file to /home/pi directory.
Grant execution permission on both the files

```
sudo chmod +x keepalive_ngrok.py
sudo chmod +x keepalive_ngrok.sh
```

### Setup cron job to execute the shell script
We are going to setup our cron job to execute the shell script every our at 59 minutes. If you want to change the schedule, please check _run_ngrok method in keepalive_ngrok.py

```
crontab -e
```

Then add following entries to the crontab, save and exit. 

```
59 * * * * sh /home/pi/keepalive_ngrok.sh &
@reboot sh /home/pi/keepalive_ngrok.sh &
```
