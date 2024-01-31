- ``Name``: **EYE_GAZE_DATA_SET**

- ``Data_list``: **['MpiiGaze', 'Sysnthetic Human Eyes(Kaggle)', 'RIT-Eyes', 'NVGaze', 'SYNTHESEYES', 'UNITYEYES', 'UTMULTIVIEW', 'ShanghaiTechGaze', 'Eye_Gaze', 'TeyeD_GazeinTheWild', 'TeyeD_Dikablis', 'U2Eyes', 'GI4E', 'ETH-gaze', 'ETH-Xgaze', 'RT-GENE', 'GazeCapture', 'Gaze360', 'EYEDIAP', 'OpenEDS : Open Eye Dataset']**

- ``Data_list_number``: **20**

- ``ShanghaiTechGaze``:
    - ``Name``: **ShanghaiTechGaze**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``: **467592**

        - ``id``: **137**

    - ``Path``:
        - ``Official_URL``: **https://github.com/dongzelian/multi-view-gaze**

        - ``Relavant_URL``: **https://sci-hub.se/10.1109/TNNLS.2018.2865525**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/ShanghaiTechGaze**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **RGB**

    - ``Format``:
        - ``image ``: **jpg**

        - ``label``: **mat**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **90X90**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **Ground truth of normalized 2D gaze direction vector**

        - ``head``: **None**

        - ``landmark``:
            - ``2D_Eye``: **6 points - normalized  value**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``UTMULTIVIEW``:
    - ``Name``: **UTMULTIVIEW**

    - ``Volume``:
        - ``total``:
            - ``original``: **1280**

            - ``crop``: **1216000**

        - ``id``: **50**

    - ``Path``:
        - ``Official_URL``: **https://www.ut-vision.org/datasets/**

        - ``Relavant_URL``: **https://www.cv-foundation.org/openaccess/content_cvpr_2014/html/Sugano_Learning-by-Synthesis_for_Appearance-based_2014_CVPR_paper.html**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/UTMULTIVIEW**

    - ``Type``:
        - ``original``: **RGB**

        - ``crop``: **Grayscale**

    - ``Format``:
        - ``image ``: **jpg**

        - ``label``: **mat**

    - ``Resolution``:
        - ``original``: **1280X1024**

        - ``crop``: **60X36**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **Ground truth of normalized 2D gaze direction vector**

            - ``3D_Gaze``: ****

        - ``head``:
            - ``2D_Head``: **6 points - normalized  value**

            - ``3D_Head``: ****

        - ``landmark``: **None**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``UNITYEYES``:
    - ``Name``: **UNITYEYES**

    - ``Volume``:
        - ``total``: **None**

        - ``id``: **None**

    - ``Path``:
        - ``Official_URL``: **https://www.cl.cam.ac.uk/research/rainbow/projects/unityeyes/**

        - ``Relavant_URL``: **https://www.cl.cam.ac.uk/research/rainbow/projects/unityeyes/tutorial.html**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/UNITYEYES**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **None**

    - ``Format``:
        - ``image ``: **None**

        - ``label``: **None**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **None**

    - ``Annotation``:
        - ``gaze``: **None**

        - ``head``: **None**

        - ``landmark``: **None**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``SYNTHESEYES``:
    - ``Name``: **SYNTHESEYES**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``: **11382**

        - ``id``: **10**

    - ``Path``:
        - ``Official_URL``: **https://www.cl.cam.ac.uk/research/rainbow/projects/syntheseyes/**

        - ``Relavant_URL``: **None**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/SYNTHESEYES**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **RGB**

    - ``Format``:
        - ``image ``: **png**

        - ``label``: **pkl**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **120X80**

    - ``Annotation``:
        - ``gaze``:
            - ``3D_Gaze``: **the 3D gaze direction in camera space**

        - ``head``:
            - ``3D_Head``: **3x3 matrix rotation from world space to camera space**

        - ``landmark``:
            - ``2D_Lids``: **containing the following 2D lids landmarks in screen space**

            - ``3D_Lids``: **containing the following 3D lids landmarks in camera space**

            - ``2D_Iris``: **containing the following 2D iris landmarks in screen space**

            - ``3D_Iris``: **containing the following 3D iris landmarks in camera space**

            - ``2D_Pupil``: **containing the following 2D pupil landmarks in screen space**

            - ``3D_Pupil``: **containing the following 3D pupil landmarksin camera space**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``NVGaze``:
    - ``Name``: **NVGaze**

    - ``Volume``:
        - ``total``:
            - ``original``: ****

            - ``crop``: ****

        - ``id``: ****

    - ``Path``:
        - ``Official_URL``: ****

        - ``Relavant_URL``: ****

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/NVGaze**

    - ``Type``:
        - ``original``: ****

        - ``crop``: ****

    - ``Format``:
        - ``image ``: ****

        - ``label``: ****

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: ****

    - ``Annotation``:
        - ``gaze``:
            - ````: ****

        - ``head``:
            - ````: ****

        - ``landmark``:
            - ````: ****

        - ``camera``:
            - ````: ****

        - ``eye_info``: **None**

- ``RIT-Eyes``:
    - ``Name``: **RIT-Eyes**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``:
                - ``S_general``: **48000**

                - ``S_natural``: **48000**

                - ``S_nvgaze``: **51600**

                - ``S_openeds``: **51600**

        - ``id``: **24**

    - ``Path``:
        - ``Official_URL``: **https://cs.rit.edu/~cgaplab/RIT-Eyes/**

        - ``Relavant_URL``: **https://arxiv.org/pdf/2006.03642v1.pdf**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/RIT-Eyes**

    - ``Type``:
        - ``original``: **None**

        - ``crop``:
            - ``S_general``: **IR **

            - ``S_natural``: **RGB **

            - ``S_nvgaze``: **IR **

            - ``S_openeds``: **IR **

    - ``Format``:
        - ``image ``: **tif**

        - ``label``: **p**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``:
            - ``S_general``: **640X480**

            - ``S_natural``: **640X480**

            - ``S_nvgaze``: **640X480**

            - ``S_openeds``: **400X640**

    - ``Annotation``:
        - ``gaze``:
            - ``gaze_az``: **the 2D gaze direction in camera space(rad)**

            - ``gaze_el``: **the 2D gaze direction in camera space(rad)**

        - ``head``: **None**

        - ``landmark``:
            - ``iris_loc``: ****

            - ``eye_loc``: ****

            - ``eye_lid``: ****

            - ``pupil``: ****

            - ``iris_rot``: ****

            - ``left_corner``: ****

            - ``right_corner``: ****

            - ``sclera``: ****

        - ``camera``:
            - ``3D_camera_center``: ****

            - ``camera_distance``: ****

            - ``camera_az(rad)``: ****

            - ``camera_el(rad)``: ****

            - ``ortho_scale``: ****

        - ``eye_info``:
            - ``glasses``: ****

- ``Sysnthetic Human Eyes``:
    - ``Name``: **Synthetic Human Eyes**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``: **49999**

        - ``id``: **24**

    - ``Path``:
        - ``Official_URL``: **https://cs.rit.edu/~cgaplab/RIT-Eyes/**

        - ``Relavant_URL``: **https://arxiv.org/pdf/2006.03642v1.pdf**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/Sysnthetic Human Eyes**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **RGB**

    - ``Format``:
        - ``image ``: **png**

        - ``label``: **json**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **640X360**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **the 3D gaze direction in camera space**

            - ``3D_Gaze``: **3x3 matrix rotation from world space to camera space**

        - ``head``: **None**

        - ``landmark``:
            - ``pupiloffset``: ****

            - ``EyelidLower1``: ****

            - ``EyelidLower2``: ****

            - ``EyelidLower3``: ****

            - ``EyeCornerOuter``: ****

            - ``EyeCornerOuter1``: ****

            - ``EyeCornerOuter2``: ****

            - ``EyeCornerInner``: ****

            - ``EyeCornerInner1``: ****

            - ``EyeCornerInner2``: ****

            - ``EyePupil``: ****

            - ``EyelidUpper1``: ****

            - ``EyelidUpper2``: ****

            - ``EyelidUpper3``: ****

        - ``camera``:
            - ``ViewProjection``: ****

        - ``eye_info``:
            - ``Side``: ****

            - ``EyeBlink``: ****

            - ``EyeLookDown``: ****

            - ``EyeLookIn``: ****

            - ``EyeLookOut``: ****

            - ``EyeLookUp``: ****

            - ``EyeSquint``: ****

            - ``EyeWide``: ****

- ``U2Eyes``:
    - ``Name``: **U2Eyes**

    - ``Volume``:
        - ``total``:
            - ``original``: **117500**

            - ``crop``: **None**

        - ``id``: ****

    - ``Path``:
        - ``Official_URL``: **https://www.unavarra.es/gi4e/databases/u2eyes**

        - ``Relavant_URL``: **https://openaccess.thecvf.com/content_ICCVW_2019/papers/OpenEDS/Porta_U2Eyes_A_Binocular_Dataset_for_Eye_Tracking_and_Gaze_Estimation_ICCVW_2019_paper.pdf**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/U2Eyes**

    - ``Type``:
        - ``original``: **RGB **

        - ``crop``: **None**

    - ``Format``:
        - ``image ``: **png**

        - ``label``:
            - ``original``: **xml**

            - ``crop``: **None**

    - ``Resolution``:
        - ``original``: **3840 X 2160**

        - ``crop``: **None**

    - ``Annotation``:
        - ``gaze``: **None**

        - ``head``:
            - ``Rotation``: **x,y,z (roll,pitch,yaw)**

            - ``Position``: **x,y,z (coordinate)**

            - ``LookAtPoint``: **x,y,z (coordinate)**

        - ``landmark``:
            - ``2D_Caruncle``: ****

            - ``3D_Caruncle``: ****

            - ``2D_InteriorMargin``: ****

            - ``3D_InteriorMargin``: ****

            - ``2D_Iris``: ****

            - ``3D_Iris``: ****

            - ``2D_Pupil``: ****

            - ``3D_Pupil``: ****

            - ``2D_CorneaCenter``: ****

            - ``3D_CorneaCenter``: ****

            - ``2D_GlobeCenter``: ****

            - ``3D_GlobeCenter``: ****

            - ``2D_IrisCenter``: ****

            - ``3D_IrisCenter``: ****

            - ``2D_PupilCenter``: ****

            - ``3D_PupilCenter``: ****

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``GI4E``:
    - ``Name``: **GI4E**

    - ``Volume``:
        - ``total``:
            - ``original``: **1236**

            - ``crop``: **None**

        - ``id``: ****

    - ``Path``:
        - ``Official_URL``: **https://www.unavarra.es/gi4e/databases/gi4e/?languageId=1**

        - ``Relavant_URL``: **None**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/GI4E**

    - ``Type``:
        - ``original``: **RGB**

        - ``crop``: **None**

    - ``Format``:
        - ``image ``: **png**

        - ``label``:
            - ``original``: **txt**

            - ``crop``: **None**

    - ``Resolution``:
        - ``original``: **800X600**

        - ``crop``: **None**

    - ``Annotation``:
        - ``gaze``: **None**

        - ``head``: **None**

        - ``landmark``:
            - ``Eye_landmark``: **3 points - value**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``ETH-Xgaze``:
    - ``Name``: **ETH-Xgaze**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``: **1083492**

        - ``id``: **110**

    - ``Path``:
        - ``Official_URL``: **https://ait.ethz.ch/xgaze**

        - ``Relavant_URL``: **https://files.ait.ethz.ch/projects/xgaze/xucongzhang2020eccv.pdf**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/ETH-Xgaze**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **RGB **

    - ``Format``:
        - ``image ``: **jpg**

        - ``label``:
            - ``original``: **None**

            - ``crop``: **label**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **448X448**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **the normalized gaze direction with size of 2 dimensions as horizontal and vertical gaze directions.**

        - ``head``:
            - ``2D_Head``: **the normalized head pose with size of 2 dimensions horizontal and vertical head rotations.**

        - ``landmark``: **None**

        - ``camera``:
            - ``face_patch``: **the face patch image with size of number of samples * 448 * 448 * 3**

            - ``face_mat_norm``: **the rotation matrix during data normalization**

            - ``cam_index``: **the camera index of the image range from 0 to 17**

        - ``eye_info``: **None**

- ``RT-GENE``:
    - ``Name``: **RT-GENE**

    - ``Volume``:
        - ``total``:
            - ``original``: **326895**

            - ``crop``:
                - ``left_eye``: **326895**

                - ``right_eye``: **326895**

        - ``id``: ****

    - ``Path``:
        - ``Official_URL``: **https://zenodo.org/records/2529036**

        - ``Relavant_URL``: **['https://github.com/Tobias-Fischer/rt_gene', 'https://openaccess.thecvf.com/content_ECCV_2018/papers/Tobias_Fischer_RT-GENE_Real-Time_Eye_ECCV_2018_paper.pdf', 'https://openaccess.thecvf.com/content_ICCVW_2019/papers/GAZE/Cortacero_RT-BENE_A_Dataset_and_Baselines_for_Real-Time_Blink_Estimation_in_ICCVW_2019_paper.pdf']**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/RT-GENE**

    - ``Type``:
        - ``original``: **RGB**

        - ``crop``: **RGB**

    - ``Format``:
        - ``image ``: **png**

        - ``label``:
            - ``original``: **label**

            - ``crop``: **label**

    - ``Resolution``:
        - ``original``: **224X224**

        - ``crop``: **224X224**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **Ground truth of 2D gaze direction vector i.e. yaw and pitch.**

            - ``3D_Gaze``: **Ground truth of normalized 3D gaze direction vector**

        - ``head``:
            - ``2D_Head``: **Ground truth of normalized 2D head orientation vector.**

            - ``3D_Head``: **Ground truth of normalized 3D head orientation vector.**

        - ``landmark``: **None**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``GazeCapture``:
    - ``Name``: **GazeCapture**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``: **124831**

        - ``id``: **None**

    - ``Path``:
        - ``Official_URL``: **http://gaze360.csail.mit.edu**

        - ``Relavant_URL``: **['https://openaccess.thecvf.com/content_ICCV_2019/papers/Kellnhofer_Gaze360_Physically_Unconstrained_Gaze_Estimation_in_the_Wild_ICCV_2019_paper.pdf', 'https://phi-ai.buaa.edu.cn/Gazehub/3D-dataset/#gaze360']**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/GazeCapture**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **RGB **

    - ``Format``:
        - ``image ``: **jpg**

        - ``label``:
            - ``original``: **None**

            - ``crop``: **label**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **224X224**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **Ground truth of 2D gaze direction vector i.e. yaw and pitch.**

            - ``3D_Gaze``: **Ground truth of normalized 3D gaze direction vector**

        - ``head``: **None**

        - ``landmark``: **None**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``Gaze360``:
    - ``Name``: **Gaze360**

    - ``Volume``:
        - ``total``:
            - ``original``: **None**

            - ``crop``: **124831**

        - ``id``: **None**

    - ``Path``:
        - ``Official_URL``: **http://gaze360.csail.mit.edu**

        - ``Relavant_URL``: **['https://openaccess.thecvf.com/content_ICCV_2019/papers/Kellnhofer_Gaze360_Physically_Unconstrained_Gaze_Estimation_in_the_Wild_ICCV_2019_paper.pdf', 'https://phi-ai.buaa.edu.cn/Gazehub/3D-dataset/#gaze360']**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/Gaze360**

    - ``Type``:
        - ``original``: **None**

        - ``crop``: **RGB **

    - ``Format``:
        - ``image ``: **jpg**

        - ``label``:
            - ``original``: **None**

            - ``crop``: **label**

    - ``Resolution``:
        - ``original``: **None**

        - ``crop``: **224X224**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **Ground truth of 2D gaze direction vector i.e. yaw and pitch.**

            - ``3D_Gaze``: **Ground truth of normalized 3D gaze direction vector**

        - ``head``: **None**

        - ``landmark``: **None**

        - ``camera``: **None**

        - ``eye_info``: **None**

- ``MpiiGaze``:
    - ``Name``: **MpiiGaze**

    - ``Volume``:
        - ``total``:
            - ``original``: **213658**

            - ``crop``: **427316**

        - ``id``: **None**

    - ``Path``:
        - ``Official_URL``: **https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild**

        - ``Relavant_URL``: **['https://phi-ai.buaa.edu.cn/Gazehub/3D-dataset/#mpiifacegaze', 'https://phi-ai.buaa.edu.cn/Gazehub/Guideline/EyeBased/MPIIGaze.pdf']**

        - ``IP``: **192.168.0.128:5002(Synology)**

        - ``DIR``: **DataBase/MpiiGaze**

    - ``Type``:
        - ``original``: **RGB**

        - ``crop``: **Grayscale**

    - ``Format``:
        - ``image ``: **jpg**

        - ``label``:
            - ``original``: **mat**

            - ``crop``: **label**

    - ``Resolution``:
        - ``original``: **1280X720**

        - ``crop``: **60X36**

    - ``Annotation``:
        - ``gaze``:
            - ``2D_Gaze``: **Ground truth of normalized 2D gaze direction vector(rad)**

            - ``3D_Gaze``: **Ground truth of normalized 3D gaze direction vector(rad)**

            - ``Gaze_Origin``: **Origin of 3D gaze vector in the normalized CCS**

        - ``head``:
            - ``2D_Head``: **Ground truth of normalized 2D head orientation vector**

            - ``3D_Head``: **Ground truth of normalized 3D head orientation vector.**

        - ``landmark``: **None**

        - ``camera``:
            - ``Rmat``: **Rotation vector from original Camera Coordinate System (CCS) to the normalized CCS**

            - ``Smat``: **The diagonal elements of the scale matrix used in the normalization procedure**

        - ``eye_info``: **None**

- ``Eye_Gaze``:
- ``TeyeD_GazeinTheWild``:
- ``TeyeD_Dikablis``:
- ``OpenEDS : Open Eye Dataset``:
- ``EYEDIAP``:
