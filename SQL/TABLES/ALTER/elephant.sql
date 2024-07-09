-- ALTER
-- ENABLE you to update an existing table.

ALTER TABLE <table> ADD COLUMN 
ALTER TABLE <table_name> DROP COLUMN <column>

ALTER TABLE student 
DROP COLUMN password


ALTER TABLE student
ADD COLUMN
password VARCHAR(255) NOT NULL DEFAULT '12345'


ALTER TABLE student 
DROP COLUMN password


ALTER TABLE student 
ADD COLUMN password VARCHAR(255); 

ALTER TABLE student 
ADD COLUMN phone BIGINT