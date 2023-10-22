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


def get_simular_sock(input_picture_path):
    input_sock_color_name = get_uploadedpic_color(input_picture_path)
    with open('socks_center_pixel.csv', 'r') as datafile:
        for value in datafile.readlines():
            csv_value = value.split(',')
            csv_value[2] = csv_value[2].strip()
            if input_sock_color_name == csv_value[2]:
                return csv_value[0]
