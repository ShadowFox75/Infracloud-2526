import requests 
import json 
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "OTBmYWZhNWQtNDQwOS00ZjEyLTkwMmYtYzc3NWEzYzYxYzUxZTI3OWM3NWUtODli_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea"

groups_struc = {
 "groups": [
      { "group": { "group_id": "G1" , "group_name": "GROUP_YRO_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Gergely", "email": "gergely.desmecht@student.odisee.be"},
                     {"person_id": "P-2" , "person_name": "Gavin", "email": "gavin.ahamat@student.odisee.be"},
                     {"person_id": "P-3" , "person_name": "Sasha", "email": "sasha.harus@student.odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G2" , "group_name": "GROUP_YRO_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Mohamed", "email": "mohamed.elkaddourri3@student.odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "Adam", "email": "adam.elbouab@student.odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Chun", "email": "chun.bruylandt@student.odisee.be"} 
                   ]     
                 }
      }
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)

    NEW_SPACE_ID = res_space.json()["id"]
    for mbr in rec["group"]["members"]:
        room_id = NEW_SPACE_ID
        person_email = mbr["email"] 
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'roomId': room_id, 'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)