import questionary
import sys
from pathlib import Path
import yaml


def saveConfig(args):
    configStored = Path() / "config.yaml"
    configData = dict()

    if configStored.is_file():
        questions = [
            {
                'type': 'confirm',
                'message': 'File {0} already exist, are you sure you want to continue?\n\nTHIS WILL OVERWRITE YOUR CURRENT CONFIG!'.format(configStored),
                'name': 'continue',
                'default': True,
            },
        ]
        answers = questionary.prompt(questions)
        if answers['continue']:
            print("> continuing with preview config configuration...")
        else:
            print("> exiting ...")
            sys.exit(0)
        configpath = str(configStored)
    print("Start new config file...")

    questions = [
        {
            'type': 'select',
            'message': 'which xfi vuln',
            'name': 'xfivuln',
            'choices': ['LFI', 'RFI'],
        },
        {
            'type': 'text',
            'message': 'Enter target base url:',
            'name': 'url',
            'default': "",
        },
        {
            'type': 'confirm',
            'message': 'Do you need to be logged for load this url ?',
            'name': 'needauth',
            'default': False,
        }
    ]
    # http://192.168.245.40/vulnerabilities/fi/?page=
        
    answers = questionary.prompt(questions)
    
    if answers['needauth']:
        print("> Sorry for the moment we are not able to perform this test on Auth mode.")
        sys.exit(0)
    
    configData['url']= answers['url']
    configData['type']= answers['xfivuln']
    configData['needauth']= answers['needauth']

    with open(configStored, 'w') as outfile:
        yaml.dump(configData, outfile, default_flow_style=False, sort_keys=False)

    print("> configuration file was written to: {0}, Now you can  run `python xfi.py run`".format(Path(configStored).resolve()))
    sys.exit(0)