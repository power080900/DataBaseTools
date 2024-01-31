import seaborn as sns
import matplotlib.pyplot as plt
import cv2
import SQL_utils as SU

def draw_heatmap(dataset, xlabel, ylabel, save_name, unit='degree', font_size=20,reverse=False):
    plt.figure(figsize=(16, 12))
    sns.heatmap(data=dataset, cmap='YlGnBu', annot=True, fmt="d", linewidths=.5, annot_kws={"size": font_size})
    plt.xlabel(f'{xlabel}_{unit}', fontsize=font_size)
    plt.xticks(fontsize=20)
    plt.ylabel(f'{ylabel}_{unit}', fontsize=font_size)
    plt.yticks(fontsize=20)
    if reverse == True: 
        plt.gca().invert_yaxis()
    plt.savefig(save_name)
    print('save',save_name)

def draw_jointplot(dataset, xlabel, ylabel, save_name, unit='degree', reverse=False):
    plt.figure(figsize=(16, 12))
    sns.jointplot(x=xlabel, y=ylabel, data=dataset, kind='kde', cmap='RdYlGn')
    plt.xlabel(f'{xlabel}_{unit}', fontsize=20)
    plt.ylabel(f'{ylabel}_{unit}', fontsize=20)
    if reverse == True: 
        plt.gca().invert_yaxis()
    plt.savefig(save_name)
    print('save',save_name)

def save_frames_from_video(video_path, output_folder):
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
        
    # example
    #if __name__ == "__main__":
    #    video_path = "nsmount/TEyeD_GazeinTheWild/data/IR/resize_videodata/GW_2/GW_2_1_resize.mp4"
    #    output_folder = "GW_2_1"
    
    #    os.makedirs(output_folder, exist_ok=True)

    #    save_frames_from_video(video_path, output_folder)
    
    import matplotlib.pyplot as plt
import EDA_utils as EU

def image_visualization(dataset_name, index):
    
    img_dir = SU.MakeSQL.load_img_dir(dataset_name)
    
    # Modify the route to suit your own
    # if mac
    file_name = str(img_dir.loc[index, 'img_dir']).replace("DataBase", "nsmount")
    # if window
    #file_name = 
    
    image = plt.imread(file_name)

    plt.imshow(image)
    plt.show()
    
    # example
    # dataset_name = "ETH_Xgaze"
    # index = 1

    # image_visualization(dataset_name, index)
    
    