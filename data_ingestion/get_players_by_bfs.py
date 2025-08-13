import requests

username = "magnuscarlsen"
url = f"https://api.chess.com/pub/player/{username}"

headers = {"User-Agent": "chess-insights-bot"}
response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)

'''

ACCESSING: https://api.chess.com/pub/player/magnuscarlsen

GIVES US:

{
  "avatar": "...",
  "player_id": 3889224,
  "@id": "https://api.chess.com/pub/player/magnuscarlsen",
  "url": "https://www.chess.com/member/MagnusCarlsen",
  "name": "Magnus Carlsen",
  "username": "magnuscarlsen",
  "title": "GM",
  "followers": 268967,
  "country": "https://api.chess.com/pub/country/NO",
  "location": "Norway",
  "last_online": 1754949587,
  "joined": 1282856720,
  "status": "premium",
  "is_streamer": false,
  "verified": false,
  "league": "Champion",
  "streaming_platforms": []
}

'''