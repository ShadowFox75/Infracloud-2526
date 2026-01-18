# test script for flask_app_login.py -- use in Virtualbox VM, not in Docker
# programm flask_app_login needs to be running
echo "Deleting all test records"
curl -k -X DELETE "http://127.0.0.1:5500/delete/all"
INSECURE_USER="ICHIGO"
INSECURE_PW="Kurosaki123"
SECURE_USER="Luffy"
SECURE_PW="Monkey123"
echo "Creating new user v1 insecure"
curl -k -X POST -F "username="$INSECURE_USER -F "password="$INSECURE_PW "http://127.0.0.1:5500/signup/v1"
echo "Testing login v1"
curl -k -X POST -F "username="$INSECURE_USER -F "password="$INSECURE_PW "http://127.0.0.1:5500/login/v1"
#### Replace fixed username with a variable SECURE_USER and a variable passord SECURE_PW
echo "Creating new user v2 secure"
curl -k -X POST -F "username="$SECURE_USER -F "password="$SECURE_PW "http://127.0.0.1:5500/signup/v2"
echo "Testing login v2"
curl -k -X POST -F "username="$SECURE_USER -F "password="$SECURE_PW "http://127.0.0.1:5500/login/v2"