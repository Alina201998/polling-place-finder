CREATE TABLE Polling_place (
    polling_place_id INT PRIMARY KEY, -- Unique identifier for each polling place
    polling_place_name VARCHAR(100),
    address VARCHAR(100),         
    city VARCHAR(50),              
    state CHAR(2),              
    zip_code CHAR(5)
);


CREATE TABLE Voters (

    voter_id INT PRIMARY KEY,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    address VARCHAR(100),

    city VARCHAR(50),

    state CHAR(2),

    zip_code CHAR(5),

    precinct_number INT,

    polling_place_id INT,

    FOREIGN KEY (polling_place_id) REFERENCES Polling_place(polling_place_id)

);

