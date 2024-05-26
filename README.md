# SubSniper
```SubSniper``` is a powerful subdomain enumeration tool designed to quickly discover subdomains of a target domain. With its simple yet efficient approach, ```SubSniper``` helps security professionals, penetration testers, and bug bounty hunters in their reconnaissance phase to identify potential entry points and vulnerabilities in web applications.

## Features
- **Fast and Efficient:** SubSniper utilizes multi-threading to perform subdomain enumeration swiftly.
- **Customizable Wordlists:** Users can specify their own wordlists or rely on a default wordlist for subdomain discovery.
- **Colorful Output:** SubSniper presents results in a visually appealing format, making it easy to distinguish discovered subdomains.
- **User-Friendly:** With a straightforward command-line interface, SubSniper is easy to use for both beginners and experienced users.
- **Flexible:** SubSniper allows users to customize various parameters to suit their specific needs, including the target domain and wordlist.

## Usage
To start using ```SubSniper```, simply specify the target domain using the -d or --domain option and provide a wordlist using the -w or --wordlist option. If no wordlist is provided, ```SubSniper``` will default to using default.txt.
```
python3 subsniper.py -h
```

#### Example usage:
```
python3 subsniper.py -d example.com -w path/to/wordlist
```
## Installation:

> Clone the SubSniper repository from GitHub:
```
git clone https://github.com/midknight-mihir/SubSniper.git
```

> Navigate to the SubSniper directory:
```
cd SubSniper
```

> Ensure you have Python 3 installed on your system.

> Run SubSniper using Python:
```
python3 subsniper.py -d example.com -w path/to/wordlist
```
### Note: Press Enter to use default wordlist.!
