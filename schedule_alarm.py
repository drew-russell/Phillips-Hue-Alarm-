import datetime, paramiko, time

class color:
   bold = '\033[1m'
   blue = '\033[94m'
   end = '\033[0m'
   red = '\033[91m'

#region Paramiko

#Define the variables required to SSH into a client
ssh = paramiko.SSHClient()

#Auto accepts unknown keys - do not use if connecting to an untrusted machine
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Update the variables to match your home setup
ssh.connect('$ip_address', username='$username', password='$password')

def run_command(command):
    #Set Standard In, Standard Output, and Standard Error for SSH to the exeucted command
    stdin,stdout,stderr = ssh.exec_command(command)



#endregion


print
print (color.bold + color.red + ' *** Schedule Phillips Hue Wake Up Time ***' + color.end)
print

print ('0  (Midnight)  1 (1:00 AM) ')
print ('2  (2:00 AM )  3 (3:00 AM) ')
print ('4  (4:00 AM )  5 (5:00 AM) ')
print ('6  (6:00 AM )  7 (7:00 AM) ')
print ('8  (8:00 AM )  9 (9:00 AM) ')
print ('10 (10:00 AM) 11 (11:00 AM) ')
print
print ('12 (  Noon  )  13 (1:00 PM ) ')
print ('14 (2:00 PM )  15 (3:00 PM ) ')
print ('16 (4:00 PM )  17 (5:00 PM ) ')
print ('18 (6:00 PM )  19 (7:00 PM ) ')
print ('20 (8:00 PM )  21 (9:00 PM ) ')
print ('22 (10:00 PM)  23 (11:00 PM) ')

now = datetime.datetime.now()

#the current month
month = now.month

#Tomorrows date
date = now.day

#Tomorrows day of the week where 1 = Monday, 2 = Tuesday, etc.
day_of_the_week = now.isoweekday()

#What hour to wake up at (miliary time)
print
tomorrow = raw_input(color.blue + 'Schedule for tomorrow (yes/no): ' + color.end)
wake_up_hour = raw_input(color.blue + 'Enter the wake up hour: ' + color.end)
wake_up_minute = raw_input(color.blue + 'Enter the wake up minute: ' + color.end)

if tomorrow == 'yes':
    date = date + 1
    day_of_the_week = day_of_the_week + 1


print

#Update the path to your bedroom_lighton.py script (i.e after 'python'
command = ("{ crontab -l -u pi; echo '%s %s %d %d %s python $Path/light_on.py'; } | crontab -u pi -")% (wake_up_minute, wake_up_hour,date
                                                                                               ,month, day_of_the_week)

run_command('crontab -r')
time.sleep(1)
run_command(command)
print
print (color.bold + color.red + ' *** Successfully scheduled Phillips Hue Wake Up Time ***' + color.end)
print ''


