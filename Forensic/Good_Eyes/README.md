
# Good_Eyes

Difficulty Level: Hard

Some interesting data is hidden inside the pcap file, try to spot it if you can.

### Hints

-  cThere is something very significant in the least significant bits.



## Deployment

Upload flag.pcapng in distrib to static file server.

- Flag.Pcapng
    - SHA1:e8945b2ff16457808bdc51290861404d1a33c308
	- Pcap File
	
## Solution

Parse the packet capture using python and scapy. Filter all DNS traffic and extract the additional payloads. Join all payloads to form base64 string. Decode string to get flag.

Sample solution can be found in /solution/solution.py

### Flag
`19C4{y0u_h4V3_a_g00D_eY3}`
