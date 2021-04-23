import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://spookytanuki:admin@localhost:5432/wannabe_spotify')
connection = engine.connect()
# print(engine.table_names())

# check = connection.execute("""SELECT * FROM genre;
# """).fetchone()
# print(check)

# connection.execute("""INSERT INTO genre(id, name)
#            VALUES(1, 'Minimal Dub');
# """)

# connection.execute("""INSERT INTO genre(id, name)
#            VALUES(2, 'Hard Techno');
# """)
#
# connection.execute("""INSERT INTO genre(id, name)
#            VALUES(3, 'Minimal Techno');
# """)
#
# connection.execute("""INSERT INTO genre(id, name)
#            VALUES(4, 'Dark Psytrance');
# """)
#
# connection.execute("""INSERT INTO genre(id, name)
#            VALUES(5, 'Psychedelic Trance');
# """)

# connection.execute("""INSERT INTO artist(id, name, genre_id)
#            VALUES
#            (1, 'Kontain', 1),
#            (2, 'Kozlov', 1),
#            (3, 'TWAN', 1),
#            (4, 'Absntmnded', 2),
#            (5, 'KLAMER', 3),
#            (6, 'Nico Moreno', 3),
#            (7, 'Estella Boersma', 4),
#            (8, 'Jacidorex', 5);
# """)

# connection.execute("""INSERT INTO album(id, name, year, artist_id)
#            VALUES
#            (1, 'Your Job is to Make Art', '20200101', 1),
#            (2, 'Fear Is The Only Darkness', '19990101', 3),
#            (3, 'Byronic Hero', '20180101', 4),
#            (4, 'Patient Zero', '20210101', 2),
#            (5, 'Pinnacle Of Us', '20130101', 5),
#            (6, 'Hope To Live', '20180101', 6),
#            (7, 'Subdued Nation', '20200101', 8),
#            (8, 'Revival', '20180101', 7);
# """)



# connection.execute("""INSERT INTO track(id, name, duration, album_id)
#            VALUES
#            (1, 'Fear Is The Only Darkness', '031500', 1),
#            (2, 'Trance Sorcery', '031500', 1),
#            (3, 'I Am The Dominate', '041800', 2),
#            (4, 'The Future Is Female', '021600', 3),
#            (5, 'Dont Talk Too Much', '075500', 3),
#            (6, 'Typhoid Mary', '030500', 4),
#            (7, 'From The Fire', '121500', 5),
#            (8, 'Wenn Swen Nein Sagt', '131900', 6),
#            (9, 'Purple Widow', '031600', 6),
#            (10, 'Multipass', '035500', 7),
#            (11, 'Extinctor', '035900', 7),
#            (12, 'Vertigo', '033100', 7),
#            (13, 'Dont be fooled by their agenda', '090900', 7),
#            (14, 'Byronic Hero', '031500', 8),
#            (15, 'Patient Zero Original Mix', '081500', 8);
# """)


# connection.execute("""INSERT INTO collection(id, name, year)
#            VALUES
#            (1, 'Diavoli', '20200101'),
#            (2, 'Purple Widow', '20180101'),
#            (3, 'Molekul 11', '20130101'),
#            (4, 'Everyone On Acid', '19890101'),
#            (5, 'War Anthems', '20070101'),
#            (6, 'Afterschool Activity', '20140101'),
#            (7, 'Agathism Records', '20190101'),
#            (8, 'FAHVA002', '20010101');
# """)

connection.execute("""INSERT INTO trackcollection(id, track_id, collection_id)
           VALUES
           (1, 8, 2),
           (2, 9, 4);
""")

connection.execute("""INSERT INTO genreartist(id, genre_id, artist_id)
           VALUES
           (1, 1, 2),
           (2, 3, 2),
           (3, 5, 8),
           (4, 4, 8),
           (5, 1, 1),
           (6, 1, 3),
           (7, 3, 5),
           (8, 3, 6),
           (9, 4, 7);
""")


