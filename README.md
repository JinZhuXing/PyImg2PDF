# PyImg2PDF

Make pdf file from image files using python.

## Usage

First install python3.7(or higher) or Anaconda. We recommend to install Anaconda.

After installing, please install requirement packages with following command.

    pip install -r requirements.txt

Now, it's ready to use Img2PDF.

You can simply make PDF files from image with following command.s

    python img2pdf.py --srcpath=<source dir> --dstpath=<output dir> --imgtype=<image type> --autocrop=<1: use autocrop, 0: do not use>

The **source directory** must be placed like this.

    <source directory name>
    |---book name
        |---1.bmp
        |---2.bmp
        |---3.bmp
        ...
        |---90.bmp
    |---book name
        |---1.bmp
        |---2.bmp
        ...
        |---80.bmp

## Example Usage

    python img2pdf.py --srcpath='./src' --dstpath='./dst' --imgtype='bmp'
