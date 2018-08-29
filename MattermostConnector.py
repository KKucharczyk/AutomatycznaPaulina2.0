import json
import requests


def send_mattermost_notification(hook, username, message):
    data = {}
    data['username'] = username
    data['text'] = message
    json_data = json.dumps(data)
    response = requests.post(hook, json_data);
    if response.status_code != 200:
            try:
                response = json.loads(response.text)
            except ValueError:
                response = {'message': response.text, 'status_code': response.status_code}
            raise RuntimeError("{} ({})".format(response['message'], response['status_code']))