import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector 
import pandas as pd
import keycode

class MakeSQL():
    def create_table(query):
        config = keycode.config
        db = mysql.connector.connect(**config)
        conn = db.cursor()
        conn.execute(query)
        db.commit()
        conn.close()
        db.close()
        print('create table done')

    def insert_dataset_values(query,value_list):
        config = keycode.config
        db = mysql.connector.connect(**config)
        conn = db.cursor()
        print(value_list[0])
        conn.executemany(query,value_list)
        db.commit()
        print(f'insert {len(value_list)} done')

    def search_SQL (dataset):
        config = keycode.config
        db = mysql.connector.connect(**config)
        conn = db.cursor(dictionary=True)
        conn.execute(f'''
            SELECT * FROM DeepInSight.{dataset}_info;''')
        # Get column names from the cursor description
        column_names = [desc[0] for desc in conn.description]
        
        # Fetch all the results
        result = conn.fetchall()

        # Close the cursor and database connection
        conn.close()
        db.close()

        # Create a DataFrame with column names
        df = pd.DataFrame(result, columns=column_names)
        
        return df
        
    
    def load_img_dir(dataset):
        config = keycode.config
        db = mysql.connector.connect(**config)
        conn = db.cursor(dictionary=True)
        
        # Execute the query
        conn.execute(f"SELECT img_dir FROM DeepInSight.{dataset}_info;")
        
        # Fetch all the results
        result = conn.fetchall()
        # Close the cursor and database connection
        conn.close()
        db.close()

        # Create a DataFrame with both the default index and 'img_dir' as columns
        df = pd.DataFrame(result,columns=['img_dir'])
        return df