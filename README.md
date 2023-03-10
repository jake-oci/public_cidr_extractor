***This script was Authored by Jake Bloom OCI Principal Network Solution Architect. This is not an Oracle supported script. No liability from this script will be assumed and support is best effort.***


### cidr_extractor.py
If you want to get a general understanding of what CIDR ranges are being used for a specific OCI service using the Oracle Service Network, this is the script that will do it. Most of the output from the script is shown on the terminal so you understand what is being run. The ***Unique CIDR BLOCKS matched with OCI JSON file*** output at the end of the file is the data you are most likely interested in if it's absolutely necessary to filter the public CIDR asvertisements from the OCI Service Gateway. 


### Usage:
#python3 cidr_extractor.py --list OCI_DNS_NAME_1 OCI_DNS_NAME_2 OCI_DNS_NAME_3



### What does the script do?
*Downloads the latest OCI CIDR JSON file. https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json

*Runs 100 DNS queries for each DNS name specified, and collects the IP address.

*Compares the IP addresses it collected with the CIDR ranges in the JSON file



### Example Usage for JMS in Ashburn:
python3 cidr_extractor.py --list auth.us-ashburn-1.oraclecloud.com telemetry-ingestion.us-ashburn-1.oraclecloud.com management-agent.us-ashburn-1.oci.oraclecloud.com javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com javamanagement.us-ashburn-1.oci.oraclecloud.com ingestion.logging.us-ashburn-1.oci.oraclecloud.com objectstorage.us-ashburn-1.oraclecloud.com


### Example Output:

[HOSTNAME IP MAPPINGS]
auth.us-ashburn-1.oraclecloud.com
[1]['129.213.2.151']

telemetry-ingestion.us-ashburn-1.oraclecloud.com
[13]['140.91.11.145', '140.91.11.146', '140.91.11.62', '140.91.11.80', '140.91.12.148', '140.91.12.149', '140.91.12.150', '140.91.12.152', '140.91.12.154', '140.91.12.81', '140.91.15.120', '140.91.15.122', '140.91.15.125']

management-agent.us-ashburn-1.oci.oraclecloud.com
[1]['147.154.13.111']

javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com
[1]['147.154.13.111']

javamanagement.us-ashburn-1.oci.oraclecloud.com
[1]['147.154.13.111']

ingestion.logging.us-ashburn-1.oci.oraclecloud.com
[3]['138.1.48.202', '147.154.25.141', '147.154.7.99']

objectstorage.us-ashburn-1.oraclecloud.com
[3]['134.70.24.1', '134.70.28.1', '134.70.32.1']

**********OCI SPECIFIC INFORMATION**********
OCI REGIONS
[1]['us-ashburn-1']

OCI CIDR MATCHES
[7]['129.213.2.128/25', '140.91.10.0/23', '140.91.12.0/22', '147.154.0.0/19', '138.1.48.0/21', '134.70.24.0/21', '134.70.32.0/22']
