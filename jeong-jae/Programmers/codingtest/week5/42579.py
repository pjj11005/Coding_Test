def solution(genres, plays):
    answer = []
    genre = {}  # 장르별 총 재생 수
    song = {}  # 장르별 노래들
    n = len(genres)
    for i in range(n):
        genre[genres[i]] = genre.get(genres[i], 0) + plays[i]
        song[genres[i]] = song.get(genres[i], [])
        song[genres[i]].append([plays[i], i])

    sorted_genre = []
    for key, value in genre.items():
        sorted_genre.append((-value, key))

    sorted_genre.sort()
    for _, key in sorted_genre:
        sorted_song = sorted(song[key], key=lambda x: (-x[0], x[1]))
        if len(sorted_song) >= 2:  # 2개 이상
            answer.append(sorted_song[0][1])
            answer.append(sorted_song[1][1])
        else:  # 1개
            answer.append(sorted_song[0][1])

    return answer