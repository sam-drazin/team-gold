def run_create_and_import():
    # IMPORTS FOR CHECKING IF DB IS UP TO DATE
    import datetime as dt 
    #
    # IMPORTS FOR EDGAR
    from sec_api import QueryApi
    # IMPORTS FOR SQL DB CONNECTION
    import pymysql

    import Import_Data_To_DB as import_data

    #CHANGE FIELDS TO YOUR OWN PERSONAL FIELDS
    db = pymysql.connect(
      host = 'your database hosting site',
      user = 'your username',
      password = 'your password',
      db = 'Name of the database you are connecting to'
    )
    c = db.cursor()

    print("For this demo, we're calling our table \'All_Holdings_Raw_Data\'")
    #THIS IS WHAT WE CHOSE OUR TABLE NAME TO BE:
    Your_Table_Name = "All_Holdings_Raw_Data"
    # CREATE TABLE
    sql = '''
    create table %s (
    filingDate text,
    shares int,
    value int,
    cusip varchar(255),
    nameOfIssuer text,
    CIK int
    )
    ''' % Your_Table_Name
    c.execute(sql)

    # Choose how far back you want the data from, we chose 4 quarters worth.
    number_of_quarters = 4
    import_data.run_import(number_of_quarters)
    return Your_Table_Name