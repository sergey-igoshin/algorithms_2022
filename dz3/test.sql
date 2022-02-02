DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
USE test;


CREATE TABLE calendars(
    id INT AUTO_INCREMENT,
    fulldate DATE UNIQUE,
    PRIMARY KEY(id)
);

DELIMITER $$
DROP PROCEDURE IF EXISTS LoadCalendars$$
CREATE PROCEDURE LoadCalendars(day INT)
BEGIN    
    DECLARE counter INT DEFAULT 1;
    DECLARE dt DATE DEFAULT CONCAT(LEFT(current_date(), 7), '-01');-- current_date();

    WHILE counter <= day DO
    	INSERT INTO calendars(fulldate) VALUES(dt);
        SET counter = counter + 1;
        SET dt = DATE_ADD(dt,INTERVAL 1 month);
    END WHILE;
END$$
DELIMITER ;


CALL LoadCalendars(12);

# SELECT CONCAT(LEFT(current_date(), 7), '-01'); 


