-- create database Games;
CREATE TABLE Games1 (
id INT NOT NULL AUTO_INCREMENT,
Name VARCHAR(255) NOT NULL,
Platform VARCHAR(255) NOT NULL,
Year INT NOT NULL,
Genre VARCHAR(255) NOT NULL,
Publisher VARCHAR(255) NOT NULL,
Developer varchar(255) NOT Null,
Critic_Score Float,
User_Score Float,
NA_Sales  FLOAT NOT NULL,
EU_Sales  FLOAT NOT NULL,
JP_Sales FLOAT NOT NULL,
Other_Sales  FLOAT NOT NULL,
Global_Sales FLOAT NOT NULL,
Card_image varchar(255) NOT NULL,
Full_image varchar(255) Not Null,

PRIMARY KEY (id)
);