import os.path as osp
import os
import pandas as pd

DEFAULT_ROOT_DIR = osp.join(osp.dirname(osp.dirname(osp.abspath(osp.dirname(__file__)))))

DEFAULT_KEYBOARD_DATASET_DIR = osp.join(DEFAULT_ROOT_DIR, 'data', 'kbd')

keys_for_labeling = ['screenshot_name', 'keyboard_name', 'keyboard_index',
                     # basic info about the screenshot
                     'text', 'theme', 'border', 'mode', 'number_row', 'word_prediction',
                     # coordinate of texts
                     'input_box', 'predictive_text_1', 'predictive_text_2', 'predictive_text_3',
                     # coordinate of characters
                     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                     'z', 'x', 'c', 'v', 'b', 'n', 'm',
                     # coordinate of numbers
                     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                     # coordinate of symbols
                     'backspace', 'space', 'enter', 'shift', 'symbol',
                     # punctuations
                     ",", ".", "!", "?", "-", "'"
                     ]

keyboard_index = {
    'Gboard': '00',
    'Microsoft SwiftKey': '01',
    'Fonts Keyboard': '02',
    'Emojikeyboard': '03',
    'GoKeyboardLite': '04',
    'LED Keyboard': '05',
    'Grammarly': '06',
    'Yandex Keyboard': '07',
    'Design Keyboard': '08',
    'Kika Keyboard': '09',
    'Giphy Keyboard': '10',
    'Fonts Art Keyboard': '11',
    'Stylish Text Keyboard': '12',
    'GoKeyboardPro': '13',
    'Deco Keyboard': '14',
    '2023 Keyboard': '15',
    'iKeyboard GIF Keyboard': '16',
    'Classic Big Keyboard': '17',
    'Stylish Fonts and Keyboard': '18',
    'Neon LED Keyboard': '19',
    'My Photo Keyboard With Themes': '20',
    'Facemoji Emoji Keyboard': '21',
    'Bobble Keyboard': '22',
    'Laban Key': '23',
    'Fast Typing Keyboard': '24',
    'Malayalam Keyboard': '25',
    'Ridmik Keyboard': '26',
    'Hacker\'s Keyboard': '27',
    'Decoration Text Keyboard': '28',
    'Cute Emoji Keyboard': '29',
    'iMore Keyboard': '30',
    'All Arabic Keyboard': '31',
    'CHI21_keyboard': '99',
    # just for the research project
    'Gboard_small': '001',
    'Gboard_medium': '002',
    'Gboard_large': '003',
    'SwiftKey_small': '011',
    'SwiftKey_medium': '012',
    'SwiftKey_large': '013',
    'GoKeyboard_small': '041',
    'GoKeyboard_medium': '042',
    'GoKeyboard_large': '043',
}

keyboard_name = {v: k for k, v in keyboard_index.items()}

CHI21_KEYS = {
    'screenshot_name': '99_0_1_0_0_1',
    'keyboard_name': "CHI21_keyboard",
    'keyboard_index': "99",
    'text': None,
    'theme': None,
    'border': None,
    'mode': None,
    'number_row': None,
    'word_prediction': None,
    'input_box': [0, 130, 1080, 224],
    'q': [0, 1230, 98, 1403],
    'w': [98, 1230, 196, 1403],
    'e': [196, 1230, 294, 1403],
    'r': [294, 1230, 393, 1403],
    't': [393, 1230, 492, 1403],
    'y': [492, 1230, 590, 1403],
    'u': [590, 1230, 689, 1403],
    'i': [689, 1230, 787, 1403],
    'o': [787, 1230, 886, 1403],
    'p': [886, 1230, 984, 1403],
    'å': [984, 1230, 1080, 1403],
    'a': [0, 1403, 98, 1576],
    's': [98, 1403, 196, 1576],
    'd': [196, 1403, 294, 1576],
    'f': [294, 1403, 393, 1576],
    'g': [393, 1403, 492, 1576],
    'h': [492, 1403, 590, 1576],
    'j': [590, 1403, 689, 1576],
    'k': [689, 1403, 787, 1576],
    'l': [787, 1403, 886, 1576],
    'ö': [886, 1403, 984, 1576],
    'ä': [984, 1403, 1080, 1576],
    'z': [196, 1576, 294, 1749],
    'x': [294, 1576, 393, 1749],
    'c': [393, 1576, 492, 1749],
    'v': [492, 1576, 590, 1749],
    'b': [590, 1576, 689, 1749],
    'n': [689, 1576, 787, 1749],
    'm': [787, 1576, 886, 1749],
    'backspace': [886, 1576, 1080, 1749],
    'shift': [0, 1576, 196, 1749],
    'symbol': [0, 1749, 269, 1920],
    'space': [269, 1749, 763, 1920],
    'enter': [763, 1749, 1080, 1920],
}

research_project = {
    # just for the research project
    'Gboard_small': '001',
    'Gboard_medium': '002',
    'Gboard_large': '003',
    'SwiftKey_small': '011',
    'SwiftKey_medium': '012',
    'SwiftKey_large': '013',
    'GoKeyboard_small': '041',
    'GoKeyboard_medium': '042',
    'GoKeyboard_large': '043',
}


def get_imgpath(keyboard_name, dataset_dir=DEFAULT_KEYBOARD_DATASET_DIR, size='medium'):
    """
    Get image path based on given keyboard name and dataset dir (/keyboard_dataset)
    :param keyboard_name:
    :param dataset_dir:
    :param number_row:
    :return:
    """
    # TODO: modify when there is a csv for keyboard name and index
    assert osp.exists(dataset_dir), "No dataset under current dataset dir"
    if keyboard_name == 'Gboard_small':
        img_name = '001_0_0_1_0_1.png'
    elif keyboard_name == 'Gboard_medium':
        img_name = '002_0_0_1_0_1.png'
    elif keyboard_name == 'Gboard_large':
        img_name = '003_0_0_1_0_1.png'
    elif keyboard_name == 'SwiftKey_small':
        img_name = '011_0_0_1_1_1.png'
    elif keyboard_name == 'SwiftKey_medium':
        img_name = '012_0_0_1_1_1.png'
    elif keyboard_name == 'SwiftKey_large':
        img_name = '013_0_0_1_1_1.png'
    elif keyboard_name == 'GoKeyboard_small':
        img_name = '041_0_1_1_0_1.png'
    elif keyboard_name == 'GoKeyboard_medium':
        img_name = '042_0_1_1_0_1.png'
    elif keyboard_name == 'GoKeyboard_large':
        img_name = '043_0_1_1_0_1.png'
    else:
        raise Exception("Do not have {}".format(keyboard_name))
    return dataset_dir + '/' + img_name


def load_dataframe(save_path=DEFAULT_KEYBOARD_DATASET_DIR, file_name='research_project.csv'):
    """
    load the saved csv and make sure the coordinate type is list
    """
    df = pd.read_csv(osp.join(save_path, file_name), header=0, index_col=0)
    if 'chi' in file_name:
        return df
    else:
        indexs = df.index
        columns = df.columns
        new_df = pd.DataFrame(columns=keys_for_labeling, index=['index'])
        for index in indexs:
            for column in columns:
                info = df.loc[index, column]
                if isinstance(info, str) and '[' in info:
                    x_str = info.strip('][').split(', ')
                    new_df.loc[index, column] = list(map(int, x_str))
                else:
                    new_df.loc[index, column] = info
        # print(new_df)
    return new_df
