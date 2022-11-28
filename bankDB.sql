DROP DATABASE IF EXISTS bankDB;
CREATE DATABASE IF NOT EXISTS bankDB;
USE bankDB;

DROP TABLE if EXISTS user;
CREATE TABLE IF NOT EXISTS user(
    name varchar(9) NOT NULL,
    sex varchar(6) NOT NULL,
    ssn varchar(13) NOT NULL,
    phone varchar(11) NOT NULL,
    address varchar(64) NOT NULL,
    ID varchar(11) NOT NULL,
    answer CHAR(13),
    PRIMARY KEY(ID),
    UNIQUE(ssn)); 
    
 DELETE FROM user;
 INSERT INTO user 
 VALUES ('john', 'm', '9709111053734', '01087566734', 'seoul,songpa', 'johnnywhat','jamsil'),
 ('elice', 'f', '8621251394923', '01032514632','texas, dellas', 'elicerabbit', 'texas'),
 ('travis', 'm', '2385193421395', '01035234628','tokyo, japan', 'travisscott', 'tokyo');
    
DROP TABLE if EXISTS account;
CREATE TABLE IF NOT EXISTS account(
    ac_name varchar(15),
    ac_number varchar(15) NOT NULL,
    password int(4) NOT NULL,
    interest decimal(4,2) DEFAULT 00.00,
    userID VARCHAR(11) NOT NULL,
    money int DEFAULT 0,
    PRIMARY KEY(ac_number),
    FOREIGN KEY(userID) REFERENCES user(ID));

DELETE FROM account;
INSERT INTO account VALUES
('account1','12345678910account11',1234, 03.40, 'johnnywhat', 1000000),
('account2','1110987654321',4321, 02.40, 'elicerabbit', 0),
('account3','1111111111111',1111, 03.10, 'travisscott', 0);

DROP TABLE if EXISTS history;
CREATE TABLE IF NOT EXISTS history(
    transNum int(4) primary key auto_increment,
    userID VARCHAR(11) NOT NULL,
    accountID VARCHAR(15) NOT NULL,
    deporwith varchar(5) NOT NULL,
    amount INT(20) NOT NULL,
    
    FOREIGN KEY(userID) REFERENCES user(ID),
    FOREIGN KEY(accountID) REFERENCES account(ac_number));

DELETE FROM history;
INSERT INTO history(userID, accountID, deporwith, amount) VALUES
('johnnywhat','1234567891011', 'dep', 100000),
('elicerabbit', '1110987654321', 'dep', 90000000),
('travisscott', '1111111111111', 'dep', 1111111111);

DROP TABLE if EXISTS admin;
CREATE TABLE IF NOT EXISTS admin(
    name varchar(9) NOT NULL,
    essn char(9) NOT NULL,
    depart varchar(15),
    PRIMARY KEY(essn));

DELETE FROM admin;
INSERT INTO admin VALUES
('jack', '123456789', 'customerservice'),
('mary', '987654321', 'insurance');


CREATE VIEW user_account
AS SELECT name, ssn, phone, address, ac_number, interest, userID
	FROM user, account
	WHERE ID=userID;

