import mysql.connector
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import platform
import getpass
import cv2
import subprocess

class SQL():
    """execute SQL query and handle the SQL connection"""

    def __init__(self):
        """Connect to the SQL server and create a cursor object to execute SQL queries."""

        host = input('host: ')
        user = input('user: ')
        password = getpass.getpass('password: ')

        config = {
            'host': host,
            'user': user,
            'password': password,
            'database': 'DeepInSight',
            'port': 3306,
            'raise_on_warnings': True}
        
        self.config = config
        self.db = mysql.connector.connect(**config)
        self.conn = self.db.cursor()
        print('SQL connection done')
    
    def create_table(self,query):
        """Create a table in the database."""

        db = self.db
        conn = self.conn
        conn.execute(query)
        db.commit()
        print('create table done')

    def insert_dataset_values(self,query,value_list):
        """Insert values into the table."""

        db = self.db
        conn = self.conn
        conn.executemany(query,value_list)
        db.commit()
        print(f'insert {len(value_list)} done')

    def search_SQL (self,dataset):
        """Search the database for a specific dataset and return the results as a DataFrame."""

        db = self.db
        conn = self.conn
        conn.execute(f'''
            SELECT * FROM DeepInSight.{dataset}_info;''')
        # Get column names from the cursor description
        column_names = [desc[0] for desc in conn.description]
        
        # Fetch all the results
        result = conn.fetchall()

        # Create a DataFrame with column names
        df = pd.DataFrame(result, columns=column_names)
        db.commit()
        return df
    
    def Draw_label(self, dataset, df):
        """Draw the label from the dataset"""

        try:
            plt.figure(figsize=(16, 12))
            plt.title(f'{dataset}')
            sns.barplot(x='label', y='count(label)', data=df)
            save_path = f'label/{dataset}_label.png'
            if not os.path.exists('label'):
                os.makedirs('label')
            if os.path.exists(save_path):
                os.remove(save_path)
            for index, value in enumerate(df['count(label)']):
                plt.text(index, value, str(value), ha='center', va='bottom')
            plt.savefig(save_path)
            plt.show()
        except Exception as e:
            print(e)
        
    def load_img_dir(self,dataset):
        """Load the image directory from the database and return the results as a DataFrame."""

        db = self.db
        conn = self.conn
        
        # Execute the query
        conn.execute(f"SELECT img_dir FROM DeepInSight.{dataset}_info;")
        
        # Fetch all the results
        result = conn.fetchall()

        # Create a DataFrame with both the default index and 'img_dir' as columns
        df = pd.DataFrame(result,columns=['img_dir'])
        db.commit()
        return df
    
    def connect_end(self):
        """Close the SQL connection."""

        self.conn.close()
        self.db.close()
        print('SQL connection closed')

class SearchDataset():
    """Search the dataset from the json file and SQL database"""

    def __init__(self):
        """Approch to Synology NAS server using NFS protocol
        Warning! : this fucntion is Volatiled"""
        
        server_ip = input('server ip: ')
        server_port = input('server port: ')
        nfs_username = input('nfs username: ')
        nfs_password = getpass.getpass('nfs password: ')
        share_path = input('share path: ')

        my_os = platform.system()
        if my_os == 'Linux':
            # Linux에 접속하는 코드
            import subprocess
            mount_command = f'sudo mount -t nfs {server_ip}:{share_path} /mnt/nfs_share -o username={nfs_username},password={nfs_password}'
            subprocess.run(mount_command.split())
        elif my_os == 'Windows':
            # Windows에 접속하는 코드
            import subprocess
            mount_command = f'net use Z: \\\\{server_ip}\\{share_path} /user:{nfs_username} {nfs_password}'
            subprocess.run(mount_command, shell=True)
        else:
            print(f'This {my_os} is not supported yet')

        """Search dataset from json file"""
        # hard coding to json file path should be changed to relative path
        with open('Eye_Gaze.json', 'r') as f:
            json_data = json.load(f)
        self.json_data = json_data

    def read_meta_data(self):
        """Read the meta data from the json file"""

        meta_data = self.json_data.get('meta_data',{})
        return meta_data

    def Type(self,search_type):
        """Search the dataset by the type of data. e.g. 'RGB', 'IR'"""

        data_sets = []
        meta_data = self.json_data.get('meta_data',{})
        for data_key, data_info in meta_data.items():
            data_type = data_info.get('Type', '')
            print(f'{data_key}:{data_type}')
            for Type_key, Type_value in data_type.items():
                if Type_value == search_type:
                    data_sets.append(data_key)
        return data_sets

    def DataSet(self,data_name):
        """Search the dataset by the name of data. e.g. 'ETH_Xgaze','RIT_Eyes'"""

        meta_data = self.json_data.get('meta_data',{})
        for data_key, data_info in meta_data.items():
            if data_key == data_name:
                # data_info = markdown.markdown(data_info)
                return data_info
            
    def Show_images(data_name, img_count=5):
        """Show the images from the dataset"""
        
        # Modify the route to suit your own
        file_name = data_name['img_dir']
        for image_name in file_name[:img_count]:
            print(image_name)
            
            if platform.system() == 'linux':
                image_name = image_name.replace("DataBase", "nsmount")
            elif platform.system() == 'Windows':
                image_name = image_name.replace("DataBase", "Z:")
            image_name = cv2.imread(image_name)
            cv2.imshow('image', image_name)
            cv2.waitKey(0)
            cv2.destroyAllWindows()        

    def Draw_landmark(data_name, img_count=5):
        """Draw the landmark on the image from the dataset"""

        file_name = data_name['img_dir']
        for i in range(int(img_count)):
            if platform.system() == 'linux':
                img_name = file_name[i].replace("DataBase", "nsmount")
            elif platform.system() == 'Windows':
                img_name = file_name[i].replace("DataBase", "Z:")
            img = cv2.imread(img_name)
            landmark = data_name['landmark'][i].split('),(')

            for i in landmark:
                i = i.replace('(','').replace(')','')
                x, y = i.split(', ')
                cv2.circle(img, (int(x), int(y)), 3, (0, 0, 255), -1)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def Draw_Gaze(data_name, img_count=5):
        """Draw the gaze on the image from the dataset"""

        file_name = data_name['img_dir']
        for i in range(int(img_count)):
            if platform.system() == 'linux':
                img_name = file_name[i].replace("DataBase", "nsmount")
            elif platform.system() == 'Windows':
                img_name = file_name[i].replace("DataBase", "Z:")
            img = cv2.imread(img_name)
            gaze = data_name['gaze'][i].split('),(')
            cv2.line(img, (int(gaze[0]), int(gaze[1])), (int(gaze[2]), int(gaze[3])), (0, 0, 255), 2)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        pass     

    def Draw_BBox(data_name, img_count=5):
        """Draw the bounding box on the image from the dataset"""

        file_name = data_name['img_dir']
        for i in range(int(img_count)):
            if platform.system() == 'linux':
                img_name = file_name[i].replace("DataBase", "nsmount")
            elif platform.system() == 'Windows':
                img_name = file_name[i].replace("DataBase", "Z:")
            img = cv2.imread(img_name)
            bbox = data_name['box_xtl'][i], data_name['box_ytl'][i], data_name['box_xbr'][i], data_name['box_ybr'][i]
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 0, 255), 2)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    
    def DownLoad_rawdata(self, data_name):
        """Download raw data from nas server"""

        # meta_data = self.json_data.get('meta_data',{})
        # print(f'This Dataset size is {meta_data[data_name]["Size"]}. Do you want to download?')
        # print('y/n')
        # answer = input()
        # if answer == 'y':
        #     conn = self.conn
        #     conn.execute("SELECT * FROM DeepInSight." + data_name + "_info")
        #     column_names = [description[0] for description in conn.description]
        #     rows = pd.DataFrame(conn.fetchall(), columns=column_names)
        #     img_path_list = rows['img_dir'].tolist()
        #     print('Download start')
        #     # for img_path in img_path_list:
        #     #     sftp = Approch_To_Synology()
        #     #     sftp.get(img_path, save_path)
        #     #     sftp.close()
    
        #     print('Download done')
        # else:
        #     print('Download cancel')
        pass
        
    def draw_heatmap(data_name, save_name, font_size=20,reverse=False):
        """Draw the heatmap from the dataset"""

        plt.figure(figsize=(16, 12))
        sns.heatmap(data=data_name, cmap='YlGnBu', annot=True, fmt="d", linewidths=.5, annot_kws={"size": font_size})
        if reverse == True: 
            plt.gca().invert_yaxis()
        plt.savefig(save_name)
        print('save',save_name)

    def draw_jointplot(data_name, save_name, reverse=False):
        """Draw the jointplot from the dataset"""

        plt.figure(figsize=(16, 12))
        sns.jointplot(data=data_name, kind='kde', cmap='RdYlGn')
        if reverse == True: 
            plt.gca().invert_yaxis()
        plt.savefig(save_name)
        print('save',save_name)

    def save_frames_from_video(video_path, output_folder):
        """Save the frames from the video"""

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Check if the video file is opened successfully
        if not cap.isOpened():
            print("Error: Could not open video file.")
            return

        # Get the frames per second (fps) of the video
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Get the width and height of the video frames
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        try:
            # Loop through each frame
            frame_count = 0
            while True:
                # Read a frame from the video
                ret, frame = cap.read()

                # If the frame is not read successfully, break the loop
                if not ret:
                    break

                # Save the frame as an image using sudo
                frame_count += 1
                frame_filename = f"{output_folder}/frame_{frame_count}.png"
                cv2.imwrite(frame_filename, frame)

                # Break the loop if the 'Esc' key is pressed
                if cv2.waitKey(int(1000 / fps)) & 0xFF == 27:
                    break

        finally:
            # Release the video capture object
            cap.release()
        