import cv2
from cropper.cropper import crop_card
from detector.detector import detect_info
from reader import reader


def tat_ca_tinh_tuy_tap_hop_o_trong_function_nay(path_to_image="img.jpg"):

    img = cv2.imread(path_to_image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plot_img(img)

    warped = crop_card(path_to_image)
    if warped is None:
        print('Cant find id card in image 1')
        # sys.exit()
        return None

    try:
        face, number_img, name_img, dob_img, gender_img, nation_img, country_img, \
            address_img, country_img_list, address_img_list = detect_info(
                warped)
    except:
        print('Cant find id card in image 2')
        # sys.exit()
        return None

    # list_image = [face, number_img, name_img, dob_img,
    #             gender_img, nation_img, country_img, address_img]

    number_text = reader.get_id_numbers_text(number_img)
    name_text = reader.get_name_text(name_img)
    dob_text = reader.get_dob_text(dob_img)
    gender_text = reader.get_gender_text(gender_img)
    nation_text = reader.get_nation_text(nation_img)
    country_text = reader.process_list_img(country_img_list, is_country=True)
    address_text = reader.process_list_img(address_img_list, is_country=False)

    texts = {'Số': number_text,
             'Họ và tên': name_text,
             'Ngày tháng năm sinh': dob_text,
             'Giới tính': gender_text,
             'Quốc tịch': nation_text,
             'Quê quán': country_text,
             'Nơi thường trú': address_text}
    return texts


print(tat_ca_tinh_tuy_tap_hop_o_trong_function_nay(
    "/Users/macintosh/Downloads/2.jpg"))
