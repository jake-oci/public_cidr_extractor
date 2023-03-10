import json, ipaddress, requests, argparse

#Requires dnspython to be installed
try: 
    import dns.resolver
except ImportError: 
    print("This script requires dnspython modules")
    print("pip3 install dnspython")
    raise SystemExit

#Pass Hostname Argument through CLI
CLI=argparse.ArgumentParser()
CLI.add_argument('--list', nargs='+', required=True)
args=CLI.parse_args()
hostname_list=[]
hostname_list=args.list

#Return A Record 100 Times. Run a new DNS query every time to avoid cache lookups.
list=[]
print("")
print("[HOSTNAME IP MAPPINGS]")
for hostname in hostname_list:
    count=int(0)
    ip_list=[]
    if count<int(100):
        resolver=dns.resolver.Resolver(configure=False)
        resolver.nameservers = ['1.1.1.1','8.8.8.8']
        answer=resolver.resolve(hostname, 'a')
        for ipval in answer:
            unique_list_counter=[]
            ipaddr=(ipval.to_text())
            list.append(ipaddr)
            ip_list.append(ipaddr)
            unique_list_counter.append(ipaddr)
            count=count+1
    print(hostname)
    print("[{}]{}".format(len(ip_list),sorted(ip_list)))
    print("")
        
#Iterate Through List of IPs, and return Unique IPs
unique_ip_list=[]
for x in list:
    if x not in unique_ip_list:
        unique_ip_list.append(x)

# Download Latest OCI JSON file
url = 'https://docs.oracle.com/iaas/tools/public_ip_ranges.json'
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    with open('cidrs.json', 'w') as f:
        f.write(response.text)
    #print('Latest JSON downloaded')
    regions = json.loads(response.text)
    cidrs = (regions["regions"])
else:
    print(f'Error retrieving JSON file: {response.status_code}')

cidr_blocks=[]
regions_in_json=[]
for ip_addr in unique_ip_list:
    match=None
    for region in cidrs:
        for c in region['cidrs']:
            if ipaddress.ip_address(ip_addr) in ipaddress.ip_network(c['cidr']):
                region_found=(region['region'])
                regions_in_json.append(region_found)
                cidr_found=("{}").format(c['cidr'])
                cidr_blocks.append(cidr_found)
                match=True
    if match is None:
        print("ERROR: {} does not belong to an OCI CIDR range. Script will not continue".format(hostname))
        raise SystemExit
unique_cidr_blocks=[]
for x in cidr_blocks:
    if x not in unique_cidr_blocks:
        unique_cidr_blocks.append(x)
    
unique_regions=[]
for x in regions_in_json:
    if x not in unique_regions:
        unique_regions.append(x)

print("**********OCI SPECIFIC INFORMATION**********")
print("OCI REGIONS")
print("[{}]{}".format(len(unique_regions),unique_regions))
print("")
print("OCI CIDR MATCHES")
print("[{}]{}".format(len(unique_cidr_blocks),unique_cidr_blocks))
