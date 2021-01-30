
# Slacker

Difficulty Level: Hard

My friend gave me a thumb drive and said that it will help me for my examination. It also contained some hidden cool tips on how to ace the examination while being a slacker. However, he accidentally deleted it before passing me the drive and I need you to help me recover the document.

### Hints

-  No hints are needed.



## Deployment

Upload Flash.dd in the distrib folder to the static file server

- Flash.dd
    - SHA1: e900ac7ec6667fff2915e530a61e28341b6c55ea
	
## Solution

- In the FAT file system, the deleted files' data remains intact in the Data Area until it is overwritten. This area is also known as the slack space, and is a key part of forensic investigations.
- Mount the dd image - mount secret.dd /mnt/tmp (Linux)
- Mount the dd image - OSFMount(Windows)
- Use forensics toolkit to examine the mounted drive and the deleted files inside - e.g: TestDisk
- Using TestDisk, run the sudo ./testdisk_static. Afterwards, Select "No Log" > The mounted disk name > "None" > "Undelete"

### Flag
`19C4{w0w_4_7ru3_5l4ck3r}`
