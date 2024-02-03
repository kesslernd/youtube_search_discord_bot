import requests
import json

class YoutubeSearchClient():
    api_key = ''

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, input):
        url = 'https://youtube.googleapis.com/youtube/v3/search'
        headers = {
            'Accept': 'application/json'
        }
        data = {
            'q': input,
            'part': 'snippet',
            'key': self.api_key,
            'type': 'video'
        }
        response = requests.get(url, params=data, headers=headers)
        data = json.loads(response.content)
        return [
            {
                'id': item['id']['videoId'],
                'title': item['snippet']['title']
            } for item in data['items']
        ]