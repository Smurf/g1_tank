./nginx/kill_container.sh
./nginx/start_container.sh
python3 web_tank.py --cert-file nginx/certs/fullchain.pem --key-file nginx/certs/privkey.pem 
