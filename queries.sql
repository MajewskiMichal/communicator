CREATE TABLE User (
	  id int AUTO_INCREMENT,
    email varchar(255) UNIQUE,
    username varchar(255),
    hashed_password varchar(60),
    PRIMARY KEY(id)
);

CREATE TABLE Message (
	  id int AUTO_INCREMENT,
    sender_id int NOT NULL,
    receiver_id int NOT NULL,
    content text,
    PRIMARY KEY(id),
    FOREIGN KEY(sender_id) REFERENCES User(id),
    FOREIGN KEY(receiver_id) REFERENCES User(id)
);