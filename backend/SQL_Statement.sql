CREATE TABLE User (
    ID INTEGER PRIMARY KEY,
    Username varchar(255),
    Password varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Email varchar(255) NOT NULL,
    ProfilePic BLOB
)

CREATE TABLE Event (
    ID INTEGER PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description VARCHAR(255),
    EventImage BLOB
)

CREATE TABLE User_Event (
    ID INTEGER PRIMARY KEY,
    UserID INTEGER NOT NULL,
    EventID INTEGER NOT NULL
);