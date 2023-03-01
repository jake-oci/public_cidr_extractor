## cidr_extractor script
If you want to get a general understanding of what CIDR ranges are being used for a specific OCI service using the Oracle Service Network, this is the script that will do it.

## Usage:
#python3 cidr_extractor.py --list OCI_DNS_NAME_1 OCI_DNS_NAME_2 OCI_DNS_NAME_3

## What does the script do?
*Downloads the latest OCI CIDR JSON file. https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json
*Runs 50 DNS queries for each DNS name specified, and collects the IP address.
*Compares the IP addresses it collected with the CIDR ranges in the JSON file

## Example Usage for JMS in Ashburn:
python3 4_cleanup.py --list auth.us-ashburn-1.oraclecloud.com telemetry-ingestion.us-ashburn-1.oraclecloud.com management-agent.us-ashburn-1.oci.oraclecloud.com javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com javamanagement.us-ashburn-1.oci.oraclecloud.com ingestion.logging.us-ashburn-1.oci.oraclecloud.com objectstorage.us-ashburn-1.oraclecloud.com

### Example Output:

Unique IP's From DNS A Records
['129.213.0.145', '129.213.4.156', '134.70.24.1', '134.70.28.1', '134.70.32.1', '138.1.48.202', '140.91.11.142', '140.91.11.143', '140.91.11.144', '140.91.11.145', '140.91.11.146', '140.91.11.148', '140.91.11.62', '140.91.11.80', '140.91.11.81', '140.91.12.148', '140.91.12.149', '140.91.12.150', '140.91.12.151', '140.91.12.152', '140.91.12.154', '140.91.12.81', '140.91.12.98', '140.91.12.99', '140.91.15.120', '140.91.15.121', '140.91.15.122', '140.91.15.123', '140.91.15.124', '140.91.15.125', '140.91.15.59', '140.91.15.75', '140.91.15.77', '147.154.13.111', '147.154.25.141', '147.154.7.99']

CIDRs are from the following OCI Regions
['us-ashburn-1']

Unique CIDR BLOCKS matched with OCI JSON file
['129.213.0.128/25', '129.213.4.128/25', '134.70.24.0/21', '134.70.32.0/22', '138.1.48.0/21', '140.91.10.0/23', '140.91.12.0/22', '147.154.0.0/19']
