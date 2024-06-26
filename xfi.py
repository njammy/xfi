import sys
import argparse
from modules import config
from modules.ymlReader import YmlReader
from modules.xfiController import xfiController

def main(args):    
    parser = argparse.ArgumentParser(description="Evaluate Local and Remote File inclusion on web sever")
    parser.set_defaults(func=lambda _: parser.print_help())

    action = parser.add_subparsers()
    configure_action = action.add_parser("configure", help="configure target")
    run_parser = action.add_parser("run", help="run xfi")

    configure_action.set_defaults(func = configure)
    run_parser.set_defaults(func = run)

    args = parser.parse_args()
    return args.func(args)


def configure(args):
    config.saveConfig(args)

def run(args):
    config = YmlReader.load_file('config.yaml')
    controller = xfiController()
    controller.lfi() if config['type']=='LFI' else controller.rfi()

if __name__ == "__main__":
    main(sys.argv[1:])