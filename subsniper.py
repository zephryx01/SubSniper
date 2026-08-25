#!/usr/bin/env python3

import argparse
import concurrent.futures

import requests

DEFAULT_TIMEOUT = 10


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
    print_red("                                               by zephryx")


def check_subdomain(target, subdomain, timeout):
    test_url = f"{subdomain}.{target}"
    for scheme in ("https", "http"):
        try:
            response = requests.get(f"{scheme}://{test_url}", timeout=timeout)
        except requests.exceptions.RequestException:
            continue
        if response.ok:
            print(f"[+] Discovered Subdomain -----> {test_url} ({scheme}, {response.status_code})")
        return


def main():
    parser = argparse.ArgumentParser(description="Subdomains Enumerating Tool by Zephryx01")
    parser.add_argument("-d", "--domain", help="Target domain (ex. google.com)", required=True)
    parser.add_argument("-w", "--wordlist", help="Path of the wordlist")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of concurrent threads (default: 20)")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help="Request timeout in seconds (default: 10)")
    args = parser.parse_args()

    target = args.domain
    wordlist_path = args.wordlist if args.wordlist else 'default.txt'

    banner()
    print("")
    print("Domain:", target)
    print("Wordlist:", wordlist_path)
    print("Threads:", args.threads)
    print("")

    with open(wordlist_path, 'r') as wordlist_file:
        subdomains = [line.strip() for line in wordlist_file if line.strip()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [
            executor.submit(check_subdomain, target, subdomain, args.timeout)
            for subdomain in subdomains
        ]
        try:
            for future in concurrent.futures.as_completed(futures):
                future.result()
        except KeyboardInterrupt:
            for future in futures:
                future.cancel()
            print_red("\nInterrupted, stopping.")


if __name__ == "__main__":
    main()
