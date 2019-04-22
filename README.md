# GTConnect

```
Class: CS 6675 Advanced Internet Computing, College of Computing, Georgia Institute of Technology

Professor & Project Guide: Dr. Ling Liu(lingliu@cc.gatech.edu)

Authors:  Sathish Sampath,
	    Jenita Lydia Jebasingh(jenita.lydia17@gmail.com),
	    Sai Tadikonda(saitadikonda001@gmail.com),
	    Sreyas Sriram(sreyas28@gmail.com)

Demo : http://advertiser-gt-aic.herokuapp.com/advertisements

```

## Getting Started

Install Anaconda, if not available


Create the environment from the environment.yml file:

	conda env create -f environment.yml

Activate the Environment

	activate GTConnect

To Start the server

	python my_app_name.py

## Running

The server will run in the localhost(127.0.0.1:5000)

Visualize the existing spatial alarms using link

	http://127.0.0.1:5000/advertisements

To Add an Event

	http://127.0.0.1:5000/events

To Add an Emergency

	http://127.0.0.1:5000/emergency

To Add an Advertisement

	http://127.0.0.1:5000/advertise

To Delete User Spatial Alarm Cache

	http://127.0.0.1:5000/clear_user_ad

API to request Spatial alarms

	http://127.0.0.1:5000/userlocation?lat=<lattidue value> &long=<longitutde value>&user=<unique user id>

Response is JSON

If running in another url, replace `127.0.0.1:5000`, with the respective website url and port number



###### Contact the authors for the Secret Key.





