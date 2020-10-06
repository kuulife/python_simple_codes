import whois
import sys

try:
	inputdomain = input('enter domain name: ') # example: copyassignment.com
	domain = whois.whois(inputdomain)
	if domain.domain_name == None:
		sys.exit()
except:
	print('This domain name is available')
else:
	print('Sorry, this domain name  is already purchased')
