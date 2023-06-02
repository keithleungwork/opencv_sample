import matplotlib.pyplot as plt
import cv2 as cv


def plt_show(bgr_img, color_scale=cv.COLOR_BGR2RGB, is_gray=False, axs_obj=None):
    if axs_obj:
        cus_plt = axs_obj
    else:
        cus_plt = plt

    if is_gray:
        cus_plt.imshow(bgr_img, cmap='gray', vmin=0, vmax=255)
    else:
        rgb_img = cv.cvtColor(bgr_img, color_scale)
        cus_plt.imshow(rgb_img)
