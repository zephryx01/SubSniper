#!/usr/bin/env python3

import argparse
import requests


def print_red(text):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(RED + text + RESET)

def banner():
    banner = """
░██████╗██╗░░░██╗██████╗░░██████╗███╗░░██╗██╗██████╗░███████╗██████╗░
██╔════╝██║░░░██║██╔══██╗██╔════╝████╗░██║██║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝╚█████╗░██╔██╗██║██║██████╔╝█████╗░░██████╔╝
░╚═══██╗██║░░░██║██╔══██╗░╚═══██╗██║╚████║██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██████╦╝██████╔╝██║░╚███║██║██║░░░░░███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝       
    """
    print(banner)
    print_red("                                               by M1dkn1ght-M1h1r")

if __name__ == "__main__":
    banner()
    print("")

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Subdomains Enumerating Tool!")
    parser.add_argument("-d", "--domain", help="Target domain (ex. google.com)", required=True)
    parser.add_argument("-w", "--wordlist", help="Path of the wordlist")
    args = parser.parse_args()

    target = args.domain
    wordlist_path = args.wordlist if args.wordlist else 'default.txt'

    print("Domain:", target)
    print("Wordlist:", wordlist_path)

    with open(wordlist_path, 'r') as wordlist_file:
        try:
            for line in wordlist_file:
                subdomain = line.strip()
                test_url = subdomain + '.' + target
                response = request(test_url)
                if response:
                    print("[+] Discovered Subdomain ----->", test_url)
        except KeyboardInterrupt:
            exit 

if __name__ == "__main__":
    main()
