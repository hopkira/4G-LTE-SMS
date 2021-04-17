import requests
import argparse

class SMS(ip, userid, password):
    def __init__(self,self.ip,):
        print("SMS gateway started on",string(self.ip))
    def send (self, number, message):
        print("Message",string(message),"sent to",string(number))    

def main():
    parser = argparse.ArgumentParser(description='Creates 4G LTE SMS gateway.')
    parser.add_argument('-n','number',
                        type=string,
                        default="",
                        nargs='?',
                        help='Telephone number to send to')
    parser.add_argument('-m', 'message',
                        type=string,
                        default="Hello from K9!",
                        nargs='?',
                        help='Message of the text to send')
    parser.add_argument('-i', 'ip_address',
                        type=string,
                        default="192.168.1.1",
                        nargs='?',
                        help='Address of the 4G router')
    parser.add_argument('-t', '--test',
                        action='store_true',
                        help='execute in simulation mode')
    args = parser.parse_args()
    sim = args.test

    r1 = requests.get('http://192.168.1.1/log/in?un=admin&password&rd&rd=%2Fuir%2Fstatus.htm&rd2=%2Fuir%2Fwanst.htm&Nrd=1
    ')
    r2 = requests.get(' http://192.168.1.1/smsmsg.htm?Nsend=1&Nmsgindex=0&S801E2700=6979555555&S801E2800=Test%20send%20sms,cookies=r1.cookies)
    r3 = requests.get('http://192.168.1.1/sms2.htm?Ncmd=2', cookies=r1.cookies)

if __name__ == '__main__':
    main()