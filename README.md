# f5_ssl_cipher_report
Python script that generates list of VIPs, associated profiles, and cipher string/list for SSL profiles in use

Usage:

1) Modify the script and set the BIG_IP variables (IP address, username and password)
2) Execute 'python f5_ssl_scan.py'

Sample output:

Found Client SSL profile: clientssl\n
 -> Ciphers: DEFAULT\n
 -> Retreiving complete cipher list\n
Found Client SSL profile: clientssl-insecure-compatible\n
 -> Ciphers: !SSLv2:ALL:!DH:!ADH:!EDH:@SPEED\n
 -> Retreiving complete cipher list\n
Found Client SSL profile: clientssl-secure\n
 -> Ciphers: ecdhe:rsa:!sslv3:!rc4:!exp:!des\n
 -> Retreiving complete cipher list\n
Found Client SSL profile: crypto-server-default-clientssl\n
 -> Ciphers: DHE-RSA-AES256-GCM-SHA384\n
 -> Retreiving complete cipher list\n
Found Client SSL profile: greg_example_1\n
 -> Ciphers: !TLSv1:ECDHE\n
 -> Retreiving complete cipher list\n
Found Client SSL profile: greg_example_2\n
 -> Ciphers: !EDH:RSA\n
 -> Retreiving complete cipher list\n
Found Client SSL profile: wom-default-clientssl\n
 -> Ciphers: DEFAULT\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: apm-default-serverssl\n
 -> Ciphers: DEFAULT\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: crypto-client-default-serverssl\n
 -> Ciphers: DHE-RSA-AES256-GCM-SHA384\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: greg_example_4\n
 -> Ciphers: ECDHE:!RSA\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: pcoip-default-serverssl\n
 -> Ciphers: DEFAULT\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: serverssl\n
 -> Ciphers: DEFAULT\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: serverssl-insecure-compatible\n
 -> Ciphers: !SSLv2:!EXPORT:!DH:RSA+RC4:RSA+AES:RSA+DES:RSA+3DES:ECDHE+AES:ECDHE+3DES:@SPEED\n
 -> Retreiving complete cipher list\n
Found Server SSL profile: wom-default-serverssl\n
 -> Ciphers: DEFAULT\n
 -> Retreiving complete cipher list\n
************************************************************************************************************************\n
Virtual server found: greg_example_1\n
************************************************************************************************************************\n
 -> Profile found: greg_example_1 (Context: clientside)\n
   -> Cipher string: !TLSv1:ECDHE\n
   -> Complete cipher list: \n
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX\n
 0: 49200  ECDHE-RSA-AES256-GCM-SHA384      256  TLS1.2  Native  AES-GCM   SHA384  ECDHE_RSA \n
 1: 49192  ECDHE-RSA-AES256-SHA384          256  TLS1.2  Native  AES       SHA384  ECDHE_RSA \n
 2: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.1  Native  AES       SHA     ECDHE_RSA \n
 3: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.2  Native  AES       SHA     ECDHE_RSA \n
 4: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.1  Native  DES       SHA     ECDHE_RSA \n
 5: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.2  Native  DES       SHA     ECDHE_RSA \n
 6: 49199  ECDHE-RSA-AES128-GCM-SHA256      128  TLS1.2  Native  AES-GCM   SHA256  ECDHE_RSA \n
 7: 49191  ECDHE-RSA-AES128-SHA256          128  TLS1.2  Native  AES       SHA256  ECDHE_RSA \n
 8: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.1  Native  AES       SHA     ECDHE_RSA \n
 9: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.2  Native  AES       SHA     ECDHE_RSA \n
\n
 -> Profile found: tcp (Context: all)\n
   -> Non-SSL Profile\n
*************************\n
* END OF VIRTUAL SERVER *\n
*************************\n
************************************************************************************************************************\n
Virtual server found: greg_example_2\n
************************************************************************************************************************\n
 -> Profile found: greg_example_2 (Context: clientside)\n
   -> Cipher string: !EDH:RSA\n
   -> Complete cipher list: \n
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX\n
 0:   157  AES256-GCM-SHA384                256  TLS1.2  Native  AES-GCM   SHA384  RSA       \n
 1:    61  AES256-SHA256                    256  TLS1.2  Native  AES       SHA256  RSA       \n
 2:    53  AES256-SHA                       256  SSL3    Native  AES       SHA     RSA       \n
 3:    53  AES256-SHA                       256  TLS1    Native  AES       SHA     RSA       \n
 4:    53  AES256-SHA                       256  TLS1.1  Native  AES       SHA     RSA       \n
 5:    53  AES256-SHA                       256  TLS1.2  Native  AES       SHA     RSA       \n
 6:    53  AES256-SHA                       256  DTLS1   Native  AES       SHA     RSA       \n
 7:    10  DES-CBC3-SHA                     168  SSL3    Native  DES       SHA     RSA       \n
 8:    10  DES-CBC3-SHA                     168  TLS1    Native  DES       SHA     RSA       \n
 9:    10  DES-CBC3-SHA                     168  TLS1.1  Native  DES       SHA     RSA       \n
10:    10  DES-CBC3-SHA                     168  TLS1.2  Native  DES       SHA     RSA       \n
11:    10  DES-CBC3-SHA                     168  DTLS1   Native  DES       SHA     RSA       \n
12:   156  AES128-GCM-SHA256                128  TLS1.2  Native  AES-GCM   SHA256  RSA       \n
13:    60  AES128-SHA256                    128  TLS1.2  Native  AES       SHA256  RSA       \n
14:    47  AES128-SHA                       128  SSL3    Native  AES       SHA     RSA       \n
15:    47  AES128-SHA                       128  TLS1    Native  AES       SHA     RSA       \n
16:    47  AES128-SHA                       128  TLS1.1  Native  AES       SHA     RSA       \n
17:    47  AES128-SHA                       128  TLS1.2  Native  AES       SHA     RSA       \n
18:    47  AES128-SHA                       128  DTLS1   Native  AES       SHA     RSA       \n
19:     5  RC4-SHA                          128  SSL3    Native  RC4       SHA     RSA       \n
20:     5  RC4-SHA                          128  TLS1    Native  RC4       SHA     RSA       \n
21:     5  RC4-SHA                          128  TLS1.1  Native  RC4       SHA     RSA       \n
22:     5  RC4-SHA                          128  TLS1.2  Native  RC4       SHA     RSA       \n
23:     4  RC4-MD5                          128  SSL3    Native  RC4       MD5     RSA       \n
24:     4  RC4-MD5                          128  TLS1    Native  RC4       MD5     RSA       \n
25:     4  RC4-MD5                          128  TLS1.1  Native  RC4       MD5     RSA       \n
26:     4  RC4-MD5                          128  TLS1.2  Native  RC4       MD5     RSA       \n
27:     9  DES-CBC-SHA                       64  SSL3    Native  DES       SHA     RSA       \n
28:     9  DES-CBC-SHA                       64  TLS1    Native  DES       SHA     RSA       \n
29:     9  DES-CBC-SHA                       64  TLS1.1  Native  DES       SHA     RSA       \n
30:     9  DES-CBC-SHA                       64  DTLS1   Native  DES       SHA     RSA       \n
31:    98  EXP1024-DES-CBC-SHA               56  SSL3    Native  DES       SHA     RSA       \n
32:    98  EXP1024-DES-CBC-SHA               56  TLS1    Native  DES       SHA     RSA       \n
33:    98  EXP1024-DES-CBC-SHA               56  DTLS1   Native  DES       SHA     RSA       \n
34:   100  EXP1024-RC4-SHA                   56  SSL3    Native  RC4       SHA     RSA       \n
35:   100  EXP1024-RC4-SHA                   56  TLS1    Native  RC4       SHA     RSA       \n
36:     8  EXP-DES-CBC-SHA                   40  SSL3    Native  DES       SHA     RSA       \n
37:     8  EXP-DES-CBC-SHA                   40  TLS1    Native  DES       SHA     RSA       \n
38:     8  EXP-DES-CBC-SHA                   40  DTLS1   Native  DES       SHA     RSA       \n
39:     3  EXP-RC4-MD5                       40  SSL3    Native  RC4       MD5     RSA       \n
40:     3  EXP-RC4-MD5                       40  TLS1    Native  RC4       MD5     RSA       \n
41:   132  CAMELLIA256-SHA                  256  TLS1    Native  CAMELLIA  SHA     RSA       \n
42:   132  CAMELLIA256-SHA                  256  TLS1.1  Native  CAMELLIA  SHA     RSA       \n
43:   132  CAMELLIA256-SHA                  256  TLS1.2  Native  CAMELLIA  SHA     RSA       \n
44:    65  CAMELLIA128-SHA                  128  TLS1    Native  CAMELLIA  SHA     RSA       \n
45:    65  CAMELLIA128-SHA                  128  TLS1.1  Native  CAMELLIA  SHA     RSA       \n
46:    65  CAMELLIA128-SHA                  128  TLS1.2  Native  CAMELLIA  SHA     RSA       \n
\n
 -> Profile found: http (Context: all)\n
   -> Non-SSL Profile\n
 -> Profile found: oneconnect (Context: all)\n
   -> Non-SSL Profile\n
 -> Profile found: tcp (Context: all)\n
   -> Non-SSL Profile\n
*************************\n
* END OF VIRTUAL SERVER *\n
*************************\n
************************************************************************************************************************\n
Virtual server found: greg_example_3\n
************************************************************************************************************************\n
 -> Profile found: clientssl-secure (Context: clientside)\n
   -> Cipher string: ecdhe:rsa:!sslv3:!rc4:!exp:!des\n
   -> Complete cipher list: \n
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX\n
 0: 49200  ECDHE-RSA-AES256-GCM-SHA384      256  TLS1.2  Native  AES-GCM   SHA384  ECDHE_RSA \n
 1: 49192  ECDHE-RSA-AES256-SHA384          256  TLS1.2  Native  AES       SHA384  ECDHE_RSA \n
 2: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1    Native  AES       SHA     ECDHE_RSA \n
 3: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.1  Native  AES       SHA     ECDHE_RSA \n
 4: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.2  Native  AES       SHA     ECDHE_RSA \n
 5: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1    Native  DES       SHA     ECDHE_RSA \n
 6: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.1  Native  DES       SHA     ECDHE_RSA \n
 7: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.2  Native  DES       SHA     ECDHE_RSA \n
 8: 49199  ECDHE-RSA-AES128-GCM-SHA256      128  TLS1.2  Native  AES-GCM   SHA256  ECDHE_RSA \n
 9: 49191  ECDHE-RSA-AES128-SHA256          128  TLS1.2  Native  AES       SHA256  ECDHE_RSA \n
10: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1    Native  AES       SHA     ECDHE_RSA \n
11: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.1  Native  AES       SHA     ECDHE_RSA \n
12: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.2  Native  AES       SHA     ECDHE_RSA \n
13:   157  AES256-GCM-SHA384                256  TLS1.2  Native  AES-GCM   SHA384  RSA       \n
14:    61  AES256-SHA256                    256  TLS1.2  Native  AES       SHA256  RSA       \n
15:    53  AES256-SHA                       256  TLS1    Native  AES       SHA     RSA       \n
16:    53  AES256-SHA                       256  TLS1.1  Native  AES       SHA     RSA       \n
17:    53  AES256-SHA                       256  TLS1.2  Native  AES       SHA     RSA       \n
18:    53  AES256-SHA                       256  DTLS1   Native  AES       SHA     RSA       \n
19:    10  DES-CBC3-SHA                     168  TLS1    Native  DES       SHA     RSA       \n
20:    10  DES-CBC3-SHA                     168  TLS1.1  Native  DES       SHA     RSA       \n
21:    10  DES-CBC3-SHA                     168  TLS1.2  Native  DES       SHA     RSA       \n
22:    10  DES-CBC3-SHA                     168  DTLS1   Native  DES       SHA     RSA       \n
23:   156  AES128-GCM-SHA256                128  TLS1.2  Native  AES-GCM   SHA256  RSA       \n
24:    60  AES128-SHA256                    128  TLS1.2  Native  AES       SHA256  RSA       \n
25:    47  AES128-SHA                       128  TLS1    Native  AES       SHA     RSA       \n
26:    47  AES128-SHA                       128  TLS1.1  Native  AES       SHA     RSA       \n
27:    47  AES128-SHA                       128  TLS1.2  Native  AES       SHA     RSA       \n
28:    47  AES128-SHA                       128  DTLS1   Native  AES       SHA     RSA       \n
29:   132  CAMELLIA256-SHA                  256  TLS1    Native  CAMELLIA  SHA     RSA       \n
30:   132  CAMELLIA256-SHA                  256  TLS1.1  Native  CAMELLIA  SHA     RSA       \n
31:   132  CAMELLIA256-SHA                  256  TLS1.2  Native  CAMELLIA  SHA     RSA       \n
32:    65  CAMELLIA128-SHA                  128  TLS1    Native  CAMELLIA  SHA     RSA       \n
33:    65  CAMELLIA128-SHA                  128  TLS1.1  Native  CAMELLIA  SHA     RSA       \n
34:    65  CAMELLIA128-SHA                  128  TLS1.2  Native  CAMELLIA  SHA     RSA       \n
\n
 -> Profile found: tcp (Context: all)\n
   -> Non-SSL Profile\n
*************************\n
* END OF VIRTUAL SERVER *\n
*************************\n
************************************************************************************************************************\n
Virtual server found: greg_example_4\n
************************************************************************************************************************\n
 -> Profile found: greg_example_4 (Context: serverside)\n
   -> Cipher string: ECDHE:!RSA\n
   -> Complete cipher list: \n
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX\n
 0: 49200  ECDHE-RSA-AES256-GCM-SHA384      256  TLS1.2  Native  AES-GCM   SHA384  ECDHE_RSA \n
 1: 49192  ECDHE-RSA-AES256-SHA384          256  TLS1.2  Native  AES       SHA384  ECDHE_RSA \n
 2: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1    Native  AES       SHA     ECDHE_RSA \n
 3: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.1  Native  AES       SHA     ECDHE_RSA \n
 4: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.2  Native  AES       SHA     ECDHE_RSA \n
 5: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1    Native  DES       SHA     ECDHE_RSA \n
 6: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.1  Native  DES       SHA     ECDHE_RSA \n
 7: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.2  Native  DES       SHA     ECDHE_RSA \n
 8: 49199  ECDHE-RSA-AES128-GCM-SHA256      128  TLS1.2  Native  AES-GCM   SHA256  ECDHE_RSA \n
 9: 49191  ECDHE-RSA-AES128-SHA256          128  TLS1.2  Native  AES       SHA256  ECDHE_RSA \n
10: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1    Native  AES       SHA     ECDHE_RSA \n
11: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.1  Native  AES       SHA     ECDHE_RSA \n
12: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.2  Native  AES       SHA     ECDHE_RSA \n
\n
 -> Profile found: tcp (Context: all)\n
   -> Non-SSL Profile\n
*************************\n
* END OF VIRTUAL SERVER *\n
*************************\n
