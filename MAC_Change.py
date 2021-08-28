#!/usr/bin/env python

import subprocess
import optparse


class bcolors:
        GREEN = "\033[92m"
        LUV = "\033[0m"
        RED = "\033[1;31;40m"
        YELLOW = "\033[1;33;40m"




def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface To Change Its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(bcolors.RED +"[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error(bcolors.RED +"[-] Please specify an interface, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print(bcolors.GREEN + "[+] Changing MAC Address For " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
