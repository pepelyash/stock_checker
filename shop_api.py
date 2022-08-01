import requests
from requests.exceptions import HTTPError


def get_access_token():
    url = 'https://api.samokat.ru/showcase/oauth/token'
    refresh_token = 'aaee99bfe7f21095568c4578cfea62894f33fd3a84af6ae338171e5ec7055b8d'
    data = f'grant_type=refresh_token&refresh_token={refresh_token}'  # copy-paste refresh_token from opened app
    deviceid = 'c76c85cc15c59094f0586a7383cd03b8'
    app_ver = '3.56.0'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'deviceid': deviceid,
        'x-application-platform': 'android',
        'x-application-version': app_ver,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '103',
        'Host': 'api.samokat.ru',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.1'
    }
    access_token = ''
    try:
        response = requests.post(url=url, data=data, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        if response.status_code == 200:
            access_token = response.json()['access_token']
            return access_token


def get_products_list():
    url = 'https://api.samokat.ru/showcase/showcases/de1c674b-ddda-4485-9b7c-e13f5e901088/stocks'
    # authorization = 'Bearer eyJraWQiOiI2MTg2OTEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3NhbW9rYXQucnUiLCJzdWIiOiI1NzY5OTQxMzkiLCJkZXZpY2VfaWQiOiJkYjI0YjRmOTc2MGZjNGVhIiwic2NvcGUiOlsiQ0FSVF9NQU5BR0VNRU5UIiwiUFJPRklMRV9NQU5BR0VNRU5UIl0sImV4cCI6MTY1OTM1ODYzMSwiaWF0IjoxNjU5MzU4MzMxLCJ1c2VyIjp7InVzZXJJZCI6IjU3Njk5NDEzOSIsInVzZXJUeXBlIjoiQU5PTllNT1VTIn0sImp0aSI6IjI2MzkyODQ5ODIiLCJjbGllbnRfaWQiOiJzYW1va2F0In0.IP4eUU2wtuA_R8Pfbu_Sf2q9_tlwNT1Su6BLTxFLDfE_mHxzv1o9mmzoiUC7Vh-QlcSewDPNTjSM64abA79srYkNtQNxUKN99YMqnBCiPCLjVZcS0RQITIFZDgzlmN8-WPyFNVFSQ6jXGthja9QFZ-Iqowi3yDmWI7Uec1Yk830'
    # authorization = 'Bearer eyJraWQiOiI2MTg2OTEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3NhbW9rYXQucnUiLCJzdWIiOiI1NzY5OTQxMzkiLCJkZXZpY2VfaWQiOiJkYjI0YjRmOTc2MGZjNGVhIiwic2NvcGUiOlsiQ0FSVF9NQU5BR0VNRU5UIiwiUFJPRklMRV9NQU5BR0VNRU5UIl0sImV4cCI6MTY1OTM1ODYzMSwiaWF0IjoxNjU5MzU4MzMxLCJ1c2VyIjp7InVzZXJJZCI6IjU3Njk5NDEzOSIsInVzZXJUeXBlIjoiQU5PTllNT1VTIn0sImp0aSI6IjI2MzkyODQ5ODIiLCJjbGllbnRfaWQiOiJzYW1va2F0In0.IP4eUU2wtuA_R8Pfbu_Sf2q9_tlwNT1Su6BLTxFLDfE_mHxzv1o9mmzoiUC7Vh-QlcSewDPNTjSM64abA79srYkNtQNxUKN99YMqnBCiPCLjVZcS0RQITIFZDgzlmN8-WPyFNVFSQ6jXGthja9QFZ-Iqowi3yDmWI7Uec1Yk830'
    # authorization = 'Bearer eyJraWQiOiI2MTg2OTEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3NhbW9rYXQucnUiLCJzdWIiOiI1NzY5OTQxMzkiLCJkZXZpY2VfaWQiOiJkYjI0YjRmOTc2MGZjNGVhIiwic2NvcGUiOlsiQ0FSVF9NQU5BR0VNRU5UIiwiUFJPRklMRV9NQU5BR0VNRU5UIl0sImV4cCI6MTY1OTM1OTg1NCwiaWF0IjoxNjU5MzU5NTU0LCJ1c2VyIjp7InVzZXJJZCI6IjU3Njk5NDEzOSIsInVzZXJUeXBlIjoiQU5PTllNT1VTIn0sImp0aSI6IjI2MzkzOTE1ODEiLCJjbGllbnRfaWQiOiJzYW1va2F0In0.Y8KcYO5QodyAyy5jhAYb84SR2qipzOQuns2EGoSY3A8pb0xBE31wIAWj6e2kuzfrnZdp8fS7wUAaZD9s_RNDqwIvMBB3KUy-zDaJZAb3tKROA8RyGZTVEjL-XtpsOenqeKhS5-7g75Yxzc_CIHcqz-t4E2asrPRxQ5cuTuMZEkk'
    # atkn = get_access_token()
    # print(atkn)
    # authorization = f'Bearer {atkn}'
    # authorization = 'Bearer eyJraWQiOiI2MTg2OTEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3NhbW9rYXQucnUiLCJzdWIiOiI1NzY5OTQxMzkiLCJkZXZpY2VfaWQiOiJkYjI0YjRmOTc2MGZjNGVhIiwic2NvcGUiOlsiQ0FSVF9NQU5BR0VNRU5UIiwiUFJPRklMRV9NQU5BR0VNRU5UIl0sImV4cCI6MTY1OTM2MTM2MywiaWF0IjoxNjU5MzYxMDYzLCJ1c2VyIjp7InVzZXJJZCI6IjU3Njk5NDEzOSIsInVzZXJUeXBlIjoiQU5PTllNT1VTIn0sImp0aSI6IjI2Mzk1MjU0MTIiLCJjbGllbnRfaWQiOiJzYW1va2F0In0.dL9q7gJ0vLGvz1Lh8doyyM3Mk1lzoL0y_786MdEpD6JDzHTqtCU7BhaHSol8eOTnsmzdtLnNZFR2dkffnkfM8YtgPwG3GNeuUSoYS7gkIuudV_CRbb_gyqtZ_QUax2vmHvQpBqe5VV-dID9C18q9M9sJXicn0ge9EblY2KOGfn8'
    authorization = 'Bearer eyJraWQiOiI2MTg2OTEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3NhbW9rYXQucnUiLCJzdWIiOiI1NzY5OTQxMzkiLCJkZXZpY2VfaWQiOiJkYjI0YjRmOTc2MGZjNGVhIiwic2NvcGUiOlsiQ0FSVF9NQU5BR0VNRU5UIiwiUFJPRklMRV9NQU5BR0VNRU5UIl0sImV4cCI6MTY1OTM2MTY5MCwiaWF0IjoxNjU5MzYxMzkwLCJ1c2VyIjp7InVzZXJJZCI6IjU3Njk5NDEzOSIsInVzZXJUeXBlIjoiQU5PTllNT1VTIn0sImp0aSI6IjI2Mzk1NDgwNjgiLCJjbGllbnRfaWQiOiJzYW1va2F0In0.J7jo3iXHigDM27QvwiRCyJn6EJaJQheTaxpkbvnk7T7_ws0EzGDppWmi95kqYSwe8nV78q03d8ZjmQCL4mqaPuUiD1QE8WMKF28DvbdTbpovRJduoHuK3rOnVCb_VREWSExY_MqDGyu52aqTBwutl86p64bSCs7X8Wtbtsmfiew'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': authorization,
        'x-application-platform': 'android',
        'x-application-version': '3.56.0',
        'Content-Type': 'application/json;charset=utf-8',
        'Content-Length': '2',
        'Host': 'api.samokat.ru',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.1'
    }
    # with requests.Session as s:
    #     resp = s.post(url=url, headers=headers)

    # product_list = requests.post(url=url, headers=headers)
    # product_list = response.json().
    try:
        response = requests.post(url=url, headers=headers, timeout=2)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    # else:
    #
    # return product_list


def big_req():
    with requests.Session() as s:
        url = 'https://core-colibri-api.samokat.ru/api/events/track'
        headers = {
            'x-signature': '9b19bac801bb01fadbd9d693b95859b7e66722724663aed65e75a6fc3d30d63e',
            'Content-Type': 'application/json',
            'Content-Length': '862',
            'Host': 'core-colibri-api.samokat.ru',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.1'
        }
        data = {"source":"https://samokat.ru/samokat-app","type":"Catalog - Main - Banners View","app_session_id":"e8256de9-16e6-4a62-9180-2b2fef3b6779","device_id":"db24b4f9760fc4ea","device_time":1659363515984,"data":{"banners":["Скидки до 50% на продукты, напитки и бытовую химию"],"device_brand":"samsung","device_carrier":"Mobile TeleSystems","device_type":"Handset","device_name":"SM-N976N","device_manufacturer":"samsung","device_model":"SM-N976N","device_os_name":"Android","device_os_version":"5.1.1","device_app_version":"3.56.0","device_ip":"172.16.63.15","app_session_started_at":1659361819259,"user_properties":{"manual_set_device_model":"SM-N976N","userId":"576994139","showcase_id":"88e1a598-2530-435e-9e04-d5f85f12a2ce","showcase_type":"MINIMARKET"}},"id":"90ef11c8d4467561e8d0361bd1280820b75416bdd951698df2ba07cd1e2cc51a"}
        try:
            response = s.post(url=url, json=data, headers=headers, timeout=2)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print(response.json()['result'])
        url = 'https://api.samokat.ru/showcase/showcases/88e1a598-2530-435e-9e04-d5f85f12a2ce/stocks'
        authorization = 'Bearer eyJraWQiOiI2MTg2OTEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL3NhbW9rYXQucnUiLCJzdWIiOiI1NzY5OTQxMzkiLCJkZXZpY2VfaWQiOiJkYjI0YjRmOTc2MGZjNGVhIiwic2NvcGUiOlsiQ0FSVF9NQU5BR0VNRU5UIiwiUFJPRklMRV9NQU5BR0VNRU5UIl0sImV4cCI6MTY1OTM2Mzk2NSwiaWF0IjoxNjU5MzYzNjY1LCJ1c2VyIjp7InVzZXJJZCI6IjU3Njk5NDEzOSIsInVzZXJUeXBlIjoiQU5PTllNT1VTIn0sImp0aSI6IjI2Mzk3Mjc0MTMiLCJjbGllbnRfaWQiOiJzYW1va2F0In0.V1umvqY_VLQBu7qJjL8yEDhomMhN7D-KhDRxzewdWbl53dsje_uA9Qfto5SjJE3CYZCw3us1Vbp5gmHwoXsgpkQbgvE_DZYkTZ4dd-OOqfleQUdZF1CFYPnj8cVw9GerSKEjqOu7vFJET8agbkQLZ49uZjy62kTS5LyFyR1Qy-g'
        headers = {
            'accept': 'application/json, text/plain, */*',
            'authorization': authorization,
            'x-application-platform': 'android',
            'x-application-version': '3.56.0',
            'Content-Type': 'application/json;charset=utf-8',
            'Content-Length': '2',
            'Host': 'api.samokat.ru',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.1'
        }
        url = 'https://api.samokat.ru/showcase/showcases/88e1a598-2530-435e-9e04-d5f85f12a2ce/stocks'
        try:
            response = s.post(url=url, headers=headers, timeout=20)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print(response.json())


def main():
    print(get_access_token())
    # get_products_list()
    # big_req()
    pass


if __name__ == '__main__':
    main()
