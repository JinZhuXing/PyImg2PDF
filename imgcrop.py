import argparse
import os
import sys
from PIL import Image


# main process
def main(args):
    # check argument
    src_path = args.srcpath
    dst_path = args.dstpath
    img_type = args.imgtype
    cropx = args.cropx
    cropy = args.cropy
    cropw = args.cropw
    croph = args.croph

    print('Process start ************************************')
    print('SrcPath: ', src_path)
    print('DstPath: ', dst_path)
    print('')

    # get book list
    book_list = os.listdir(src_path)

    # process every book
    for book_item in book_list:
        new_book_path = src_path + '/' + book_item
        new_dst_path = dst_path + '/' + book_item
        if (os.path.isdir(new_book_path) == False):
            continue
        print('Book Name: ', book_item)

        # make destination directory
        os.mkdir(new_dst_path)

        # get image list
        img_file_list = os.listdir(new_book_path)
        img_cnt = len(img_file_list)

        # take first image
        for img_idx in range(1, img_cnt + 1):
            img_item = '{0:d}.{1}'.format(img_idx, img_type)
            new_img_path = new_book_path + '/' + img_item
            new_dst_img_path = new_dst_path + '/' + '{0:d}.jpg'.format(img_idx)
            try:
                # open image
                img_base = Image.open(new_img_path)

                # crop image
                real_rgn = (cropx, cropy, cropx + cropw - 1, cropy + croph - 1)
                img_dst = img_base.crop(real_rgn)
                img_dst.save(new_dst_img_path)
            except Exception as e:
                print('Error start image at ', new_img_path)
                continue

        print('')


# argument parser
def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--srcpath', type = str,
                        help = 'Source directory path', default = './src')
    parser.add_argument('--dstpath', type = str,
                        help = 'Destination directory path', default = './dst')
    parser.add_argument('--imgtype', type = str,
                        help = 'Image file type (Extension)', default = 'bmp')
    parser.add_argument('--cropx', type = int,
                        help = 'Crop position left', default = 780)
    parser.add_argument('--cropy', type = int,
                        help = 'Crop position top', default = 120)
    parser.add_argument('--cropw', type = int,
                        help = 'Crop width', default = 2570)
    parser.add_argument('--croph', type = int,
                        help = 'Crop height', default = 1730)
    
    return (parser.parse_args(argv))


# start point
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
