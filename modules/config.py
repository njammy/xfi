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
            'name': 'baseurl',
            'default': "",
        },
        {
            'type': 'text',
            'message': 'Enter target route:',
            'name': 'route',
            'default': "",
        },
        {
            'type': 'text',
            'message': 'Enter specified param:',
            'name': 'param',
            'default': "",
        },
    ]
    answers = questionary.prompt(questions)
    configData['baseurl']= answers['baseurl']
    configData['type']= answers['xfivuln']
    configData['route']= answers['route']
    configData['param']= answers['param']

    with open(configStored, 'w') as outfile:
        yaml.dump(configData, outfile, default_flow_style=False, sort_keys=False)

    print("> configuration file was written to: {0}, Now you can  run `python xfi.py run`".format(Path(configStored).resolve()))
    print("\n\n target url: ")
    sys.exit(0)