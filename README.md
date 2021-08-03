# Team Gold Stock Analysis Tool
Students will build a tool for stock analysis and selection using publicly available data sets such as 13F filings, Yahoo Finance, and SEC filings. The project will require students to gather, clean, and combine data from the multiple data sources.  The consolidated data will then be analyzed to provide the end user with insight to support stock selection decision-making. The tool should be designed so that data and analysis can be easily updated by the end user as data refreshes become available.

# Summary
SEC-API is used to pull hedge fund 13F filings from a list of hedge funds. The data is entered into a MySQL database. After the data is cleaned and analyzed, the hedge funds' top holdings are extracted. Before returning these holdings to the user, each stock will be run through an Long-Short-Term-Memory (LSTM) stock predictor to assess whether the stock has met performance expectations since the end of the quarter, since 13F forms are filed quartarly, up to 45 days after the end of the quarter. 

# Prerequisites 
**Clone Repo**
    - Open the command line interface on your local machine
    - Clone the repo with the command: <br />
    ```git clone https://github.com/davidlifschitz/team-gold.git```

**Required Python Libraries to install**<br />
    -All code must be run using python3<br />
    -Install the following python libraries on your machine with the following commands:<br />
        -  pandas - ```pip install pandas```<br />
        -  pandas_datareader - ```pip install pandas_datareader```<br />
        -  numpy - ```pip install numpy```<br />
        -  tensorflow - ```pip install tensorflow```<br />
        -  sklearn - ```pip install sklearn```<br />
        -  keras - ```pip install keras```<br />
        -  sec-api - ```pip install sec-api```<br />
        -  pymysql - ```pip install pymysql```<br />
Or to install all of them at once:
```pip install pandas pandas_datareader numpy tensorflow sklearn keras sec-api pymysql```


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

# Running the Stock Analysis Tool
Before any stocks can be recommended, the database must be built. In In Stock_Analysis_Tool.py (lines 48-51), Create_Table_And_Import_Data_From_EDGAR.py (lines 13-16), and Import_Data_To_DB.py (lines 12-15) enter your hostname (also known as endpoint), username, password and database name as indicated in the program. Make sure they are all entered as strings (they should be in quotation marks). Additionally, enter your QueryAPI in Import_Data_To_DB (line 27). This will allow the program to query EDGAR's database and download the 13F filings. Make sure each of these are copied exactly and contain no extra spaces or other characters, as any error will prevent the program from connection to the database.<br />
Once this is done, simply run Stock_Analysis_Tool.py from your command line using python3.
If there is no table in the database, the program will create a new table in the database you have created. It will then download the 13F filings from EDGAR using the SEC-API and will enter each fund's holdings into the database. On any subsequent uses of the stock analysis tool, there will be no need to create a table. Instead, the program will check whether or not the databse contains the most recent filings for each fund. If it does not contain the most recent data, the program will query EDGAR's database and input the data into the table in the database you have created before continuing.<br />
Once the table contains the most recent data, the program will query the database in order to find each fund's top twenty-five holdings in the last quarter. It will then assign each stock a score based on its position in each fund's top twenty-five holdings. The program will also determine the amount of turnover each stock has undergone at a particular fund since the end of the previous quarter, allowing the user to see whether a fund has increased or decreased its stake in a particular position. <br />
The program will then take the top ten stocks, based on the score mentioned above and run a Long-Short-Term-Memory (LSTM)prediction on each one. The code used for this prediction is based on the tutorial found at https://www.datasciencecentral.com/profiles/blogs/stock-price-prediction-using-lstm-long-short-term-memory. The LSTM model analyzes the patterns in each stock's daily close price from January 1, 2018 until the end of the most recent quarter for which data is available. This provides a possible to outlook as to a fund's thinking when they owned each stock at the end of the quarter. Additionally, it allows the user to verify if the stock has performed up to the model's expectations from the end of the quarter until the day on which the program is being run. <br />
The program will return a .csv containing each fund's top twenty-five holdings as well as an additional .csv file containing the top ten stocks and the percent error of each stock's prediction. The percent error indicates how close the model was to correctly predicting the stock - the closer to zero percent, the more accurate the prediction. If the percentage is positive, the stock outperformed the model's predictions and if it is negative, it underperformed predictions. 

****
