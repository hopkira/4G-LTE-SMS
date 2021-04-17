import fourgsms as sms
mySMS = sms.SMS(sms.secrets.ip, sms.secrets.userid, sms.secrets.password)
number = "01234567890"
message = "This is a test text"
mySMS.send(number, message)