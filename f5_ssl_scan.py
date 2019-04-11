#!/usr/bin/env python3

import requests,json,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def abort_script(reason):
    print('*** Aborting script execution! ***')
    if len(str(reason)) > 0:
        print('ERROR: ' + str(reason))
    sys.exit(2)
    
def icontrol_get(host,username,password,path):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path
    try:
        apiResponse = apiCall.get(apiUri,verify=False)
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse.text)

def icontrol_post(host,username,password,path,api_payload):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path
    try:
        apiResponse = apiCall.post(apiUri,verify=False,data=json.dumps(api_payload))
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse.text)

BIG_IP = {}
BIG_IP['mgmt_ip'] = '192.168.1.101'
BIG_IP['username'] = 'admin'
BIG_IP['password'] = 'admin'
CLIENTSSL_PROFILE_CIPHERS = {}
SERVERSSL_PROFILE_CIPHERS = {}
VIPS = {}
dictionary_entry = {}

# Retrieve all SSL profiles

api_response = icontrol_get(BIG_IP['mgmt_ip'],BIG_IP['username'],BIG_IP['password'],'/ltm/profile/client-ssl')                  
api_response_dict = json.loads(api_response)
clientssl_profile_list = api_response_dict['items']
for current_clientssl_profile in clientssl_profile_list:
	current_clientssl_profile_name = str(current_clientssl_profile['name'])
	current_clientssl_profile_cipherstring = str(current_clientssl_profile['ciphers'])
	print('Found Client SSL profile: ' + current_clientssl_profile_name)
	print(' -> Ciphers: ' + current_clientssl_profile_cipherstring)
	print(' -> Retreiving complete cipher list')
	api_payload = {"command":"run","utilCmdArgs":"-c 'tmm --serverciphers " + current_clientssl_profile_cipherstring + "'"}
	api_response = icontrol_post(BIG_IP['mgmt_ip'],BIG_IP['username'],BIG_IP['password'],'/util/bash',api_payload) 
	api_response_dict = json.loads(api_response)
	current_clientssl_profile_cipherlist = api_response_dict['commandResult']
	CLIENTSSL_PROFILE_CIPHERS[current_clientssl_profile_name] = {}
	CLIENTSSL_PROFILE_CIPHERS[current_clientssl_profile_name]['name'] = current_clientssl_profile_name
	CLIENTSSL_PROFILE_CIPHERS[current_clientssl_profile_name]['cipherstring'] = current_clientssl_profile_cipherstring
	CLIENTSSL_PROFILE_CIPHERS[current_clientssl_profile_name]['cipherlist'] = current_clientssl_profile_cipherlist

api_response = icontrol_get(BIG_IP['mgmt_ip'],BIG_IP['username'],BIG_IP['password'],'/ltm/profile/server-ssl')
api_response_dict = json.loads(api_response)
serverssl_profile_list = api_response_dict['items']
for current_serverssl_profile in serverssl_profile_list:
        current_serverssl_profile_name = str(current_serverssl_profile['name'])
        current_serverssl_profile_cipherstring = str(current_serverssl_profile['ciphers'])
        print('Found Server SSL profile: ' + current_serverssl_profile_name)
        print(' -> Ciphers: ' + current_serverssl_profile_cipherstring)
        print(' -> Retreiving complete cipher list')
        api_payload = {"command":"run","utilCmdArgs":"-c 'tmm --serverciphers " + current_serverssl_profile_cipherstring + "'"}
        api_response = icontrol_post(BIG_IP['mgmt_ip'],BIG_IP['username'],BIG_IP['password'],'/util/bash',api_payload) 
        api_response_dict = json.loads(api_response)
        current_serverssl_profile_cipherlist = api_response_dict['commandResult']
        SERVERSSL_PROFILE_CIPHERS[current_serverssl_profile_name] = {}
        SERVERSSL_PROFILE_CIPHERS[current_serverssl_profile_name]['name'] = current_serverssl_profile_name
        SERVERSSL_PROFILE_CIPHERS[current_serverssl_profile_name]['cipherstring'] = current_serverssl_profile_cipherstring
        SERVERSSL_PROFILE_CIPHERS[current_serverssl_profile_name]['cipherlist'] = current_serverssl_profile_cipherlist

# Retrieve all the VIPs 
api_response = icontrol_get(BIG_IP['mgmt_ip'],BIG_IP['username'],BIG_IP['password'],'/ltm/virtual')
api_response_dict = json.loads(api_response)
ltm_virtual_list = api_response_dict['items']
for current_virtual in ltm_virtual_list:
	print('************************************************************************************************************************')
	print('Virtual server found: ' + current_virtual['name'])
	print('************************************************************************************************************************')
	api_response = icontrol_get(BIG_IP['mgmt_ip'],BIG_IP['username'],BIG_IP['password'],'/ltm/virtual/' + current_virtual['name'] + '/profiles')
	api_response_dict = json.loads(api_response)
	current_virtual_profiles = api_response_dict['items']
	for current_virtual_profile in current_virtual_profiles:
		print(' -> Profile found: ' + current_virtual_profile['name'] + ' (Context: ' + current_virtual_profile['context'] + ')')	
		if current_virtual_profile['context'] == 'clientside' and current_virtual_profile['name'] in CLIENTSSL_PROFILE_CIPHERS:
			print('   -> Cipher string: ' + CLIENTSSL_PROFILE_CIPHERS[current_virtual_profile['name']]['cipherstring'])
			print('   -> Complete cipher list: \n' + CLIENTSSL_PROFILE_CIPHERS[current_virtual_profile['name']]['cipherlist'])
		elif current_virtual_profile['context'] == 'serverside' and current_virtual_profile['name'] in SERVERSSL_PROFILE_CIPHERS:
			print('   -> Cipher string: ' + SERVERSSL_PROFILE_CIPHERS[current_virtual_profile['name']]['cipherstring'])
			print('   -> Complete cipher list: \n' + SERVERSSL_PROFILE_CIPHERS[current_virtual_profile['name']]['cipherlist'])
		else:
			print('   -> Non-SSL Profile')
	print('*************************')
	print('* END OF VIRTUAL SERVER *') 
	print('*************************')


