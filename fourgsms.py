import requests
from requests.exceptions import HTTPError
import argparse
import urllib
import secrets
import time
import xml.etree.ElementTree as ET

print('Gateway address:', secrets.ip)
print('Default number:', secrets.number)

class SMS():
    def __init__(self, ip):
        self.ip = ip
        self.logged_on = False
        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'}
        print('SMS gateway started on',self.ip)

    def msg_print(self, request):
        print(str(request.status_code))
        print(str(request.cookies))
        print(str(request.url))

    def logon(self, userid, password):
        r0 = requests.get('http://192.168.1.1/space.xml')
        root = ET.fromstring(r0.text)
        req_time = str(root[1].text)
        print("Time:",req_time)
        self.msg_print(r0)
        r1_params = {'un': userid,
                     'pw': password,
                     'rd':'/uir/login.htm',
                     'rd2':'/uir/login.htm',
                     'Nrd':1,
                     'Ntime': req_time}
        r1 = requests.get('http://192.168.1.1/log/in',
                          params = r1_params,
                          headers = self.headers,
                          allow_redirects = False)
        self.msg_print(r1)
        self.logged_on = True
        self.cookies = r1.cookies
        print("Logged on")

    def send (self, number, message):
        # message = urllib.parse.quote_plus(message
        r2_params = {'S801E2701': number,
                     'S801E2801': message,
                     'Nindex' : '0',
                     'Nfr' : '1'
                     }
        r3_params = {'Ncmd' : '2',
                     'Nindex' : '0'}
        try:
            r2 = requests.get('http://192.168.1.1/mobile_sms.htm',
                              params = r2_params,
                              headers = self.headers,
                              cookies = self.cookies)   
            self.msg_print(r2)
            r3 = requests.get('http://192.168.1.1/mobile_sms2.htm',
                              params = r3_params,
                              headers = self.headers,
                              cookies = self.cookies)
            self.msg_print(r3)      
        except HTTPError as http_err:
            print('HTTP error occurred:', http_err)
        except Exception as err:
            print('Error occurred:', err)
        print("Sent", message, "to", number)

def main():
    parser = argparse.ArgumentParser(description='Sends SMS message via 4G/LTE router.')
    parser.add_argument('-n','--number',
                        type=str,
                        default="07802461448",
                        help='Telephone number to send to')
    parser.add_argument('-m', '--message',
                        type=str,
                        default="Hello from K9!",
                        help='Message of the text to send')
    args = parser.parse_args()
    number = args.number
    message = args.message
    mySMS = SMS(secrets.ip)
    mySMS.logon(secrets.userid, secrets.password)
    mySMS.send(number, message)
    time.sleep(5.0)
    mySMS.send(number, "Second message")
    time.sleep(5.0)
    mySMS.send(number, "Third message")

if __name__ == '__main__':
    main()