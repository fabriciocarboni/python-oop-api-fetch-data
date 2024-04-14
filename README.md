# Python OOP practice

This program fetches data from an external API and insert data into Snowflake Database

Create .env file
```
USER=<SNOWFLAKE-DATABASE-USER>
ACCOUNT=<SNOWFLAKE-ACCOUNT>
PRIVATE_KEY=<SNOWFLAKE-PRIVATE-KEY-FILE>
WAREHOUSE=<SNOWFLAKE-WHAREHOUSE>
DATABASE=<SNOWFLAKE-DATABASE-NAME>
SCHEMA=<SNOWFLAKE-SCHEMA>
API_TOKEN=<API-TOKEN>
API_URL=<API-URL>
```

Create a venv for the project and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```