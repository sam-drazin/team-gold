import pandas as pd
obj = [
    {
    "valSum" : "2147483647",
    "cik" : "934639",
    "cusip" : "22266T109",
    "nameOfIssuer" : "COUPANG INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "1",
    "totals" : "2147483647"
    },
{
    "valSum" : "399068000",
    "cik" : "934639",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "2",
    "totals" : "-43709000"
    },
{
    "valSum" : "282029000",
    "cik" : "934639",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "3",
    "totals" : "-38102000"
    },
{
    "valSum" : "273557000",
    "cik" : "934639",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "4",
    "totals" : "104646000"
    },
{
    "valSum" : "261874000",
    "cik" : "934639",
    "cusip" : "81578P106",
    "nameOfIssuer" : "SEER INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "5",
    "totals" : "-17327000"
    },
{
    "valSum" : "224790000",
    "cik" : "934639",
    "cusip" : "02079K107",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "6",
    "totals" : "-27542000"
    },
{
    "valSum" : "211747000",
    "cik" : "934639",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "7",
    "totals" : "55149000"
    },
{
    "valSum" : "186623000",
    "cik" : "934639",
    "cusip" : "38222105",
    "nameOfIssuer" : "APPLIED MATLS INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "8",
    "totals" : "-82230000"
    },
{
    "valSum" : "171423000",
    "cik" : "934639",
    "cusip" : "512807108",
    "nameOfIssuer" : "LAM RESEARCH CORP",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "9",
    "totals" : "-96377000"
    },
{
    "valSum" : "146793000",
    "cik" : "934639",
    "cusip" : "339041105",
    "nameOfIssuer" : "FLEETCOR TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "10",
    "totals" : "-120454000"
    },
{
    "valSum" : "143842000",
    "cik" : "934639",
    "cusip" : "872590104",
    "nameOfIssuer" : "T-MOBILE US INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "11",
    "totals" : "143842000"
    },
{
    "valSum" : "143209000",
    "cik" : "934639",
    "cusip" : "88322Q108",
    "nameOfIssuer" : "TG THERAPEUTICS INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "12",
    "totals" : "-23362000"
    },
{
    "valSum" : "143080000",
    "cik" : "934639",
    "cusip" : "68269G107",
    "nameOfIssuer" : "1LIFE HEALTHCARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "13",
    "totals" : "-16732000"
    },
{
    "valSum" : "128638000",
    "cik" : "934639",
    "cusip" : "G98239109",
    "nameOfIssuer" : "XP INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "14",
    "totals" : "52630000"
    },
{
    "valSum" : "125952000",
    "cik" : "934639",
    "cusip" : "G0403H108",
    "nameOfIssuer" : "AON PLC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "15",
    "totals" : "125703000"
    },
{
    "valSum" : "121121000",
    "cik" : "934639",
    "cusip" : "50212V100",
    "nameOfIssuer" : "LPL FINL HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "16",
    "totals" : "120582000"
    },
{
    "valSum" : "117166000",
    "cik" : "934639",
    "cusip" : "640268108",
    "nameOfIssuer" : "NEKTAR THERAPEUTICS",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "17",
    "totals" : "4020000"
    },
{
    "valSum" : "113137000",
    "cik" : "934639",
    "cusip" : "444859102",
    "nameOfIssuer" : "HUMANA INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "18",
    "totals" : "-4332000"
    },
{
    "valSum" : "112420000",
    "cik" : "934639",
    "cusip" : "02043Q107",
    "nameOfIssuer" : "ALNYLAM PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "19",
    "totals" : "-15536000"
    },
{
    "valSum" : "110968000",
    "cik" : "934639",
    "cusip" : "459506101",
    "nameOfIssuer" : "INTERNATIONAL FLAVORS&FRAGRA",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "20",
    "totals" : "110968000"
    },
{
    "valSum" : "106071000",
    "cik" : "934639",
    "cusip" : "228368106",
    "nameOfIssuer" : "CROWN HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "21",
    "totals" : "-46068000"
    },
{
    "valSum" : "96778000",
    "cik" : "934639",
    "cusip" : "46513107",
    "nameOfIssuer" : "ATARA BIOTHERAPEUTICS INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "22",
    "totals" : "-47003000"
    },
{
    "valSum" : "88381000",
    "cik" : "934639",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "23",
    "totals" : "61423000"
    },
{
    "valSum" : "86149000",
    "cik" : "934639",
    "cusip" : "G5509L101",
    "nameOfIssuer" : "LIVANOVA PLC",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "24",
    "totals" : "-24350000"
    },
{
    "valSum" : "79910000",
    "cik" : "934639",
    "cusip" : "00724F101",
    "nameOfIssuer" : "ADOBE SYSTEMS INCORPORATED",
    "filingDate" : "2021-03-31",
    "name" : "Maverick",
    "rnk" : "25",
    "totals" : "-55053000"
    },
{
    "valSum" : "2477106000",
    "cik" : "1009207",
    "cusip" : "88160R101",
    "nameOfIssuer" : "TESLA INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "1",
    "totals" : "676758000"
    },
{
    "valSum" : "2059324000",
    "cik" : "1009207",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "2",
    "totals" : "8219000"
    },
{
    "valSum" : "1953455000",
    "cik" : "1009207",
    "cusip" : "37833100",
    "nameOfIssuer" : "APPLE INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "3",
    "totals" : "-53245000"
    },
{
    "valSum" : "1891454000",
    "cik" : "1009207",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "4",
    "totals" : "-1436605000"
    },
{
    "valSum" : "1080891000",
    "cik" : "1009207",
    "cusip" : "852234103",
    "nameOfIssuer" : "SQUARE INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "5",
    "totals" : "-518476000"
    },
{
    "valSum" : "1053281000",
    "cik" : "1009207",
    "cusip" : "254687106",
    "nameOfIssuer" : "DISNEY WALT CO",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "6",
    "totals" : "-308269000"
    },
{
    "valSum" : "851176000",
    "cik" : "1009207",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "7",
    "totals" : "-179058000"
    },
{
    "valSum" : "846057000",
    "cik" : "1009207",
    "cusip" : "191216100",
    "nameOfIssuer" : "COCA COLA CO",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "8",
    "totals" : "359660000"
    },
{
    "valSum" : "836878000",
    "cik" : "1009207",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "9",
    "totals" : "137660000"
    },
{
    "valSum" : "833274000",
    "cik" : "1009207",
    "cusip" : "58933Y105",
    "nameOfIssuer" : "MERCK & CO. INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "10",
    "totals" : "-38564000"
    },
{
    "valSum" : "813987000",
    "cik" : "1009207",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "11",
    "totals" : "-951000"
    },
{
    "valSum" : "801520000",
    "cik" : "1009207",
    "cusip" : "83304A106",
    "nameOfIssuer" : "SNAP INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "12",
    "totals" : "-48114000"
    },
{
    "valSum" : "800187000",
    "cik" : "1009207",
    "cusip" : "595112103",
    "nameOfIssuer" : "MICRON TECHNOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "13",
    "totals" : "-123421000"
    },
{
    "valSum" : "767761000",
    "cik" : "1009207",
    "cusip" : "56752108",
    "nameOfIssuer" : "BAIDU INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "14",
    "totals" : "640590000"
    },
{
    "valSum" : "738006000",
    "cik" : "1009207",
    "cusip" : "67066G104",
    "nameOfIssuer" : "NVIDIA CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "15",
    "totals" : "90404000"
    },
{
    "valSum" : "732798000",
    "cik" : "1009207",
    "cusip" : "82509L107",
    "nameOfIssuer" : "SHOPIFY INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "16",
    "totals" : "-15874000"
    },
{
    "valSum" : "718796000",
    "cik" : "1009207",
    "cusip" : "949746101",
    "nameOfIssuer" : "WELLS FARGO CO NEW",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "17",
    "totals" : "-463998000"
    },
{
    "valSum" : "716769000",
    "cik" : "1009207",
    "cusip" : "58733R102",
    "nameOfIssuer" : "MERCADOLIBRE INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "18",
    "totals" : "-160033000"
    },
{
    "valSum" : "663206000",
    "cik" : "1009207",
    "cusip" : "22160K105",
    "nameOfIssuer" : "COSTCO WHSL CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "19",
    "totals" : "194065000"
    },
{
    "valSum" : "647832000",
    "cik" : "1009207",
    "cusip" : "62914V106",
    "nameOfIssuer" : "NIO INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "20",
    "totals" : "-347884000"
    },
{
    "valSum" : "587943000",
    "cik" : "1009207",
    "cusip" : "00206R102",
    "nameOfIssuer" : "AT&T INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "21",
    "totals" : "55724000"
    },
{
    "valSum" : "573621000",
    "cik" : "1009207",
    "cusip" : "22788C105",
    "nameOfIssuer" : "CROWDSTRIKE HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "22",
    "totals" : "-115866000"
    },
{
    "valSum" : "573390000",
    "cik" : "1009207",
    "cusip" : "742718109",
    "nameOfIssuer" : "PROCTER AND GAMBLE CO",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "23",
    "totals" : "-116355000"
    },
{
    "valSum" : "564705000",
    "cik" : "1009207",
    "cusip" : "30231G102",
    "nameOfIssuer" : "EXXON MOBIL CORP",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "24",
    "totals" : "212901000"
    },
{
    "valSum" : "536892000",
    "cik" : "1009207",
    "cusip" : "00724F101",
    "nameOfIssuer" : "ADOBE SYSTEMS INCORPORATED",
    "filingDate" : "2021-03-31",
    "name" : "DE Shaw",
    "rnk" : "25",
    "totals" : "325618000"
    },
{
    "valSum" : "631058000",
    "cik" : "1029160",
    "cusip" : "530307305",
    "nameOfIssuer" : "LIBERTY BROADBAND CORP",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "1",
    "totals" : "-205415000"
    },
{
    "valSum" : "480748000",
    "cik" : "1029160",
    "cusip" : "46090",
    "nameOfIssuer" : "INVESCO QQQ TR",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "2",
    "totals" : "126889000"
    },
{
    "valSum" : "392819000",
    "cik" : "1029160",
    "cusip" : "23331A109",
    "nameOfIssuer" : "D R HORTON INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "3",
    "totals" : "137546000"
    },
{
    "valSum" : "213473000",
    "cik" : "1029160",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "4",
    "totals" : "195296000"
    },
{
    "valSum" : "206270000",
    "cik" : "1029160",
    "cusip" : "464287242",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "5",
    "totals" : "-12815000"
    },
{
    "valSum" : "194287000",
    "cik" : "1029160",
    "cusip" : "92556H206",
    "nameOfIssuer" : "VIACOMCBS INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "6",
    "totals" : "194287000"
    },
{
    "valSum" : "148349000",
    "cik" : "1029160",
    "cusip" : "74767V109",
    "nameOfIssuer" : "QUANTUMSCAPE CORP",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "7",
    "totals" : "-131608000"
    },
{
    "valSum" : "142324000",
    "cik" : "1029160",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "8",
    "totals" : "108034000"
    },
{
    "valSum" : "134684000",
    "cik" : "1029160",
    "cusip" : "00507V109",
    "nameOfIssuer" : "ACTIVISION BLIZZARD INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "9",
    "totals" : "14163000"
    },
{
    "valSum" : "127556000",
    "cik" : "1029160",
    "cusip" : "81369Y506",
    "nameOfIssuer" : "SELECT SECTOR SPDR TR",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "10",
    "totals" : "46071000"
    },
{
    "valSum" : "92829000",
    "cik" : "1029160",
    "cusip" : "925652109",
    "nameOfIssuer" : "VICI PPTYS INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "11",
    "totals" : "15270000"
    },
{
    "valSum" : "77343000",
    "cik" : "1029160",
    "cusip" : "91680M107",
    "nameOfIssuer" : "UPSTART HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "12",
    "totals" : "52885000"
    },
{
    "valSum" : "76968000",
    "cik" : "1029160",
    "cusip" : "56752108",
    "nameOfIssuer" : "BAIDU INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "13",
    "totals" : "76968000"
    },
{
    "valSum" : "75587000",
    "cik" : "1029160",
    "cusip" : "81141RAD2",
    "nameOfIssuer" : "SEA LTD",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "14",
    "totals" : "8171000"
    },
{
    "valSum" : "73686000",
    "cik" : "1029160",
    "cusip" : "03852U106",
    "nameOfIssuer" : "ARAMARK",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "15",
    "totals" : "6331000"
    },
{
    "valSum" : "68947000",
    "cik" : "1029160",
    "cusip" : "872590104",
    "nameOfIssuer" : "T-MOBILE US INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "16",
    "totals" : "-2808000"
    },
{
    "valSum" : "63413000",
    "cik" : "1029160",
    "cusip" : "78462F103",
    "nameOfIssuer" : "SPDR S&P 500 ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "17",
    "totals" : "63413000"
    },
{
    "valSum" : "60859000",
    "cik" : "1029160",
    "cusip" : "464288646",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "18",
    "totals" : "-545000"
    },
{
    "valSum" : "55235000",
    "cik" : "1029160",
    "cusip" : "464287655",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "19",
    "totals" : "55235000"
    },
{
    "valSum" : "52483000",
    "cik" : "1029160",
    "cusip" : "98954MAG6",
    "nameOfIssuer" : "ZILLOW GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "20",
    "totals" : "-255000"
    },
{
    "valSum" : "51448000",
    "cik" : "1029160",
    "cusip" : "02376RAF9",
    "nameOfIssuer" : "AMERICAN AIRLS GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "21",
    "totals" : "36827000"
    },
{
    "valSum" : "47890000",
    "cik" : "1029160",
    "cusip" : "24790A101",
    "nameOfIssuer" : "DENBURY INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "22",
    "totals" : "27632000"
    },
{
    "valSum" : "47524000",
    "cik" : "1029160",
    "cusip" : "405217100",
    "nameOfIssuer" : "HAIN CELESTIAL GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "23",
    "totals" : "-35794000"
    },
{
    "valSum" : "47120000",
    "cik" : "1029160",
    "cusip" : "28414H103",
    "nameOfIssuer" : "ELANCO ANIMAL HEALTH INC",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "24",
    "totals" : "1115000"
    },
{
    "valSum" : "46412000",
    "cik" : "1029160",
    "cusip" : "92763W103",
    "nameOfIssuer" : "VIPSHOP HOLDINGS LIMITED",
    "filingDate" : "2021-03-31",
    "name" : "Soros Fund",
    "rnk" : "25",
    "totals" : "46412000"
    },
{
    "valSum" : "123684000",
    "cik" : "1040198",
    "cusip" : "15351109",
    "nameOfIssuer" : "ALEXION PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "1",
    "totals" : "34627000"
    },
{
    "valSum" : "93371000",
    "cik" : "1040198",
    "cusip" : "92220P105",
    "nameOfIssuer" : "VARIAN MED SYS INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "2",
    "totals" : "-14138000"
    },
{
    "valSum" : "80163000",
    "cik" : "1040198",
    "cusip" : "75606N109",
    "nameOfIssuer" : "REALPAGE INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "3",
    "totals" : "70130000"
    },
{
    "valSum" : "65827000",
    "cik" : "1040198",
    "cusip" : "228368106",
    "nameOfIssuer" : "CROWN HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "4",
    "totals" : "-3411000"
    },
{
    "valSum" : "58592000",
    "cik" : "1040198",
    "cusip" : "74167P108",
    "nameOfIssuer" : "PRIMO WATER CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "5",
    "totals" : "24218000"
    },
{
    "valSum" : "56403000",
    "cik" : "1040198",
    "cusip" : "7800105",
    "nameOfIssuer" : "AEROJET ROCKETDYNE HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "6",
    "totals" : "51116000"
    },
{
    "valSum" : "48474000",
    "cik" : "1040198",
    "cusip" : "983793100",
    "nameOfIssuer" : "XPO LOGISTICS INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "7",
    "totals" : "1150000"
    },
{
    "valSum" : "44975000",
    "cik" : "1040198",
    "cusip" : "500255104",
    "nameOfIssuer" : "KOHLS CORP",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "8",
    "totals" : "44975000"
    },
{
    "valSum" : "34687000",
    "cik" : "1040198",
    "cusip" : "G96629103",
    "nameOfIssuer" : "WILLIS TOWERS WATSON PLC LTD",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "9",
    "totals" : "34687000"
    },
{
    "valSum" : "34356000",
    "cik" : "1040198",
    "cusip" : "38388F108",
    "nameOfIssuer" : "GRACE W R & CO DEL NEW",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "10",
    "totals" : "27915000"
    },
{
    "valSum" : "29611000",
    "cik" : "1040198",
    "cusip" : "92244F109",
    "nameOfIssuer" : "VECTOIQ ACQUISITION CORP II",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "11",
    "totals" : "29611000"
    },
{
    "valSum" : "27519000",
    "cik" : "1040198",
    "cusip" : "337932107",
    "nameOfIssuer" : "FIRSTENERGY CORP",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "12",
    "totals" : "2989000"
    },
{
    "valSum" : "26805000",
    "cik" : "1040198",
    "cusip" : "131193104",
    "nameOfIssuer" : "CALLAWAY GOLF CO",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "13",
    "totals" : "17201000"
    },
{
    "valSum" : "26425000",
    "cik" : "1040198",
    "cusip" : "G37288100",
    "nameOfIssuer" : "FTAC OLYMPUS ACQUISITION COR",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "14",
    "totals" : "675000"
    },
{
    "valSum" : "24994000",
    "cik" : "1040198",
    "cusip" : "21871D103",
    "nameOfIssuer" : "CORELOGIC INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "15",
    "totals" : "-20377000"
    },
{
    "valSum" : "24064000",
    "cik" : "1040198",
    "cusip" : "501797104",
    "nameOfIssuer" : "L BRANDS INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "16",
    "totals" : "24064000"
    },
{
    "valSum" : "21605000",
    "cik" : "1040198",
    "cusip" : "31810Q107",
    "nameOfIssuer" : "FINTECH ACQUISITION CORP V",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "17",
    "totals" : "21605000"
    },
{
    "valSum" : "20450000",
    "cik" : "1040198",
    "cusip" : "10316T104",
    "nameOfIssuer" : "BOX INC",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "18",
    "totals" : "20450000"
    },
{
    "valSum" : "20227000",
    "cik" : "1040198",
    "cusip" : "464287739",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "19",
    "totals" : "20227000"
    },
{
    "valSum" : "19920000",
    "cik" : "1040198",
    "cusip" : "98880C201",
    "nameOfIssuer" : "Z-WORK ACQUISITION CORP",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "20",
    "totals" : "19920000"
    },
{
    "valSum" : "19900000",
    "cik" : "1040198",
    "cusip" : "457817104",
    "nameOfIssuer" : "INSU ACQUISITION CORP III",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "21",
    "totals" : "19900000"
    },
{
    "valSum" : "17173000",
    "cik" : "1040198",
    "cusip" : "88025V107",
    "nameOfIssuer" : "10X CAPITAL VENTURE ACQU COR",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "22",
    "totals" : "17173000"
    },
{
    "valSum" : "16919000",
    "cik" : "1040198",
    "cusip" : "31810N104",
    "nameOfIssuer" : "FINTECH ACQUISITION CORP IV",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "23",
    "totals" : "-4551000"
    },
{
    "valSum" : "14895000",
    "cik" : "1040198",
    "cusip" : "30319B207",
    "nameOfIssuer" : "FTAC PARNASSUS ACQUISITN COR",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "24",
    "totals" : "14895000"
    },
{
    "valSum" : "14880000",
    "cik" : "1040198",
    "cusip" : "66516U101",
    "nameOfIssuer" : "NORTHERN GENESIS ACQUISITION",
    "filingDate" : "2021-03-31",
    "name" : "Schoenfeld",
    "rnk" : "25",
    "totals" : "14880000"
    },
{
    "valSum" : "1688860000",
    "cik" : "1040273",
    "cusip" : "91680M107",
    "nameOfIssuer" : "UPSTART HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "1",
    "totals" : "1168416000"
    },
{
    "valSum" : "971172000",
    "cik" : "1040273",
    "cusip" : "69331C108",
    "nameOfIssuer" : "PG&E CORP",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "2",
    "totals" : "-87121000"
    },
{
    "valSum" : "774984000",
    "cik" : "1040273",
    "cusip" : "254687106",
    "nameOfIssuer" : "DISNEY WALT CO",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "3",
    "totals" : "-94680000"
    },
{
    "valSum" : "652732000",
    "cik" : "1040273",
    "cusip" : "235851102",
    "nameOfIssuer" : "DANAHER CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "4",
    "totals" : "-13688000"
    },
{
    "valSum" : "560250000",
    "cik" : "1040273",
    "cusip" : "G6964L107",
    "nameOfIssuer" : "PAYSAFE LIMITED",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "5",
    "totals" : "560250000"
    },
{
    "valSum" : "479646000",
    "cik" : "1040273",
    "cusip" : "449253103",
    "nameOfIssuer" : "IAA INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "6",
    "totals" : "-163656000"
    },
{
    "valSum" : "459672000",
    "cik" : "1040273",
    "cusip" : "461202103",
    "nameOfIssuer" : "INTUIT",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "7",
    "totals" : "79822000"
    },
{
    "valSum" : "452040000",
    "cik" : "1040273",
    "cusip" : "22160N109",
    "nameOfIssuer" : "COSTAR GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "8",
    "totals" : "452040000"
    },
{
    "valSum" : "448200000",
    "cik" : "1040273",
    "cusip" : "122017106",
    "nameOfIssuer" : "BURLINGTON STORES INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "9",
    "totals" : "11412000"
    },
{
    "valSum" : "433129000",
    "cik" : "1040273",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "10",
    "totals" : "-22557000"
    },
{
    "valSum" : "401063000",
    "cik" : "1040273",
    "cusip" : "16119P108",
    "nameOfIssuer" : "CHARTER COMMUNICATIONS INC N",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "11",
    "totals" : "-95099000"
    },
{
    "valSum" : "377232000",
    "cik" : "1040273",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "12",
    "totals" : "88086000"
    },
{
    "valSum" : "367942000",
    "cik" : "1040273",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "13",
    "totals" : "367942000"
    },
{
    "valSum" : "352870000",
    "cik" : "1040273",
    "cusip" : "78409V104",
    "nameOfIssuer" : "S&P GLOBAL INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "14",
    "totals" : "57013000"
    },
{
    "valSum" : "352725000",
    "cik" : "1040273",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "15",
    "totals" : "-119530000"
    },
{
    "valSum" : "349661000",
    "cik" : "1040273",
    "cusip" : "46266C105",
    "nameOfIssuer" : "IQVIA HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "16",
    "totals" : "25292000"
    },
{
    "valSum" : "318230000",
    "cik" : "1040273",
    "cusip" : "05352A100",
    "nameOfIssuer" : "AVANTOR INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "17",
    "totals" : "8580000"
    },
{
    "valSum" : "317595000",
    "cik" : "1040273",
    "cusip" : "92826C839",
    "nameOfIssuer" : "VISA INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "18",
    "totals" : "-21437000"
    },
{
    "valSum" : "294530000",
    "cik" : "1040273",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "19",
    "totals" : "-5946000"
    },
{
    "valSum" : "285141000",
    "cik" : "1040273",
    "cusip" : "893641100",
    "nameOfIssuer" : "TRANSDIGM GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "20",
    "totals" : "-15001000"
    },
{
    "valSum" : "280670000",
    "cik" : "1040273",
    "cusip" : "518439104",
    "nameOfIssuer" : "LAUDER ESTEE COS INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "21",
    "totals" : "227432000"
    },
{
    "valSum" : "278289000",
    "cik" : "1040273",
    "cusip" : "47215P106",
    "nameOfIssuer" : "JD.COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "22",
    "totals" : "-20571000"
    },
{
    "valSum" : "223242000",
    "cik" : "1040273",
    "cusip" : "91324P102",
    "nameOfIssuer" : "UNITEDHEALTH GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "23",
    "totals" : "111024000"
    },
{
    "valSum" : "213745000",
    "cik" : "1040273",
    "cusip" : "G6095L109",
    "nameOfIssuer" : "APTIV PLC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "24",
    "totals" : "18310000"
    },
{
    "valSum" : "206724000",
    "cik" : "1040273",
    "cusip" : "26614N102",
    "nameOfIssuer" : "DUPONT DE NEMOURS INC",
    "filingDate" : "2021-03-31",
    "name" : "Third Point",
    "rnk" : "25",
    "totals" : "206724000"
    },
{
    "valSum" : "1894870000",
    "cik" : "1061165",
    "cusip" : "82509L107",
    "nameOfIssuer" : "SHOPIFY INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "1",
    "totals" : "-137309000"
    },
{
    "valSum" : "1844805000",
    "cik" : "1061165",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "2",
    "totals" : "440780000"
    },
{
    "valSum" : "1667735000",
    "cik" : "1061165",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "3",
    "totals" : "691039000"
    },
{
    "valSum" : "1624759000",
    "cik" : "1061165",
    "cusip" : "501797104",
    "nameOfIssuer" : "L BRANDS INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "4",
    "totals" : "647960000"
    },
{
    "valSum" : "1490554000",
    "cik" : "1061165",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "5",
    "totals" : "653113000"
    },
{
    "valSum" : "1255774000",
    "cik" : "1061165",
    "cusip" : "83304A106",
    "nameOfIssuer" : "SNAP INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "6",
    "totals" : "278879000"
    },
{
    "valSum" : "1246613000",
    "cik" : "1061165",
    "cusip" : "00724F101",
    "nameOfIssuer" : "ADOBE SYSTEMS INCORPORATED",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "7",
    "totals" : "236002000"
    },
{
    "valSum" : "1170746000",
    "cik" : "1061165",
    "cusip" : "91324P102",
    "nameOfIssuer" : "UNITEDHEALTH GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "8",
    "totals" : "55577000"
    },
{
    "valSum" : "1056579000",
    "cik" : "1061165",
    "cusip" : "22266L106",
    "nameOfIssuer" : "COUPA SOFTWARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "9",
    "totals" : "-373860000"
    },
{
    "valSum" : "1052804000",
    "cik" : "1061165",
    "cusip" : "58733R102",
    "nameOfIssuer" : "MERCADOLIBRE INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "10",
    "totals" : "52512000"
    },
{
    "valSum" : "953657000",
    "cik" : "1061165",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "11",
    "totals" : "-372278000"
    },
{
    "valSum" : "881659000",
    "cik" : "1061165",
    "cusip" : "25809K105",
    "nameOfIssuer" : "DOORDASH INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "12",
    "totals" : "559482000"
    },
{
    "valSum" : "855767000",
    "cik" : "1061165",
    "cusip" : "37940X102",
    "nameOfIssuer" : "GLOBAL PMTS INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "13",
    "totals" : "-508061000"
    },
{
    "valSum" : "852886000",
    "cik" : "1061165",
    "cusip" : "252131107",
    "nameOfIssuer" : "DEXCOM INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "14",
    "totals" : "14432000"
    },
{
    "valSum" : "852400000",
    "cik" : "1061165",
    "cusip" : "57667L107",
    "nameOfIssuer" : "MATCH GROUP INC NEW",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "15",
    "totals" : "56070000"
    },
{
    "valSum" : "739525000",
    "cik" : "1061165",
    "cusip" : "81762P102",
    "nameOfIssuer" : "SERVICENOW INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "16",
    "totals" : "73182000"
    },
{
    "valSum" : "725384000",
    "cik" : "1061165",
    "cusip" : "30744W107",
    "nameOfIssuer" : "FARFETCH LTD",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "17",
    "totals" : "210784000"
    },
{
    "valSum" : "723399000",
    "cik" : "1061165",
    "cusip" : "57636Q104",
    "nameOfIssuer" : "MASTERCARD INCORPORATED",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "18",
    "totals" : "-247263000"
    },
{
    "valSum" : "714105000",
    "cik" : "1061165",
    "cusip" : "852234103",
    "nameOfIssuer" : "SQUARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "19",
    "totals" : "-199858000"
    },
{
    "valSum" : "691788000",
    "cik" : "1061165",
    "cusip" : "45104G104",
    "nameOfIssuer" : "ICICI BANK LIMITED",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "20",
    "totals" : "691788000"
    },
{
    "valSum" : "631914000",
    "cik" : "1061165",
    "cusip" : "146869102",
    "nameOfIssuer" : "CARVANA CO",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "21",
    "totals" : "45457000"
    },
{
    "valSum" : "626921000",
    "cik" : "1061165",
    "cusip" : "G06242104",
    "nameOfIssuer" : "ATLASSIAN CORP PLC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "22",
    "totals" : "-173644000"
    },
{
    "valSum" : "545207000",
    "cik" : "1061165",
    "cusip" : "23804L103",
    "nameOfIssuer" : "DATADOG INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "23",
    "totals" : "-152743000"
    },
{
    "valSum" : "534985000",
    "cik" : "1061165",
    "cusip" : "98138H101",
    "nameOfIssuer" : "WORKDAY INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "24",
    "totals" : "534985000"
    },
{
    "valSum" : "449688000",
    "cik" : "1061165",
    "cusip" : "90040106",
    "nameOfIssuer" : "BILIBILI INC",
    "filingDate" : "2021-03-31",
    "name" : "Lone Pine",
    "rnk" : "25",
    "totals" : "-64986000"
    },
{
    "valSum" : "9824000",
    "cik" : "1092838",
    "cusip" : "00768Y453",
    "nameOfIssuer" : "ADVISORSHARES TR PURE US CANNA",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "1",
    "totals" : "9824000"
    },
{
    "valSum" : "8987000",
    "cik" : "1092838",
    "cusip" : "874054109",
    "nameOfIssuer" : "TAKE-TWO INTERACTIVE SOFTWARE",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "2",
    "totals" : "-1468000"
    },
{
    "valSum" : "8751000",
    "cik" : "1092838",
    "cusip" : "830566105",
    "nameOfIssuer" : "SKECHERS U S A INC CL A",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "3",
    "totals" : "-295000"
    },
{
    "valSum" : "8058000",
    "cik" : "1092838",
    "cusip" : "87900YAE3",
    "nameOfIssuer" : "TEEKAY CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "4",
    "totals" : "1005000"
    },
{
    "valSum" : "6948000",
    "cik" : "1092838",
    "cusip" : "92932M101",
    "nameOfIssuer" : "WNS HLDGS LTD SPON ADR",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "5",
    "totals" : "276000"
    },
{
    "valSum" : "6608000",
    "cik" : "1092838",
    "cusip" : "44891N109",
    "nameOfIssuer" : "IAC INTERACTIVECORP NEW COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "6",
    "totals" : "-219000"
    },
{
    "valSum" : "6343000",
    "cik" : "1092838",
    "cusip" : "210226AD8",
    "nameOfIssuer" : "CTO REALTY GROWTH INC",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "7",
    "totals" : "-1043000"
    },
{
    "valSum" : "5588000",
    "cik" : "1092838",
    "cusip" : "50187T106",
    "nameOfIssuer" : "LGI HOMES INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "8",
    "totals" : "2202000"
    },
{
    "valSum" : "5282000",
    "cik" : "1092838",
    "cusip" : "302301AF3",
    "nameOfIssuer" : "EZCORP INC",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "9",
    "totals" : "90000"
    },
{
    "valSum" : "4936000",
    "cik" : "1092838",
    "cusip" : "78469C103",
    "nameOfIssuer" : "SP PLUS CORP COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "10",
    "totals" : "2023000"
    },
{
    "valSum" : "4814000",
    "cik" : "1092838",
    "cusip" : "26210C104",
    "nameOfIssuer" : "DROPBOX INC CL A",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "11",
    "totals" : "3406000"
    },
{
    "valSum" : "4727000",
    "cik" : "1092838",
    "cusip" : "449253103",
    "nameOfIssuer" : "IAA INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "12",
    "totals" : "-130000"
    },
{
    "valSum" : "4589000",
    "cik" : "1092838",
    "cusip" : "122017106",
    "nameOfIssuer" : "BURLINGTON STORES INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "13",
    "totals" : "408000"
    },
{
    "valSum" : "4446000",
    "cik" : "1092838",
    "cusip" : "47233W109",
    "nameOfIssuer" : "JEFFERIES FINL GROUP INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "14",
    "totals" : "1253000"
    },
{
    "valSum" : "4408000",
    "cik" : "1092838",
    "cusip" : "90041L105",
    "nameOfIssuer" : "TURNING PT BRANDS INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "15",
    "totals" : "4408000"
    },
{
    "valSum" : "4365000",
    "cik" : "1092838",
    "cusip" : "90184L102",
    "nameOfIssuer" : "TWITTER INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "16",
    "totals" : "829000"
    },
{
    "valSum" : "4204000",
    "cik" : "1092838",
    "cusip" : "737630103",
    "nameOfIssuer" : "POTLATCHDELTIC CORPORATION COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "17",
    "totals" : "649000"
    },
{
    "valSum" : "3747000",
    "cik" : "1092838",
    "cusip" : "00508Y102",
    "nameOfIssuer" : "ACUITY BRANDS INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "18",
    "totals" : "1204000"
    },
{
    "valSum" : "3692000",
    "cik" : "1092838",
    "cusip" : "53069QAB5",
    "nameOfIssuer" : "LIBERTY LATIN AMERICA LTD",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "19",
    "totals" : "-810000"
    },
{
    "valSum" : "3617000",
    "cik" : "1092838",
    "cusip" : "90041LAE5",
    "nameOfIssuer" : "TURNING PT BRANDS INC",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "20",
    "totals" : "-2860000"
    },
{
    "valSum" : "3467000",
    "cik" : "1092838",
    "cusip" : "G1151C101",
    "nameOfIssuer" : "ACCENTURE PLC IRELAND SHS CLAS",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "21",
    "totals" : "177000"
    },
{
    "valSum" : "3431000",
    "cik" : "1092838",
    "cusip" : "84670702",
    "nameOfIssuer" : "BERKSHIRE HATHAWAY CLASS B",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "22",
    "totals" : "308000"
    },
{
    "valSum" : "3412000",
    "cik" : "1092838",
    "cusip" : "217204106",
    "nameOfIssuer" : "COPART INC COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "23",
    "totals" : "-1711000"
    },
{
    "valSum" : "3210000",
    "cik" : "1092838",
    "cusip" : "256677105",
    "nameOfIssuer" : "DOLLAR GEN CORP NEW COM",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "24",
    "totals" : "-1152000"
    },
{
    "valSum" : "3171000",
    "cik" : "1092838",
    "cusip" : "808524201",
    "nameOfIssuer" : "SCHWAB STRATEGIC TR US LRG CAP",
    "filingDate" : "2021-03-31",
    "name" : "Intrepid Capital",
    "rnk" : "25",
    "totals" : "-981000"
    },
{
    "valSum" : "175224000",
    "cik" : "1106500",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "1",
    "totals" : "5607000"
    },
{
    "valSum" : "129438000",
    "cik" : "1106500",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "2",
    "totals" : "-46178000"
    },
{
    "valSum" : "120032000",
    "cik" : "1106500",
    "cusip" : "37940X102",
    "nameOfIssuer" : "GLOBAL PMTS INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "3",
    "totals" : "45587000"
    },
{
    "valSum" : "65419000",
    "cik" : "1106500",
    "cusip" : "53814L108",
    "nameOfIssuer" : "LIVENT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "4",
    "totals" : "-5440000"
    },
{
    "valSum" : "64993000",
    "cik" : "1106500",
    "cusip" : "298736109",
    "nameOfIssuer" : "EURONET WORLDWIDE INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "5",
    "totals" : "-1411000"
    },
{
    "valSum" : "35437000",
    "cik" : "1106500",
    "cusip" : "268150109",
    "nameOfIssuer" : "DYNATRACE INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "6",
    "totals" : "34866000"
    },
{
    "valSum" : "15593000",
    "cik" : "1106500",
    "cusip" : "15677J108",
    "nameOfIssuer" : "CERIDIAN HCM HLDG INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "7",
    "totals" : "15593000"
    },
{
    "valSum" : "5384000",
    "cik" : "1106500",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "8",
    "totals" : "-283000"
    },
{
    "valSum" : "3772000",
    "cik" : "1106500",
    "cusip" : "742718109",
    "nameOfIssuer" : "PROCTER AND GAMBLE CO",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "9",
    "totals" : "1117000"
    },
{
    "valSum" : "3747000",
    "cik" : "1106500",
    "cusip" : "21036P108",
    "nameOfIssuer" : "CONSTELLATION BRANDS INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "10",
    "totals" : "1395000"
    },
{
    "valSum" : "3602000",
    "cik" : "1106500",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "11",
    "totals" : "261000"
    },
{
    "valSum" : "3492000",
    "cik" : "1106500",
    "cusip" : "32095101",
    "nameOfIssuer" : "AMPHENOL CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "12",
    "totals" : "3492000"
    },
{
    "valSum" : "3346000",
    "cik" : "1106500",
    "cusip" : "81762P102",
    "nameOfIssuer" : "SERVICENOW INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "13",
    "totals" : "258000"
    },
{
    "valSum" : "2667000",
    "cik" : "1106500",
    "cusip" : "00724F101",
    "nameOfIssuer" : "ADOBE SYSTEMS INCORPORATED",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "14",
    "totals" : "-139000"
    },
{
    "valSum" : "2591000",
    "cik" : "1106500",
    "cusip" : "518439104",
    "nameOfIssuer" : "LAUDER ESTEE COS INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "15",
    "totals" : "855000"
    },
{
    "valSum" : "2276000",
    "cik" : "1106500",
    "cusip" : "71377A103",
    "nameOfIssuer" : "PERFORMANCE FOOD GROUP CO",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "16",
    "totals" : "1671000"
    },
{
    "valSum" : "1793000",
    "cik" : "1106500",
    "cusip" : "52769106",
    "nameOfIssuer" : "AUTODESK INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "17",
    "totals" : "1793000"
    },
{
    "valSum" : "1653000",
    "cik" : "1106500",
    "cusip" : "278865100",
    "nameOfIssuer" : "ECOLAB INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "18",
    "totals" : "589000"
    },
{
    "valSum" : "1444000",
    "cik" : "1106500",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "19",
    "totals" : "787000"
    },
{
    "valSum" : "1142000",
    "cik" : "1106500",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "20",
    "totals" : "1142000"
    },
{
    "valSum" : "922000",
    "cik" : "1106500",
    "cusip" : "828806109",
    "nameOfIssuer" : "SIMON PPTY GROUP INC NEW",
    "filingDate" : "2021-03-31",
    "name" : "Joho",
    "rnk" : "21",
    "totals" : "922000"
    },
{
    "valSum" : "1214027000",
    "cik" : "1135730",
    "cusip" : "25809K105",
    "nameOfIssuer" : "DOORDASH INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "1",
    "totals" : "-35136000"
    },
{
    "valSum" : "1202063000",
    "cik" : "1135730",
    "cusip" : "833445109",
    "nameOfIssuer" : "SNOWFLAKE INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "2",
    "totals" : "57353000"
    },
{
    "valSum" : "1122274000",
    "cik" : "1135730",
    "cusip" : "254687106",
    "nameOfIssuer" : "DISNEY WALT CO",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "3",
    "totals" : "-880900000"
    },
{
    "valSum" : "1086004000",
    "cik" : "1135730",
    "cusip" : "88160R101",
    "nameOfIssuer" : "TESLA INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "4",
    "totals" : "-431602000"
    },
{
    "valSum" : "1028999000",
    "cik" : "1135730",
    "cusip" : "86771W105",
    "nameOfIssuer" : "SUNRUN INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "5",
    "totals" : "-267919000"
    },
{
    "valSum" : "880960000",
    "cik" : "1135730",
    "cusip" : "852234103",
    "nameOfIssuer" : "SQUARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "6",
    "totals" : "-454270000"
    },
{
    "valSum" : "821339000",
    "cik" : "1135730",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "7",
    "totals" : "140204000"
    },
{
    "valSum" : "727660000",
    "cik" : "1135730",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "8",
    "totals" : "-351809000"
    },
{
    "valSum" : "715535000",
    "cik" : "1135730",
    "cusip" : "81141R100",
    "nameOfIssuer" : "SEA LTD",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "9",
    "totals" : "89555000"
    },
{
    "valSum" : "713008000",
    "cik" : "1135730",
    "cusip" : "70450Y103",
    "nameOfIssuer" : "PAYPAL HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "10",
    "totals" : "-890445000"
    },
{
    "valSum" : "645006000",
    "cik" : "1135730",
    "cusip" : "98954M200",
    "nameOfIssuer" : "ZILLOW GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "11",
    "totals" : "-60040000"
    },
{
    "valSum" : "628106000",
    "cik" : "1135730",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "12",
    "totals" : "36660000"
    },
{
    "valSum" : "621642000",
    "cik" : "1135730",
    "cusip" : "67020Y100",
    "nameOfIssuer" : "NUANCE COMMUNICATIONS INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "13",
    "totals" : "-110908000"
    },
{
    "valSum" : "596559000",
    "cik" : "1135730",
    "cusip" : "98422D105",
    "nameOfIssuer" : "XPENG INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "14",
    "totals" : "152008000"
    },
{
    "valSum" : "486549000",
    "cik" : "1135730",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "15",
    "totals" : "-289500000"
    },
{
    "valSum" : "480711000",
    "cik" : "1135730",
    "cusip" : "00851L103",
    "nameOfIssuer" : "AGORA INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "16",
    "totals" : "82341000"
    },
{
    "valSum" : "378098000",
    "cik" : "1135730",
    "cusip" : "98980L101",
    "nameOfIssuer" : "ZOOM VIDEO COMMUNICATIONS IN",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "17",
    "totals" : "-470408000"
    },
{
    "valSum" : "336767000",
    "cik" : "1135730",
    "cusip" : "22788C105",
    "nameOfIssuer" : "CROWDSTRIKE HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "18",
    "totals" : "-502949000"
    },
{
    "valSum" : "319675000",
    "cik" : "1135730",
    "cusip" : "50202M102",
    "nameOfIssuer" : "LI AUTO INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "19",
    "totals" : "277150000"
    },
{
    "valSum" : "308117000",
    "cik" : "1135730",
    "cusip" : "40131M109",
    "nameOfIssuer" : "GUARDANT HEALTH INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "20",
    "totals" : "163959000"
    },
{
    "valSum" : "296790000",
    "cik" : "1135730",
    "cusip" : "03272L108",
    "nameOfIssuer" : "ANAPLAN INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "21",
    "totals" : "-310414000"
    },
{
    "valSum" : "285475000",
    "cik" : "1135730",
    "cusip" : "82509L107",
    "nameOfIssuer" : "SHOPIFY INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "22",
    "totals" : "-210052000"
    },
{
    "valSum" : "281490000",
    "cik" : "1135730",
    "cusip" : "501797104",
    "nameOfIssuer" : "L BRANDS INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "23",
    "totals" : "46073000"
    },
{
    "valSum" : "277264000",
    "cik" : "1135730",
    "cusip" : "37940X102",
    "nameOfIssuer" : "GLOBAL PMTS INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "24",
    "totals" : "-457166000"
    },
{
    "valSum" : "275646000",
    "cik" : "1135730",
    "cusip" : "72352L106",
    "nameOfIssuer" : "PINTEREST INC",
    "filingDate" : "2021-03-31",
    "name" : "Coatue",
    "rnk" : "25",
    "totals" : "-4708000"
    },
{
    "valSum" : "9221000",
    "cik" : "1136704",
    "cusip" : "23131L107",
    "nameOfIssuer" : "CURO GROUP HOLDINGS CORP",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "1",
    "totals" : "1594000"
    },
{
    "valSum" : "8559000",
    "cik" : "1136704",
    "cusip" : "05969A105",
    "nameOfIssuer" : "BANCORP INC DEL",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "2",
    "totals" : "2839000"
    },
{
    "valSum" : "6670000",
    "cik" : "1136704",
    "cusip" : "553810102",
    "nameOfIssuer" : "MVB FINL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "3",
    "totals" : "2734000"
    },
{
    "valSum" : "6386000",
    "cik" : "1136704",
    "cusip" : "29357K103",
    "nameOfIssuer" : "ENOVA INTL INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "4",
    "totals" : "6386000"
    },
{
    "valSum" : "5782000",
    "cik" : "1136704",
    "cusip" : "02005N100",
    "nameOfIssuer" : "ALLY FINL INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "5",
    "totals" : "1934000"
    },
{
    "valSum" : "5318000",
    "cik" : "1136704",
    "cusip" : "68268W103",
    "nameOfIssuer" : "ONEMAIN HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "6",
    "totals" : "791000"
    },
{
    "valSum" : "5301000",
    "cik" : "1136704",
    "cusip" : "89679",
    "nameOfIssuer" : "TRIUMPH BANCORP INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "7",
    "totals" : "2218000"
    },
{
    "valSum" : "3173000",
    "cik" : "1136704",
    "cusip" : "59100U108",
    "nameOfIssuer" : "META FINL GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "8",
    "totals" : "613000"
    },
{
    "valSum" : "2741000",
    "cik" : "1136704",
    "cusip" : "292554102",
    "nameOfIssuer" : "ENCORE CAP GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "9",
    "totals" : "866000"
    },
{
    "valSum" : "2585000",
    "cik" : "1136704",
    "cusip" : "G9078F107",
    "nameOfIssuer" : "TRITON INTL LTD",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "10",
    "totals" : "2585000"
    },
{
    "valSum" : "2571000",
    "cik" : "1136704",
    "cusip" : "89678F100",
    "nameOfIssuer" : "TRISTATE CAP HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "11",
    "totals" : "-1372000"
    },
{
    "valSum" : "2479000",
    "cik" : "1136704",
    "cusip" : "75902K106",
    "nameOfIssuer" : "REGIONAL MGMT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "12",
    "totals" : "-574000"
    },
{
    "valSum" : "2354000",
    "cik" : "1136704",
    "cusip" : "14040H105",
    "nameOfIssuer" : "CAPITAL ONE FINL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "13",
    "totals" : "525000"
    },
{
    "valSum" : "1987000",
    "cik" : "1136704",
    "cusip" : "675234108",
    "nameOfIssuer" : "OCEANFIRST FINL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "14",
    "totals" : "-6000"
    },
{
    "valSum" : "1868000",
    "cik" : "1136704",
    "cusip" : "46571Y107",
    "nameOfIssuer" : "I3 VERTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "15",
    "totals" : "1868000"
    },
{
    "valSum" : "1472000",
    "cik" : "1136704",
    "cusip" : "923451108",
    "nameOfIssuer" : "VERITEX HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "16",
    "totals" : "1472000"
    },
{
    "valSum" : "1241000",
    "cik" : "1136704",
    "cusip" : "72346Q104",
    "nameOfIssuer" : "PINNACLE FINL PARTNERS INC",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "17",
    "totals" : "-305000"
    },
{
    "valSum" : "1131000",
    "cik" : "1136704",
    "cusip" : "82669G104",
    "nameOfIssuer" : "SIGNATURE BK NEW YORK N Y",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "18",
    "totals" : "-222000"
    },
{
    "valSum" : "200000",
    "cik" : "1136704",
    "cusip" : "493267108",
    "nameOfIssuer" : "KEYCORP",
    "filingDate" : "2021-03-31",
    "name" : "Second Curve",
    "rnk" : "19",
    "totals" : "200000"
    },
{
    "valSum" : "64599000",
    "cik" : "1166309",
    "cusip" : "380237107",
    "nameOfIssuer" : "GODADDY INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "1",
    "totals" : "-14217000"
    },
{
    "valSum" : "53813000",
    "cik" : "1166309",
    "cusip" : "12769G100",
    "nameOfIssuer" : "CAESARS ENTERTAINMENT INC NE",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "2",
    "totals" : "-28642000"
    },
{
    "valSum" : "51707000",
    "cik" : "1166309",
    "cusip" : "737446104",
    "nameOfIssuer" : "POST HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "3",
    "totals" : "-3567000"
    },
{
    "valSum" : "50798000",
    "cik" : "1166309",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "4",
    "totals" : "-1146000"
    },
{
    "valSum" : "49204000",
    "cik" : "1166309",
    "cusip" : "H01301128",
    "nameOfIssuer" : "ALCON AG",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "5",
    "totals" : "-5063000"
    },
{
    "valSum" : "46030000",
    "cik" : "1166309",
    "cusip" : "778296103",
    "nameOfIssuer" : "ROSS STORES INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "6",
    "totals" : "-9208000"
    },
{
    "valSum" : "45361000",
    "cik" : "1166309",
    "cusip" : "617446448",
    "nameOfIssuer" : "MORGAN STANLEY",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "7",
    "totals" : "575000"
    },
{
    "valSum" : "43464000",
    "cik" : "1166309",
    "cusip" : "40412C101",
    "nameOfIssuer" : "HCA HEALTHCARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "8",
    "totals" : "7537000"
    },
{
    "valSum" : "39460000",
    "cik" : "1166309",
    "cusip" : "632307104",
    "nameOfIssuer" : "NATERA INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "9",
    "totals" : "-30607000"
    },
{
    "valSum" : "38933000",
    "cik" : "1166309",
    "cusip" : "83601L102",
    "nameOfIssuer" : "SOTERA HEALTH CO",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "10",
    "totals" : "38933000"
    },
{
    "valSum" : "38204000",
    "cik" : "1166309",
    "cusip" : "92343",
    "nameOfIssuer" : "VERISIGN INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "11",
    "totals" : "852000"
    },
{
    "valSum" : "34642000",
    "cik" : "1166309",
    "cusip" : "501889208",
    "nameOfIssuer" : "LKQ CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "12",
    "totals" : "-5009000"
    },
{
    "valSum" : "33911000",
    "cik" : "1166309",
    "cusip" : "16119P108",
    "nameOfIssuer" : "CHARTER COMMUNICATIONS INC N",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "13",
    "totals" : "-20546000"
    },
{
    "valSum" : "32076000",
    "cik" : "1166309",
    "cusip" : "35905A109",
    "nameOfIssuer" : "FRONTDOOR INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "14",
    "totals" : "8226000"
    },
{
    "valSum" : "32033000",
    "cik" : "1166309",
    "cusip" : "36165L108",
    "nameOfIssuer" : "GDS HLDGS LTD",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "15",
    "totals" : "-11032000"
    },
{
    "valSum" : "31980000",
    "cik" : "1166309",
    "cusip" : "02043Q107",
    "nameOfIssuer" : "ALNYLAM PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "16",
    "totals" : "-8783000"
    },
{
    "valSum" : "31890000",
    "cik" : "1166309",
    "cusip" : "46333X108",
    "nameOfIssuer" : "IRONWOOD PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "17",
    "totals" : "3791000"
    },
{
    "valSum" : "28289000",
    "cik" : "1166309",
    "cusip" : "03044L105",
    "nameOfIssuer" : "AMERICAN WELL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "18",
    "totals" : "-89058000"
    },
{
    "valSum" : "26946000",
    "cik" : "1166309",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "19",
    "totals" : "26946000"
    },
{
    "valSum" : "24864000",
    "cik" : "1166309",
    "cusip" : "45784P101",
    "nameOfIssuer" : "INSULET CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "20",
    "totals" : "24864000"
    },
{
    "valSum" : "23976000",
    "cik" : "1166309",
    "cusip" : "46513107",
    "nameOfIssuer" : "ATARA BIOTHERAPEUTICS INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "21",
    "totals" : "-5955000"
    },
{
    "valSum" : "22669000",
    "cik" : "1166309",
    "cusip" : "G21810109",
    "nameOfIssuer" : "CLARIVATE PLC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "22",
    "totals" : "22669000"
    },
{
    "valSum" : "19716000",
    "cik" : "1166309",
    "cusip" : "29786A106",
    "nameOfIssuer" : "ETSY INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "23",
    "totals" : "-13322000"
    },
{
    "valSum" : "18540000",
    "cik" : "1166309",
    "cusip" : "98978L204",
    "nameOfIssuer" : "ZOGENIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "24",
    "totals" : "18540000"
    },
{
    "valSum" : "17310000",
    "cik" : "1166309",
    "cusip" : "881624209",
    "nameOfIssuer" : "TEVA PHARMACEUTICAL INDS LTD",
    "filingDate" : "2021-03-31",
    "name" : "Bridger",
    "rnk" : "25",
    "totals" : "2835000"
    },
{
    "valSum" : "2147483647",
    "cik" : "1167483",
    "cusip" : "47215P106",
    "nameOfIssuer" : "JD.COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "1",
    "totals" : "0"
    },
{
    "valSum" : "2147483647",
    "cik" : "1167483",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "2",
    "totals" : "0"
    },
{
    "valSum" : "2147483647",
    "cik" : "1167483",
    "cusip" : "771049103",
    "nameOfIssuer" : "ROBLOX CORP",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "3",
    "totals" : "2147483647"
    },
{
    "valSum" : "2121913000",
    "cik" : "1167483",
    "cusip" : "81141R100",
    "nameOfIssuer" : "SEA LTD",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "4",
    "totals" : "285378000"
    },
{
    "valSum" : "1896965000",
    "cik" : "1167483",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "5",
    "totals" : "-99843000"
    },
{
    "valSum" : "1881424000",
    "cik" : "1167483",
    "cusip" : "722304102",
    "nameOfIssuer" : "PINDUODUO INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "6",
    "totals" : "-266059647"
    },
{
    "valSum" : "1641284000",
    "cik" : "1167483",
    "cusip" : "3768",
    "nameOfIssuer" : "APOLLO GLOBAL MGMT INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "7",
    "totals" : "-19799000"
    },
{
    "valSum" : "1637627000",
    "cik" : "1167483",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "8",
    "totals" : "-90602000"
    },
{
    "valSum" : "1577787000",
    "cik" : "1167483",
    "cusip" : "146869102",
    "nameOfIssuer" : "CARVANA CO",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "9",
    "totals" : "137455000"
    },
{
    "valSum" : "1375578000",
    "cik" : "1167483",
    "cusip" : "22788C105",
    "nameOfIssuer" : "CROWDSTRIKE HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "10",
    "totals" : "-220909000"
    },
{
    "valSum" : "1134992000",
    "cik" : "1167483",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "11",
    "totals" : "-276759000"
    },
{
    "valSum" : "1078237000",
    "cik" : "1167483",
    "cusip" : "81762P102",
    "nameOfIssuer" : "SERVICENOW INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "12",
    "totals" : "173881000"
    },
{
    "valSum" : "1042820000",
    "cik" : "1167483",
    "cusip" : "256163106",
    "nameOfIssuer" : "DOCUSIGN INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "13",
    "totals" : "648682000"
    },
{
    "valSum" : "1033119000",
    "cik" : "1167483",
    "cusip" : "893641100",
    "nameOfIssuer" : "TRANSDIGM GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "14",
    "totals" : "-54352000"
    },
{
    "valSum" : "1025382000",
    "cik" : "1167483",
    "cusip" : "98138H101",
    "nameOfIssuer" : "WORKDAY INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "15",
    "totals" : "36404000"
    },
{
    "valSum" : "1015311000",
    "cik" : "1167483",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "16",
    "totals" : "-26868000"
    },
{
    "valSum" : "990859000",
    "cik" : "1167483",
    "cusip" : "76680R206",
    "nameOfIssuer" : "RINGCENTRAL INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "17",
    "totals" : "-269735000"
    },
{
    "valSum" : "883528000",
    "cik" : "1167483",
    "cusip" : "70614W100",
    "nameOfIssuer" : "PELOTON INTERACTIVE INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "18",
    "totals" : "-308651000"
    },
{
    "valSum" : "852935000",
    "cik" : "1167483",
    "cusip" : "L8681T102",
    "nameOfIssuer" : "SPOTIFY TECHNOLOGY S A",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "19",
    "totals" : "-148947000"
    },
{
    "valSum" : "787226000",
    "cik" : "1167483",
    "cusip" : "98980L101",
    "nameOfIssuer" : "ZOOM VIDEO COMMUNICATIONS IN",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "20",
    "totals" : "299808000"
    },
{
    "valSum" : "761415000",
    "cik" : "1167483",
    "cusip" : "25809K105",
    "nameOfIssuer" : "DOORDASH INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "21",
    "totals" : "533586000"
    },
{
    "valSum" : "572669000",
    "cik" : "1167483",
    "cusip" : "82509L107",
    "nameOfIssuer" : "SHOPIFY INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "22",
    "totals" : "353279000"
    },
{
    "valSum" : "551024000",
    "cik" : "1167483",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "23",
    "totals" : "-20144000"
    },
{
    "valSum" : "530459000",
    "cik" : "1167483",
    "cusip" : "36118L106",
    "nameOfIssuer" : "FUTU HLDGS LTD",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "24",
    "totals" : "530459000"
    },
{
    "valSum" : "519608000",
    "cik" : "1167483",
    "cusip" : "G06242104",
    "nameOfIssuer" : "ATLASSIAN CORP PLC",
    "filingDate" : "2021-03-31",
    "name" : "Tiger Global",
    "rnk" : "25",
    "totals" : "-56975000"
    },
{
    "valSum" : "4643656647",
    "cik" : "1273087",
    "cusip" : "37833100",
    "nameOfIssuer" : "APPLE INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "1",
    "totals" : "-211647647"
    },
{
    "valSum" : "4416007294",
    "cik" : "1273087",
    "cusip" : "46090",
    "nameOfIssuer" : "INVESCO QQQ TR",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "2",
    "totals" : "753450647"
    },
{
    "valSum" : "4294967294",
    "cik" : "1273087",
    "cusip" : "464287655",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "3",
    "totals" : "-246934353"
    },
{
    "valSum" : "4191661647",
    "cik" : "1273087",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "4",
    "totals" : "-852962000"
    },
{
    "valSum" : "3944878000",
    "cik" : "1273087",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "5",
    "totals" : "653072000"
    },
{
    "valSum" : "3330617647",
    "cik" : "1273087",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "6",
    "totals" : "-1117455353"
    },
{
    "valSum" : "2429942000",
    "cik" : "1273087",
    "cusip" : "78462F103",
    "nameOfIssuer" : "SPDR S&P 500 ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "7",
    "totals" : "-1690131647"
    },
{
    "valSum" : "2253761000",
    "cik" : "1273087",
    "cusip" : "88160R101",
    "nameOfIssuer" : "TESLA INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "8",
    "totals" : "-460109647"
    },
{
    "valSum" : "2101035000",
    "cik" : "1273087",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "9",
    "totals" : "-549815000"
    },
{
    "valSum" : "1653052000",
    "cik" : "1273087",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "10",
    "totals" : "9698000"
    },
{
    "valSum" : "1446981000",
    "cik" : "1273087",
    "cusip" : "67066G104",
    "nameOfIssuer" : "NVIDIA CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "11",
    "totals" : "-910612000"
    },
{
    "valSum" : "1257693000",
    "cik" : "1273087",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "12",
    "totals" : "-199158000"
    },
{
    "valSum" : "1187662000",
    "cik" : "1273087",
    "cusip" : "81369Y803",
    "nameOfIssuer" : "SELECT SECTOR SPDR TR",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "13",
    "totals" : "426119000"
    },
{
    "valSum" : "1026581000",
    "cik" : "1273087",
    "cusip" : "81369Y605",
    "nameOfIssuer" : "SELECT SECTOR SPDR TR",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "14",
    "totals" : "479540000"
    },
{
    "valSum" : "874793000",
    "cik" : "1273087",
    "cusip" : "458140100",
    "nameOfIssuer" : "INTEL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "15",
    "totals" : "-500592000"
    },
{
    "valSum" : "838261000",
    "cik" : "1273087",
    "cusip" : "97023105",
    "nameOfIssuer" : "BOEING CO",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "16",
    "totals" : "479772000"
    },
{
    "valSum" : "766906000",
    "cik" : "1273087",
    "cusip" : "7903107",
    "nameOfIssuer" : "ADVANCED MICRO DEVICES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "17",
    "totals" : "109165000"
    },
{
    "valSum" : "757907000",
    "cik" : "1273087",
    "cusip" : "595112103",
    "nameOfIssuer" : "MICRON TECHNOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "18",
    "totals" : "168209000"
    },
{
    "valSum" : "737048000",
    "cik" : "1273087",
    "cusip" : "70450Y103",
    "nameOfIssuer" : "PAYPAL HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "19",
    "totals" : "249241000"
    },
{
    "valSum" : "632164000",
    "cik" : "1273087",
    "cusip" : "82509L107",
    "nameOfIssuer" : "SHOPIFY INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "20",
    "totals" : "597198000"
    },
{
    "valSum" : "617739000",
    "cik" : "1273087",
    "cusip" : "17275R102",
    "nameOfIssuer" : "CISCO SYS INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "21",
    "totals" : "97033000"
    },
{
    "valSum" : "608606000",
    "cik" : "1273087",
    "cusip" : "464288513",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "22",
    "totals" : "-554530000"
    },
{
    "valSum" : "605893000",
    "cik" : "1273087",
    "cusip" : "46625H100",
    "nameOfIssuer" : "JPMORGAN CHASE & CO",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "23",
    "totals" : "-57528000"
    },
{
    "valSum" : "576266000",
    "cik" : "1273087",
    "cusip" : "02079K107",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "24",
    "totals" : "-185393000"
    },
{
    "valSum" : "569282000",
    "cik" : "1273087",
    "cusip" : "79466L302",
    "nameOfIssuer" : "SALESFORCE COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Millennium",
    "rnk" : "25",
    "totals" : "-341792000"
    },
{
    "valSum" : "42101000",
    "cik" : "1280493",
    "cusip" : "78463V107",
    "nameOfIssuer" : "SPDR GOLD TR",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "1",
    "totals" : "42101000"
    },
{
    "valSum" : "39337000",
    "cik" : "1280493",
    "cusip" : "11532108",
    "nameOfIssuer" : "ALAMOS GOLD INC NEW",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "2",
    "totals" : "-4601000"
    },
{
    "valSum" : "31080000",
    "cik" : "1280493",
    "cusip" : "74139C102",
    "nameOfIssuer" : "PRETIUM RES INC",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "3",
    "totals" : "7923000"
    },
{
    "valSum" : "27004000",
    "cik" : "1280493",
    "cusip" : "36352H100",
    "nameOfIssuer" : "GALIANO GOLD INC",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "4",
    "totals" : "368000"
    },
{
    "valSum" : "24792000",
    "cik" : "1280493",
    "cusip" : "68827L101",
    "nameOfIssuer" : "OSISKO GOLD ROYALTIES LTD",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "5",
    "totals" : "-3709000"
    },
{
    "valSum" : "20950000",
    "cik" : "1280493",
    "cusip" : "380738104",
    "nameOfIssuer" : "GOLD STD VENTURES CORP",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "6",
    "totals" : "8663000"
    },
{
    "valSum" : "20104000",
    "cik" : "1280493",
    "cusip" : "852066208",
    "nameOfIssuer" : "SPROTT INC",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "7",
    "totals" : "4752000"
    },
{
    "valSum" : "19740000",
    "cik" : "1280493",
    "cusip" : "927926303",
    "nameOfIssuer" : "VISTA GOLD CORP",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "8",
    "totals" : "-372000"
    },
{
    "valSum" : "14125000",
    "cik" : "1280493",
    "cusip" : "11777Q209",
    "nameOfIssuer" : "B2GOLD CORP",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "9",
    "totals" : "-4237000"
    },
{
    "valSum" : "11981000",
    "cik" : "1280493",
    "cusip" : "49741",
    "nameOfIssuer" : "KIRKLAND LAKE GOLD LTD",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "10",
    "totals" : "-2665000"
    },
{
    "valSum" : "10417000",
    "cik" : "1280493",
    "cusip" : "828363101",
    "nameOfIssuer" : "SILVERCREST METALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "11",
    "totals" : "10417000"
    },
{
    "valSum" : "10324000",
    "cik" : "1280493",
    "cusip" : "784730103",
    "nameOfIssuer" : "SSR MNG INC",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "12",
    "totals" : "-4215000"
    },
{
    "valSum" : "7638000",
    "cik" : "1280493",
    "cusip" : "714266103",
    "nameOfIssuer" : "PERPETUA RESOURCES CORP",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "13",
    "totals" : "7638000"
    },
{
    "valSum" : "1489000",
    "cik" : "1280493",
    "cusip" : "450913108",
    "nameOfIssuer" : "IAMGOLD CORP",
    "filingDate" : "2021-03-31",
    "name" : "Sun Valley Gold",
    "rnk" : "14",
    "totals" : "1489000"
    },
{
    "valSum" : "227842000",
    "cik" : "1294571",
    "cusip" : "464287507",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "1",
    "totals" : "-2057000"
    },
{
    "valSum" : "195040000",
    "cik" : "1294571",
    "cusip" : "464287622",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "2",
    "totals" : "9663000"
    },
{
    "valSum" : "162053000",
    "cik" : "1294571",
    "cusip" : "464287655",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "3",
    "totals" : "-5386000"
    },
{
    "valSum" : "130215000",
    "cik" : "1294571",
    "cusip" : "464287804",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "4",
    "totals" : "-7512000"
    },
{
    "valSum" : "77003000",
    "cik" : "1294571",
    "cusip" : "922908629",
    "nameOfIssuer" : "VANGUARD INDEX FDS",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "5",
    "totals" : "-5117000"
    },
{
    "valSum" : "75907000",
    "cik" : "1294571",
    "cusip" : "922908553",
    "nameOfIssuer" : "VANGUARD INDEX FDS",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "6",
    "totals" : "-2991000"
    },
{
    "valSum" : "61445000",
    "cik" : "1294571",
    "cusip" : "922908751",
    "nameOfIssuer" : "VANGUARD INDEX FDS",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "7",
    "totals" : "-1226000"
    },
{
    "valSum" : "51564000",
    "cik" : "1294571",
    "cusip" : "464287499",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "8",
    "totals" : "-3313000"
    },
{
    "valSum" : "43810000",
    "cik" : "1294571",
    "cusip" : "922042858",
    "nameOfIssuer" : "VANGUARD INTL EQUITY INDEX F",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "9",
    "totals" : "128000"
    },
{
    "valSum" : "41923000",
    "cik" : "1294571",
    "cusip" : "922908363",
    "nameOfIssuer" : "VANGUARD INDEX FDS",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "10",
    "totals" : "78000"
    },
{
    "valSum" : "38452000",
    "cik" : "1294571",
    "cusip" : "922908637",
    "nameOfIssuer" : "VANGUARD INDEX FDS",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "11",
    "totals" : "1772000"
    },
{
    "valSum" : "16445000",
    "cik" : "1294571",
    "cusip" : "922042874",
    "nameOfIssuer" : "VANGUARD INTL EQUITY INDEX F",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "12",
    "totals" : "-528000"
    },
{
    "valSum" : "11140000",
    "cik" : "1294571",
    "cusip" : "808524847",
    "nameOfIssuer" : "SCHWAB STRATEGIC TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "13",
    "totals" : "138000"
    },
{
    "valSum" : "7990000",
    "cik" : "1294571",
    "cusip" : "92189F403",
    "nameOfIssuer" : "VANECK VECTORS ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "14",
    "totals" : "517000"
    },
{
    "valSum" : "7935000",
    "cik" : "1294571",
    "cusip" : "46434G822",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "15",
    "totals" : "-137000"
    },
{
    "valSum" : "7920000",
    "cik" : "1294571",
    "cusip" : "464286400",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "16",
    "totals" : "213000"
    },
{
    "valSum" : "7885000",
    "cik" : "1294571",
    "cusip" : "464286871",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "17",
    "totals" : "-64000"
    },
{
    "valSum" : "7844000",
    "cik" : "1294571",
    "cusip" : "464286509",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "18",
    "totals" : "265000"
    },
{
    "valSum" : "7827000",
    "cik" : "1294571",
    "cusip" : "46434G772",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "19",
    "totals" : "-119000"
    },
{
    "valSum" : "7739000",
    "cik" : "1294571",
    "cusip" : "464287184",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "20",
    "totals" : "321000"
    },
{
    "valSum" : "7733000",
    "cik" : "1294571",
    "cusip" : "464286103",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "21",
    "totals" : "-230000"
    },
{
    "valSum" : "7520000",
    "cik" : "1294571",
    "cusip" : "464286772",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "22",
    "totals" : "319000"
    },
{
    "valSum" : "7167000",
    "cik" : "1294571",
    "cusip" : "464286822",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "23",
    "totals" : "158000"
    },
{
    "valSum" : "6675000",
    "cik" : "1294571",
    "cusip" : "97717W422",
    "nameOfIssuer" : "WISDOMTREE TR",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "24",
    "totals" : "-253000"
    },
{
    "valSum" : "5882000",
    "cik" : "1294571",
    "cusip" : "464286749",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Millburn Ridgefield",
    "rnk" : "25",
    "totals" : "-48000"
    },
{
    "valSum" : "161759000",
    "cik" : "1317679",
    "cusip" : "952845105",
    "nameOfIssuer" : "WEST FRASER TIMBER CO LTD",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "1",
    "totals" : "161759000"
    },
{
    "valSum" : "161331000",
    "cik" : "1317679",
    "cusip" : "767204100",
    "nameOfIssuer" : "RIO TINTO PLC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "2",
    "totals" : "17938000"
    },
{
    "valSum" : "102002000",
    "cik" : "1317679",
    "cusip" : "412822108",
    "nameOfIssuer" : "HARLEY DAVIDSON INC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "3",
    "totals" : "-14544000"
    },
{
    "valSum" : "69840000",
    "cik" : "1317679",
    "cusip" : "62944T105",
    "nameOfIssuer" : "NVR INC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "4",
    "totals" : "-13883000"
    },
{
    "valSum" : "58592000",
    "cik" : "1317679",
    "cusip" : "25179M103",
    "nameOfIssuer" : "DEVON ENERGY CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "5",
    "totals" : "25286000"
    },
{
    "valSum" : "48535000",
    "cik" : "1317679",
    "cusip" : "546347105",
    "nameOfIssuer" : "LOUISIANA PAC CORP",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "6",
    "totals" : "7791000"
    },
{
    "valSum" : "44052000",
    "cik" : "1317679",
    "cusip" : "536797103",
    "nameOfIssuer" : "LITHIA MTRS INC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "7",
    "totals" : "18233000"
    },
{
    "valSum" : "43799000",
    "cik" : "1317679",
    "cusip" : "904677200",
    "nameOfIssuer" : "UNIFI INC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "8",
    "totals" : "15606000"
    },
{
    "valSum" : "41015000",
    "cik" : "1317679",
    "cusip" : "Y1968P121",
    "nameOfIssuer" : "DANAOS CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "9",
    "totals" : "35456000"
    },
{
    "valSum" : "39446000",
    "cik" : "1317679",
    "cusip" : "723787107",
    "nameOfIssuer" : "PIONEER NAT RES CO",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "10",
    "totals" : "39446000"
    },
{
    "valSum" : "38387000",
    "cik" : "1317679",
    "cusip" : "G0084W101",
    "nameOfIssuer" : "ADIENT PLC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "11",
    "totals" : "22569000"
    },
{
    "valSum" : "36611000",
    "cik" : "1317679",
    "cusip" : "910047109",
    "nameOfIssuer" : "UNITED AIRLS HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "12",
    "totals" : "28401000"
    },
{
    "valSum" : "36183000",
    "cik" : "1317679",
    "cusip" : "G9087Q102",
    "nameOfIssuer" : "TRONOX HOLDINGS PLC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "13",
    "totals" : "22676000"
    },
{
    "valSum" : "35676000",
    "cik" : "1317679",
    "cusip" : "343412102",
    "nameOfIssuer" : "FLUOR CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "14",
    "totals" : "15092000"
    },
{
    "valSum" : "35535000",
    "cik" : "1317679",
    "cusip" : "42809H107",
    "nameOfIssuer" : "HESS CORP",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "15",
    "totals" : "27614000"
    },
{
    "valSum" : "30710000",
    "cik" : "1317679",
    "cusip" : "N53745100",
    "nameOfIssuer" : "LYONDELLBASELL INDUSTRIES N",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "16",
    "totals" : "30710000"
    },
{
    "valSum" : "28391000",
    "cik" : "1317679",
    "cusip" : "31428X106",
    "nameOfIssuer" : "FEDEX CORP",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "17",
    "totals" : "-1033000"
    },
{
    "valSum" : "27899000",
    "cik" : "1317679",
    "cusip" : "Y8162K204",
    "nameOfIssuer" : "STAR BULK CARRIERS CORP.",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "18",
    "totals" : "10813000"
    },
{
    "valSum" : "26649000",
    "cik" : "1317679",
    "cusip" : "499049104",
    "nameOfIssuer" : "KNIGHT-SWIFT TRANSN HLDGS IN",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "19",
    "totals" : "-21541000"
    },
{
    "valSum" : "26166000",
    "cik" : "1317679",
    "cusip" : "806857108",
    "nameOfIssuer" : "SCHLUMBERGER LTD",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "20",
    "totals" : "-5489000"
    },
{
    "valSum" : "25719000",
    "cik" : "1317679",
    "cusip" : "82575P107",
    "nameOfIssuer" : "SIBANYE STILLWATER LTD",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "21",
    "totals" : "-3685000"
    },
{
    "valSum" : "24969000",
    "cik" : "1317679",
    "cusip" : "91912",
    "nameOfIssuer" : "VALE S A",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "22",
    "totals" : "1581000"
    },
{
    "valSum" : "24199000",
    "cik" : "1317679",
    "cusip" : "874054109",
    "nameOfIssuer" : "TAKE-TWO INTERACTIVE SOFTWAR",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "23",
    "totals" : "8192000"
    },
{
    "valSum" : "23682000",
    "cik" : "1317679",
    "cusip" : "M9T951109",
    "nameOfIssuer" : "ZIM INTEGRATED SHIPPING SERV",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "24",
    "totals" : "23682000"
    },
{
    "valSum" : "22520000",
    "cik" : "1317679",
    "cusip" : "43283X105",
    "nameOfIssuer" : "HILTON GRAND VACATIONS INC",
    "filingDate" : "2021-03-31",
    "name" : "Impala",
    "rnk" : "25",
    "totals" : "-4029000"
    },
{
    "valSum" : "467173000",
    "cik" : "1318757",
    "cusip" : "464288513",
    "nameOfIssuer" : "April 21 Calls on HYG US at 87, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "1",
 "totals" : "190764000"
 },
{
    "valSum" : "357988000",
    "cik" : "1318757",
    "cusip" : "464287655",
    "nameOfIssuer" : "August 21 Calls on IWM US at 225, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "2",
 "totals" : "24211000"
 },
{
    "valSum" : "324949000",
    "cik" : "1318757",
    "cusip" : "90572207",
    "nameOfIssuer" : "BIO-RAD LABS-A",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "3",
    "totals" : "109606000"
    },
{
    "valSum" : "319625000",
    "cik" : "1318757",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON.COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "4",
    "totals" : "84614000"
    },
{
    "valSum" : "318213000",
    "cik" : "1318757",
    "cusip" : "879369106",
    "nameOfIssuer" : "TELEFLEX INC",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "5",
    "totals" : "-45169000"
    },
{
    "valSum" : "304927000",
    "cik" : "1318757",
    "cusip" : "594918104",
    "nameOfIssuer" : "April 21 Puts on MSFT US at 235, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "6",
 "totals" : "59583000"
 },
{
    "valSum" : "272268000",
    "cik" : "1318757",
    "cusip" : "92556H206",
    "nameOfIssuer" : "April 21 Puts on VIAC US at 100, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "7",
 "totals" : "272268000"
 },
{
    "valSum" : "270608000",
    "cik" : "1318757",
    "cusip" : "98978V103",
    "nameOfIssuer" : "ZOETIS INC",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "8",
    "totals" : "-203532000"
    },
{
    "valSum" : "265790000",
    "cik" : "1318757",
    "cusip" : "159864107",
    "nameOfIssuer" : "CHARLES RIVER LA",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "9",
    "totals" : "52682000"
    },
{
    "valSum" : "238745000",
    "cik" : "1318757",
    "cusip" : "464287242",
    "nameOfIssuer" : "April 21 Calls on LQD US at 130, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "10",
 "totals" : "174479000"
 },
{
    "valSum" : "201762000",
    "cik" : "1318757",
    "cusip" : "78462F103",
    "nameOfIssuer" : "August 21 Puts on SPY US at 390, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "11",
 "totals" : "-393010000"
 },
{
    "valSum" : "200951000",
    "cik" : "1318757",
    "cusip" : "883556102",
    "nameOfIssuer" : "April 21 Puts on TMO US at 460, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "12",
 "totals" : "-203062000"
 },
{
    "valSum" : "199220000",
    "cik" : "1318757",
    "cusip" : "37833100",
    "nameOfIssuer" : "APPLE INC",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "13",
    "totals" : "55722000"
    },
{
    "valSum" : "195788000",
    "cik" : "1318757",
    "cusip" : "46090",
    "nameOfIssuer" : "INVESCO QQQ TRUS",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "14",
    "totals" : "29160000"
    },
{
    "valSum" : "189771000",
    "cik" : "1318757",
    "cusip" : "G11196105",
    "nameOfIssuer" : "BIOHAVEN PHARMAC",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "15",
    "totals" : "-29350000"
    },
{
    "valSum" : "183471000",
    "cik" : "1318757",
    "cusip" : "759916109",
    "nameOfIssuer" : "REPLIGEN CORP",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "16",
    "totals" : "-100386000"
    },
{
    "valSum" : "177848000",
    "cik" : "1318757",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GRP-ADR",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "17",
    "totals" : "20589000"
    },
{
    "valSum" : "174755000",
    "cik" : "1318757",
    "cusip" : "89400J107",
    "nameOfIssuer" : "TRANSUNION",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "18",
    "totals" : "-41027000"
    },
{
    "valSum" : "159742000",
    "cik" : "1318757",
    "cusip" : "30744W107",
    "nameOfIssuer" : "FARFETCH LTD-A",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "19",
    "totals" : "157406000"
    },
{
    "valSum" : "148631000",
    "cik" : "1318757",
    "cusip" : "88034P109",
    "nameOfIssuer" : "TENCENT MUSI-ADR",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "20",
    "totals" : "148631000"
    },
{
    "valSum" : "148259000",
    "cik" : "1318757",
    "cusip" : "56752108",
    "nameOfIssuer" : "April 21 Calls on BIDU US at 220, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "21",
 "totals" : "131165000"
 },
{
    "valSum" : "140066000",
    "cik" : "1318757",
    "cusip" : "88160R101",
    "nameOfIssuer" : "April 21 Calls on TSLA US at 1000, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "22",
 "totals" : "123558000"
 },
{
    "valSum" : "133264000",
    "cik" : "1318757",
    "cusip" : "464288281",
    "nameOfIssuer" : "April 21 Calls on EMB US at 116, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "23",
 "totals" : "91262000"
 },
{
    "valSum" : "119209000",
    "cik" : "1318757",
    "cusip" : "632307104",
    "nameOfIssuer" : "NATERA INC",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "24",
    "totals" : "28520000"
    },
{
    "valSum" : "115357000",
    "cik" : "1318757",
    "cusip" : "458140100",
    "nameOfIssuer" : "April 21 Calls on INTC US at 67.5, American",
    "filingDate" : "2021-03-31",
    "name" : "Marshall Wace",
    "rnk" : "25",
 "totals" : "109953000"
 },
{
    "valSum" : "183400000",
    "cik" : "1343781",
    "cusip" : "92532F100",
    "nameOfIssuer" : "VERTEX PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "1",
    "totals" : "45545000"
    },
{
    "valSum" : "158829000",
    "cik" : "1343781",
    "cusip" : "G46188101",
    "nameOfIssuer" : "HORIZON THERAPEUTICS PUB L",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "2",
    "totals" : "-25369000"
    },
{
    "valSum" : "121610000",
    "cik" : "1343781",
    "cusip" : "98956P102",
    "nameOfIssuer" : "ZIMMER BIOMET HOLDINGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "3",
    "totals" : "36647000"
    },
{
    "valSum" : "120569000",
    "cik" : "1343781",
    "cusip" : "235851102",
    "nameOfIssuer" : "DANAHER CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "4",
    "totals" : "120569000"
    },
{
    "valSum" : "105395000",
    "cik" : "1343781",
    "cusip" : "444859102",
    "nameOfIssuer" : "HUMANA INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "5",
    "totals" : "15061000"
    },
{
    "valSum" : "94044000",
    "cik" : "1343781",
    "cusip" : "G5960L103",
    "nameOfIssuer" : "MEDTRONIC PLC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "6",
    "totals" : "23274000"
    },
{
    "valSum" : "92996000",
    "cik" : "1343781",
    "cusip" : "45337C102",
    "nameOfIssuer" : "INCYTE CORP",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "7",
    "totals" : "91297000"
    },
{
    "valSum" : "92318000",
    "cik" : "1343781",
    "cusip" : "58155Q103",
    "nameOfIssuer" : "MCKESSON CORP",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "8",
    "totals" : "18785000"
    },
{
    "valSum" : "85989000",
    "cik" : "1343781",
    "cusip" : "56600D107",
    "nameOfIssuer" : "MARAVAI LIFESCIENCES HLDGS I",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "9",
    "totals" : "-1940000"
    },
{
    "valSum" : "82335000",
    "cik" : "1343781",
    "cusip" : "29261A100",
    "nameOfIssuer" : "ENCOMPASS HEALTH CORP",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "10",
    "totals" : "82335000"
    },
{
    "valSum" : "79162000",
    "cik" : "1343781",
    "cusip" : "00847X104",
    "nameOfIssuer" : "AGIOS PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "11",
    "totals" : "35959000"
    },
{
    "valSum" : "78938000",
    "cik" : "1343781",
    "cusip" : "00287Y109",
    "nameOfIssuer" : "ABBVIE INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "12",
    "totals" : "-12531000"
    },
{
    "valSum" : "78159000",
    "cik" : "1343781",
    "cusip" : "40412C101",
    "nameOfIssuer" : "HCA HEALTHCARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "13",
    "totals" : "-38812000"
    },
{
    "valSum" : "77582000",
    "cik" : "1343781",
    "cusip" : "46266C105",
    "nameOfIssuer" : "IQVIA HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "14",
    "totals" : "-66347000"
    },
{
    "valSum" : "68869000",
    "cik" : "1343781",
    "cusip" : "3073",
    "nameOfIssuer" : "AMERISOURCEBERGEN CORP",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "15",
    "totals" : "68869000"
    },
{
    "valSum" : "68430000",
    "cik" : "1343781",
    "cusip" : "71601V105",
    "nameOfIssuer" : "PETCO HEALTH & WELLNESS CO I",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "16",
    "totals" : "68430000"
    },
{
    "valSum" : "66435000",
    "cik" : "1343781",
    "cusip" : "98978V103",
    "nameOfIssuer" : "ZOETIS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "17",
    "totals" : "66435000"
    },
{
    "valSum" : "66404000",
    "cik" : "1343781",
    "cusip" : "95040Q104",
    "nameOfIssuer" : "WELLTOWER INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "18",
    "totals" : "43327000"
    },
{
    "valSum" : "61334000",
    "cik" : "1343781",
    "cusip" : "92276F100",
    "nameOfIssuer" : "VENTAS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "19",
    "totals" : "29049000"
    },
{
    "valSum" : "58563000",
    "cik" : "1343781",
    "cusip" : "29415F104",
    "nameOfIssuer" : "ENVISTA HOLDINGS CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "20",
    "totals" : "23508000"
    },
{
    "valSum" : "51073000",
    "cik" : "1343781",
    "cusip" : "252131107",
    "nameOfIssuer" : "DEXCOM INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "21",
    "totals" : "51073000"
    },
{
    "valSum" : "49695000",
    "cik" : "1343781",
    "cusip" : "09058V103",
    "nameOfIssuer" : "BIOCRYST PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "22",
    "totals" : "49695000"
    },
{
    "valSum" : "45407000",
    "cik" : "1343781",
    "cusip" : "101137107",
    "nameOfIssuer" : "BOSTON SCIENTIFIC CORP",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "23",
    "totals" : "45407000"
    },
{
    "valSum" : "43466000",
    "cik" : "1343781",
    "cusip" : "216648402",
    "nameOfIssuer" : "COOPER COS INC",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "24",
    "totals" : "-82108000"
    },
{
    "valSum" : "40822000",
    "cik" : "1343781",
    "cusip" : "N72482123",
    "nameOfIssuer" : "QIAGEN NV",
    "filingDate" : "2021-03-31",
    "name" : "Healthcor",
    "rnk" : "25",
    "totals" : "40822000"
    },
{
    "valSum" : "1243762000",
    "cik" : "1350694",
    "cusip" : "78462F103",
    "nameOfIssuer" : "SPDR S&P 500 ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "1",
    "totals" : "-134525000"
    },
{
    "valSum" : "577224000",
    "cik" : "1350694",
    "cusip" : "922042858",
    "nameOfIssuer" : "VANGUARD INTL EQUITY INDEX F",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "2",
    "totals" : "-82580000"
    },
{
    "valSum" : "487757000",
    "cik" : "1350694",
    "cusip" : "931142103",
    "nameOfIssuer" : "WALMART INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "3",
    "totals" : "43978000"
    },
{
    "valSum" : "435899000",
    "cik" : "1350694",
    "cusip" : "742718109",
    "nameOfIssuer" : "PROCTER AND GAMBLE CO",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "4",
    "totals" : "60854000"
    },
{
    "valSum" : "318039000",
    "cik" : "1350694",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "5",
    "totals" : "-54445000"
    },
{
    "valSum" : "298699000",
    "cik" : "1350694",
    "cusip" : "191216100",
    "nameOfIssuer" : "COCA COLA CO",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "6",
    "totals" : "50273000"
    },
{
    "valSum" : "281021000",
    "cik" : "1350694",
    "cusip" : "478160104",
    "nameOfIssuer" : "JOHNSON & JOHNSON",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "7",
    "totals" : "49709000"
    },
{
    "valSum" : "277114000",
    "cik" : "1350694",
    "cusip" : "78463V107",
    "nameOfIssuer" : "SPDR GOLD TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "8",
    "totals" : "-255305000"
    },
{
    "valSum" : "252980000",
    "cik" : "1350694",
    "cusip" : "713448108",
    "nameOfIssuer" : "PEPSICO INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "9",
    "totals" : "33839000"
    },
{
    "valSum" : "242530000",
    "cik" : "1350694",
    "cusip" : "46434G103",
    "nameOfIssuer" : "ISHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "10",
    "totals" : "-91415000"
    },
{
    "valSum" : "210780000",
    "cik" : "1350694",
    "cusip" : "580135101",
    "nameOfIssuer" : "MCDONALDS CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "11",
    "totals" : "45515000"
    },
{
    "valSum" : "198439000",
    "cik" : "1350694",
    "cusip" : "22160K105",
    "nameOfIssuer" : "COSTCO WHSL CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "12",
    "totals" : "15149000"
    },
{
    "valSum" : "176801000",
    "cik" : "1350694",
    "cusip" : "464287184",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "13",
    "totals" : "12186000"
    },
{
    "valSum" : "168875000",
    "cik" : "1350694",
    "cusip" : "464287200",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "14",
    "totals" : "-131842000"
    },
{
    "valSum" : "152976000",
    "cik" : "1350694",
    "cusip" : "855244109",
    "nameOfIssuer" : "STARBUCKS CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "15",
    "totals" : "25347000"
    },
{
    "valSum" : "149408000",
    "cik" : "1350694",
    "cusip" : "722304102",
    "nameOfIssuer" : "PINDUODUO INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "16",
    "totals" : "-103261000"
    },
{
    "valSum" : "145952000",
    "cik" : "1350694",
    "cusip" : "46429B671",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "17",
    "totals" : "12478000"
    },
{
    "valSum" : "143754000",
    "cik" : "1350694",
    "cusip" : "464285105",
    "nameOfIssuer" : "ISHARES GOLD TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "18",
    "totals" : "-136987000"
    },
{
    "valSum" : "142714000",
    "cik" : "1350694",
    "cusip" : "464287242",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "19",
    "totals" : "-9395000"
    },
{
    "valSum" : "136766000",
    "cik" : "1350694",
    "cusip" : "518439104",
    "nameOfIssuer" : "LAUDER ESTEE COS INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "20",
    "totals" : "36438000"
    },
{
    "valSum" : "130440000",
    "cik" : "1350694",
    "cusip" : "2824100",
    "nameOfIssuer" : "ABBOTT LABS",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "21",
    "totals" : "30484000"
    },
{
    "valSum" : "113203000",
    "cik" : "1350694",
    "cusip" : "87612",
    "nameOfIssuer" : "TARGET CORP",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "22",
    "totals" : "18064000"
    },
{
    "valSum" : "107178000",
    "cik" : "1350694",
    "cusip" : "609207105",
    "nameOfIssuer" : "MONDELEZ INTL INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "23",
    "totals" : "21098000"
    },
{
    "valSum" : "104624000",
    "cik" : "1350694",
    "cusip" : "47215P106",
    "nameOfIssuer" : "JD.COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "24",
    "totals" : "-46036000"
    },
{
    "valSum" : "99692000",
    "cik" : "1350694",
    "cusip" : "235851102",
    "nameOfIssuer" : "DANAHER CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Bridgewater",
    "rnk" : "25",
    "totals" : "7114000"
    },
{
    "valSum" : "58657000",
    "cik" : "1389507",
    "cusip" : "670002401",
    "nameOfIssuer" : "NOVAVAX INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "1",
    "totals" : "3610000"
    },
{
    "valSum" : "55498000",
    "cik" : "1389507",
    "cusip" : "24790A101",
    "nameOfIssuer" : "DENBURY INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "2",
    "totals" : "55498000"
    },
{
    "valSum" : "52636000",
    "cik" : "1389507",
    "cusip" : "92537N108",
    "nameOfIssuer" : "VERTIV HOLDINGS CO",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "3",
    "totals" : "2226000"
    },
{
    "valSum" : "51314000",
    "cik" : "1389507",
    "cusip" : "458140100",
    "nameOfIssuer" : "INTEL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "4",
    "totals" : "-13172000"
    },
{
    "valSum" : "44926000",
    "cik" : "1389507",
    "cusip" : "337738108",
    "nameOfIssuer" : "FISERV INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "5",
    "totals" : "-16092000"
    },
{
    "valSum" : "43380000",
    "cik" : "1389507",
    "cusip" : "98973P101",
    "nameOfIssuer" : "ZIOPHARM ONCOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "6",
    "totals" : "13160000"
    },
{
    "valSum" : "37199000",
    "cik" : "1389507",
    "cusip" : "595017104",
    "nameOfIssuer" : "MICROCHIP TECHNOLOGY INC.",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "7",
    "totals" : "1723000"
    },
{
    "valSum" : "34341000",
    "cik" : "1389507",
    "cusip" : "928881101",
    "nameOfIssuer" : "VONTIER CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "8",
    "totals" : "19445000"
    },
{
    "valSum" : "22915000",
    "cik" : "1389507",
    "cusip" : "212873103",
    "nameOfIssuer" : "CONX CORP",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "9",
    "totals" : "22915000"
    },
{
    "valSum" : "18671000",
    "cik" : "1389507",
    "cusip" : "595112103",
    "nameOfIssuer" : "MICRON TECHNOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "10",
    "totals" : "14411000"
    },
{
    "valSum" : "17920000",
    "cik" : "1389507",
    "cusip" : "38141G104",
    "nameOfIssuer" : "GOLDMAN SACHS GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "11",
    "totals" : "17920000"
    },
{
    "valSum" : "16828000",
    "cik" : "1389507",
    "cusip" : "22266T109",
    "nameOfIssuer" : "COUPANG INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "12",
    "totals" : "16828000"
    },
{
    "valSum" : "14657000",
    "cik" : "1389507",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "13",
    "totals" : "14657000"
    },
{
    "valSum" : "14279000",
    "cik" : "1389507",
    "cusip" : "02364W105",
    "nameOfIssuer" : "AMERICA MOVIL SAB DE CV",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "14",
    "totals" : "-11455000"
    },
{
    "valSum" : "13851000",
    "cik" : "1389507",
    "cusip" : "84918M205",
    "nameOfIssuer" : "SPORTS ENTERTAINMENT ACQU CO",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "15",
    "totals" : "-662000"
    },
{
    "valSum" : "13088000",
    "cik" : "1389507",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "16",
    "totals" : "13088000"
    },
{
    "valSum" : "13055000",
    "cik" : "1389507",
    "cusip" : "26884U109",
    "nameOfIssuer" : "EPR PPTYS",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "17",
    "totals" : "13055000"
    },
{
    "valSum" : "12842000",
    "cik" : "1389507",
    "cusip" : "00183L102",
    "nameOfIssuer" : "ANGI INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "18",
    "totals" : "1981000"
    },
{
    "valSum" : "11171000",
    "cik" : "1389507",
    "cusip" : "92556H206",
    "nameOfIssuer" : "VIACOMCBS INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "19",
    "totals" : "11171000"
    },
{
    "valSum" : "10867000",
    "cik" : "1389507",
    "cusip" : "13100M509",
    "nameOfIssuer" : "CALIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "20",
    "totals" : "7222000"
    },
{
    "valSum" : "10550000",
    "cik" : "1389507",
    "cusip" : "44487N208",
    "nameOfIssuer" : "HUMANCO ACQUISITION CORP",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "21",
    "totals" : "-470000"
    },
{
    "valSum" : "8758000",
    "cik" : "1389507",
    "cusip" : "H8817H100",
    "nameOfIssuer" : "TRANSOCEAN LTD",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "22",
    "totals" : "3229000"
    },
{
    "valSum" : "8315000",
    "cik" : "1389507",
    "cusip" : "98986T108",
    "nameOfIssuer" : "ZYNGA INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "23",
    "totals" : "4857000"
    },
{
    "valSum" : "8284000",
    "cik" : "1389507",
    "cusip" : "20337X109",
    "nameOfIssuer" : "COMMSCOPE HLDG CO INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "24",
    "totals" : "-22481000"
    },
{
    "valSum" : "8085000",
    "cik" : "1389507",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Discovery Capital",
    "rnk" : "25",
    "totals" : "4036000"
    },
{
    "valSum" : "1043320000",
    "cik" : "1410830",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "1",
    "totals" : "-38140000"
    },
{
    "valSum" : "774984000",
    "cik" : "1410830",
    "cusip" : "254687106",
    "nameOfIssuer" : "DISNEY WALT CO",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "2",
    "totals" : "14028000"
    },
{
    "valSum" : "643714000",
    "cik" : "1410830",
    "cusip" : "893641100",
    "nameOfIssuer" : "TRANSDIGM GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "3",
    "totals" : "-33865000"
    },
{
    "valSum" : "555589000",
    "cik" : "1410830",
    "cusip" : "79466L302",
    "nameOfIssuer" : "SALESFORCE COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "4",
    "totals" : "-27953000"
    },
{
    "valSum" : "547530000",
    "cik" : "1410830",
    "cusip" : "22788C105",
    "nameOfIssuer" : "CROWDSTRIKE HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "5",
    "totals" : "-87930000"
    },
{
    "valSum" : "496408000",
    "cik" : "1410830",
    "cusip" : "37940X102",
    "nameOfIssuer" : "GLOBAL PMTS INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "6",
    "totals" : "-34083000"
    },
{
    "valSum" : "495564000",
    "cik" : "1410830",
    "cusip" : "00650F109",
    "nameOfIssuer" : "ADAPTIVE BIOTECHNOLOGIES COR",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "7",
    "totals" : "-279931000"
    },
{
    "valSum" : "442501000",
    "cik" : "1410830",
    "cusip" : "747525103",
    "nameOfIssuer" : "QUALCOMM INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "8",
    "totals" : "-65912000"
    },
{
    "valSum" : "402537000",
    "cik" : "1410830",
    "cusip" : "38222105",
    "nameOfIssuer" : "APPLIED MATLS INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "9",
    "totals" : "142515000"
    },
{
    "valSum" : "322550000",
    "cik" : "1410830",
    "cusip" : "21369103",
    "nameOfIssuer" : "ALTAIR ENGR INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "10",
    "totals" : "22631000"
    },
{
    "valSum" : "310180000",
    "cik" : "1410830",
    "cusip" : "595112103",
    "nameOfIssuer" : "MICRON TECHNOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "11",
    "totals" : "-290132000"
    },
{
    "valSum" : "307400000",
    "cik" : "1410830",
    "cusip" : "64829B100",
    "nameOfIssuer" : "NEW RELIC INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "12",
    "totals" : "-19600000"
    },
{
    "valSum" : "262353000",
    "cik" : "1410830",
    "cusip" : "98138H101",
    "nameOfIssuer" : "WORKDAY INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "13",
    "totals" : "9315000"
    },
{
    "valSum" : "260190000",
    "cik" : "1410830",
    "cusip" : "983919101",
    "nameOfIssuer" : "XILINX INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "14",
    "totals" : "-37527000"
    },
{
    "valSum" : "225420000",
    "cik" : "1410830",
    "cusip" : "08975P108",
    "nameOfIssuer" : "BIGCOMMERCE HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "15",
    "totals" : "7072000"
    },
{
    "valSum" : "206953000",
    "cik" : "1410830",
    "cusip" : "00653A107",
    "nameOfIssuer" : "ADAPTIMMUNE THERAPEUTICS PLC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "16",
    "totals" : "-3118000"
    },
{
    "valSum" : "193408000",
    "cik" : "1410830",
    "cusip" : "458140100",
    "nameOfIssuer" : "INTEL CORP",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "17",
    "totals" : "193408000"
    },
{
    "valSum" : "170380000",
    "cik" : "1410830",
    "cusip" : "90138F102",
    "nameOfIssuer" : "TWILIO INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "18",
    "totals" : "170380000"
    },
{
    "valSum" : "165825000",
    "cik" : "1410830",
    "cusip" : "98943L107",
    "nameOfIssuer" : "ZENTALIS PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "19",
    "totals" : "-32676000"
    },
{
    "valSum" : "160015000",
    "cik" : "1410830",
    "cusip" : "92337F107",
    "nameOfIssuer" : "VERACYTE INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "20",
    "totals" : "160015000"
    },
{
    "valSum" : "159345000",
    "cik" : "1410830",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "21",
    "totals" : "-8387000"
    },
{
    "valSum" : "120600000",
    "cik" : "1410830",
    "cusip" : "268150109",
    "nameOfIssuer" : "DYNATRACE INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "22",
    "totals" : "12425000"
    },
{
    "valSum" : "97982000",
    "cik" : "1410830",
    "cusip" : "14167L103",
    "nameOfIssuer" : "CAREDX INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "23",
    "totals" : "97982000"
    },
{
    "valSum" : "89286000",
    "cik" : "1410830",
    "cusip" : "512807108",
    "nameOfIssuer" : "LAM RESEARCH CORP",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "24",
    "totals" : "18445000"
    },
{
    "valSum" : "68460000",
    "cik" : "1410830",
    "cusip" : "14843C105",
    "nameOfIssuer" : "CASTLE BIOSCIENCES INC",
    "filingDate" : "2021-03-31",
    "name" : "Matrix Capital Company",
    "rnk" : "25",
    "totals" : "1310000"
    },
{
    "valSum" : "5411821294",
    "cik" : "1423053",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "1",
    "totals" : "-67737000"
    },
{
    "valSum" : "5156399294",
    "cik" : "1423053",
    "cusip" : "37833100",
    "nameOfIssuer" : "APPLE INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "2",
    "totals" : "178439000"
    },
{
    "valSum" : "5139174294",
    "cik" : "1423053",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "3",
    "totals" : "-295426000"
    },
{
    "valSum" : "4991282294",
    "cik" : "1423053",
    "cusip" : "46090",
    "nameOfIssuer" : "INVESCO QQQ TR",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "4",
    "totals" : "-502345000"
    },
{
    "valSum" : "4846117294",
    "cik" : "1423053",
    "cusip" : "67066G104",
    "nameOfIssuer" : "NVIDIA CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "5",
    "totals" : "428886000"
    },
{
    "valSum" : "4751416294",
    "cik" : "1423053",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "6",
    "totals" : "361347647"
    },
{
    "valSum" : "4658928294",
    "cik" : "1423053",
    "cusip" : "464287655",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "7",
    "totals" : "225131647"
    },
{
    "valSum" : "4644187647",
    "cik" : "1423053",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "8",
    "totals" : "-216537000"
    },
{
    "valSum" : "4537848647",
    "cik" : "1423053",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "9",
    "totals" : "-330147000"
    },
{
    "valSum" : "4520456294",
    "cik" : "1423053",
    "cusip" : "78462F103",
    "nameOfIssuer" : "SPDR S&P 500 ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "10",
    "totals" : "-748825000"
    },
{
    "valSum" : "4388399647",
    "cik" : "1423053",
    "cusip" : "64110L106",
    "nameOfIssuer" : "NETFLIX INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "11",
    "totals" : "-86718647"
    },
{
    "valSum" : "4333825294",
    "cik" : "1423053",
    "cusip" : "88160R101",
    "nameOfIssuer" : "TESLA INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "12",
    "totals" : "-213389000"
    },
{
    "valSum" : "4272972647",
    "cik" : "1423053",
    "cusip" : "02079K107",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "13",
    "totals" : "17557000"
    },
{
    "valSum" : "4099581000",
    "cik" : "1423053",
    "cusip" : "97023105",
    "nameOfIssuer" : "BOEING CO",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "14",
    "totals" : "637531000"
    },
{
    "valSum" : "3777152000",
    "cik" : "1423053",
    "cusip" : "7903107",
    "nameOfIssuer" : "ADVANCED MICRO DEVICES INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "15",
    "totals" : "1231450000"
    },
{
    "valSum" : "3178862000",
    "cik" : "1423053",
    "cusip" : "464288513",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "16",
    "totals" : "613517000"
    },
{
    "valSum" : "2520879000",
    "cik" : "1423053",
    "cusip" : "82509L107",
    "nameOfIssuer" : "SHOPIFY INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "17",
    "totals" : "185717000"
    },
{
    "valSum" : "2387937000",
    "cik" : "1423053",
    "cusip" : "70450Y103",
    "nameOfIssuer" : "PAYPAL HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "18",
    "totals" : "753814000"
    },
{
    "valSum" : "2387482000",
    "cik" : "1423053",
    "cusip" : "79466L302",
    "nameOfIssuer" : "SALESFORCE COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "19",
    "totals" : "361405000"
    },
{
    "valSum" : "2149329000",
    "cik" : "1423053",
    "cusip" : "852234103",
    "nameOfIssuer" : "SQUARE INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "20",
    "totals" : "138320000"
    },
{
    "valSum" : "2086760000",
    "cik" : "1423053",
    "cusip" : "254687106",
    "nameOfIssuer" : "DISNEY WALT CO",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "21",
    "totals" : "-675811000"
    },
{
    "valSum" : "1906448000",
    "cik" : "1423053",
    "cusip" : "92826C839",
    "nameOfIssuer" : "VISA INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "22",
    "totals" : "133968000"
    },
{
    "valSum" : "1883582000",
    "cik" : "1423053",
    "cusip" : "56752108",
    "nameOfIssuer" : "BAIDU INC",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "23",
    "totals" : "889143000"
    },
{
    "valSum" : "1795473000",
    "cik" : "1423053",
    "cusip" : "22160K105",
    "nameOfIssuer" : "COSTCO WHSL CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "24",
    "totals" : "393372000"
    },
{
    "valSum" : "1794464000",
    "cik" : "1423053",
    "cusip" : "78463V107",
    "nameOfIssuer" : "SPDR GOLD TR",
    "filingDate" : "2021-03-31",
    "name" : "Citadel",
    "rnk" : "25",
    "totals" : "-2010304647"
    },
{
    "valSum" : "15035000",
    "cik" : "1439289",
    "cusip" : "811246107",
    "nameOfIssuer" : "SCULPTOR CAP MGMT",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "1",
    "totals" : "1312000"
    },
{
    "valSum" : "11626000",
    "cik" : "1439289",
    "cusip" : "31946M103",
    "nameOfIssuer" : "FIRST CITIZENS BANCSHARES INC",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "2",
    "totals" : "4561000"
    },
{
    "valSum" : "9104000",
    "cik" : "1439289",
    "cusip" : "12769G100",
    "nameOfIssuer" : "CAESARS ENTERTAINMENT INC",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "3",
    "totals" : "-461000"
    },
{
    "valSum" : "7045000",
    "cik" : "1439289",
    "cusip" : "949746101",
    "nameOfIssuer" : "WELLS FARGO CO",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "4",
    "totals" : "7045000"
    },
{
    "valSum" : "7025000",
    "cik" : "1439289",
    "cusip" : "617446448",
    "nameOfIssuer" : "MORGAN STANLEY",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "5",
    "totals" : "5175000"
    },
{
    "valSum" : "6516000",
    "cik" : "1439289",
    "cusip" : "82669G104",
    "nameOfIssuer" : "SIGNATURE BK NEW YORK NY",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "6",
    "totals" : "6516000"
    },
{
    "valSum" : "6402000",
    "cik" : "1439289",
    "cusip" : "03750L109",
    "nameOfIssuer" : "APARTMENT INCOME REIT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "7",
    "totals" : "6402000"
    },
{
    "valSum" : "6323000",
    "cik" : "1439289",
    "cusip" : "10948W103",
    "nameOfIssuer" : "BRIGHTSPHERE INVT GROUP",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "8",
    "totals" : "787000"
    },
{
    "valSum" : "5738000",
    "cik" : "1439289",
    "cusip" : "70450Y103",
    "nameOfIssuer" : "PAYPAL HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "9",
    "totals" : "453000"
    },
{
    "valSum" : "4890000",
    "cik" : "1439289",
    "cusip" : "46592C100",
    "nameOfIssuer" : "JOFF FINTECH ACQUISITION COR",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "10",
    "totals" : "4890000"
    },
{
    "valSum" : "4789000",
    "cik" : "1439289",
    "cusip" : "05589G102",
    "nameOfIssuer" : "BRP GROUP INC C",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "11",
    "totals" : "-595000"
    },
{
    "valSum" : "4442000",
    "cik" : "1439289",
    "cusip" : "37518G200",
    "nameOfIssuer" : "GIFCAPITAL4 INC",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "12",
    "totals" : "4442000"
    },
{
    "valSum" : "3661000",
    "cik" : "1439289",
    "cusip" : "846775104",
    "nameOfIssuer" : "SPARTAN ACQUISITION CORP II",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "13",
    "totals" : "3661000"
    },
{
    "valSum" : "2530000",
    "cik" : "1439289",
    "cusip" : "302438205",
    "nameOfIssuer" : "FIGURE ACQUISITION CORP I",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "14",
    "totals" : "2530000"
    },
{
    "valSum" : "983000",
    "cik" : "1439289",
    "cusip" : "37954A204",
    "nameOfIssuer" : "GLOBAL MED REIT INC",
    "filingDate" : "2021-03-31",
    "name" : "Toscafund",
    "rnk" : "15",
    "totals" : "983000"
    },
{
    "valSum" : "112910",
    "cik" : "1569049",
    "cusip" : "81141R100",
    "nameOfIssuer" : "SEA LTD",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "1",
    "totals" : "-160839090"
    },
{
    "valSum" : "87091",
    "cik" : "1569049",
    "cusip" : "86771W105",
    "nameOfIssuer" : "SUNRUN INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "2",
    "totals" : "-134669909"
    },
{
    "valSum" : "82321",
    "cik" : "1569049",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "3",
    "totals" : "82321"
    },
{
    "valSum" : "80572",
    "cik" : "1569049",
    "cusip" : "874224207",
    "nameOfIssuer" : "TALEND S A",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "4",
    "totals" : "-51755428"
    },
{
    "valSum" : "75437",
    "cik" : "1569049",
    "cusip" : "70614W100",
    "nameOfIssuer" : "PELOTON INTERACTIVE INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "5",
    "totals" : "-82608563"
    },
{
    "valSum" : "72253",
    "cik" : "1569049",
    "cusip" : "G8990D125",
    "nameOfIssuer" : "TPG PACE BEN FIN CORP",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "6",
    "totals" : "-86618747"
    },
{
    "valSum" : "65840",
    "cik" : "1569049",
    "cusip" : "55087P104",
    "nameOfIssuer" : "LYFT INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "7",
    "totals" : "-14733160"
    },
{
    "valSum" : "65620",
    "cik" : "1569049",
    "cusip" : "67066G104",
    "nameOfIssuer" : "NVIDIA CORPORATION",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "8",
    "totals" : "65620"
    },
{
    "valSum" : "62117",
    "cik" : "1569049",
    "cusip" : "11135F101",
    "nameOfIssuer" : "BROADCOM INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "9",
    "totals" : "-54462883"
    },
{
    "valSum" : "60325",
    "cik" : "1569049",
    "cusip" : "38246G108",
    "nameOfIssuer" : "GOODRX HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "10",
    "totals" : "-81863675"
    },
{
    "valSum" : "59234",
    "cik" : "1569049",
    "cusip" : "72352L106",
    "nameOfIssuer" : "PINTEREST INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "11",
    "totals" : "-63240766"
    },
{
    "valSum" : "59069",
    "cik" : "1569049",
    "cusip" : "79466L302",
    "nameOfIssuer" : "SALESFORCE COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "12",
    "totals" : "59069"
    },
{
    "valSum" : "58555",
    "cik" : "1569049",
    "cusip" : "12769G100",
    "nameOfIssuer" : "CAESARS ENTERTAINMENT INC NE",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "13",
    "totals" : "-79701445"
    },
{
    "valSum" : "55117",
    "cik" : "1569049",
    "cusip" : "81762P102",
    "nameOfIssuer" : "SERVICENOW INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "14",
    "totals" : "55117"
    },
{
    "valSum" : "53425",
    "cik" : "1569049",
    "cusip" : "70450Y103",
    "nameOfIssuer" : "PAYPAL HLDGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "15",
    "totals" : "-50943575"
    },
{
    "valSum" : "52582",
    "cik" : "1569049",
    "cusip" : "62886",
    "nameOfIssuer" : "NCR CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "16",
    "totals" : "-85726418"
    },
{
    "valSum" : "52523",
    "cik" : "1569049",
    "cusip" : "G8990Y103",
    "nameOfIssuer" : "TPG PACE TECH OPPORTUNITIES",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "17",
    "totals" : "52523"
    },
{
    "valSum" : "51083",
    "cik" : "1569049",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "18",
    "totals" : "-77072917"
    },
{
    "valSum" : "50775",
    "cik" : "1569049",
    "cusip" : "74640Y106",
    "nameOfIssuer" : "PURPLE INNOVATION INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "19",
    "totals" : "-109834225"
    },
{
    "valSum" : "50500",
    "cik" : "1569049",
    "cusip" : "90117G204",
    "nameOfIssuer" : "TWC TECH HLDGS II CORP",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "20",
    "totals" : "-53699500"
    },
{
    "valSum" : "50148",
    "cik" : "1569049",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "21",
    "totals" : "50148"
    },
{
    "valSum" : "49959",
    "cik" : "1569049",
    "cusip" : "268150109",
    "nameOfIssuer" : "DYNATRACE INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "22",
    "totals" : "-101362041"
    },
{
    "valSum" : "49349",
    "cik" : "1569049",
    "cusip" : "00436Q106",
    "nameOfIssuer" : "ACCEL ENTERTAINMENT INC",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "23",
    "totals" : "-47814651"
    },
{
    "valSum" : "44949",
    "cik" : "1569049",
    "cusip" : "538034109",
    "nameOfIssuer" : "LIVE NATION ENTERTAINMENT IN",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "24",
    "totals" : "44949"
    },
{
    "valSum" : "43706",
    "cik" : "1569049",
    "cusip" : "861012102",
    "nameOfIssuer" : "STMICROELECTRONICS N V",
    "filingDate" : "2021-03-31",
    "name" : "Light Street",
    "rnk" : "25",
    "totals" : "43706"
    },
{
    "valSum" : "928324000",
    "cik" : "1603466",
    "cusip" : "78462F103",
    "nameOfIssuer" : "SPDR S&P 500 ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "1",
    "totals" : "364774000"
    },
{
    "valSum" : "516753000",
    "cik" : "1603466",
    "cusip" : "90353T100",
    "nameOfIssuer" : "UBER TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "2",
    "totals" : "310699000"
    },
{
    "valSum" : "360964000",
    "cik" : "1603466",
    "cusip" : "958102105",
    "nameOfIssuer" : "WESTERN DIGITAL CORP.",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "3",
    "totals" : "346224000"
    },
{
    "valSum" : "348602000",
    "cik" : "1603466",
    "cusip" : "56752108",
    "nameOfIssuer" : "BAIDU INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "4",
    "totals" : "299245000"
    },
{
    "valSum" : "327420000",
    "cik" : "1603466",
    "cusip" : "92826C839",
    "nameOfIssuer" : "VISA INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "5",
    "totals" : "46327000"
    },
{
    "valSum" : "276959000",
    "cik" : "1603466",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "6",
    "totals" : "-365642000"
    },
{
    "valSum" : "255304000",
    "cik" : "1603466",
    "cusip" : "46090",
    "nameOfIssuer" : "INVESCO QQQ TR",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "7",
    "totals" : "255304000"
    },
{
    "valSum" : "255171000",
    "cik" : "1603466",
    "cusip" : "38222105",
    "nameOfIssuer" : "APPLIED MATLS INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "8",
    "totals" : "255171000"
    },
{
    "valSum" : "247458000",
    "cik" : "1603466",
    "cusip" : "23135106",
    "nameOfIssuer" : "AMAZON COM INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "9",
    "totals" : "95187000"
    },
{
    "valSum" : "241598000",
    "cik" : "1603466",
    "cusip" : "30303M102",
    "nameOfIssuer" : "FACEBOOK INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "10",
    "totals" : "-112288000"
    },
{
    "valSum" : "234999000",
    "cik" : "1603466",
    "cusip" : "23355L106",
    "nameOfIssuer" : "DXC TECHNOLOGY CO",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "11",
    "totals" : "156776000"
    },
{
    "valSum" : "229835000",
    "cik" : "1603466",
    "cusip" : "90184L102",
    "nameOfIssuer" : "TWITTER INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "12",
    "totals" : "43595000"
    },
{
    "valSum" : "185318000",
    "cik" : "1603466",
    "cusip" : "595112103",
    "nameOfIssuer" : "MICRON TECHNOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "13",
    "totals" : "-10049000"
    },
{
    "valSum" : "183437000",
    "cik" : "1603466",
    "cusip" : "G68707101",
    "nameOfIssuer" : "PAGSEGURO DIGITAL LTD",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "14",
    "totals" : "83557000"
    },
{
    "valSum" : "176648000",
    "cik" : "1603466",
    "cusip" : "46353108",
    "nameOfIssuer" : "ASTRAZENECA PLC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "15",
    "totals" : "-35225000"
    },
{
    "valSum" : "167230000",
    "cik" : "1603466",
    "cusip" : "466313103",
    "nameOfIssuer" : "JABIL INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "16",
    "totals" : "60471000"
    },
{
    "valSum" : "160347000",
    "cik" : "1603466",
    "cusip" : "58933Y105",
    "nameOfIssuer" : "MERCK & CO. INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "17",
    "totals" : "28364000"
    },
{
    "valSum" : "158161000",
    "cik" : "1603466",
    "cusip" : "N6596X109",
    "nameOfIssuer" : "NXP SEMICONDUCTORS N V",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "18",
    "totals" : "49661000"
    },
{
    "valSum" : "147537000",
    "cik" : "1603466",
    "cusip" : "517834107",
    "nameOfIssuer" : "LAS VEGAS SANDS CORP",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "19",
    "totals" : "-54194000"
    },
{
    "valSum" : "142681000",
    "cik" : "1603466",
    "cusip" : "92532F100",
    "nameOfIssuer" : "VERTEX PHARMACEUTICALS INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "20",
    "totals" : "89954000"
    },
{
    "valSum" : "142152000",
    "cik" : "1603466",
    "cusip" : "16255101",
    "nameOfIssuer" : "ALIGN TECHNOLOGY INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "21",
    "totals" : "129380000"
    },
{
    "valSum" : "140532000",
    "cik" : "1603466",
    "cusip" : "594918104",
    "nameOfIssuer" : "MICROSOFT CORP",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "22",
    "totals" : "-110931000"
    },
{
    "valSum" : "139404000",
    "cik" : "1603466",
    "cusip" : "09857L108",
    "nameOfIssuer" : "BOOKING HOLDINGS INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "23",
    "totals" : "21947000"
    },
{
    "valSum" : "134184000",
    "cik" : "1603466",
    "cusip" : "30212P303",
    "nameOfIssuer" : "EXPEDIA GROUP INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "24",
    "totals" : "134184000"
    },
{
    "valSum" : "130938000",
    "cik" : "1603466",
    "cusip" : "24703L202",
    "nameOfIssuer" : "DELL TECHNOLOGIES INC",
    "filingDate" : "2021-03-31",
    "name" : "Point72",
    "rnk" : "25",
    "totals" : "-69341000"
    },
{
    "valSum" : "1120522000",
    "cik" : "1736225",
    "cusip" : "01609W102",
    "nameOfIssuer" : "ALIBABA GROUP HLDG LTD",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "1",
    "totals" : "-634952000"
    },
{
    "valSum" : "180636000",
    "cik" : "1736225",
    "cusip" : "78462F103",
    "nameOfIssuer" : "SPDR S&P 500 ETF TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "2",
    "totals" : "-489912000"
    },
{
    "valSum" : "171159000",
    "cik" : "1736225",
    "cusip" : "46090",
    "nameOfIssuer" : "INVESCO QQQ TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "3",
    "totals" : "148429000"
    },
{
    "valSum" : "130902000",
    "cik" : "1736225",
    "cusip" : "83304A106",
    "nameOfIssuer" : "SNAP INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "4",
    "totals" : "-241802000"
    },
{
    "valSum" : "76953000",
    "cik" : "1736225",
    "cusip" : "29364G103",
    "nameOfIssuer" : "ENTERGY CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "5",
    "totals" : "31997000"
    },
{
    "valSum" : "68352000",
    "cik" : "1736225",
    "cusip" : "55087P104",
    "nameOfIssuer" : "LYFT INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "6",
    "totals" : "-20093000"
    },
{
    "valSum" : "62841000",
    "cik" : "1736225",
    "cusip" : "464287598",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "7",
    "totals" : "51468000"
    },
{
    "valSum" : "55957000",
    "cik" : "1736225",
    "cusip" : "464287234",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "8",
    "totals" : "-34960000"
    },
{
    "valSum" : "49645000",
    "cik" : "1736225",
    "cusip" : "20030N101",
    "nameOfIssuer" : "COMCAST CORP NEW",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "9",
    "totals" : "-268219000"
    },
{
    "valSum" : "47407000",
    "cik" : "1736225",
    "cusip" : "25537101",
    "nameOfIssuer" : "AMERICAN ELEC PWR CO INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "10",
    "totals" : "43062000"
    },
{
    "valSum" : "45974000",
    "cik" : "1736225",
    "cusip" : "125896100",
    "nameOfIssuer" : "CMS ENERGY CORP",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "11",
    "totals" : "15596000"
    },
{
    "valSum" : "40679000",
    "cik" : "1736225",
    "cusip" : "744573106",
    "nameOfIssuer" : "PUBLIC SVC ENTERPRISE GRP IN",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "12",
    "totals" : "23080000"
    },
{
    "valSum" : "38104000",
    "cik" : "1736225",
    "cusip" : "81141R100",
    "nameOfIssuer" : "SEA LTD",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "13",
    "totals" : "-56392000"
    },
{
    "valSum" : "37923000",
    "cik" : "1736225",
    "cusip" : "65473P105",
    "nameOfIssuer" : "NISOURCE INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "14",
    "totals" : "25587000"
    },
{
    "valSum" : "37016000",
    "cik" : "1736225",
    "cusip" : "30034W106",
    "nameOfIssuer" : "EVERGY INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "15",
    "totals" : "1504000"
    },
{
    "valSum" : "35963000",
    "cik" : "1736225",
    "cusip" : "56585A102",
    "nameOfIssuer" : "MARATHON PETE CORP",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "16",
    "totals" : "3974000"
    },
{
    "valSum" : "34680000",
    "cik" : "1736225",
    "cusip" : "29362U104",
    "nameOfIssuer" : "ENTEGRIS INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "17",
    "totals" : "27044000"
    },
{
    "valSum" : "32332000",
    "cik" : "1736225",
    "cusip" : "464288513",
    "nameOfIssuer" : "ISHARES TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "18",
    "totals" : "32246000"
    },
{
    "valSum" : "31534000",
    "cik" : "1736225",
    "cusip" : "15189T107",
    "nameOfIssuer" : "CENTERPOINT ENERGY INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "19",
    "totals" : "15300000"
    },
{
    "valSum" : "29529000",
    "cik" : "1736225",
    "cusip" : "81369Y506",
    "nameOfIssuer" : "SELECT SECTOR SPDR TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "20",
    "totals" : "27999000"
    },
{
    "valSum" : "29069000",
    "cik" : "1736225",
    "cusip" : "02079K305",
    "nameOfIssuer" : "ALPHABET INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "21",
    "totals" : "5245000"
    },
{
    "valSum" : "28819000",
    "cik" : "1736225",
    "cusip" : "458140100",
    "nameOfIssuer" : "INTEL CORP",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "22",
    "totals" : "28819000"
    },
{
    "valSum" : "28792000",
    "cik" : "1736225",
    "cusip" : "38222105",
    "nameOfIssuer" : "APPLIED MATLS INC",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "23",
    "totals" : "25846000"
    },
{
    "valSum" : "28493000",
    "cik" : "1736225",
    "cusip" : "81369Y803",
    "nameOfIssuer" : "SELECT SECTOR SPDR TR",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "24",
    "totals" : "28106000"
    },
{
    "valSum" : "28334000",
    "cik" : "1736225",
    "cusip" : "09073M104",
    "nameOfIssuer" : "BIO-TECHNE CORP",
    "filingDate" : "2021-03-31",
    "name" : "ExodusPoint",
    "rnk" : "25",
    "totals" : "27223000"
    }
]
df_json = pd.read_json(obj)
print(df_json)