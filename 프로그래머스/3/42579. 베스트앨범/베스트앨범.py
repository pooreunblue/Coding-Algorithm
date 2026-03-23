def solution(genres, plays):
    answer = []
    genre_play = {}
    play_sum = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_play:
            genre_play[genre] = []
            play_sum[genre] = 0
        genre_play[genre].append((i, play))
        play_sum[genre] += play
    
    sorted_genres = sorted(play_sum.items(), key=lambda x:-x[1])

    for genre, play in sorted_genres:
        sorted_songs = sorted(genre_play[genre], key=lambda x:(-x[1], x[0]))
        answer.append(sorted_songs[0][0])
        if len(sorted_songs) > 1:
            answer.append(sorted_songs[1][0])
    return answer