***This script was Authored by Jake Bloom OCI Principal Network Solution Architect. This is not an Oracle supported script. No liability from this script will be assumed and support is best effort.***

# osn\_cidr\_extractor.py

**Description:** Associates IP addresses with OCI CIDRs for specific OCI SaaS Services. This narrows the scope of public IP addresses to test OCI services.

**General Use Case:** Allows firewall and network administrators to create more precise firewall and route filtering for OCI Proof of Concepts where restrictions are necessary on routes advertised from the Service Gateway over FastConnect.

**WARNING:** These IP's can change at any time. The output from this script is not recommended to be used for a production environment due to the dynamic nature of DNS names.

**WARNING2:** Other OCI services may share the same public CIDRs as the service you are trying to look up. There may be unintended consequences of this script if you only allow traffic from a single SaaS service and multiple SaaS services are in use.

# What does the script actually do?

*Downloads the latest OCI CIDR JSON file. [https://docs.oracle.com/en-us/iaas/tools/public\_ip\_ranges.json](https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json)

*Runs 100 DNS queries for each DNS name specified and collects the unique IP address.

*Compares the IP addresses it collected with the OSN (Oracle Services Network) CIDR ranges in the OCI CIDR JSON file.

# Usage:

**python3 osn\_cidr\_extractor.py --list OCI\_DNS\_NAME\_1 OCI\_DNS\_NAME\_2 OCI\_DNS\_NAME_3**

### Example Usage for JMS Services in Ashburn:

python3 osn\_cidr\_extractor.py --list auth.us-ashburn-1.oraclecloud.com telemetry-ingestion.us-ashburn-1.oraclecloud.com management-agent.us-ashburn-1.oci.oraclecloud.com javamanagement-ingest.us-ashburn-1.oci.oraclecloud.com javamanagement.us-ashburn-1.oci.oraclecloud.com ingestion.logging.us-ashburn-1.oci.oraclecloud.com objectstorage.us-ashburn-1.oraclecloud.com

# Parsing the Output

**\[HOSTNAME IP MAPPINGS\] ->** Displays the unique IP addresses of each hostname based on the 100 DNS requests.

**OCI REGIONS ->** Displays which region your IP blocks are associated with.

**OCI CIDR MATCHES ->** Iterates through the OCI JSON file, and finds which OCI CIDR blocks the DNS names are associated with.

# **Example Output for JMS Services in Ashburn**

![image](https://user-images.githubusercontent.com/126630123/224348444-f4e0c255-c5f7-4155-8a50-027304ee3f07.png)

