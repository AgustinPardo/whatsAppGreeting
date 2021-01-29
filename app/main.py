import argparse
import os
import sys
import appCore

def captureParse(file):
    with open(file) as file:
        phrase=file.readlines()
        phrase=[ element.rstrip() for element in phrase ]
    print(phrase)
    return phrase

def parse_arguments():
    """Inputs parser"""
    parser = argparse.ArgumentParser(description='Respond to the selected words automatically')
    parser.add_argument("-c", '--capture', default=None, help="File that contains the capture of words/phrases that indicate that you should respond")
    parser.add_argument("-r", '--response', default=None, help="Response message")

    return parser

def main():
    parser=parse_arguments()
    args=parser.parse_args()

    # Check if the capture file exist and is not empty
    if args.capture:
        if not(os.path.exists(args.capture)):
            raise FileNotFoundError(f'{args.capture} file does not exists')
        assert os.stat(args.capture).st_size > 1, f'{args.capture} is empty'
    else:
        sys.stderr.write(
        f'error: You must specify a capture file\n')
        parser.print_help(sys.stderr)
        sys.exit(1)

    driver = appCore.Driver()
    panel = appCore.Panel(driver.driver, driver.getUser(), captureParse(args.capture), args.response)
    panel.greetChats()
    driver.disconnect()

    return 0

if __name__ == "__main__":
    main()
