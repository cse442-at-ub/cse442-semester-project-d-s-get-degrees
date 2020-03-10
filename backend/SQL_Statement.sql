CREATE TABLE Persons (
    Username varchar(255) NOT NULL PRIMARY KEY,
    Password varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Email varchar(255) NOT NULL,
    Profile_Pic varchar(255),
    PreferGame varchar(255),
    EventList varchar(255)
);