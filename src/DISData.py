import mysql.connector
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import markdown
import subprocess
import paramiko
import platform
import getpass


def Approch_To_Synology():
    "Approch to Synology NAS server using NFS protocol"
    "Warning! : this fucntion is Volatiled"
    server_ip = input('server ip: ')
    server_port = input('server port: ')
    nfs_username = input('nfs username: ')
    nfs_password = getpass.getpass('nfs password: ')
    share_path = input('share path: ')
    drive_letter = input('drive letter: ')

    my_os = platform.system()
    if my_os == 'Windows':
        try:
            # connect to the NFS server on Windows
            # PowerShell command to mount the NFS share
            command = f"""mount -o mtype=hard,ro \\\\{server_ip}\{share_path} {drive_letter}: -u:{nfs_username} -p:{nfs_password}"""
            print(command)

            # Run the PowerShell command using subprocess
            return subprocess.check_output(["cmd.exe", command], shell=True)

        except subprocess.CalledProcessError as e:
            print(f"Failed to mount {server_ip}:{share_path}. Error: {e} please setting nfs client on windows first")
        except Exception as e:
            print(f"Error: {e}")

        # try:
        #     # sftp 접속 방식
        #     ssh_client = paramiko.SSHClient()
        #     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #     ssh_client.connect(hostname=server_ip, port=server_port, username=nfs_username, password=nfs_password)
        #     sftp = ssh_client.open_sftp()
        #     sftp.chdir(share_path)
        #     print(f"Successfully mounted {server_ip}:{share_path}")
        #     return sftp
        # except Exception as e:
        #     print(f"Error: {e}")
    elif my_os == 'Linux':
        try:
            # connet to the NFS server on Linux
            mount_command = f"sudo mount -t nfs -o username={nfs_username},password={nfs_password} {server_ip}:{share_path} "
            subprocess.run(mount_command, shell=True, check=True)
            print(f"Successfully mounted {server_ip}:{share_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to mount {server_ip}:{share_path}. Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        
    else:
        print(f'this {my_os} is not supported yet')
        pass    

    
class SearchDataset():
    """Search dataset from json file"""
    # hard coding to json file path should be changed to relative path
    with open('Eye_Gaze.json', 'r') as f:
        json_data = json.load(f)

    def __init__(self, json_data=json_data):
        self.json_data = json_data
        
    def Type(self,search_type):
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
        meta_data = self.json_data.get('meta_data',{})
        for data_key, data_info in meta_data.items():
            if data_key == data_name:
                # data_info = markdown.markdown(data_info)
                return data_info
            
    def Show_images(self, data_name, image_count):
        pass     

    def Load_labeldata(self, data_name):
        """Load label data from mysql database"""

        sql_ip = input('sql ip: ')
        sql_port = input('sql port: ')
        sql_username = input('sql username: ')
        sql_password = getpass.getpass('sql password: ')

        config = {
            'user': sql_username,
            'password': sql_password,
            'host': sql_ip,
            'port': sql_port,
            'database': 'DeepInSight',
            'raise_on_warnings': True
        }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM DeepInSight." + data_name + "_info")
        column_names = [description[0] for description in cursor.description]
        rows = pd.DataFrame(cursor.fetchall(), columns=column_names)
        cursor.close()
        conn.close()

        return rows
    
    def DownLoad_rawdata(self, data_name):
        """Download raw data from nas server"""
        meta_data = self.json_data.get('meta_data',{})
        print(f'This Dataset size is {meta_data[data_name]["Size"]}. Do you want to download?')
        print('y/n')
        answer = input()
        if answer == 'y':
            sql_ip = input('sql ip: ')
            sql_port = input('sql port: ')
            sql_username = input('sql username: ')
            sql_password = getpass.getpass('sql password: ')
            save_path = input('save path: ')

            config = {
                'user': sql_username,
                'password': sql_password,
                'host': sql_ip,
                'port': sql_port,
                'database': 'DeepInSight',
                'raise_on_warnings': True
            }
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM DeepInSight." + data_name + "_info")
            cursor.close()
            conn.close()
            column_names = [description[0] for description in cursor.description]
            rows = pd.DataFrame(cursor.fetchall(), columns=column_names)
            img_path_list = rows['img_dir'].tolist()
            print('Download start')
            # for img_path in img_path_list:
            #     sftp = Approch_To_Synology()
            #     sftp.get(img_path, save_path)
            #     sftp.close()
    
            print('Download done')
        else:
            print('Download cancel')
            pass
        
    def draw_heatmap(data_name, save_name, font_size=20,reverse=False):
        plt.figure(figsize=(16, 12))
        sns.heatmap(data=data_name, cmap='YlGnBu', annot=True, fmt="d", linewidths=.5, annot_kws={"size": font_size})
        if reverse == True: 
            plt.gca().invert_yaxis()
        plt.savefig(save_name)
        print('save',save_name)

    def draw_jointplot(data_name, save_name, reverse=False):
        plt.figure(figsize=(16, 12))
        sns.jointplot(data=data_name, kind='kde', cmap='RdYlGn')
        if reverse == True: 
            plt.gca().invert_yaxis()
        plt.savefig(save_name)
        print('save',save_name)

# result1 = SearchDataset().Type("Grayscale")
# print(result1)
# result2 = SearchDataset().DataSet("SYNTHESEYES")
# print(result2)
# # result3 = SearchDataset().Load_label("ETH_Xgaze")
# # print(result3)
