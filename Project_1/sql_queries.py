# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fact_song_play"
user_table_drop = "DROP TABLE IF EXISTS dim_user"
song_table_drop = "DROP TABLE IF EXISTS dim_song"
artist_table_drop = "DROP TABLE IF EXISTS dim_artist"
time_table_drop = "DROP TABLE IF EXISTS dim_time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE fact_song_play (songplay_id SERIAL,
                                                        start_time bigint,
                                                        user_id varchar,
                                                        level varchar,
                                                        song_id varchar,
                                                        artist_id varchar,
                                                        session_id int,
                                                        location varchar,
                                                        user_agent varchar)
""")

user_table_create = ("""CREATE TABLE dim_user (user_id int,
                                                first_name varchar,
                                                last_name varchar,
                                                gender char,
                                                level varchar)
""")

song_table_create = ("""CREATE TABLE dim_song (song_id varchar,
                                                title varchar,
                                                artist_id varchar,
                                                year int,
                                                duration numeric)
""")

artist_table_create = ("""CREATE TABLE dim_artist (artist_id varchar,
                                                    name varchar,
                                                    location varchar,
                                                    lattitude float,
                                                    longitude float)
""")

time_table_create = ("""CREATE TABLE dim_time (start_time bigint,
                                                hour int,
                                                day int,
                                                week int,
                                                month int,
                                                year int,
                                                weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO fact_song_play (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO dim_user (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO dim_song (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO dim_artist (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO dim_time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""Select song_id,
                        s.artist_id 
                FROM dim_song s
                LEFT JOIN dim_artist a ON s.artist_id = a.artist_id
                WHERE s.title = %s
                AND name = %s
                AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]