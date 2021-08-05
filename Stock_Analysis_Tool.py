#This program downloads the data from the last 2 years of 13F-HR filings from a pre-selected group of hedge funds.
#Each funds filings will be saved in a .json file contained in a folder called 'filings' in the working directory.
import auto_run as ar 
import demo_run as dr
def run_auto_or_demo():
    print("Type demo and press Enter if you want to try demo.")
    print("Type auto and press Enter if you want the code to all run automatically.")
    auto_or_demo = str(input())
    auto_or_demo = auto_or_demo.upper()
    if(auto_or_demo == "AUTO"):
      ar.run_auto()
    elif (auto_or_demo == "DEMO"):
      dr.run_demo()
    else:
      run_auto_or_demo()
run_auto_or_demo()