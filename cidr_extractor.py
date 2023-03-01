import json, ipaddress, requests, argparse

#Usage
#python3 cidr_extractor.py --list OCI_DNS_NAME_1 OCI_DNS_NAME_2 OCI_DNS_NAME_3

#Example for JMS
#python3 cidr_extractor.py --list auth.us-ashburn-1.oraclecloud.com telemetry-ingestion.us-ashburn-1.oraclecloud.com management-agent.us-ashburn-1.oci.oraclecloud.com javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com javamanagement.us-ashburn-1.oci.oraclecloud.com ingestion.logging.us-ashburn-1.oci.oraclecloud.com objectstorage.us-ashburn-1.oraclecloud.com

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

#Return A Record 50 Times. Run a new DNS query every time to avoid cache lookups.
list=[]
for hostname in hostname_list:
    count=0
    print(hostname)
    while count<50:
        resolver=dns.resolver.Resolver(configure=False)
        resolver.nameservers = ['1.1.1.1','8.8.8.8']
        answer=resolver.resolve(hostname, 'a')
        for ipval in answer:
            ipaddr=(ipval.to_text())
            print("HOSTNAME - {} IP ADDRESS - {}".format(hostname,ipaddr))
            list.append(ipaddr)
        count=count+1

#Iterate Through List of IPs, and return Unique IPs
unique_ip_list=[]
for x in list:
    if x not in unique_ip_list:
        unique_ip_list.append(x)
print("")
print("Unique IP's From DNS A Records")
print(sorted(unique_ip_list))

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

# Parse through the JSON and find matching CIDR blocks. Searches through all of the regions, just in case.
cidr_blocks=[]
regions_in_json=[]
for ip_addr in unique_ip_list:
    for region in cidrs:
        for c in region['cidrs']:
            if ipaddress.ip_address(ip_addr) in ipaddress.ip_network(c['cidr']):
                #cidr_found=("{}-{}").format(region['region'], c['cidr'])
                #Uncomment this line if you want to see the region for each prefix.
                region_found=(region['region'])
                regions_in_json.append(region_found)
                cidr_found=("{}").format(c['cidr'])
                cidr_blocks.append(cidr_found)

#Find the unique CIDR Blocks
unique_cidr_blocks=[]
for x in cidr_blocks:
    if x not in unique_cidr_blocks:
        unique_cidr_blocks.append(x)

#Find the unique Regions
unique_regions=[]
for x in regions_in_json:
    if x not in unique_regions:
        unique_regions.append(x)

print("")
print("CIDRs are from the following OCI Regions")
print(unique_regions)
print("")
print("Unique CIDR BLOCKS matched with OCI JSON file")
print(sorted(unique_cidr_blocks))
print("")
print("There are {} unique CIDRs in this list.".format(len(unique_cidr_blocks)))
