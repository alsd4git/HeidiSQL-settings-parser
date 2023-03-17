# README

## HeidiSQL (Export) Settings Parser

This Python script parses a text file containing HeidiSQL exported settings, which also have database connection settings in them and prints the information in a human-readable format
The password field is encoded in the settings export, so we print both the original encoded version and the decoded one, this code works as of HeidiSQL 12.x but this may change in future 

### Dependencies

- Python 3.x

### How to use

1. Place the text file containing the connection settings in the same directory as the script.
2. Rename the text file to "export_heidi.txt", or change the file name in the script to match the actual file name.
3. Run the script in the command line or IDE of your choice. The script will print out the connection settings in the following format:

```
Connection name: <connection name>
Host: <host address>
Port: <port number>
User: <user name>
Password (encoded): <encoded password>
Password (decoded): <decoded password>
Library: <library name>
ServerVersion: <server version number>
ServerVersionFull: <server full version>
```

If a setting is not found in the file for a particular connection, the corresponding value will be blank.

### Input File Format

The script expects the input file to follow the following format, lines that don't follow this format will be ignored:

```
Servers\<connection name>\key1<|||>datatype<|||>value
Servers\<connection name>\key2<|||>datatype<|||>value
...
Servers\<connection name>\keyN<|||>datatype<|||>value

Servers\<connection name 2>\key1<|||>datatype<|||>value
Servers\<connection name 2>\key2<|||>datatype<|||>value
...
Servers\<connection name 2>\keyM<|||>datatype<|||>value
```

Where:
- \<connection name\> is the name of the connection, and must not contain any "\\" characters.
- \<keyN\> and \<keyM\> are the names of the connection settings (e.g. Host, Port, User, Password, Library, ServerVersion)
- \<datatype\> is a number that usually is 1 or 3, I have no idea what it means, but don't need it
- \<value\> is the value of the key

### Example

#### Input File

```
Servers\dev_db\Host<|||>1<|||>localhost
Servers\dev_db\Port<|||>1<|||>3306
Servers\dev_db\User<|||>1<|||>dev_user
Servers\dev_db\Password<|||>1<|||>32FOPIR1SIha
Servers\prod_db\Host<|||>1<|||>prod.host.com
Servers\prod_db\Port<|||>1<|||>5432
Servers\prod_db\User<|||>1<|||>prod_user
Servers\prod_db\Password<|||>1<|||>7375726762736476767a7275673
Servers\prod_db\Library<|||>1<|||>libmariadb.dll
Servers\prod_db\ServerVersion<|||>1<|||>50154
Servers\prod_db\ServerVersionFull<|||>1<|||>5.1.54 - MySQL Community Server
```

#### Output

```
Connection name: dev_db
Host: localhost
Port: 3306
User: dev_user
Password (encoded): 32FOPIR1SIha
Password (decoded): dev_password
Library:
ServerVersion:
ServerVersionFull:

Connection name: prod_db
Host: prod.host.com
Port: 5432
User: prod_user
Password (encoded): 7375726762736476767a7275673
Password (decoded): prod_password
Library: libmariadb.dll
ServerVersion: 50154
ServerVersionFull: 5.1.54 - MySQL Community Server
```