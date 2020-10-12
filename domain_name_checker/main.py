import whois
import sys

try:
	inputdomain = 'copyassignment.com' # example: 
	domain = whois.whois(inputdomain)
	if domain.domain_name == None:
		sys.exit()
except:
	print('Sorry, this domain name  is already purchased')
else:
	print('This domain name is available')
