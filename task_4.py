def check_ip():
    data = requests.get('https://ifconfig.me/')
    return str(data.content,"utf-8")

# print(check_ip())