***This script was Authored by Jake Bloom OCI Principal Network Solution Architect. This is not an Oracle supported script. No liability from this script will be assumed and support is best effort.***

# osn\_cidr\_extractor.py

**Description:** Associates IP addresses with OCI CIDRs for specific OCI SaaS Services. This narrows the scope of public IP addresses to test OCI services. 

**General Use Case:** Allows firewall and network administrators to create more precise firewall and route filtering for OCI Proof of Concepts where restrictions are necessary on routes advertised from the Service Gateway over FastConnect.

**WARNING:** These IP's can change at any time. The output from this script is not recommended to be used for a production environment due to the dynamic nature of DNS names.


# What does the script actually do?

*Downloads the latest OCI CIDR JSON file. [https://docs.oracle.com/en-us/iaas/tools/public\_ip\_ranges.json](https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json)

*Runs 100 DNS queries for each DNS name specified and collects the unique IP address.

*Compares the IP addresses it collected with the OSN (Oracle Services Network) CIDR ranges in the OCI CIDR JSON file.

# Usage:

**python3 osn_cidr\_extractor.py --list OCI\_DNS\_NAME\_1 OCI\_DNS\_NAME\_2 OCI\_DNS\_NAME\_3**

### Example Usage for JMS Services in Ashburn:

python3 osn_cidr_extractor.py --list auth.us-ashburn-1.oraclecloud.com telemetry-ingestion.us-ashburn-1.oraclecloud.com management-agent.us-ashburn-1.oci.oraclecloud.com javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com javamanagement.us-ashburn-1.oci.oraclecloud.com ingestion.logging.us-ashburn-1.oci.oraclecloud.com objectstorage.us-ashburn-1.oraclecloud.com


# Parsing the Output

There are 3 pieces of data you will see

**\[HOSTNAME IP MAPPINGS\] ->** Displays the unique IP addresses of each hostname based on the 100 DNS requests.

**OCI REGIONS ->** Displays which region your IP blocks are associated with. 

**OCI CIDR MATCHES ->** Iterates through the OCI JSON file, and finds which OCI CIDR blocks the DNS names are associated with.

**Example Output for JMS Services in Ashburn**

\[HOSTNAME IP MAPPINGS\]

auth.us-ashburn-1.oraclecloud.com

\[1\]\['129.213.2.151'\]

telemetry-ingestion.us-ashburn-1.oraclecloud.com

\[13\]\['140.91.11.145', '140.91.11.146', '140.91.11.62', '140.91.11.80', '140.91.12.148', '140.91.12.149', '140.91.12.150', '140.91.12.152', '140.91.12.154', '140.91.12.81', '140.91.15.120', '140.91.15.122', '140.91.15.125'\]

management-agent.us-ashburn-1.oci.oraclecloud.com

\[1\]\['147.154.13.111'\]

javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com
\[1\]\['147.154.13.111'\]

javamanagement.us-ashburn-1.oci.oraclecloud.com
\[1\]\['147.154.13.111'\]

ingestion.logging.us-ashburn-1.oci.oraclecloud.com
\[3\]\['138.1.48.202', '147.154.25.141', '147.154.7.99'\]

objectstorage.us-ashburn-1.oraclecloud.com
\[3\]\['134.70.24.1', '134.70.28.1', '134.70.32.1'\]

**********OCI SPECIFIC INFORMATION**********
OCI REGIONS
\[1\]\['us-ashburn-1'\]

OCI CIDR MATCHES
\[7\]\['129.213.2.128/25', '140.91.10.0/23', '140.91.12.0/22', '147.154.0.0/19', '138.1.48.0/21', '134.70.24.0/21', '134.70.32.0/22'\]
