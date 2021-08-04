# Team Gold Stock Analysis Tool
Students will build a tool for stock analysis and selection using publicly available data sets such as 13F filings, Yahoo Finance, and SEC filings. The project will require students to gather, clean, and combine data from the multiple data sources.  The consolidated data will then be analyzed to provide the end user with insight to support stock selection decision-making. The tool should be designed so that data and analysis can be easily updated by the end user as data refreshes become available.

# Summary
SEC-API is used to pull hedge fund 13F filings from a list of hedge funds. The data is entered into a MySQL database. After the data is cleaned and analyzed, the hedge funds' top holdings are extracted. Before returning these holdings to the user, each stock will be run through an Long-Short-Term-Memory (LSTM) stock predictor to assess whether the stock has met performance expectations since the end of the quarter, since 13F forms are filed quarterly, up to 45 days after the end of the quarter. <br />
These are the hedge funds that are used in the Stock Analysis Tool:
* Bridger Capital, L.L.C.
* Bridgewater Associates, L.P.
* Citadel, L.L.C.
* Coatue Management, L.P.
* D. E. Shaw & Co., L.P. 
* Discovery Capital Management, L.L.C.
* ExodusPoint Capital Management, L.P.
* HealthCor Management, L.P.
* Impala Asset Management, L.L.C.
* Intrepid Capital, L.P.
* Joho Capital, L.L.C.
* Light Street Capital, L.L.C.
* Lone Pine Capital, L.L.C.
* Marshall Wace, L.L.P.
* Matrix Capital Management, L.P.
* Maverick Capital, Ltd.
* Millburn Ridgefield Corp.
* Millennium Management, LLC
* Point72 Asset Management, L.P.
* Schonfeld Strategic Advisors, L.L.C.
* Second Curve Capital, L.L.C.
* Soros Fund Management, L.L.C.
* Sun Valley Gold, L.L.C.
* Third Point Management, L.L.C.
* Tiger Global Management, L.L.C.
* Toscafund Asset Management, L.L.P.

# Steps to Use the Stock Analysis Tool
1. Clone this repository to your machine using the command ```git clone https://github.com/davidlifschitz/team-gold.git```
2. Set up a MySQL database (Using Amazon RDS is recommended - see steps listed below).
3. (Optional) Connect to the database in MySQL workbench (see steps listed below).
4. Create an account at [SEC-API](https://sec-api.io/) to obtain an API Key.
5. Input the relevant database information and query API where listed below.
6. Install the necessary libraries on your machine using the command ```pip3 install -r requirements.txt```
7. Run the program using python3.
8. View the files that have been created in your working directory.

# Prerequisites 
**Clone Repo**
1. Open the command line interface on your local machine
2. Clone the repo with the command: <br />
    ```git clone https://github.com/davidlifschitz/team-gold.git```

**Required Python Libraries to install**<br />
1. All code must be run using python3<br />
2. Install the following python libraries on your machine with the following commands:<br />
    ```pip3 install -r requirements.txt```<br />

**Setting up Amazon Web Services RDS**<br />
1. From the AWS Management console open EC2<br />
2. Click the orange "Create security group" button.<br />
3. Choose a "Security group name" and "Description".<br />
    * Save the security group name.<br />
4. Under "Inbound rules" select "Add rule".<br />
5. Under "Type" select "All traffic" and under "Source" select "Anywhere-IPv4".<br />
6. Select "Add rule" again.<br />
7. Under "Type" select "All traffic" and under "Source" select "Anywhere-IPv6".<br />
8. From the AWS Management console open RDS.<br />
9. Click the orange "Create database" button.<br />
10. Under "Engine options" select MySQL.<br />
11. Under "Templates" select "Free tier".<br />
12. Under "Settings" choose a name for your Database instance.<br />
    * Note that this is not the name of the database.<br />
13. Under "Credentials settings" choose a "Master username" and "Master password" and confirm the password.<br />
    * Save the username and password.<br />
14. Under "DB instance class" select "db.t2.micro".<br />
15. Under "Public access" select "Yes".<br />
16. Under "VPC Security group" select "Choose existing" and under "Existing security groups" choose the security group you created.<br />
17. Under "Database authentication" select "Password authentication"<br />
18. Under "Additional configuration" choose an "Initial databse name" for your database.<br />
    * Save this name.<br />
    * If this is not done, the database will not be created.<br /> 
19. Click "Create database".<br />
20. Once the database is created (it will take a few minutes), find the "Endpoint" and "Port" (the port should be 3306).<br />
    * Save these for later use.

**(Optional) Setting up MySQL Workbench**<br />
1. Download MySQL Workbench from [here](https://dev.mysql.com/downloads/workbench/)<br />
2. Click the "+" to add a new connection.<br />
3. Create a "Connection Name".<br />
4. Enter your database endpoint under "Host".<br />
5. Enter your port number (3306) under "Port".<br />
6. Enter your database "Master username" under "username" and your database "Master password" under "Password".<br />
7. Click "OK".<br />

**Create an SEC-API Account**<br />
1. Go to https://sec-api.io/<br />
2. Click "Get Free API Key" and create an account.<br />
3. Save your API key.<br />

# Running the Stock Analysis Tool
1. Before any stocks can be recommended, the database must be built. In Stock_Analysis_Tool.py, Create_Table_And_Import_Data_From_EDGAR.py, and Import_Data_To_DB.py enter your hostname (also known as endpoint), username, password and database name as indicated in the program. Make sure they are all entered as strings (they should be in quotation marks). 
2. Additionally, enter your QueryAPI in Import_Data_To_DB (line 27). This will allow the program to query EDGAR's database and download the 13F filings. 
3. Finally, in Create_Table_And_Import_Data_From_EDGAR.py, enter the desired name for the created table, where indicated. 
    * Make sure each of these are copied exactly and contain no extra spaces or other characters, as any error will prevent the program from connecting to the database.<br />
4. Once this is done, simply run Stock_Analysis_Tool.py from your command line using python3.
5. If there is no table in the database, the program will create a new table in the database you have created. It will then download the 13F filings from EDGAR using the SEC-API and will enter each fund's holdings into the database. 
6. On any subsequent uses of the stock analysis tool, there will be no need to create a table. Instead, the program will check whether or not the databse contains the most recent filings for each fund. If it does not contain the most recent data, the program will query EDGAR's database and input the data into the table in the database you have created before continuing.<br />
7. Once the table contains the most recent data, the program will query the database in order to find each fund's top twenty-five holdings in the last quarter. It will then assign each stock a score based on its position in each fund's top twenty-five holdings. The program will also determine the amount of turnover each stock has undergone at a particular fund since the end of the previous quarter, allowing the user to see whether a fund has increased or decreased its stake in a particular position. <br />
    * The stocks' will be returned as a list of their Committee on Uniform Securities Identification Procedures (CUSIP) numbers.
    * Stocks that are in a fund's top 1-5 holdings receive 5 points, stocks in a fund's top 6-10 holdings receive 4 points, stocks in a fund's top 11-15 holdings receive 3 points, stocks in a fund's top 16-20 holdings receive 2 points, and stocks in a fund's top 21-25 holdings receive 1 point.
9. The program will take the CUSIP numbers and use the Finnhub API to find each the stock symbol the corresponds to each CUSIP.
10. The program will then take the top twenty-five stocks, based on the score mentioned above and run a Long-Short-Term-Memory (LSTM) prediction on each one. The code used for this prediction is based on the tutorial found [here](https://www.datasciencecentral.com/profiles/blogs/stock-price-prediction-using-lstm-long-short-term-memory). 
11. The LSTM model analyzes the patterns in each stock's daily close price from January 1, 2018 until the end of the most recent quarter for which data is available. This provides a possibility to have an outlook into a fund's possible thinking when they held each position at the end of the quarter. Additionally, it allows the user to verify if the stock has performed up to the model's expectations from the end of the quarter until the day on which the program is being run. <br />
    * Each stock's data is obtained by using the Pandas Datareader to pull the data from [Yahoo! Finance](finance.yahoo.com).
12. The program will return a .csv file containing each fund's top twenty-five holdings as well as an additional .csv file containing the top twenty-five stocks based on their score and the percent error of each stock's prediction.
13. The percent error indicates how close the model was to correctly predicting the stock - the closer to zero percent, the more accurate the prediction. If the percentage is positive, the stock outperformed the model's predictions and if it is negative, it underperformed predictions. 

****
