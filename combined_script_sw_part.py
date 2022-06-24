'''
    Project: Universal IR Remote
    Created on: 15-06-2022
    Last Modified on: 24-06-2022
    Project Info.: Internship Project 2022(Renesys Power systems Pvt.Ltd.)
'''

######################################################################################################################
################################################ IMPORTING DEPENDECIES ###############################################
######################################################################################################################

import paho.mqtt.client as mqttclient
import time
import mysql.connector

######################################################################################################################
################################################# DEFINING VARIABLES #################################################
######################################################################################################################

send_message = ""  # empty message string to store the message to be sent to the broker
isNotFound = True  # variable that use to indicate whither query is found or not in database

######################################################################################################################
############################################## CONNCTION TO THE DATABASE #############################################
######################################################################################################################

mydb = mysql.connector.connect(host="localhost", user="keyur", passwd="keyur@0212", database="irDB")  # connect to irDB database by providing database user id, password and database name
mycursor = mydb.cursor()  # cursor that points to database row
mycursor.execute("select * from remote")  # selecting all row from database
result = mycursor.fetchall()  # fetching all data from database and storing into result variable

######################################################################################################################
################################################# ON_CONNECT FUNCTION ################################################
######################################################################################################################

def on_connect(client, usedata, flags, rc):
    if rc == 0:  # checking rc status if it is 0 means connection is successful
        print("client is connected")  # printing debug info
        global connected  # it indicate that on_connect function uses the global variable
        connected = True  # making connection flag to true, indicate that client is connected
        return True  # function returns true if client is connected to MQTT broker
    else:
        print("connection failed")  # printing debug info
        connected = False  # making connection flag to false, indicate that client is failed to connect
        return False  # function returns false if client is failed to connect to MQTT broker


connected = False  # connected flag indicates that initially is not connected to MQTT broker

######################################################################################################################
################################################## CLIENT INFORMATION ################################################
######################################################################################################################

broker_address = "broker.hivemq.com"  # broker address
port = 1883  # port is given for process to process delivery
user = "engineer"  # client user name
password = "ec@ldce"  # client password

client = mqttclient.Client("MQTT")  # providing client name

######################################################################################################################
############################# FATCHING QUERY FROM DATABASE AND SEND HEX DATA TO THE BROKER ###########################
######################################################################################################################

while True:
    isNotFound = True  # variable that use to indicate whither query is found or not in database
    mqttQuery = input("enter your query (type exit to exit the prompt): ").lower()  # take user input for search user query in database also convert user query into lower case to avoide caseing issue

    if "exit" in mqttQuery:
        print("Leaving prompt...")
        time.sleep(2)
        exit()  # exit the programme

    for i in result:  # looping through all row in data base to match user query
        if i[0] == mqttQuery:  # condition for match user query to database data
            print("data is found: " + i[1])  # user query is found in database and reading hex data from database according to user request
            send_message = i[1]  # storing hex data to empty message string that we declared earlier
            time.sleep(0.1)  # waiting for some time to complete fetching process

            client.username_pw_set(user, password=password)  # setting up client user name and password
            client.on_connect = on_connect  # calling a on_connect function to connect client with the broker
            client.connect(broker_address, port=port)  # providing address and port number for connecting to broker
            client.loop_start()  # start a client loop to begin a transmission of message

            while not connected:  # waiting if client is not connected
                time.sleep(2)  # wait for 2 seconds

            client.publish("mqtt/eci", send_message)  # publish the message to particular topic
            client.loop_stop()  # stop client loop to end transmission
            isNotFound = False  # isNotFound flag indicate that user query is not found in database
            break  # break if user request is found on database

    if isNotFound:  # condition that checks user query is found or not in database, if not in database then condition is true
        print("data is not found")  # printing debug information

