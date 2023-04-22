from colorama import *
import requests, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL to scan", required=True)
parser.add_argument("-p", "--payloads", help="Payloads list", required=True)
args = parser.parse_args()

init(autoreset=True)
def fuzz(url, payloads):
    for playload in open(payloads, "r").readlines():
        new_url = url.replace('{fuzz}', playload)
        request = requests.get(new_url)

        if request.elapsed.total_seconds() > 7:
            print(Style.BRIGHT + Fore.RED + "Timeout detected with ", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not work with this playload: ", playload)

def verify(url):
    url_test = url.replace('{fuzz}', '')
    req = requests.get(url_test)

    if req.elapsed.total_seconds() > 6:
        sys.exit(Style.BRIGHT + Fore.RED + "Please make sure you have a good connection to run the scanner")
    else:
        fuzz(args.url, args.payloads)

if not '{fuzz}' in args.url:
    sys.exit(Style.BRIGHT + Fore.RED + 'Missing {fuzz} parameter !')
else:
    verify(args.url)
