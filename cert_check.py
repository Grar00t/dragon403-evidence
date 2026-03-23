import ssl
import OpenSSL

cert = ssl.get_server_certificate(('hiloconn.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
print("الجهة المصدرة للشهادة:", x509.get_issuer().commonName)
print("الاسم المسجل في الشهادة:", x509.get_subject().commonName)
