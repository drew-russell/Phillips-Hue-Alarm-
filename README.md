# Phillips Hue Alarm
After having reliability issues with setting an alarm in the official [Phillips Hue app](https://itunes.apple.com/us/app/philips-hue/id557206189?mt=8) I decided to
create a Python script that will automatically turn on my Phillips Hue bulb at a certain hour by utilizing a [Linux cronjob](https://en.wikipedia.org/wiki/Cron). For this particular setup
I am utilizing a [Rasberry Pi](http://www.amazon.com/Raspberry-Pi-Model-Project-Board/dp/B00T2U7R7I/ref=sr_1_4?s=pc&ie=UTF8&qid=1453429240&sr=1-4&keywords=raspberry+pi) as my Linux server.

# Overview of the Scheduling System
The scheduling of an alarm utilizes two main files:

* schedule_alarm.py
* light_on.py

#### schedule_alarm.py

In order to make the process of creating the Linux cronjobs as easy as possible I have created an automation script that will SSH into your sever (Rasberry Pi in this case) and create the necessary cronjob. This script should be installed on a client machine (i.e your laptop) that has the ability to connect to your Linux server.

!(https://cloud.githubusercontent.com/assets/8610203/12501032/65b73e4c-c07e-11e5-8e6a-35dc396ac544.png)


The cronjobs will utilize the 24-hour clock so it you're like me and are not used to that format I have included a list of the 12-hour clock equivalents.

In order to update the script to work in your environment you will need to update the following:

* *Line 15*
```python
ssh.connect('$server_ip_address', username='$server_username', password='$server_password')
```

* *Line 72*
```python
command = ("{ crontab -l -u pi; echo '%s %s %d %d %s python $Path/light_on.py'; } | crontab -u pi -")
```

Please note that this script will also will also issue *crontab -r* which will remove all previously scheduled cronjobs (aka alarms) on your Linux server.

 #### light_on.py

This is the actual Python script that will interact with your Phillips Hue light bulb and tell it to turn on. In order to customize this script for you environment you will need to update the following variables:

* $Bridge_IP_Address
* $Bridge_API_username
* $SpecifcLightNumber

In you do not know these variables please review the official [Getting Started guide](http://www.developers.meethue.com/documentation/getting-started) from Phillips Hue.

This script also utilizes [qhue.py](https://github.com/quentinsf/qhue) which is a Python wrapper for the Phillips Hue API that was developed by Quentin Stafford-Fraser.

You will need both the light_on.py and qhue.py files in the same directory on your Linus Server.
