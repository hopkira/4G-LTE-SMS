import fourgsms as sms
import time
mySMS = sms.SMS(sms.secrets.ip)
mySMS.logon(sms.secrets.userid, sms.secrets.password)
mySMS.send(sms.secrets.number, "First message")
time.sleep(5.0)
mySMS.send(sms.secrets.number, "Second message")
time.sleep(5.0)
mySMS.send(sms.secrets.number, "Third message")