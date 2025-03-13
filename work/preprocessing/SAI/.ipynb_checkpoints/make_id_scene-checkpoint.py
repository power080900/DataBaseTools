import os
import json
import itertools


# 원본 파일 경로
org_dir = "C:\\lee\\work\\SAI\\json\\id_org"
org_files = os.listdir(org_dir)
ids = [
    4297,1128,2776,8228,6744, # Male_Asian
    1139,8433,7219,7658,1127, # Female_Asian
    7032,5675,7066,6360,56, # Male_Black
    7415,5855,8412,2902,6565, # Female_Black
    8692,4201,7839,5582,1476, # Male_Hispanic
    1126,7038,4844,6803,679, # Female_Hispanic
    6201,2464,8384,8596,1176, # Male_indian
    1564,3582,5860,6915,5927, # Female_indian
    408, 2124,2364,2439,7592, # Male_White
    499, 1173,362, 4032,325 #Female_White
        ]
        
glasses = [
  {
    "sex_matched_only": True,
    "style": [
      "all"
    ],
    "lens_color": [
      "black"
    ],
    "metalness": {
      "type": "list",
      "values": [
        0,
        1
      ]
    },
    "transparency": {
      "type": "range",
      "values": {
        "max": 1,
        "min": 0
      }
    },
    "percent": 10
  },
  {
    "sex_matched_only": True,
    "style": [
      "all"
    ],
    "lens_color": [
      "default"
    ],
    "metalness": {
      "type": "list",
      "values": [
        0,
        1
      ]
    },
    "transparency": {
      "type": "range",
      "values": {
        "max": 0.15,
        "min": 0
      }
    },
    "percent": 15
  },
  {
    "sex_matched_only": True,
    "style": [
      "all"
    ],
    "lens_color": [
      "default"
    ],
    "metalness": {
      "type": "list",
      "values": [
        0,
        1
      ]
    },
    "transparency": {
      "type": "range",
      "values": {
        "max": 1,
        "min": 0.7
      }
    },
    "percent": 15
  },
  {
    "sex_matched_only": True,
    "style": [
      "none"
    ],
    "lens_color": [
      "default"
    ],
    "metalness": {
      "type": "list",
      "values": [
        0
      ]
    },
    "transparency": {
      "type": "list",
      "values": [
        1
      ]
    },
    "percent": 60
  }
]

headwear=  [
          {
            "style": [
              "all"
            ],
            "sex_matched_only": True,
            "percent": 30
          },
          {
            "style": [
              "none"
            ],
            "sex_matched_only": True,
            "percent": 70
          }
]

gesture = [
        {
          "percent": 60,
          "name": [
            "vehicle_answer_phone_talk",
            "vehicle_asleep_back_02",
            "vehicle_asleep_forward_02",
            "vehicle_asleep_back_03",
            "vehicle_asleep_forward_03",
            "vehicle_asleep_left_02",
            "vehicle_asleep_right_02",
            "vehicle_asleep_left_03",
            "vehicle_asleep_right_03",
            "vehicle_chat_left",
            "vehicle_chat_right",
            "vehicle_counting_in_1",
            "vehicle_counting_in_2",
            "vehicle_counting_in_3",
            "vehicle_counting_in_4",
            "vehicle_counting_in_5",
            "vehicle_counting_out_1",
            "vehicle_counting_out_3",
            "vehicle_counting_out_2",
            "vehicle_counting_out_4",
            "vehicle_counting_out_5",
            "vehicle_hand_talking_1",
            "vehicle_hand_talking_4",
            "vehicle_look_left",
            "vehicle_look_over_shoulder",
            "vehicle_look_right",
            "vehicle_phone_check_quick",
            "vehicle_pointing_vertical_surface",
            "vehicle_pour",
            "vehicle_radio_reach",
            "vehicle_relaxed",
            "vehicle_shhhh",
            "vehicle_whisper",
            "vehicle_wave_hello",
            "vehicle_shrug_hands_out",
            "vehicle_shake_head_no",
            "vehicle_opens_arms_hand_talking",
            "vehicle_ok",
            "vehicle_head_down",
            "vehicle_chat_side"
          ],
          "keyframe_only": True,
          "mirrored": False,
          "position_seed": {
            "type": "list",
            "values": [
              0
            ]
          }
        },
        {
          "percent": 20,
          "name": [
            "vehicle_default"
          ],
          "keyframe_only": True,
          "mirrored": False,
          "position_seed": {
            "type": "list",
            "values": [
              0
            ]
          }
        },
        {
          "percent": 20,
          "name": [
            "vehicle_at_ear_right_phone_10",
            "vehicle_drink_from_glass",
            "vehicle_drink_from_cup",
            "vehicle_talk_mic_left_phone_12",
            "vehicle_tap_texting_left_phone_13",
            "vehicle_viewing_left_phone_10",
            "vehicle_viewing_right_phone_12"
          ],
          "keyframe_only": True,
          "mirrored": False,
          "position_seed": {
            "type": "list",
            "values": [
              0
            ]
          }
        }
      ]
clothing = [
        {
          "percent": 100,
          "outfit": [
            "all"
          ],
          "sex_matched_only": True,
          "single_style_per_id": True
        }
      ]

fat = ['highest','higher','median','lower','lowest']
height = ['tallest','taller','tall','median','short','shorter','shortest']

combinations = list(itertools.product(fat, height))



for i in range(10,65):
    fat_content, height_content = combinations[i % len(combinations)]

    body = [{
          "enabled": True,
          "fat_content": [
            f"{fat_content}"
          ],
          "height": [
            f"{height_content}"
          ],
          "percent": 100
        }]

    # 변경된 파일 경로
    modified_dir = f"C:\\lee\\work\\SAI\\json\\id_{i:02d}"
    merged_humans = []
    for num, org_file in enumerate(org_files):
        
        image_per_id = {'1':50,'2':30,'3':30,'4':49,
                        '5':30,'6':28,'7':28,'8':30,
                        '9':30,'10':28,'11':28,'12':30,
                        '13':50,'14':30,'15':30,'16':49,
                        '17':30,'18':28,'19':28,'20':30,
                        '21':28,'22':26,'23':26,'24':28,
                        '25':28,'26':26,'27':26,'28':28,
                        '29':30,'30':28,'31':28,'32':30,
                        '33':30,'34':28,'35':28,'36':30,
                        '37':28,'38':26,'39':26,'40':28,
                        '41':28,'42':26,'43':26,'44':28,
                        '45':30,'46':28,'47':28,'48':30,
                        '49':50,'50':30,'51':30,'52':49,
                        '53':30,'54':28,'55':28,'56':30,
                        '57':50,'58':30,'59':30,'60':49,
                        '61':30,'62':28,'63':28,'64':30}
        print(org_file,image_per_id[f'{num+1}'])

        if not os.path.exists(modified_dir):
            os.makedirs(modified_dir)

        # 파일 경로
        original_file_path = os.path.join(org_dir, org_file)
        modified_file_path = os.path.join(modified_dir, f'id_{i:02d}_{org_file}')
        # 원본 파일 열기
        with open(original_file_path, "r") as original_file:
            # JSON 데이터 읽기
            data = json.load(original_file)
            
            # ids 변경
            data["humans"][0]["identities"]["renders_per_identity"] = image_per_id[f'{num+1}']
            data["humans"][0]["identities"]["ids"][0] = ids[i]
            data["humans"][0]["accessories"]["glasses"] = glasses
            data["humans"][0]["accessories"]["headwear"] = headwear
            data["humans"][0]["gesture"] = gesture
            data["humans"][0]['clothing'] = clothing
            data["humans"][0]['body'] = body

        # 변경된 내용을 새 파일에 쓰기
        with open(modified_file_path, "w") as modified_file:
            # JSON 데이터 쓰기
            json.dump(data, modified_file, indent=4)