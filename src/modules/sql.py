import threading
import random
import requests
from datetime import datetime
"""
SQLI TESTING FUNCTION DEFS
"""

class Injthread(threading.Thread):
    def __init__(self, hosts):
        self.hosts = hosts
        self.fcount = 0
        self.check = True
        threading.Thread.__init__(self)

    def run(self):
        urls = list(self.hosts)
        for url in urls:
            try:
                if self.check:
                    sqli_scanning(url)  # Call the function to scan
                else:
                    break
            except KeyboardInterrupt:
                pass
        self.fcount += 1

    def stop(self):
        self.check = False

def sqli_scanning(url, vuln, col, vuln_scan_count, sqli_errors):
    # Removed print here to avoid printing all URLs during the scan
    vuln_scan_count.append(url)
    header = [line.strip() for line in open("lists/header", "r", encoding="utf-8")]
    ua = random.choice(header)
    headers = {"user-agent": ua}
    aug_url = url + "'"
    
    try:
        r = requests.get(aug_url, timeout=2, headers=headers)
    except:
        pass

    remove_dups = []
    with open("v3n0m-sqli.txt", "a+", encoding="utf-8") as sqli_log_file:
        for error in sqli_errors:
            try:
                if str(error) in r.text and url not in remove_dups:
                    remove_dups.append(url)
                    print(url + " is vulnerable --> %s" % str(error))
                    sqli_log_file.write("\n" + url)
                    vuln.append(url)
                    col.append(url)
                    sqli_log_file.flush()
            except:
                pass

def sqli_testing():
    global logfile
    global pulse
    global customlist
    global sql_list_counter
    global sql_list_count
    global sqli_confirmed
    pulse = datetime.now()
    vb = len(usearch) / int(numthreads)
    i = int(vb)
    m = len(usearch) % int(numthreads)
    z = 0
    print("[+] I'm working, please just hang out for a minute...\n")
    
    try:
        if len(threads) <= int(numthreads):
            for x in range(0, int(numthreads)):
                sliced = usearch[x * i : (x + 1) * i]
                if z < m:
                    sliced.append(usearch[int(numthreads) * i + z])
                    z += 1
                thread = Injthread(sliced)
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
    except TimeoutError:
        pass
