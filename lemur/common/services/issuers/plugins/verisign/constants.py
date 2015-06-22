CSR_CONFIG = """
                # Configuration for standard CSR generation for Netflix
                # Used for procuring VeriSign certificates
                # Author: jachan
                # Contact: cloudsecurity@netflix.com

                [ req ]
                # Use a 2048 bit private key
                default_bits       = 2048
                default_keyfile    = key.pem
                prompt             = no
                encrypt_key        = no

                # base request
                distinguished_name = req_distinguished_name

                # extensions
                # Uncomment the following line if you are requesting a SAN cert
                {is_san_comment}req_extensions     = req_ext

                # distinguished_name
                [ req_distinguished_name ]
                countryName            = "US"                     # C=
                stateOrProvinceName    = "CALIFORNIA"                 # ST=
                localityName           = "Los Gatos"                 # L=
                organizationName       = "Netflix, Inc."        # O=
                organizationalUnitName = "{OU}"          # OU=
                # This is the hostname/subject name on the certificate
                commonName             = "{DNS[0]}"            # CN=

                [ req_ext ]
                # Uncomment the following line if you are requesting a SAN cert
                {is_san_comment}subjectAltName          = @alt_names

                [alt_names]
                # Put your SANs here
                {DNS_LINES}
            """

VERISIGN_INTERMEDIATE = """
-----BEGIN CERTIFICATE-----
MIIFFTCCA/2gAwIBAgIQKC4nkXkzkuQo8iGnTsk3rjANBgkqhkiG9w0BAQsFADCB
yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL
ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMTk5OSBWZXJp
U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW
ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0
aG9yaXR5IC0gRzMwHhcNMTMxMDMxMDAwMDAwWhcNMjMxMDMwMjM1OTU5WjB+MQsw
CQYDVQQGEwJVUzEdMBsGA1UEChMUU3ltYW50ZWMgQ29ycG9yYXRpb24xHzAdBgNV
BAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxLzAtBgNVBAMTJlN5bWFudGVjIENs
YXNzIDMgU2VjdXJlIFNlcnZlciBDQSAtIEc0MIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAstgFyhx0LbUXVjnFSlIJluhL2AzxaJ+aQihiw6UwU35VEYJb
A3oNL+F5BMm0lncZgQGUWfm893qZJ4Itt4PdWid/sgN6nFMl6UgfRk/InSn4vnlW
9vf92Tpo2otLgjNBEsPIPMzWlnqEIRoiBAMnF4scaGGTDw5RgDMdtLXO637QYqzu
s3sBdO9pNevK1T2p7peYyo2qRA4lmUoVlqTObQJUHypqJuIGOmNIrLRM0XWTUP8T
L9ba4cYY9Z/JJV3zADreJk20KQnNDz0jbxZKgRb78oMQw7jW2FUyPfG9D72MUpVK
Fpd6UiFjdS8W+cRmvvW1Cdj/JwDNRHxvSz+w9wIDAQABo4IBQDCCATwwHQYDVR0O
BBYEFF9gz2GQVd+EQxSKYCqy9Xr0QxjvMBIGA1UdEwEB/wQIMAYBAf8CAQAwawYD
VR0gBGQwYjBgBgpghkgBhvhFAQc2MFIwJgYIKwYBBQUHAgEWGmh0dHA6Ly93d3cu
c3ltYXV0aC5jb20vY3BzMCgGCCsGAQUFBwICMBwaGmh0dHA6Ly93d3cuc3ltYXV0
aC5jb20vcnBhMC8GA1UdHwQoMCYwJKAioCCGHmh0dHA6Ly9zLnN5bWNiLmNvbS9w
Y2EzLWczLmNybDAOBgNVHQ8BAf8EBAMCAQYwKQYDVR0RBCIwIKQeMBwxGjAYBgNV
BAMTEVN5bWFudGVjUEtJLTEtNTM0MC4GCCsGAQUFBwEBBCIwIDAeBggrBgEFBQcw
AYYSaHR0cDovL3Muc3ltY2QuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQBbF1K+1lZ7
9Pc0CUuWysf2IdBpgO/nmhnoJOJ/2S9h3RPrWmXk4WqQy04q6YoW51KN9kMbRwUN
gKOomv4p07wdKNWlStRxPA91xQtzPwBIZXkNq2oeJQzAAt5mrL1LBmuaV4oqgX5n
m7pSYHPEFfe7wVDJCKW6V0o6GxBzHOF7tpQDS65RsIJAOloknO4NWF2uuil6yjOe
soHCL47BJ89A8AShP/U3wsr8rFNtqVNpT+F2ZAwlgak3A/I5czTSwXx4GByoaxbn
5+CdKa/Y5Gk5eZVpuXtcXQGc1PfzSEUTZJXXCm5y2kMiJG8+WnDcwJLgLeVX+OQr
J+71/xuzAYN6
-----END CERTIFICATE-----
"""


VERISIGN_ROOT = """
-----BEGIN CERTIFICATE-----
MIIEGjCCAwICEQCbfgZJoz5iudXukEhxKe9XMA0GCSqGSIb3DQEBBQUAMIHKMQsw
CQYDVQQGEwJVUzEXMBUGA1UEChMOVmVyaVNpZ24sIEluYy4xHzAdBgNVBAsTFlZl
cmlTaWduIFRydXN0IE5ldHdvcmsxOjA4BgNVBAsTMShjKSAxOTk5IFZlcmlTaWdu
LCBJbmMuIC0gRm9yIGF1dGhvcml6ZWQgdXNlIG9ubHkxRTBDBgNVBAMTPFZlcmlT
aWduIENsYXNzIDMgUHVibGljIFByaW1hcnkgQ2VydGlmaWNhdGlvbiBBdXRob3Jp
dHkgLSBHMzAeFw05OTEwMDEwMDAwMDBaFw0zNjA3MTYyMzU5NTlaMIHKMQswCQYD
VQQGEwJVUzEXMBUGA1UEChMOVmVyaVNpZ24sIEluYy4xHzAdBgNVBAsTFlZlcmlT
aWduIFRydXN0IE5ldHdvcmsxOjA4BgNVBAsTMShjKSAxOTk5IFZlcmlTaWduLCBJ
bmMuIC0gRm9yIGF1dGhvcml6ZWQgdXNlIG9ubHkxRTBDBgNVBAMTPFZlcmlTaWdu
IENsYXNzIDMgUHVibGljIFByaW1hcnkgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkg
LSBHMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMu6nFL8eB8aHm8b
N3O9+MlrlBIwT/A2R/XQkQr1F8ilYcEWQE37imGQ5XYgwREGfassbqb1EUGO+i2t
KmFZpGcmTNDovFJbcCAEWNF6yaRpvIMXZK0Fi7zQWM6NjPXr8EJJC52XJ2cybuGu
kxUccLwgTS8Y3pKI6GyFVxEa6X7jJhFUokWWVYPKMIno3Nij7SqAP395ZVc+FSBm
CC+Vk7+qRy+oRpfwEuL+wgorUeZ25rdGt+INpsyow0xZVYnm6FNcHOqd8GIWC6fJ
Xwzw3sJ2zq/3avL6QaaiMxTJ5Xpj055iN9WFZZ4O5lMkdBteHRJTW8cs54NJOxWu
imi5V5cCAwEAATANBgkqhkiG9w0BAQUFAAOCAQEAERSWwauSCPc/L8my/uRan2Te
2yFPhpk0djZX3dAVL8WtfxUfN2JzPtTnX84XA9s1+ivbrmAJXx5fj267Cz3qWhMe
DGBvtcC1IyIuBwvLqXTLR7sdwdela8wv0kL9Sd2nic9TutoAWii/gt/4uhMdUIaC
/Y4wjylGsB49Ndo4YhYYSq3mtlFs3q9i6wHQHiT+eo8SGhJouPtmmRQURVyu565p
F4ErWjfJXir0xuKhXFSbplQAz/DxwceYMBo7Nhbbo27q/a2ywtrvAkcTisDxszGt
TxzhT5yvDwyd93gN2PQ1VoDat20Xj50egWTh/sVFuq1ruQp6Tk9LhO5L8X3dEQ==
-----END CERTIFICATE-----
"""

OLD_VERISIGN_INTERMEDIATE = """
-----BEGIN CERTIFICATE-----
MIIFlTCCBH2gAwIBAgIQLP62CQ7ireLp/CI3JPG2vzANBgkqhkiG9w0BAQUFADCB
yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL
ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMTk5OSBWZXJp
U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW
ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0
aG9yaXR5IC0gRzMwHhcNMTAwMjA4MDAwMDAwWhcNMjAwMjA3MjM1OTU5WjCBtTEL
MAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZW
ZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTswOQYDVQQLEzJUZXJtcyBvZiB1c2UgYXQg
aHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL3JwYSAoYykxMDEvMC0GA1UEAxMmVmVy
aVNpZ24gQ2xhc3MgMyBTZWN1cmUgU2VydmVyIENBIC0gRzMwggEiMA0GCSqGSIb3
DQEBAQUAA4IBDwAwggEKAoIBAQCxh4QfwgxF9byrJZenraI+nLr2wTm4i8rCrFbG
5btljkRPTc5v7QlK1K9OEJxoiy6Ve4mbE8riNDTB81vzSXtig0iBdNGIeGwCU/m8
f0MmV1gzgzszChew0E6RJK2GfWQS3HRKNKEdCuqWHQsV/KNLO85jiND4LQyUhhDK
tpo9yus3nABINYYpUHjoRWPNGUFP9ZXse5jUxHGzUL4os4+guVOc9cosI6n9FAbo
GLSa6Dxugf3kzTU2s1HTaewSulZub5tXxYsU5w7HnO1KVGrJTcW/EbGuHGeBy0RV
M5l/JJs/U0V/hhrzPPptf4H1uErT9YU3HLWm0AnkGHs4TvoPAgMBAAGjggGIMIIB
hDASBgNVHRMBAf8ECDAGAQH/AgEAMHAGA1UdIARpMGcwZQYLYIZIAYb4RQEHFwMw
VjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL2NwczAqBggr
BgEFBQcCAjAeGhxodHRwczovL3d3dy52ZXJpc2lnbi5jb20vcnBhMA4GA1UdDwEB
/wQEAwIBBjBtBggrBgEFBQcBDARhMF+hXaBbMFkwVzBVFglpbWFnZS9naWYwITAf
MAcGBSsOAwIaBBSP5dMahqyNjmvDz4Bq1EgYLHsZLjAlFiNodHRwOi8vbG9nby52
ZXJpc2lnbi5jb20vdnNsb2dvLmdpZjAoBgNVHREEITAfpB0wGzEZMBcGA1UEAxMQ
VmVyaVNpZ25NUEtJLTItNjAdBgNVHQ4EFgQUDURcFlNEwYJ+HSCrJfQBY9i+eaUw
NAYDVR0fBC0wKzApoCegJYYjaHR0cDovL2NybC52ZXJpc2lnbi5jb20vcGNhMy1n
My5jcmwwDQYJKoZIhvcNAQEFBQADggEBAHREFQzFWA4YY+3z8CjDeuuSSG/ghSBJ
olwwlpIX4IjoeYuzT864Hzk2tTeEeODf4YFIVsSxah8nUsGdpgVTUGPPoUJOMXvn
8wJeBSlUDXBwv3td5XbPIPXHy6vmIS6phYRetZUgq1CDTI/pvtWZKXTGM/eYXlLF
6QDvXevUHQjfb3cqQvfLljws85xLxbNFmz7cy9YmiLOd5n+gFC6X5hzSDO7+DDMi
o//+4Q/nk/UId1UCsobqYWVmqs017AmyiAPO/v3sGncYYQY2BMYgla74dZfeDNu4
MXA68Mb6ZdlkhGEmZYVBcOmkaKs+P+SggTofsK27BlpugAtNWjEy5JY=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIEOzCCA6SgAwIBAgIQSsnqCI7m94zHpfn6OaSTljANBgkqhkiG9w0BAQUFADBf
MQswCQYDVQQGEwJVUzEXMBUGA1UEChMOVmVyaVNpZ24sIEluYy4xNzA1BgNVBAsT
LkNsYXNzIDMgUHVibGljIFByaW1hcnkgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkw
HhcNMTEwNjA5MDAwMDAwWhcNMjExMTA3MjM1OTU5WjCByjELMAkGA1UEBhMCVVMx
FzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZWZXJpU2lnbiBUcnVz
dCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMTk5OSBWZXJpU2lnbiwgSW5jLiAtIEZv
ciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxWZXJpU2lnbiBDbGFzcyAz
IFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0aG9yaXR5IC0gRzMwggEi
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDLupxS/HgfGh5vGzdzvfjJa5QS
ME/wNkf10JEK9RfIpWHBFkBN+4phkOV2IMERBn2rLG6m9RFBjvotrSphWaRnJkzQ
6LxSW3AgBFjResmkabyDF2StBYu80FjOjYz16/BCSQudlydnMm7hrpMVHHC8IE0v
GN6SiOhshVcRGul+4yYRVKJFllWDyjCJ6NzYo+0qgD9/eWVXPhUgZggvlZO/qkcv
qEaX8BLi/sIKK1Hmdua3RrfiDabMqMNMWVWJ5uhTXBzqnfBiFgunyV8M8N7Cds6v
92ry+kGmojMUyeV6Y9OeYjfVhWWeDuZTJHQbXh0SU1vHLOeDSTsVropouVeXAgMB
AAGjggEGMIIBAjAPBgNVHRMBAf8EBTADAQH/MD0GA1UdIAQ2MDQwMgYEVR0gADAq
MCgGCCsGAQUFBwIBFhxodHRwczovL3d3dy52ZXJpc2lnbi5jb20vY3BzMDEGA1Ud
HwQqMCgwJqAkoCKGIGh0dHA6Ly9jcmwudmVyaXNpZ24uY29tL3BjYTMuY3JsMA4G
A1UdDwEB/wQEAwIBBjBtBggrBgEFBQcBDARhMF+hXaBbMFkwVzBVFglpbWFnZS9n
aWYwITAfMAcGBSsOAwIaBBSP5dMahqyNjmvDz4Bq1EgYLHsZLjAlFiNodHRwOi8v
bG9nby52ZXJpc2lnbi5jb20vdnNsb2dvLmdpZjANBgkqhkiG9w0BAQUFAAOBgQBl
2Sr58sJgybnqQQfKNrcYL2iu/gMk5mdU7nTDLNn1M8Fetw6Tz3iejrImFBFT0cjC
EiG0PXsq2BzUS2TsiU+/lYeH3pVk9HPGF9+9GZCX6GmBEmlmStMkQA5ZdRWwRHQX
op4GYNOwg7jdL+afe2dcFqFH284ueQXZ8fT4PuJKoQ==
-----END CERTIFICATE-----
"""