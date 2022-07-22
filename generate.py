import os
import numpy as np
from PIL import Image


class Img2PDFGen:
    def __init__(self, srcpath, dstpath, bookname, imgtype, autocrop, gensmall):
        self.src_path = srcpath
        self.dst_path = dstpath
        self.bookname = bookname
        self.img_type = imgtype
        self.autocrop = autocrop
        self.gensmall = gensmall

    def generate(self):
        # generate output pdf path
        pdf_file_path = self.dst_path + '/' + self.bookname + '.pdf'
        pdf_file_path_resize = self.dst_path + '/small/' + self.bookname + '_s.pdf'

        # check if the pdf exist
        if (os.path.exists(pdf_file_path)):
            print('Already exist (Skip): ', pdf_file_path)
            return

        # get image list
        img_file_list = os.listdir(self.src_path)
        img_cnt = len(img_file_list)
        img_start_idx = 1

        # take first image
        for img_idx in range(1, img_cnt + 1):
            img_item = '{0:d}.{1}'.format(img_idx, self.img_type)
            new_img_path = self.src_path + '/' + img_item
            try:
                # open image
                img_base = Image.open(new_img_path)
                img_resize = Image.open(new_img_path)

                # first image success
                img_start_idx = img_idx
                break
            except Exception as e:
                print('Error start image at ', new_img_path)
                continue

        # get real page region
        if (self.autocrop == 1):
            img_base = self.get_page_rgn(img_base)
            img_resize = self.get_page_rgn(img_resize)

        # process every image
        img_list = []
        # for img_item in img_list:
        for img_idx in range(img_start_idx + 1, img_cnt + 1):
            img_item = '{0:d}.{1}'.format(img_idx, self.img_type)
            new_img_path = self.src_path + '/' + img_item
            try:
                # open image
                img_org = Image.open(new_img_path)

                # crop
                if (self.autocrop == 1):
                    img_org = self.get_page_rgn(img_org)

                # append image to list
                img_list.append(img_org)
            except Exception as e:
                print('Error at ', new_img_path)
                continue

        # show book information
        print('Page: ', len(img_list) + 1)

        # make pdf from images
        img_base.save(pdf_file_path, save_all=True, append_images=img_list)
        print('PDF saved: ', pdf_file_path)

        # make small size pdf from images
        if (self.gensmall == 1):
            img_resize = img_resize.resize(((int)(img_resize.size[0] / 2), (int)(img_resize.size[1] / 2)))
            resize_img_list = self.image_list_resize(img_list)
            img_resize.save(pdf_file_path_resize, save_all=True, append_images=resize_img_list)
            print('PDF saved (Small):', pdf_file_path_resize)
            del resize_img_list[:]
            del resize_img_list

        # release buffer
        del img_list[:]
        del img_list


    def get_page_rgn(self, img_org):
        img_arr = np.array(img_org)
        # print(img_arr.shape)
        r_top = 0
        r_bottom = 0

        # get top border (row)
        for r in range(1, img_arr.shape[0]):
            curr_line_arr = img_arr[r]
            next_line_arr = img_arr[r + 1]
            if (np.array_equal(curr_line_arr, next_line_arr) == False):
                r_top = r + 1
                break
        
        # get bottom border (row)
        for r in range(img_arr.shape[0] - 1, -1, -1):
            curr_line_arr = img_arr[r]
            next_line_arr = img_arr[r - 1]
            if (np.array_equal(curr_line_arr, next_line_arr) == False):
                r_bottom = r - 1
                break
        
        real_rgn = (0, r_top, img_arr.shape[1], r_bottom)
        return img_org.crop(real_rgn)

    def image_list_resize(self, img_list):
        resize_img_list = []
        for i in range(len(img_list)):
            img = img_list[i]
            resize_img = img.resize(((int)(img.size[0] / 2), (int)(img.size[1] / 2)))
            resize_img_list.append(resize_img)
        return resize_img_list
