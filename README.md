# Universal-IR-Remote
It is a universal Ir remote which can control devices (Only devices which uses IR for their remote operation). This is an all-in-one learning remote control based on ESP8266 and MQTT protocol. This remote has two modes of operation
1. Teach mode
2. Run mode

In teach mode it can learn from any remote and store these data in a local database. In run mode it retrieves IR data from local database to control devices. At first user has to provide SSID and password to the remote through a webpage. I have implemented only run mode till now.
