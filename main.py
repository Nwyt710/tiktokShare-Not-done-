import requests
from threading import Thread


def sendsShares():

    burp0_url = "https://api16-core-c-alisg.tiktokv.com:443/aweme/v1/aweme/stats/?iid=7091629261787252486&device_id=6889057643382670850&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=240204&version_name=24.2.4&device_platform=android&ab_version=24.2.4&ssmix=a&device_type=SM-G973N&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=efd572ab83ec3af0&manifest_version_code=2022402040&resolution=900*1600&dpi=320&update_version_code=2022402040&_rticket=1651148723545&app_type=normal&sys_region=US&mcc_mnc=46002&timezone_name=Africa%2FNairobi&carrier_region_v2=310&ts=1651148722&timezone_offset=10800&build_number=24.2.4&region=US&uoo=0&app_language=en&carrier_region=SA&locale=en&op_region=SA&ac2=wifi&host_abi=x86&cdid=013df980-c859-4abe-9d16-e557fa1753fa"
    burp0_cookies = {"store-idc": "useast2a", "store-country-code": "id", "install_id": "7091629261787252486", "ttreq": "1$8785200867b886fbff277b4c1bb891740eeff3e6", "odin_tt": "b303ab71d7869b2bd9476877f42c0edaa5bcc00b1970675f50c46cef23d0ec3508a2d0a423da132f1e3361691719b953dd9ac713dd3c752be7f36b0a71b2bbdcebc3bda3c338d943d37a682b322dedde", "msToken": "mPJxdOa2TnnnROhCK9TB9gXEaE1LW41Q4nukXOABB5s1xQLIRop7BESPjpg7vezE9C7UIUfl5CIPwq3IS6B9Sd2n8ZMA_2YJcFdZvQ6bbzcfYhxVjuyQVPbklA=="}
    burp0_headers = {"X-Ss-Stub": "5C89FEDCB733EFE7A90E026CEE367A16", "Accept-Encoding": "gzip, deflate", "Passport-Sdk-Version": "19", "Sdk-Version": "2", "X-Ss-Req-Ticket": "1651148723560", "X-Vc-Bdturing-Sdk-Version": "2.2.1.i18n", "X-Tt-Dm-Status": "login=0;ct=1;rt=6", "X-Tt-Store-Idc": "useast2a", "X-Tt-Store-Region": "id", "X-Tt-Store-Region-Src": "did", "User-Agent": "com.zhiliaoapp.musically/2022402040 (Linux; U; Android 7.1.2; en; SM-G973N; Build/PPR1.190810.011;tt-ok/3.10.0.2)", "X-Ladon": "f+YLJ3F+9JmyBwjQRWBwY7uGi0DA7KQ0u+PbJ4Oc93sgcLVs", "X-Gorgon": "0404c0d80001fb3c7759c52d13da5f4551c74e0b2229fdbf4d92", "X-Khronos": "1651148723", "X-Argus": "S5QsQLY1DvTdQ0GcqA+ygwehmMDoA5hWhEdLq++hbfS2K923eJ/RYpc8/lKZZsKEyJqLySde4iG6NcJdYwmpfpvdmeoaXjd3jwtpBS+8H6QejP7ggrwrxgEiqs1T7DxfzRWR/naXEbqcPHABE8iAlZMUKB1pxMpg+FoNb4x6nciAQXBBX84h6Z4ru2tUzw4l0C11l75OsZxdia6Gdhk7F7H4IHfNXKwIqa/xMYuLaXh404N0R1mNMCXHGev747wjelpjnHPsZPL7zW0FetHDGWY06QeDuUsT2z/qeqHL7+rqoQ==", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    burp0_data = {"order": '', "first_install_time": "-1", "request_id": '', "is_ad": "0", "item_type": "1", "aweme_type": "0", "item_id": "7091033002192522497", "share_delta": "1", "sync_origin": "false", "pre_item_playtime": '', "pre_hot_sentence": '', "stats_channel": "copy", "pre_item_id": '', "action_time": "1651148723", "enter_from": "others_homepage"}
    
    for i in range(1000000):

        res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        print(f"[+] Shares sent! {res.status_code}")


th1 = Thread(target=sendsShares())
th2 = Thread(target=sendsShares())
th3 = Thread(target=sendsShares())
th4 = Thread(target=sendsShares())
th5 = Thread(target=sendsShares())
th6 = Thread(target=sendsShares())
th7 = Thread(target=sendsShares())
th8 = Thread(target=sendsShares())
th9 = Thread(target=sendsShares())
th10 = Thread(target=sendsShares())


def main():
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()
    th9.start()
    th10.start()

if __name__ == '__main__':
    main()

#https://vt.tiktok.com/ZSdf8rqo8/
#https://www.tiktok.com/@93ns/video/7091033002192522497?is_from_webapp=1&sender_device=pc

