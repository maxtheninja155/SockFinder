'''
    Authors: Zach Klein and Maxwell Wainwright
    Date Created: 10.21.23
    Date Altered:
    Purpose: When an image of a sock is loaded, it will look at a database of socks
    and give you your matching sock that has simular colors.
'''

import cv2 as cv
import webcolors


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def get_uploadedpic_color(input_picture_path):
    read_file = cv.imread(input_picture_path)
    center_columnT = int(read_file.shape[0] / 2)
    center_rowT = int(read_file.shape[1] / 2)
    center_pxT = read_file[center_columnT, center_rowT]
    requested_colour = [center_pxT[0], center_pxT[1], center_pxT[2]]
    actual_name, closest_name = get_colour_name(requested_colour)

    return closest_name
    # print("Actual colour name:", actual_name, ", closest colour name:", closest_name)


def get_simular_sock(input_picture_path):
    input_sock_color_name = get_uploadedpic_color(input_picture_path)
    with open('socks_center_pixel.csv', 'r') as datafile:
        for value in datafile.readlines():
            csv_value = value.split(',')
            csv_value[2] = csv_value[2].strip()
            if input_sock_color_name == csv_value[2]:
                return csv_value[0]


'''
socks_data_images = ['socks_images/product_images/1.jpg',
                     'socks_images/product_images/2.jpg',
                     'socks_images/product_images/3.jpg',
                     'socks_images/product_images/4.jpg',
                     'socks_images/product_images/5.jpg',
                     'socks_images/product_images/6.jpg',
                     'socks_images/product_images/7.jpg',
                     'socks_images/product_images/8.jpg',
                     'socks_images/product_images/9.jpg',
                     'socks_images/product_images/10.jpg',
                     'socks_images/product_images/11.jpg',
                     'socks_images/product_images/12.jpg',
                     'socks_images/product_images/13.jpg',
                     'socks_images/product_images/14.jpg',
                     'socks_images/product_images/15.jpg',
                     'socks_images/product_images/16.jpg',
                     'socks_images/product_images/17.jpg',
                     'socks_images/product_images/18.jpg',
                     'socks_images/product_images/19.jpg',
                     'socks_images/product_images/20.jpg',
                     'socks_images/product_images/21.jpg',
                     'socks_images/product_images/22.jpg',
                     'socks_images/product_images/23.jpg',
                     'socks_images/product_images/24.jpg',
                     'socks_images/product_images/25.jpg',
                     'socks_images/product_images/26.jpg',
                     'socks_images/product_images/27.jpg',
                     'socks_images/product_images/28.jpg',
                     'socks_images/product_images/29.jpg',
                     'socks_images/product_images/30.jpg',
                     'socks_images/product_images/31.jpg',
                     'socks_images/product_images/32.jpg',
                     'socks_images/product_images/33.jpg',
                     'socks_images/product_images/34.jpg',
                     'socks_images/product_images/35.jpg',
                     'socks_images/product_images/36.jpg',
                     'socks_images/product_images/37.jpg',
                     'socks_images/product_images/38.jpg',
                     'socks_images/product_images/39.jpg',
                     'socks_images/product_images/40.jpg',
                     'socks_images/product_images/41.jpg',
                     'socks_images/product_images/42.jpg',
                     'socks_images/product_images/43.jpg',
                     'socks_images/product_images/44.jpg',
                     'socks_images/product_images/45.jpg',
                     'socks_images/product_images/46.jpg',
                     'socks_images/product_images/47.jpg',
                     'socks_images/product_images/48.jpg',
                     'socks_images/product_images/49.jpg',
                     'socks_images/product_images/50.jpg',
                     'socks_images/product_images/51.jpg',
                     'socks_images/product_images/52.jpg',
                     'socks_images/product_images/53.jpg',
                     'socks_images/product_images/54.jpg',
                     'socks_images/product_images/55.jpg',
                     'socks_images/product_images/56.jpg',
                     'socks_images/product_images/57.jpg',
                     'socks_images/product_images/58.jpg',
                     'socks_images/product_images/59.jpg',
                     'socks_images/product_images/60.jpg',
                     'socks_images/product_images/61.jpg',
                     'socks_images/product_images/62.jpg',
                     'socks_images/product_images/63.jpg',
                     'socks_images/product_images/64.jpg',
                     'socks_images/product_images/65.jpg',
                     'socks_images/product_images/66.jpg',
                     'socks_images/product_images/67.jpg',
                     'socks_images/product_images/68.jpg',
                     'socks_images/product_images/69.jpg',
                     'socks_images/product_images/70.jpg',
                     'socks_images/product_images/71.jpg',
                     'socks_images/product_images/72.jpg',
                     'socks_images/product_images/73.jpg',
                     'socks_images/product_images/74.jpg',
                     'socks_images/product_images/75.jpg',
                     'socks_images/product_images/76.jpg',
                     'socks_images/product_images/77.jpg',
                     'socks_images/product_images/78.jpg',
                     'socks_images/product_images/79.jpg',
                     'socks_images/product_images/80.jpg',
                     'socks_images/product_images/81.jpg',
                     'socks_images/product_images/82.jpg',
                     'socks_images/product_images/83.jpg',
                     'socks_images/product_images/84.jpg',
                     'socks_images/product_images/85.jpg',
                     'socks_images/product_images/86.jpg',
                     'socks_images/product_images/87.jpg',
                     'socks_images/product_images/88.jpg',
                     'socks_images/product_images/89.jpg',
                     'socks_images/product_images/90.jpg',
                     'socks_images/product_images/91.jpg',
                     'socks_images/product_images/92.jpg',
                     'socks_images/product_images/93.jpg',
                     'socks_images/product_images/94.jpg',
                     'socks_images/product_images/95.jpg',
                     'socks_images/product_images/96.jpg',
                     'socks_images/product_images/97.jpg',
                     'socks_images/product_images/98.jpg',
                     'socks_images/product_images/99.jpg',
                     'socks_images/product_images/101.jpg',
                     'socks_images/product_images/102.jpg',
                     'socks_images/product_images/103.jpg',
                     'socks_images/product_images/104.jpg',
                     'socks_images/product_images/105.jpg',
                     'socks_images/product_images/106.jpg',
                     'socks_images/product_images/107.jpg',
                     'socks_images/product_images/108.jpg',
                     'socks_images/product_images/109.jpg',
                     'socks_images/product_images/110.jpg',
                     'socks_images/product_images/111.jpg',
                     'socks_images/product_images/112.jpg',
                     'socks_images/product_images/113.jpg',
                     'socks_images/product_images/114.jpg',
                     'socks_images/product_images/115.jpg',
                     'socks_images/product_images/116.jpg',
                     'socks_images/product_images/117.jpg'
                     ]

'''

# should turn up white ish
# get_simular_sock('socks_images/product_images/1.jpg')

'''
    for socks in socks_data_images:
        sock_read_image = cv.imread(socks)
        center_column = int(sock_read_image.shape[0] / 2)
        center_row = int(sock_read_image.shape[1] / 2)
        center_px = sock_read_image[center_column, center_row]
        requested_colour = [center_px[0], center_px[1], center_px[2]]
        actual_name, closest_name = get_colour_name(requested_colour)
        Rows.append([socks, center_px, closest_name])

        print("Actual colour name:", actual_name, ", closest colour name:", closest_name)

'''
