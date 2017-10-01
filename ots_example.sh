### create your file
# vim my_file.txt

### create the ots proof 
ots-cli.js stamp my_file.txt
# The timestamp proof 'my_file.txt.ots' has been created!

###  check availables gpg keys 
gpg --fingerprint valerio.vaccaro@gmail.com
# pub   4096R/74D20CFD 2017-02-12 [expires: 2021-02-12]
#     Key fingerprint = 67AC 09CB 8997 9409 D44B  DC83 18B4 C711 74D2 0CFD
# uid       [ultimate] Valerio Vaccaro <valerio.vaccaro@gmail.com>

### sign the file 
gpg --sign my_file.txt

### verify signature
gpg --verify my_file.txt.gpg
# gpg: Signature made Wed Sep  6 10:15:42 2017 CEST using RSA key ID 833A220E
# gpg: Good signature from "Valerio Vaccaro <valerio.vaccaro@gmail.com>" [ultimate]

### stamp the signature
ots-cli.js stamp my_file.txt.gpg
# The timestamp proof 'my_file.txt.gpg.ots' has been created!

### Upgrade the proof
ots-cli.js upgrade my_file.txt.gpg.ots
# Timestamp has been successfully upgraded!
# The file .ots was upgraded!
# The file .bak was saved!
