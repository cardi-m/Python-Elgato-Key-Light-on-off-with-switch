import json
import requests
lampe_1_ip = "192.xxx.xxx.xxx" #<--- hier IP der Lampe eingeben


lampe_1_ip_gesamt = "http://" + lampe_1_ip + ":9123/elgato/lights"
print(lampe_1_ip_gesamt)

response_1 = requests.get(lampe_1_ip_gesamt)
lampe_1 = json.loads(response_1.text)
#print(lampe_1 == response_1.json()) #Pruefung ob json Format
#type(lampe_1) #noch nicht sicher was das macht
print(lampe_1)
