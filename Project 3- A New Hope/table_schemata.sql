--Use any of the following lines to create tables as needed

-- artist_name VARCHAR(150)  NOT NULL,
-- track_name VARCHAR(150) NOT NULL,
-- track_id VARCHAR(75) NOT NULL,
-- popularity decimal NOT NULL,
-- year VARCHAR(75) NOT NULL,
-- genre VARCHAR(75) NOT NULL,
-- danceability decimal(3,1) NOT NULL,	
-- energy decimal(3,1) NOT NULL,	
-- key	FLOAT NOT NULL,
-- loudness FLOAT NOT NULL,	
-- mode FLOAT NOT NULL,
-- speechiness	decimal(3,1) NOT NULL,	
-- acousticness decimal(3,1) NOT NULL,	
-- instrumentalness decimal(3,1) NOT NULL,		
-- liveness decimal(3,1) NOT NULL,			
-- valence decimal(3,1) NOT NULL,		
-- tempo decimal(3,1) NOT NULL,		


create table top20(
	genre VARCHAR(75) NOT NULL,
	artist_name VARCHAR(150)  NOT NULL,
	popularity decimal NOT NULL
);


create table major_minor(
	genre VARCHAR(75) NOT NULL,
	mode FLOAT NOT NULL
);

	
create table tempo_popularity(
	genre VARCHAR(75) NOT NULL,
	popularity decimal NOT NULL,
	tempo decimal(3,1) NOT NULL
);	

	
create table happy_sad(
	genre VARCHAR(75) NOT NULL,
	valence decimal(3,1) NOT NULL
);	