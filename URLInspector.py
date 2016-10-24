import requests
import simplejson as json

COMPANY     =   <Company Name>
VERSION     =   <Your Product Version>
HEADER      =   {'Content-Type': 'application/json'}
SERVER      =   'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=<Your Key Goes Here> HTTP/1.1'

'''
Possible platform type values :
PLATFORM_TYPE_UNSPECIFIED	Unknown platform.
WINDOWS	                    Threat posed to Windows.
LINUX	                    Threat posed to Linux.
ANDROID	                    Threat posed to Android.
OSX	                        Threat posed to OS X.
IOS	                        Threat posed to iOS.
ANY_PLATFORM	            Threat posed to at least one of the defined platforms.
ALL_PLATFORMS	            Threat posed to all defined platforms.
CHROME	                    Threat posed to Chrome.
'''
PLATFORM        =   'ANY_PLATFORM'

'''
Threat Types:
THREAT_TYPE_UNSPECIFIED                 Unknown.
MALWARE	                                Malware threat type.
SOCIAL_ENGINEERING                      Social engineering threat type.
UNWANTED_SOFTWARE                       Unwanted software threat type.
POTENTIALLY_HARMFUL_APPLICATION	        Potentially harmful application threat type.
'''
THREAT_TYPE     =   'THREAT_TYPE_UNSPECIFIED'

'''
Threat Entry Type:
THREAT_ENTRY_TYPE_UNSPECIFIED           Unspecified.
URL                                     A URL.
EXECUTABLE                              An executable program.
IP_RANGE                                An IP range.
'''
THREAT_ENTRY_TYPE   =   'URL'

threat_type_arr =           [THREAT_TYPE]
platform_type_arr =         [PLATFORM]
threat_entry_type_arr =     [THREAT_ENTRY_TYPE]

'''
This function creates the threat type array
Create this array based on what you want to look up
'''
def create_threat_type_array():
    '''
    Put content here to fill it up
    '''
    threat_type_str = '['
    for types in threat_type_arr:
        threat_type_str += types+','
    threat_type_str = threat_type_str[:-1] +']'
    print "threat type str %s\n"%threat_type_str
    return threat_type_str

'''
This function creates the platform type array
Create this array based on your platform
'''
def create_platform_types():
    '''
    Put content here to fill it up
    '''
    platform_type_str = '['
    for types in platform_type_arr:
        platform_type_str += types+','
    platform_type_str = platform_type_str[:-1]+']'
    print "platform type str: %s\n"%platform_type_str
    return platform_type_str

'''
This function creates the threat entry type array
Create this array based on your platform
'''
def create_threat_entry_type_arr():
    '''
    Put content here to fill it up
    '''
    threat_entry_type_str = '['
    for types in threat_entry_type_arr:
        threat_entry_type_str += types+','
    threat_entry_type_str = threat_entry_type_str[:-1]+']'
    print "threat entry type str: %s \n"%threat_entry_type_str
    return threat_entry_type_str


def send_message():
    json_resp   = requests.post(SERVER,HEADER)
    resp        = json_resp.text
    return resp


def get_client_ver_json():
    client_str      =       '{"client" : {"cliendId":'+COMPANY+',"clientVersion":'+VERSION+'},'
    return client_str

def get_threat_info_json():
    tis             =       '"threatInfo":{"threatTypes":'+create_threat_type_array()+',"platformTypes":'+create_platform_types()+',"threatEntryTypes":'+create_threat_entry_type_arr()+','
    return tis

def get_threat_entries_json(threat_entry_type,threat_list):
    tij             =        '"threatEntries":['
    first           = 1
    print "Threats in threatlist: \n"
    for threat in threat_list:
        print "%s \n"%threat
        if first == 0:
            tij+=','
        tij+='{'+threat_entry_type+':'+threat+'}'
        first = 0
    tij             +=   ']'
    return tij

'''
This function parses the list of urls passed to it
and adds it to the body. Once the body is created
it will send message to the server to check url
status.
Not more than 500 urls can be queried in one shot.
'''
def create_json_string(url_list):
    uqs = ''                        #url_query_string
    cvs = ''                        #client_version_string
    tis = ''                        #threat_info_string
    for entry in threat_entry_type_arr:
        tij = get_threat_entries_json(entry,url_list)
    tis = get_threat_info_json()
    tis += tij+'}'
    cvs = get_client_ver_json()
    cvs += tis+'}'
    print cvs

url_list = ['https://google.com']
create_json_string(url_list)
