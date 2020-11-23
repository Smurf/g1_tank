#/etc/letsencrypt/live/ddns.smurf.codes/fullchain.pem
#/etc/letsencrypt/live/ddns.smurf.codes/privkey.pem
docker run -d --network host --name g1tank_nginx -d g1tank_nginx
