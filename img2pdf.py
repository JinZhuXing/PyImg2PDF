import argparse
import sys

from process import Img2PDFProc


# main process
def main(args):
    # check argument
    src_path = args.srcpath
    dst_path = args.dstpath
    img_type = args.imgtype
    autocrop = args.autocrop

    # initialize process
    proc = Img2PDFProc(src_path, dst_path, img_type, autocrop)

    # start process
    proc.process()


# argument parser
def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--srcpath', type = str,
                        help = 'Source directory path', default = './src')
    parser.add_argument('--dstpath', type = str,
                        help = 'Destination directory path', default = './dst')
    parser.add_argument('--imgtype', type = str,
                        help = 'Image file type (Extension)', default = 'bmp')
    parser.add_argument('--autocrop', type = int,
                        help = 'Use auto crop method', default = 1)
    
    return (parser.parse_args(argv))


# start point
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
