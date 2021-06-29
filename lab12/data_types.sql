### ~~~ integer_datatypes ~~~
CREATE TABLE IF NOT EXISTS integer_datatypes(
  id int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  tinyint_data tinyint(3) DEFAULT NULL,
  smallint_data smallint(6) ZEROFIL DEFAULT NULL,
  mediumint_data mediumint(9) DEFAULT NULL,
  int_data int(11) DEFAULT NULL,
  bigint_data bigint(20) DEFAULT NULL,
  PRIMARY KEY (id)
);

INSERT INTO integer_datatypes (tinyint_data,smallint_data,mediumint_data,int_data,bigint_data )
VALUES (128, 20000, 3000000, 100000000, 10000000000000000 );

### ~~~ real_datatypes ~~~
CREATE TABLE IF NOT EXISTS real_datatypes(
    id int(10)         unsigned NOT NULL AUTO_INCREMENT,
    decimal_data        NUMERIC(1,1),
    float_data          FLOAT(5,2),
    double_data         DOUBLE(10,5),
    PRIMARY KEY (id)
);
INSERT INTO real_datatypes (decimal_data,float_data,double_data)
VALUES ( 12345.12, 1.256, 1000000.2000);

### ~~~ string_datatypes ~~~
CREATE TABLE IF NOT EXISTS string_datatypes(
    id int(10)          unsigned NOT NULL AUTO_INCREMENT,
    char_data           CHAR(255),
    varchar_data        VARCHAR(50000),
    text_data           TEXT,
    blob_data           BLOB,
    enum_data           ENUM('yes','no'),
    PRIMARY KEY (id)
);
INSERT INTO string_datatypes (char_data, varchar_data, text_data, blob_data, enum_data )
VALUES('1234', '12345', 'Here should be a very very long text', 'this will be interpreted as binary data', 'yes' );

### ~~~ date_and_time_datatypes ~~~
CREATE TABLE IF NOT EXISTS date_and_time_datatypes(
    id int(10)          unsigned NOT NULL AUTO_INCREMENT,
    date_data           DATE,
    datetime_data       DATETIME,
    timestamp_data      TIMESTAMP,
    PRIMARY KEY (id)
);
INSERT INTO date_and_time_datatypes(date_data, datetime_data, timestamp_data)
VALUES ( '2016/3/28', '16/3/28 9.54.10', '2016/03/28 09.54.10');
