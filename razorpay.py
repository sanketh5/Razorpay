import requests
import calendar

details = {
    "name" : "Nofrdz",
    "email" :"sankethdesuwar5@gmail.com",
    "contact_no" : "7588425170",
    "receiptno":"456655222"
}



def generate_url(details):
    url = "https://api.razorpay.com/v1/invoices/"
    #client deatils 
    name = details["name"]
    email=details["email"]
    contact_no = details["contact_no"]
    #it should be unique for every transaction
    receiptno=details["receiptno"]
    
    #asmount in paise
    amount="10000"
    
    #description
    desc = "Payment regarding Dental test"
    
    #The url where you wanna redirect your client after transaction
    callback_url = "https://example-callback-url.com/"
    
    #Expire in 3hrs 180-min
    future = datetime.datetime.utcnow() + datetime.timedelta(minutes=180)
    expire_by=calendar.timegm(future.timetuple())
    

    data ='{"customer":{ "name":"'+name+'" ,    "email":"'+email+'",    "contact":"'+contact_no+'" },  "type":"link",  "view_less":1,  "amount":"'+amount+'",  "currency":"INR",  "description":"'+desc+'",  "receipt":"'+str(receiptno)+'",  "reminder_enable":true,  "sms_notify":1,  "email_notify":1,  "expire_by":'+str(expire_by)+',  "callback_url":"'+callback_url+'",  "callback_method":"get"}'
    
    #your razor pay uid and your secret key
    uid = <your uid>
    pwd=<your secret key>
    
    headers = {'Content-type': 'application/json'}
    
    #query
    return_data = requests.post(url,data, auth=(uid,pwd),headers=headers)
    return return_data
