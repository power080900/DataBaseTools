import json
from IPython.display import Markdown

json_file_path = ''
markdown_file_path = ''

# json load
def load_json(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    return json_data


def json_to_markdown(data, level=0):
    markdown = ""
    for key, value in data.items():
        if isinstance(value, dict):
            markdown += f"{' ' * (level * 4)}- ``{key}``:\n"
            markdown += json_to_markdown(value, level + 1)
        else:
            markdown += f"{' ' * (level * 4)}- ``{key}``: **{value}**\n\n"
    return markdown


def json_to_markdown(data, level=0):
    markdown = ""
    for key, value in data.items():
        if isinstance(value, dict):
            markdown += f"{' ' * (level * 4)}- ``{key}``:\n"
            markdown += json_to_markdown(value, level + 1)
        else:
            markdown += f"{' ' * (level * 4)}- ``{key}``: **{value}**\n\n"
    return markdown


def load_json_and_convert_to_markdown(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    markdown_output = json_to_markdown(json_data)
    return markdown_output
# example
# markdown_output = load_json_and_convert_to_markdown(json_file_path)
# output_file_path = 'output.md'
# with open(output_file_path, 'w') as output_file:
#    output_file.write(markdown_output)

# print(f"Markdown output saved to {output_file_path}")
# print(markdown_output)


def display_markdown(markdown_content):
    display(Markdown(markdown_content))
    

def print_dataset_detail_info(data,dataset_name):
    markdown = json_to_markdown(data[dataset_name], level=0)
    result = display_markdown(markdown)
    
    return result 
# json_data = load_json(json_path)
# print_dataset_detail_info(json_data,"SYNTHESEYES")


def load_and_display_markdown(markdown_file_path):
    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    display(Markdown(markdown_content))
# example
# markdown_file_path = 'output.md'
# load_and_display_markdown(markdown_file_path)            


def print_datasets_with_landmark_value(data):
    for dataset_name in json_data.get("Data_list", []):
        if dataset_name in data:
            count = 0
            name_list = []
            for key, value in data[dataset_name].items():
                if key == 'Name' :
                    name_list.append(value)
                    count += 1
                if isinstance(value, dict) and key == "Annotation" and value['landmark'] is not None:
                    print("Dataset with landmark value:", name_list[count-1])
# example
# json_data = load_json(json_path)
# print_datasets_with_landmark_value(json_data)


def print_datasets_with_gaze_value(data):
    for dataset_name in json_data.get("Data_list", []):
        if dataset_name in data:
            count = 0
            name_list = []
            for key, value in data[dataset_name].items():
                if key == 'Name' :
                    name_list.append(value)
                    count += 1
                if isinstance(value, dict) and key == "Annotation" and value['gaze'] is not None:
                    print("Dataset with gaze value:", name_list[count-1])
# example
#json_data = load_json(json_path)  
#print_datasets_with_gaze_value(json_data)


def print_datasets_with_head_value(data):
    for dataset_name in json_data.get("Data_list", []):
        if dataset_name in data:
            count = 0
            name_list = []
            for key, value in data[dataset_name].items():
                if key == 'Name' :
                    name_list.append(value)
                    count += 1
                if isinstance(value, dict) and key == "Annotation" and value['head'] is not None:
                    print("Dataset with head value:", name_list[count-1])
# example
# json_data = load_json(json_path)
# print_datasets_with_head_value(json_data)