#!/usr/bin/env python

import subprocess
import optparse
import re

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


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
         print(bcolors.RED + "[-] Could not read MAC Address.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print(bcolors.YELLOW + "[•] Current MAC = " + str(current_mac))

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
     print(bcolors.GREEN + "[+] MAC Address Was Successfully changed to " + current_mac) 
else:
     print(bcolors.RED + "[-] MAC Address did not get changed ")

#change_mac(options.interface, options.new_mac)

