import dns.resolver
from custom_dkim_selectors_list import custom_dkim_selectors_list

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '8.8.4.4']
resolver.timeout = 5
resolver.lifetime = 5

domain = input("Enter domain: ")

# Check SPF record
try:
    answers = resolver.resolve(domain, 'TXT')
    found_spf = False
    for rdata in answers:
        txt = ''.join([s.decode('utf-8') for s in rdata.strings])
        if txt.startswith('v=spf1'):
            print(f"SPF record for {domain}: {txt}")
            found_spf = True
    if not found_spf:
        print(f"No SPF record found for {domain}")
except Exception as e:
    print(f"Error checking SPF: {e}")

# Check DMARC record
try:
    answers = resolver.resolve(f"_dmarc.{domain}", 'TXT')
    found_dmarc = False
    for rdata in answers:
        txt = ''.join([s.decode('utf-8') for s in rdata.strings])
        if txt.startswith('v=DMARC1'):
            print(f"DMARC record for {domain}: {txt}")
            found_dmarc = True
    if not found_dmarc:
        print(f"No DMARC record found for {domain}")
except Exception as e:
    print(f"Error checking DMARC: {e}")


# Check DKIM selectors
dkim_found = False
for selector in custom_dkim_selectors_list:
    name = f"{selector}._domainkey.{domain}"
    try:
        answers = resolver.resolve(name, 'TXT')
        print(f"Found DKIM selector: {selector}")
        for rdata in answers:
            txt = ''.join([s.decode('utf-8') for s in rdata.strings])
            print(txt)
        dkim_found = True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        pass
    except Exception as e:
        print(f"Error checking {selector}: {e}")
if not dkim_found:
    print(f"No DKIM found for domain: {domain} using provided selectors.")
