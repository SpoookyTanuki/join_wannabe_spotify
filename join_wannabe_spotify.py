import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://spookytanuki:admin@localhost:5432/wannabe_spotify')
con = engine.connect()
# print(engine.table_names())
# ['genre', 'artist', 'album', 'track', 'genreartist', 'artistalbum', 'trackcollection', 'collection']

# количество исполнителей в каждом жанре
artist_genre = con.execute("""
SELECT g.name, COUNT(a.name) FROM artist a
LEFT JOIN genre g ON a.genre_id = g.id
GROUP BY g.name;
""").fetchall()
# print(artist_genre)

# количество треков, вошедших в альбомы 2019-2020 годов
last_albums = con.execute("""
SELECT a.name, COUNT(t.name) FROM track t
LEFT JOIN album a ON t.album_id = a.id
WHERE a.year BETWEEN '20190101' AND '20200101'
GROUP BY a.name;
""").fetchall()
# print(last_albums)

# средняя продолжительность треков по каждому альбому
avg_timing = con.execute("""
SELECT a.name, AVG(t.duration) FROM track t
LEFT JOIN album a ON t.album_id = a.id
GROUP BY a.name;
""").fetchall()
# for i in avg_timing:
#     print('For album', i[0], 'average track length is', i[1])

# все исполнители, которые не выпустили альбомы в 2020 году;
not_in_2020 = con.execute("""
SELECT al.name, ar.name FROM artist ar
LEFT JOIN album al ON ar.id = al.artist_id
WHERE al.year <> '20200101';
""").fetchall()
# print(not_in_2020)


# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
specific_artist = con.execute("""
SELECT a.name, c.name FROM collection c
JOIN trackcollection tc ON c.id = tc.collection_id
JOIN track ON tc.track_id = track.id
JOIN album ON track.album_id = album.artist_id 
JOIN artist a ON album.artist_id = a.id
WHERE a.name = 'Nico Moreno';
""").fetchall()
# print(specific_artist)


# название альбомов, в которых присутствуют исполнители более 1 жанра
multi_genres = con.execute("""
SELECT album.name, artist.name FROM album
JOIN artist ON album.id = artist.id
JOIN genreartist ga ON artist.id = ga.artist_id
JOIN genre ON ga.genre_id = genre.id
GROUP BY album.name, artist.name
HAVING COUNT(ga.genre_id) > 1;
""").fetchall()
# print(multi_genres)


# наименование треков, которые не входят в сборники
without_collection = con.execute("""
SELECT t.name FROM track t
LEFT JOIN trackcollection tc ON t.id = tc.track_id
WHERE tc.collection_id IS NULL;
""").fetchall()
# print(without_collection)


# исполнителя(-ей), написавшего самый короткий трек (теоретически таких треков может быть несколько)
short_track = con.execute("""
SELECT a.name FROM artist a
JOIN album ON a.id = album.artist_id
JOIN track ON album.id = track.album_id
    WHERE track.duration = (
        SELECT MIN(track.duration) from track)
""").fetchall()
# print(short_track)


# название альбомов, содержащих наименьшее количество треков
min_tracks = con.execute("""
SELECT album.name FROM album
JOIN track ON album.id = track.album_id
GROUP BY album.name
HAVING COUNT(track.album_id) = (
SELECT track.album_id from track
ORDER BY album_id ASC
LIMIT 1);
""").fetchall()
print(min_tracks)