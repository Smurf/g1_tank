import requests

payload = { 'client_id': 'YOURCLIENTID',
                'redirect_uri': 'http://localhost',
                'response_type': 'token',
                'scope': 'chat:read chat:edit',
                'force_verify': 'true'}
r = requests.get('https://id.twitch.tv/oauth2/authorize', params=payload)
print(r.url)
