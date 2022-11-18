import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME= 98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hzc09704;PWD=VStPUfStPi3tvFAF",'','')
print(conn)
print("connection successful...")