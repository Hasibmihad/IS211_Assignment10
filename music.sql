CREATE TABLE artists (
    artist_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    album_id INT PRIMARY KEY,
    name VARCHAR(255),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE songs (
    song_id INT PRIMARY KEY,
    name VARCHAR(255),
    album_id INT,
    track_number INT NOT NULL UNIQUE,
    duration_seconds INT,
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

-- Insert data
INSERT INTO artists (artist_id, name)
VALUES 
    (1, 'Madonna'),
     (2, 'Eminem');

INSERT INTO albums (album_id, name, artist_id)
VALUES
    (101, 'Like a Virgin', 1),
    (102, 'Ray of Light', 1),
    (201, 'The Marshall Mathers LP', 2),
    (202, 'Recovery', 2);

INSERT INTO songs (song_id, name, album_id, track_number, duration_seconds)
VALUES
    (1001, 'Like a Virgin', 101, 1, 270),
    (1002, 'Material Girl', 101, 2, 240),
    (1003, 'Frozen', 102, 1, 330),
    (1004, 'Ray of Light', 102, 2, 270),
    (2001, 'Stan', 201, 1, 360),
    (2002, 'Lose Yourself', 201, 2, 312),
    (2003, 'Not Afraid', 202, 1, 263),
    (2004, 'Love the Way You Lie', 202, 2, 263);


