# f5_ssl_cipher_report
Python script that generates list of VIPs, associated profiles, and cipher string/list for SSL profiles in use

Usage:

1) Modify the script and set the BIG_IP variables (IP address, username and password)
2) Execute 'python f5_ssl_scan.py'

Sample output:

Found Client SSL profile: clientssl<br/>
 -> Ciphers: DEFAULT<br/>
 -> Retreiving complete cipher list<br/>
Found Client SSL profile: clientssl-insecure-compatible<br/>
 -> Ciphers: !SSLv2:ALL:!DH:!ADH:!EDH:@SPEED<br/>
 -> Retreiving complete cipher list<br/>
Found Client SSL profile: clientssl-secure<br/>
 -> Ciphers: ecdhe:rsa:!sslv3:!rc4:!exp:!des<br/>
 -> Retreiving complete cipher list<br/>
Found Client SSL profile: crypto-server-default-clientssl<br/>
 -> Ciphers: DHE-RSA-AES256-GCM-SHA384<br/>
 -> Retreiving complete cipher list<br/>
Found Client SSL profile: greg_example_1<br/>
 -> Ciphers: !TLSv1:ECDHE<br/>
 -> Retreiving complete cipher list<br/>
Found Client SSL profile: greg_example_2<br/>
 -> Ciphers: !EDH:RSA<br/>
 -> Retreiving complete cipher list<br/>
Found Client SSL profile: wom-default-clientssl<br/>
 -> Ciphers: DEFAULT<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: apm-default-serverssl<br/>
 -> Ciphers: DEFAULT<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: crypto-client-default-serverssl<br/>
 -> Ciphers: DHE-RSA-AES256-GCM-SHA384<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: greg_example_4<br/>
 -> Ciphers: ECDHE:!RSA<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: pcoip-default-serverssl<br/>
 -> Ciphers: DEFAULT<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: serverssl<br/>
 -> Ciphers: DEFAULT<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: serverssl-insecure-compatible<br/>
 -> Ciphers: !SSLv2:!EXPORT:!DH:RSA+RC4:RSA+AES:RSA+DES:RSA+3DES:ECDHE+AES:ECDHE+3DES:@SPEED<br/>
 -> Retreiving complete cipher list<br/>
Found Server SSL profile: wom-default-serverssl<br/>
 -> Ciphers: DEFAULT<br/>
 -> Retreiving complete cipher list<br/>
************************************************************************************************************************<br/>
Virtual server found: greg_example_1<br/>
************************************************************************************************************************<br/>
 -> Profile found: greg_example_1 (Context: clientside)<br/>
   -> Cipher string: !TLSv1:ECDHE<br/>
   -> Complete cipher list: <br/>
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX<br/>
 0: 49200  ECDHE-RSA-AES256-GCM-SHA384      256  TLS1.2  Native  AES-GCM   SHA384  ECDHE_RSA <br/>
 1: 49192  ECDHE-RSA-AES256-SHA384          256  TLS1.2  Native  AES       SHA384  ECDHE_RSA <br/>
 2: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.1  Native  AES       SHA     ECDHE_RSA <br/>
 3: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.2  Native  AES       SHA     ECDHE_RSA <br/>
 4: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.1  Native  DES       SHA     ECDHE_RSA <br/>
 5: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.2  Native  DES       SHA     ECDHE_RSA <br/>
 6: 49199  ECDHE-RSA-AES128-GCM-SHA256      128  TLS1.2  Native  AES-GCM   SHA256  ECDHE_RSA <br/>
 7: 49191  ECDHE-RSA-AES128-SHA256          128  TLS1.2  Native  AES       SHA256  ECDHE_RSA <br/>
 8: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.1  Native  AES       SHA     ECDHE_RSA <br/>
 9: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.2  Native  AES       SHA     ECDHE_RSA <br/>
<br/>
 -> Profile found: tcp (Context: all)<br/>
   -> Non-SSL Profile<br/>
*************************<br/>
* END OF VIRTUAL SERVER *<br/>
*************************<br/>
************************************************************************************************************************<br/>
Virtual server found: greg_example_2<br/>
************************************************************************************************************************<br/>
 -> Profile found: greg_example_2 (Context: clientside)<br/>
   -> Cipher string: !EDH:RSA<br/>
   -> Complete cipher list: <br/>
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX<br/>
 0:   157  AES256-GCM-SHA384                256  TLS1.2  Native  AES-GCM   SHA384  RSA       <br/>
 1:    61  AES256-SHA256                    256  TLS1.2  Native  AES       SHA256  RSA       <br/>
 2:    53  AES256-SHA                       256  SSL3    Native  AES       SHA     RSA       <br/>
 3:    53  AES256-SHA                       256  TLS1    Native  AES       SHA     RSA       <br/>
 4:    53  AES256-SHA                       256  TLS1.1  Native  AES       SHA     RSA       <br/>
 5:    53  AES256-SHA                       256  TLS1.2  Native  AES       SHA     RSA       <br/>
 6:    53  AES256-SHA                       256  DTLS1   Native  AES       SHA     RSA       <br/>
 7:    10  DES-CBC3-SHA                     168  SSL3    Native  DES       SHA     RSA       <br/>
 8:    10  DES-CBC3-SHA                     168  TLS1    Native  DES       SHA     RSA       <br/>
 9:    10  DES-CBC3-SHA                     168  TLS1.1  Native  DES       SHA     RSA       <br/>
10:    10  DES-CBC3-SHA                     168  TLS1.2  Native  DES       SHA     RSA       <br/>
11:    10  DES-CBC3-SHA                     168  DTLS1   Native  DES       SHA     RSA       <br/>
12:   156  AES128-GCM-SHA256                128  TLS1.2  Native  AES-GCM   SHA256  RSA       <br/>
13:    60  AES128-SHA256                    128  TLS1.2  Native  AES       SHA256  RSA       <br/>
14:    47  AES128-SHA                       128  SSL3    Native  AES       SHA     RSA       <br/>
15:    47  AES128-SHA                       128  TLS1    Native  AES       SHA     RSA       <br/>
16:    47  AES128-SHA                       128  TLS1.1  Native  AES       SHA     RSA       <br/>
17:    47  AES128-SHA                       128  TLS1.2  Native  AES       SHA     RSA       <br/>
18:    47  AES128-SHA                       128  DTLS1   Native  AES       SHA     RSA       <br/>
19:     5  RC4-SHA                          128  SSL3    Native  RC4       SHA     RSA       <br/>
20:     5  RC4-SHA                          128  TLS1    Native  RC4       SHA     RSA       <br/>
21:     5  RC4-SHA                          128  TLS1.1  Native  RC4       SHA     RSA       <br/>
22:     5  RC4-SHA                          128  TLS1.2  Native  RC4       SHA     RSA       <br/>
23:     4  RC4-MD5                          128  SSL3    Native  RC4       MD5     RSA       <br/>
24:     4  RC4-MD5                          128  TLS1    Native  RC4       MD5     RSA       <br/>
25:     4  RC4-MD5                          128  TLS1.1  Native  RC4       MD5     RSA       <br/>
26:     4  RC4-MD5                          128  TLS1.2  Native  RC4       MD5     RSA       <br/>
27:     9  DES-CBC-SHA                       64  SSL3    Native  DES       SHA     RSA       <br/>
28:     9  DES-CBC-SHA                       64  TLS1    Native  DES       SHA     RSA       <br/>
29:     9  DES-CBC-SHA                       64  TLS1.1  Native  DES       SHA     RSA       <br/>
30:     9  DES-CBC-SHA                       64  DTLS1   Native  DES       SHA     RSA       <br/>
31:    98  EXP1024-DES-CBC-SHA               56  SSL3    Native  DES       SHA     RSA       <br/>
32:    98  EXP1024-DES-CBC-SHA               56  TLS1    Native  DES       SHA     RSA       <br/>
33:    98  EXP1024-DES-CBC-SHA               56  DTLS1   Native  DES       SHA     RSA       <br/>
34:   100  EXP1024-RC4-SHA                   56  SSL3    Native  RC4       SHA     RSA       <br/>
35:   100  EXP1024-RC4-SHA                   56  TLS1    Native  RC4       SHA     RSA       <br/>
36:     8  EXP-DES-CBC-SHA                   40  SSL3    Native  DES       SHA     RSA       <br/>
37:     8  EXP-DES-CBC-SHA                   40  TLS1    Native  DES       SHA     RSA       <br/>
38:     8  EXP-DES-CBC-SHA                   40  DTLS1   Native  DES       SHA     RSA       <br/>
39:     3  EXP-RC4-MD5                       40  SSL3    Native  RC4       MD5     RSA       <br/>
40:     3  EXP-RC4-MD5                       40  TLS1    Native  RC4       MD5     RSA       <br/>
41:   132  CAMELLIA256-SHA                  256  TLS1    Native  CAMELLIA  SHA     RSA       <br/>
42:   132  CAMELLIA256-SHA                  256  TLS1.1  Native  CAMELLIA  SHA     RSA       <br/>
43:   132  CAMELLIA256-SHA                  256  TLS1.2  Native  CAMELLIA  SHA     RSA       <br/>
44:    65  CAMELLIA128-SHA                  128  TLS1    Native  CAMELLIA  SHA     RSA       <br/>
45:    65  CAMELLIA128-SHA                  128  TLS1.1  Native  CAMELLIA  SHA     RSA       <br/>
46:    65  CAMELLIA128-SHA                  128  TLS1.2  Native  CAMELLIA  SHA     RSA       <br/>
<br/>
 -> Profile found: http (Context: all)<br/>
   -> Non-SSL Profile<br/>
 -> Profile found: oneconnect (Context: all)<br/>
   -> Non-SSL Profile<br/>
 -> Profile found: tcp (Context: all)<br/>
   -> Non-SSL Profile<br/>
*************************<br/>
* END OF VIRTUAL SERVER *<br/>
*************************<br/>
************************************************************************************************************************<br/>
Virtual server found: greg_example_3<br/>
************************************************************************************************************************<br/>
 -> Profile found: clientssl-secure (Context: clientside)<br/>
   -> Cipher string: ecdhe:rsa:!sslv3:!rc4:!exp:!des<br/>
   -> Complete cipher list: <br/>
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX<br/>
 0: 49200  ECDHE-RSA-AES256-GCM-SHA384      256  TLS1.2  Native  AES-GCM   SHA384  ECDHE_RSA <br/>
 1: 49192  ECDHE-RSA-AES256-SHA384          256  TLS1.2  Native  AES       SHA384  ECDHE_RSA <br/>
 2: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1    Native  AES       SHA     ECDHE_RSA <br/>
 3: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.1  Native  AES       SHA     ECDHE_RSA <br/>
 4: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.2  Native  AES       SHA     ECDHE_RSA <br/>
 5: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1    Native  DES       SHA     ECDHE_RSA <br/>
 6: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.1  Native  DES       SHA     ECDHE_RSA <br/>
 7: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.2  Native  DES       SHA     ECDHE_RSA <br/>
 8: 49199  ECDHE-RSA-AES128-GCM-SHA256      128  TLS1.2  Native  AES-GCM   SHA256  ECDHE_RSA <br/>
 9: 49191  ECDHE-RSA-AES128-SHA256          128  TLS1.2  Native  AES       SHA256  ECDHE_RSA <br/>
10: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1    Native  AES       SHA     ECDHE_RSA <br/>
11: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.1  Native  AES       SHA     ECDHE_RSA <br/>
12: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.2  Native  AES       SHA     ECDHE_RSA <br/>
13:   157  AES256-GCM-SHA384                256  TLS1.2  Native  AES-GCM   SHA384  RSA       <br/>
14:    61  AES256-SHA256                    256  TLS1.2  Native  AES       SHA256  RSA       <br/>
15:    53  AES256-SHA                       256  TLS1    Native  AES       SHA     RSA       <br/>
16:    53  AES256-SHA                       256  TLS1.1  Native  AES       SHA     RSA       <br/>
17:    53  AES256-SHA                       256  TLS1.2  Native  AES       SHA     RSA       <br/>
18:    53  AES256-SHA                       256  DTLS1   Native  AES       SHA     RSA       <br/>
19:    10  DES-CBC3-SHA                     168  TLS1    Native  DES       SHA     RSA       <br/>
20:    10  DES-CBC3-SHA                     168  TLS1.1  Native  DES       SHA     RSA       <br/>
21:    10  DES-CBC3-SHA                     168  TLS1.2  Native  DES       SHA     RSA       <br/>
22:    10  DES-CBC3-SHA                     168  DTLS1   Native  DES       SHA     RSA       <br/>
23:   156  AES128-GCM-SHA256                128  TLS1.2  Native  AES-GCM   SHA256  RSA       <br/>
24:    60  AES128-SHA256                    128  TLS1.2  Native  AES       SHA256  RSA       <br/>
25:    47  AES128-SHA                       128  TLS1    Native  AES       SHA     RSA       <br/>
26:    47  AES128-SHA                       128  TLS1.1  Native  AES       SHA     RSA       <br/>
27:    47  AES128-SHA                       128  TLS1.2  Native  AES       SHA     RSA       <br/>
28:    47  AES128-SHA                       128  DTLS1   Native  AES       SHA     RSA       <br/>
29:   132  CAMELLIA256-SHA                  256  TLS1    Native  CAMELLIA  SHA     RSA       <br/>
30:   132  CAMELLIA256-SHA                  256  TLS1.1  Native  CAMELLIA  SHA     RSA       <br/>
31:   132  CAMELLIA256-SHA                  256  TLS1.2  Native  CAMELLIA  SHA     RSA       <br/>
32:    65  CAMELLIA128-SHA                  128  TLS1    Native  CAMELLIA  SHA     RSA       <br/>
33:    65  CAMELLIA128-SHA                  128  TLS1.1  Native  CAMELLIA  SHA     RSA       <br/>
34:    65  CAMELLIA128-SHA                  128  TLS1.2  Native  CAMELLIA  SHA     RSA       <br/>
<br/>
 -> Profile found: tcp (Context: all)<br/>
   -> Non-SSL Profile<br/>
*************************<br/>
* END OF VIRTUAL SERVER *<br/>
*************************<br/>
************************************************************************************************************************<br/>
Virtual server found: greg_example_4<br/>
************************************************************************************************************************<br/>
 -> Profile found: greg_example_4 (Context: serverside)<br/>
   -> Cipher string: ECDHE:!RSA<br/>
   -> Complete cipher list: <br/>
       ID  SUITE                            BITS PROT    METHOD  CIPHER    MAC     KEYX<br/>
 0: 49200  ECDHE-RSA-AES256-GCM-SHA384      256  TLS1.2  Native  AES-GCM   SHA384  ECDHE_RSA <br/>
 1: 49192  ECDHE-RSA-AES256-SHA384          256  TLS1.2  Native  AES       SHA384  ECDHE_RSA <br/>
 2: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1    Native  AES       SHA     ECDHE_RSA <br/>
 3: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.1  Native  AES       SHA     ECDHE_RSA <br/>
 4: 49172  ECDHE-RSA-AES256-CBC-SHA         256  TLS1.2  Native  AES       SHA     ECDHE_RSA <br/>
 5: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1    Native  DES       SHA     ECDHE_RSA <br/>
 6: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.1  Native  DES       SHA     ECDHE_RSA <br/>
 7: 49170  ECDHE-RSA-DES-CBC3-SHA           168  TLS1.2  Native  DES       SHA     ECDHE_RSA <br/>
 8: 49199  ECDHE-RSA-AES128-GCM-SHA256      128  TLS1.2  Native  AES-GCM   SHA256  ECDHE_RSA <br/>
 9: 49191  ECDHE-RSA-AES128-SHA256          128  TLS1.2  Native  AES       SHA256  ECDHE_RSA <br/>
10: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1    Native  AES       SHA     ECDHE_RSA <br/>
11: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.1  Native  AES       SHA     ECDHE_RSA <br/>
12: 49171  ECDHE-RSA-AES128-CBC-SHA         128  TLS1.2  Native  AES       SHA     ECDHE_RSA <br/>
<br/>
 -> Profile found: tcp (Context: all)<br/>
   -> Non-SSL Profile<br/>
*************************<br/>
* END OF VIRTUAL SERVER *<br/>
*************************<br/>
