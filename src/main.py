import os
from dotenv import load_dotenv
from snowflake_handler import SnowflakeHandler
from api_handler import ApiHandler
from datetime import datetime, timedelta

def main() -> None:
    
    load_dotenv()
    
    user=os.getenv("USER")
    account=os.getenv("ACCOUNT")
    private_key_path=os.getenv("PRIVATE_KEY")
    warehouse=os.getenv("WAREHOUSE")
    database=os.getenv("DATABASE")
    schema=os.getenv("SCHEMA")
    api_token=os.getenv("API_TOKEN")
    url = os.getenv("API_URL")

    two_years_ago = datetime.now() - timedelta(days=730)
    params = {
        # "releaseDateMin": two_years_ago.strftime('%Y-%m-%d'),
        "releaseDateMin": '2024-04-13',
        "limit": 1000,
        "offset": 0
    }

    api_handler = ApiHandler(url, params, api_token)
    try:
        data = api_handler.fetch_data()
        print(data)
    except Exception as e:
        print(f"Error: {str(e)}")


    # Initialize the SnowflakeManager
    snowflake_manager = SnowflakeHandler(user, 
                                         account,
                                         private_key_path,
                                         warehouse,
                                         database,
                                         schema)
    
    # Use the snowflake_manager for operations...
    # e.g., snowflake_manager.insert_data(data_frame, 'your_target_table')
    
    snowflake_manager.connect()
    # TODO: Insert data


if __name__ == "__main__":
    main()
    