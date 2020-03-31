CREATE TABLE Persons (
    Username varchar(255) NOT NULL PRIMARY KEY,
    Password varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Email varchar(255) NOT NULL,
    Profile_Pic varchar(255),
    PreferGame varchar(255),
);

CREATE TABLE Events (
    ID INTEGER NOT NULL PRIMARY KEY,
    EventImage VARCHAR(255),
    Title VARCHAR(255) NOT NULL,
    Description VARCHAR(255)
);

CREATE TABLE Persons_Events (
    ID INTEGER NOT NULL PRIMARY KEY,
    UserID INTEGER NOT NULL,
    EventID INTEGER NOT NULL
);