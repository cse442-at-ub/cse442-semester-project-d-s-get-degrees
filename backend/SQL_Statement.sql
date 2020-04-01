CREATE TABLE Users (
    ID INTEGER PRIMARY KEY,
    Username varchar(255),
    Password varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Email varchar(255) NOT NULL,
    ProfilePic BLOB
);

CREATE TABLE Events (
    ID INTEGER PRIMARY KEY,
    EventImage VARCHAR(255),
    Title VARCHAR(255) NOT NULL,
    Description VARCHAR(255)
);

CREATE TABLE Persons_Events (
    ID INTEGER PRIMARY KEY,
    UserID INTEGER NOT NULL,
    EventID INTEGER NOT NULL
);