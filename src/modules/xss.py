import threading
import requests
import re
"""
XSS TESTING FUNCTION DEFS
"""
def xss_scanning(url, xsses, vuln_scan_count, vuln, xss_log_file):
    vuln_scan_count.append(url)
    for xss in xsses:
        try:
            source = requests.get(url + xss.replace("\n", ""), timeout=5)
        except:
            pass
        try:
            if re.findall("<OY1Py", source.text):
                print(f"[XSS]: {url + xss} ---> XSS Found")
                xss_log_file.write("\n" + url)
                vuln.append(url)
            if re.findall("<LOY2PyTRurb1c", source.text):
                print(f"[XSS]: {url + xss} ---> XSS Found")
                xss_log_file.write("\n" + url)
                vuln.append(url)
        except:
            pass



class XssThread(threading.Thread):
    def __init__(self, hosts, xsses, vuln_scan_count, vuln, xss_log_file, check=True):
        self.hosts = hosts
        self.xsses = xsses
        self.vuln_scan_count = vuln_scan_count
        self.vuln = vuln
        self.xss_log_file = xss_log_file
        self.check = check
        self.fcount = 0
        threading.Thread.__init__(self)

    def run(self):
        urls = list(self.hosts)
        for url in urls:
            try:
                if self.check:
                    xss_scanning(url, self.xsses, self.vuln_scan_count, self.vuln, self.xss_log_file)
                else:
                    break
            except KeyboardInterrupt:
                pass
        self.fcount += 1

    def stop(self):
        self.check = False

def xss_testing(usearch, numthreads, xsses, vuln_scan_count, vuln, xss_log_file):
    print("[+] I'm working, please just hang out for a minute...\n")
    vb = len(usearch) / int(numthreads)
    i = int(vb)
    m = len(usearch) % int(numthreads)
    z = 0
    threads = []

    if len(threads) <= int(numthreads):
        for x in range(0, int(numthreads)):
            sliced = usearch[x * i : (x + 1) * i]
            if z < m:
                sliced.append(usearch[int(numthreads) * i + z])
                z += 1
            thread = XssThread(sliced, xsses, vuln_scan_count, vuln, xss_log_file)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
