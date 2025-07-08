CREATE TABLE Polling_place (
    polling_place_id INT PRIMARY KEY, -- Unique identifier for each polling place
    polling_place_name VARCHAR(100),
    address VARCHAR(100),         
    city VARCHAR(50),              
    state CHAR(2),              
    zip_code CHAR(5)
);


INSERT INTO Polling_place(
    polling_place_id, polling_place_name, address, city, state, zip_code
) VALUES
(101, 'Central Community Center', '100 Main St', 'Chicago', 'IL', '60601'),
(102, 'Northside Library', '200 North Ave', 'Chicago', 'IL', '60602'),
(103, 'Westside School Gym', '300 West St', 'Naperville', 'IL', '60540'),
(104, 'Eastside Fire Station', '400 East Blvd', 'Aurora', 'IL', '60504'),
(105, 'Downtown Hall', '500 Center Rd', 'Springfield', 'IL', '62704'),
(106, 'Lakeside Recreation Center', '600 Lake Dr', 'Waukegan', 'IL', '60085');





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


INSERT INTO Voters (
    voter_id, first_name, last_name, address, city, state, zip_code, precinct_number, polling_place_id
) VALUES
(1, 'Alice', 'Johnson', '123 Maple St', 'Chicago', 'IL', '60601', 567, 101),
(2, 'Brian', 'Smith', '456 Oak Ave', 'Chicago', 'IL', '60602', 570, 102),
(3, 'Catherine', 'Lee', '789 Pine Dr', 'Evanston', 'IL', '60201', 490, 101),
(4, 'David', 'Garcia', '321 Birch Rd', 'Naperville', 'IL', '60540', 229, 103),
(5, 'Emily', 'Davis', '654 Cedar Ln', 'Aurora', 'IL', '60504', 529, 104),
(6, 'Frank', 'Martinez', '987 Walnut Way', 'Springfield', 'IL', '62704', 877, 105),  
(7, 'Grace', 'Nguyen', '135 Elm St', 'Peoria', 'IL', '61602', 443, 106),
(8, 'Henry', 'Brown', '246 Chestnut Blvd', 'Rockford', 'IL', '61101', 704, 104),
(9, 'Isabella', 'Wilson', '357 Spruce Ct', 'Joliet', 'IL', '60431', 882, 103),
(10, 'Jack', 'Taylor', '468 Poplar Pl', 'Waukegan', 'IL', '60085', 630, 106);
