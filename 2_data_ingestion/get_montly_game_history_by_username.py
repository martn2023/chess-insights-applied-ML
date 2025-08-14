import requests

def fetch_games_for_month(username, year, month):
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month:02d}"
    headers = {"User-Agent": "chess-insights-dev"}

    chess_api_response = requests.get(url, headers=headers)

    if chess_api_response.status_code == 200:
        data = chess_api_response.json()
        games_archive = data.get("games", [])
        print(f"✅ Pulled {len(games_archive)} games for {username} ({year}-{month:02d})")
        return games_archive
    else:
        print(f"❌ Error fetching games for {username}: {chess_api_response.status_code}")
        return None




''' SAMPLE API REQUEST
https://api.chess.com/pub/player/magnuscarlsen/games/2025/07"


SAMPLE SUBSET OF THE JSON RESPONSE, REPRESENTING 1 OF MANY GAMES ####

{
    "url": "https://www.chess.com/game/live/145713572945",
    "pgn": "[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2025.07.01\"]\n[Round \"-\"]\n[White \"MagnusCarlsen\"]\n[Black \"KnightOclock\"]\n[Result \"1-0\"]\n[Tournament \"https://www.chess.com/tournament/live/late-titled-tuesday-blitz-july-01-2025-5764807\"]\n[CurrentPosition \"8/p2n4/1p3k2/8/2KP1BR1/2P5/PP6/8 b - - 0 45\"]\n[Timezone \"UTC\"]\n[ECO \"A45\"]\n[ECOUrl \"https://www.chess.com/openings/Indian-Game...4.Nd2-d5-5.e3-O-O-6.Bd3\"]\n[UTCDate \"2025.07.01\"]\n[UTCTime \"20:00:00\"]\n[WhiteElo \"3308\"]\n[BlackElo \"2575\"]\n[TimeControl \"180+1\"]\n[Termination \"MagnusCarlsen won by resignation\"]\n[StartTime \"20:00:00\"]\n[EndDate \"2025.07.01\"]\n[EndTime \"20:07:14\"]\n[Link \"https://www.chess.com/game/live/145713572945\"]\n\n1. d4 {[%clk 0:02:55.4]} 1... Nf6 {[%clk 0:02:58.5]} 2. c3 {[%clk 0:02:56.2]} 2... g6 {[%clk 0:02:56.2]} 3. Bg5 {[%clk 0:02:55.3]} 3... Bg7 {[%clk 0:02:55]} 4. Nd2 {[%clk 0:02:56]} 4... d5 {[%clk 0:02:54.6]} 5. e3 {[%clk 0:02:56]} 5... O-O {[%clk 0:02:54.3]} 6. Bd3 {[%clk 0:02:56.5]} 6... b6 {[%clk 0:02:46.3]} 7. f4 {[%clk 0:02:54.9]} 7... c5 {[%clk 0:02:41.5]} 8. Ngf3 {[%clk 0:02:51.8]} 8... Ba6 {[%clk 0:02:36.8]} 9. Bxa6 {[%clk 0:02:50.9]} 9... Nxa6 {[%clk 0:02:37.3]} 10. Ne5 {[%clk 0:02:50.5]} 10... Qd6 {[%clk 0:02:16.8]} 11. Qf3 {[%clk 0:02:48.4]} 11... Nd7 {[%clk 0:02:04.1]} 12. Qh3 {[%clk 0:02:27.9]} 12... Rad8 {[%clk 0:01:57.7]} 13. Bh4 {[%clk 0:02:27.7]} 13... f6 {[%clk 0:01:54.3]} 14. Nd3 {[%clk 0:02:27.8]} 14... Rde8 {[%clk 0:01:43.3]} 15. f5 {[%clk 0:02:21.4]} 15... e5 {[%clk 0:01:34.7]} 16. fxe6 {[%clk 0:02:15.1]} 16... Qxe6 {[%clk 0:01:33.2]} 17. Qxe6+ {[%clk 0:02:14.8]} 17... Rxe6 {[%clk 0:01:33.8]} 18. Bf2 {[%clk 0:02:01.2]} 18... g5 {[%clk 0:01:29.6]} 19. O-O-O {[%clk 0:01:57.5]} 19... c4 {[%clk 0:01:14.9]} 20. Ne1 {[%clk 0:01:57]} 20... g4 {[%clk 0:01:07.6]} 21. Nc2 {[%clk 0:01:55.4]} 21... Nc7 {[%clk 0:01:02]} 22. Bg3 {[%clk 0:01:52.2]} 22... Ne8 {[%clk 0:00:56.6]} 23. h3 {[%clk 0:01:50.4]} 23... h5 {[%clk 0:00:52.2]} 24. hxg4 {[%clk 0:01:50.2]} 24... hxg4 {[%clk 0:00:52.9]} 25. Rdf1 {[%clk 0:01:44.1]} 25... f5 {[%clk 0:00:46.5]} 26. Rh5 {[%clk 0:01:43.7]} 26... Bh6 {[%clk 0:00:35]} 27. Rfxf5 {[%clk 0:01:34.3]} 27... Rxf5 {[%clk 0:00:35.9]} 28. Rxf5 {[%clk 0:01:34.1]} 28... Bxe3 {[%clk 0:00:27.7]} 29. Rxd5 {[%clk 0:01:30.2]} 29... Nef6 {[%clk 0:00:25.4]} 30. Nxe3 {[%clk 0:01:25.8]} 30... Rxe3 {[%clk 0:00:24.9]} 31. Rg5+ {[%clk 0:01:26.1]} 31... Kf7 {[%clk 0:00:22.1]} 32. Bh4 {[%clk 0:01:26.1]} 32... Re2 {[%clk 0:00:19.1]} 33. Nxc4 {[%clk 0:01:24.6]} 33... Rxg2 {[%clk 0:00:18.1]} 34. Ne3 {[%clk 0:01:21.8]} 34... Rg1+ {[%clk 0:00:17.5]} 35. Kc2 {[%clk 0:01:21.9]} 35... Rh1 {[%clk 0:00:17.1]} 36. Bg3 {[%clk 0:01:13.8]} 36... Rg1 {[%clk 0:00:10.8]} 37. Nxg4 {[%clk 0:01:13]} 37... Ne4 {[%clk 0:00:11]} 38. Nh6+ {[%clk 0:00:40.2]} 38... Kf6 {[%clk 0:00:10.6]} 39. Rf5+ {[%clk 0:00:40.6]} 39... Kg6 {[%clk 0:00:06.7]} 40. Bf4 {[%clk 0:00:40.9]} 40... Rg2+ {[%clk 0:00:05.8]} 41. Kd3 {[%clk 0:00:35]} 41... Nf2+ {[%clk 0:00:05.9]} 42. Kc4 {[%clk 0:00:35]} 42... Ng4 {[%clk 0:00:06]} 43. Rg5+ {[%clk 0:00:34.1]} 43... Kf6 {[%clk 0:00:05.1]} 44. Nxg4+ {[%clk 0:00:33.4]} 44... Rxg4 {[%clk 0:00:05.7]} 45. Rxg4 {[%clk 0:00:33.7]} 1-0\n",
    "time_control": "180+1",
    "end_time": 1751400434,
    "rated": true,
    "accuracies": {
      "white": 80.79,
      "black": 75.32
    },
    "tcn": "lB!Tks2UcM92blZJmu8!ftXPnDYIgv6OtO5OvK7RdvTZvx47MF1TKt78DL0KLSRSxS8SFnUMecIAteMEekOYnwY8px3NxENEdfTLhN2VfL9LNLVuLJ8TkuSuJM!1wFumlAmoAuogckghFwhguETCEV1TMLTUwDgoktCntAnELMUTVEoEME",
    "uuid": "f82f166a-56b5-11f0-a413-6cfe544c0428",
    "initial_setup": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "fen": "8/p2n4/1p3k2/8/2KP1BR1/2P5/PP6/8 b - - 0 45",
    "time_class": "blitz",
    "rules": "chess",
    "white": {
      "rating": 3308,
      "result": "win",
      "@id": "https://api.chess.com/pub/player/magnuscarlsen",
      "username": "MagnusCarlsen",
      "uuid": "a2761738-b155-11df-8018-000000000000"
    },
    "black": {
      "rating": 2575,
      "result": "resigned",
      "@id": "https://api.chess.com/pub/player/knightoclock",
      "username": "KnightOclock",
      "uuid": "d4bac70e-dc3b-11ef-84e2-e5d82c731f5e"
    },
    "eco": "https://www.chess.com/openings/Indian-Game...4.Nd2-d5-5.e3-O-O-6.Bd3",
    "tournament": "https://api.chess.com/pub/tournament/late-titled-tuesday-blitz-july-01-2025-5764807"
  }

'''