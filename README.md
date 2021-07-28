# Team Gold Stock Analysis Tool
Students will build a tool for stock analysis and selection using publicly available data sets such as 13F filings, Yahoo Finance, and SEC filings. The project will require students to gather, clean, and combine data from the multiple data sources.  The consolidated data will then be analyzed to provide the end user with insight to support stock selection decision-making. The tool should be designed so that data and analysis can be easily updated by the end user as data refreshes become available.

# Summary
SEC-API is used to pull hedge fund 13F filings from a list of hedge funds. The data is entered into a MySQL database. After the data is cleaned and analyzed, the hedge funds' top holdings are extracted. Before returning these holdings to the user, each stock will be run through an Long-Short-Term-Memory (LSTM) stock predictor to assess whether the stock has met performance expectations since the end of the quarter, since 13F forms are filed quartarly, up to 45 days after the end of the quarter. 

# Prerequisites 
**Clone Repo**
    -Open the command line interface on your local machine
    -Clone the repo with the command: git clone https://github.com/davidlifschitz/team-gold.git

**Required Python Libraries to install**
    -All code must be run using python3
    -Install the following python libraries on your machine with the following commands:
        -pandas - pip install pandas
        -pandas_datareader - pip install pandas_datareader
        -numpy - pip install numpy
        -tensorflow - pip install tensorflow
        -sklearn - pip install sklearn
        -keras - pip install keras
        -sec-api - pip install sec-api
        -pymysql - pip install pymysql

**Setting up Amazon Web Services RDS**
    -Creating an Amazon RDS database (if you do not already have a database created)
        1. From the AWS Management console open EC2
        2. Click the orange "Create security group" button.
        3. Choose a "Security group name" and "Description".
            -Save the security group name.
        4. Under "Inbound rules" select "Add rule".
        5. Under "Type" select "All traffic" and under "Source" select "Anywhere-IPv4".
        6. Select "Add rule" again.
        7. Under "Type" select "All traffic" and under "Source" select "Anywhere-IPv6".
        8. From the AWS Management console open RDS.
        9. Click the orange "Create database" button.
        10. Under "Engine options" select MySQL.
        11. Under "Templates" select "Free tier".
        12. Under "Settings" choose a name for your Database instance.
            -Note that this is not the name of the database.
        13. Under "Credentials settings" choose a "Master username" and "Master password" and confirm the password.
            -Save the username and password.
        14. Under "DB instance class" select "db.t2.micro".
        15. Under "Public access" select "Yes".
        16. Under "VPC Security group" select "Choose existing" and under "Existing security groups" choose the security group you created.
        17. Under "Database authentication" select "Password authentication"
        18. Under "Additional configuration" choose an "Initial databse name" for your database.
            -Save this name.
            -If this is not done, the database will not be created. 
        19. Click "Create database".
        20. Once the database is created (it will take a few minutes), find the "Endpoint" and "Port" (the port should be 3306).
            -Save these as well.

**Create an SEC-API Account**
    -Go to https://sec-api.io/
    -Click "Get Free API Key" and create an account.
    -Save your API key.

**(Optional) Setting up MySQL Workbench**
    -Download MySQL Workbench from https://dev.mysql.com/downloads/workbench/
    -Click the "+" to add a new connection.
    -Create a "Connection Name".
    -Enter your database endpoint under "Host".
    -Enter your port number (3306) under "Port".
    -Enter your database "Master username" under "username" and your database "Master password" under "Password".
    -Click "OK".

**Choose Funds that you want to pull data from**
(get their CIKs for EDGAR)

# Data Pulling and Cleaning
(Discuss the plan and what data you need to implement this plan)
**Pulling Fund Data from EDGAR**
(using api-sec.io for api key)

**Using SQL and Python to clean data**
(include sql statement to get top 25 of each fund from this past quarter)
(include sql statement to export as JSON file)
(include python script that ranked the different stocks)

(Discuss where we are at this point - this is where we transition from current and past information to future predictions)
# Modeling for the future
****
