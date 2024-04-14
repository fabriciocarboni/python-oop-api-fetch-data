import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import pandas as pd

class SnowflakeHandler:
    """ 
    Handles Snowflake connection
    """
    def __init__(self, user: str, account:str, private_key_path: str, 
                 warehouse: str, database:str, schema: str) -> None:
        self.user = user
        self.account = account
        self.private_key_path = private_key_path
        self.warehouse = warehouse
        self.database = database
        self.schema = schema

    
    def connect(self) -> snowflake.connector.SnowflakeConnection:
        """
        Connect to Snowflake using private key and returns SnowflakeConnection
        """
        # print(self.private_key_path)
        # print(self.account)
        # exit()
        with open(self.private_key_path, "rb") as key:
            p_key = serialization.load_pem_private_key(
                key.read(),
                password=None,
                backend=default_backend()
            )

        p_key = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        self.conn = snowflake.connector.connect(
            user=self.user,
            account=self.account,
            private_key=p_key,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )
        
        cur = self.conn.cursor()
    
        try:
            # Executing a simple query
            cur.execute("SELECT CURRENT_VERSION()")

            # Fetch one result
            one_row = cur.fetchone()
            print("Connection Successful!")
            print(f"Current Snowflake version: {one_row[0]}")

        except Exception as e:
            print(f"An error occurred: {e}")

        return self.conn

    
    def insert_data(self, data_frame, target_table_name, chunk_size=16384):
        if not hasattr(self, 'conn'):
            self.connect()

        success, nchunks, nrows, _ = write_pandas(
            self.conn,
            data_frame,
            target_table_name,
            auto_create_table=True,
            chunk_size=chunk_size
        )

        if success:
            print(f"Successfully inserted {nrows} rows into {target_table_name} in {nchunks} chunks.")
        else:
            print("Data insertion failed.")

        if self.conn:
            self.conn.close()
            print("Snowflake connection closed.")
