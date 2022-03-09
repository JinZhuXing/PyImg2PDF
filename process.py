import os
from generate import Img2PDFGen


class Img2PDFProc:
    def __init__(self, srcpath, dstpath, imgtype):
        self.src_path = srcpath
        self.dst_path = dstpath
        self.img_type = imgtype
    
    def process(self):
        print('Process start ************************************')
        print('SrcPath: ', self.src_path)
        print('DstPath: ', self.dst_path)
        print('')

        # get book list
        book_list = os.listdir(self.src_path)

        # process every book
        for book_item in book_list:
            new_book_path = self.src_path + '/' + book_item
            if (os.path.isdir(new_book_path) == False):
                continue

            # processing
            print('Book Name: ', book_item)
            gen = Img2PDFGen(new_book_path, self.dst_path, book_item, self.img_type)
            gen.generate()
            print('')
