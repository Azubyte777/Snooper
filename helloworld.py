import subprocess
from os.path import join, expanduser
from pathlib import Path
from zipfile import ZipFile
import os

# Position where the time of login is
TIME_POS = 14

# Use notify-send shell command to create a security notification
def send_notification(message):
	notification = "notify-send '" + message + "'"
	subprocess.Popen(notification, shell=True)

# Get detailed list of current processes running
def get_processes():
	# Run a shell command and get results
	cmd = 'ps -ef|grep ^$USER'
	process_result = subprocess.check_output(cmd, shell=True)#history command is set to not work in scripts for some godforsaken reason
	file_to_send = open('processes.txt', 'w')
	file_to_send.write(str(process_result, 'UTF-8'))
	file_to_send.close()
	

# Get the time of user log in
def get_time():
	# Run a shell command and get results
	finger_result = subprocess.check_output('finger')
	finger_result = str(finger_result, 'UTF-8')
	file_two = open('the_rest.txt', 'w')
	file_two.write(finger_result)
	print(finger_result)

	# Parse results for time logged in
	parse_result = finger_result.split()
	time_logged_in = parse_result[TIME_POS]
	file_two = open('the_rest.txt', 'w')
	file_two.write("Time logged in: " + time_logged_in + "\n")
	file_two.close()
	print(time_logged_in)

	return ("Time logged in: " + time_logged_in)

# Get IP of user
def get_ip():
	# Run a shell command and get results
	ifconfig_result = subprocess.check_output('ifconfig')
	ifconfig_result = str(ifconfig_result, 'UTF-8')
	print(ifconfig_result)
	file_two = open('the_rest.txt', 'a')
	file_two.write(ifconfig_result)

	# Parse results to find IPv4 and IPv6 addresses
	parse_result = ifconfig_result.split()
	ip4_index = parse_result.index("inet")
	ip6_index = parse_result.index("inet6")
	ip4 = parse_result[ip4_index + 1]
	ip6 = parse_result[ip6_index + 1]

	
	file_two.write("IP4: " + ip4 + "\nIP6: " + ip6)
	file_two.close()
	return ("IP4: " + ip4 + "\nIP6: " + ip6)

#returns recent commands used
def get_history():

  file_two = open('the_rest.txt', 'a')
  file_two.write("\n\nThe most recent commands used this session:\n")
  with open(join(expanduser('~'), '.zsh_history'), 'r') as f:
    for line in f:
        file_two.write(line)
  file_two.close()
  
get_processes()
send_notification(get_time())
send_notification(get_ip())
get_history()

# Create a ZipFile Object
with ZipFile('zipfile.zip', 'w') as zip_object:
   # Adding files that need to be zipped
   zip_object.write('processes.txt')
   zip_object.write('the_rest.txt')


# Check to see if the zip file is created
if os.path.exists('zipfile.zip'):
   print("ZIP file created")
else:
   print("ZIP file not created")
