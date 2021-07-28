# Team Gold Stock Analysis Tool
Students will build a tool for stock analysis and selection using publicly available data sets such as 13F filings, Yahoo Finance, and SEC filings. The project will require students to gather, clean, and combine data from the multiple data sources.  The consolidated data will then be analyzed to provide the end user with insight to support stock selection decision-making. The tool should be designed so that data and analysis can be easily updated by the end user as data refreshes become available.

# Summary
SEC-API is used to pull hedge fund 13F filings from a list of hedge funds. The data is entered into a MySQL database. After the data is cleaned and analyzed, the hedge funds' top holdings are extracted. Before returning these holdings to the user, each stock will be run through an Long-Short-Term-Memory (LSTM) stock predictor to assess whether the stock has met performance expectations since the end of the quarter, since 13F forms are filed quartarly, up to 45 days after the end of the quarter. 

# Prerequisites 
**Clone Repo**
    -Open the command line interface on your local machine
    -Clone the repo with the command: git clone https://github.com/davidlifschitz/team-gold.git

**Required Python Libraries to install**<br />
    -All code must be run using python3<br />
    -Install the following python libraries on your machine with the following commands:<br />
        -pandas - pip install pandas<br />
        -pandas_datareader - pip install pandas_datareader<br />
        -numpy - pip install numpy<br />
        -tensorflow - pip install tensorflow<br />
        -sklearn - pip install sklearn<br />
        -keras - pip install keras<br />
        -sec-api - pip install sec-api<br />
        -pymysql - pip install pymysql<br />


**Setting up Amazon Web Services RDS**<br />
    -Creating an Amazon RDS database (if you do not already have a database created)<br />
        1. From the AWS Management console open EC2<br />
        2. Click the orange "Create security group" button.<br />
        3. Choose a "Security group name" and "Description".<br />
            -Save the security group name.<br />
        4. Under "Inbound rules" select "Add rule".<br />
        5. Under "Type" select "All traffic" and under "Source" select "Anywhere-IPv4".<br />
        6. Select "Add rule" again.<br />
        7. Under "Type" select "All traffic" and under "Source" select "Anywhere-IPv6".<br />
        8. From the AWS Management console open RDS.<br />
        9. Click the orange "Create database" button.<br />
        10. Under "Engine options" select MySQL.<br />
        11. Under "Templates" select "Free tier".<br />
        12. Under "Settings" choose a name for your Database instance.<br />
            -Note that this is not the name of the database.<br />
        13. Under "Credentials settings" choose a "Master username" and "Master password" and confirm the password.<br />
            -Save the username and password.<br />
        14. Under "DB instance class" select "db.t2.micro".<br />
        15. Under "Public access" select "Yes".<br />
        16. Under "VPC Security group" select "Choose existing" and under "Existing security groups" choose the security group you created.<br />
        17. Under "Database authentication" select "Password authentication"<br />
        18. Under "Additional configuration" choose an "Initial databse name" for your database.<br />
            -Save this name.<br />
            -If this is not done, the database will not be created.<br /> 
        19. Click "Create database".<br />
        20. Once the database is created (it will take a few minutes), find the "Endpoint" and "Port" (the port should be 3306).<br />
            -Save these as well.<br />

**Create an SEC-API Account**<br />
    -Go to https://sec-api.io/<br />
    -Click "Get Free API Key" and create an account.<br />
    -Save your API key.<br />

**(Optional) Setting up MySQL Workbench**<br />
    -Download MySQL Workbench from https://dev.mysql.com/downloads/workbench/<br />
    -Click the "+" to add a new connection.<br />
    -Create a "Connection Name".<br />
    -Enter your database endpoint under "Host".<br />
    -Enter your port number (3306) under "Port".<br />
    -Enter your database "Master username" under "username" and your database "Master password" under "Password".<br />
    -Click "OK".<br />

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
