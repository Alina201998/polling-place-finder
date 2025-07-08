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


