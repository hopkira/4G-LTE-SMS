import requests
from requests.exceptions import HTTPError
import argparse
import urllib
import secrets

print('Gateway address:', secrets.ip)
print('Default number:', secrets.number)

class SMS():
    def __init__(self, ip, userid, password):
        self.ip = ip
        self.userid = userid
        self.password = password
        print('SMS gateway started on',self.ip)
    def send (self, number, message):
        r1_params = {'un':self.userid, 'password': self.password, 'rd':'/uir/status.htm', 'rd2':'/uir/wanst.htm', 'Nrd':1 }
        r2_params = {}
        r3_params = {"Ncmd":2}
        try:
            r1 = requests.get('http://192.168.1.1/log/in',params=r1_params)
            r2 = requests.get('http://192.168.1.1/smsmsg.htm',params = r2_params, cookies=r1.cookies)
            r3 = requests.get('http://192.168.1.1/sms2.htm', params = r3_params, cookies=r1.cookies)
        except HTTPError as http_err:
            print('HTTP error occurred:', http_err)
        except Exception as err:
            print('Error occurred:', err)
        else:
            print("Message",str(message),"sent to",str(number))    

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
    mySMS = SMS(secrets.ip, secrets.userid, secrets.password)
    mySMS.send(number, message)

if __name__ == '__main__':
    main()