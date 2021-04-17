# Python SMS Interface for Zyxel LTE3302 Series Router
This is a simple program to send SMS messages via a 4G LTE Router.  My router is a Zyxel LTE3302 Series router which provides a 4G hotspot for my robots.  The data package I am using allows for unlimited texts, so this seems like an attractive option for cool communication.

Unfortunately the router does not offer an API to enable a user to send texts - the only supported interface is via a the router's adminstration web pages.  The program apes the browser HTML GET calls to send a text.

##  Setup and usage
1. Clone this repository
~~~bash
git clone https://github.com/hopkira/4G-LTE-SMS.git
~~~
2. In the resulting directory create a secrets.py file 
~~~bash
nano secrets.py
~~~
3. Add the following content
~~~python
userid="admin" # the user id to access your router
password="1234" # the password to access your router
number="01234567890" # a default number to call
ip="192.168.1.1" # the IP address of your router
~~~
4. You can now use this program from the command line:
~~~bash
python3 4gsms.py -m 'This is my message' -n 'phone_no_to_text'
~~~
5. Alternatively you can import it as a python module and use it in your own programs
~~~python
import 4gsms as sms
import secrets
mySMS = SMS(secrets.ip, secrets.userid, secrets.password)
number = "01234567890"
message = "This is a test text"
mySMS.send(number, message)
~~~

## How does this work?
The program was created by analysing the traffic between my Mac and the Router during logon and SMS text sending activities.  It was clear that to send a text, three commands had to be sent from the browser using HTTP GET.
1. A logon interaction that creates a session cookie called AMSESSIONID
2. A SMS interaction that populates the SMS message details (and uses the cookie above) 
3. A final 'send' instruction that sends the text

## Other routers
D‑Link's DWR‑921 4G LTE Router appears to have a near identical inteface, so it is possible the code will work for it too (but I can't test this).  Given the Zyxel and D-Link software are impossibly similar, it is quite possible that the routers are using identical software that has been separately branded.  If this code works with your 4G Router and it isn't listed here, please let me know via an Issue or Comment and I will update this README.