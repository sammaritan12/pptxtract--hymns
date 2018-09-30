from glob import glob
from sys import argv

from pptx import Presentation
from pptx.enum.text import MSO_AUTO_SIZE
from pptx.util import Cm, Inches, Pt


def list_filenames(dirpath):
    if type(dirpath) is not str:
        raise TypeError('dirpath must be a string')

    return glob(dirpath + '/**/*.pptx', recursive=True)

def filenames_only(filenames):
    named_files = []
    for i in filenames:
        for j in range(len(i)):
            if i[j] == '/':
                named_files.append(i[j+1:])
                continue
            elif i[j] == '\\':
                named_files.append(i[j+2:])
                continue
    return named_files
                

if len(argv) < 3:
    print("Enter a directory to extract, and directory to place")
    print("extract.py <dir to extract> <dir to place>")
    quit()

file_dir = list_filenames(argv[1])
file_names = filenames_only(file_dir)
hymns = []

for i in range(len(file_dir)):
    current_hymn = []
    prs = Presentation(file_dir[i])

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            if not shape.text == '':
                current_hymn.append(shape.text)
    hymns.append(current_hymn)

for h in range(len(hymns)):

    prs = Presentation()

    # Create Title Slide
    title_slide_layout = prs.slide_layouts[0]
    title_slide = prs.slides.add_slide(title_slide_layout)
    title = title_slide.shapes.title
    title.text = hymns[h][0]
    title.text_frame.paragraphs[0].font.name = 'Arial'

    for i in range(1, len(hymns[h])):
        # Create Blank slide
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)

        # 1 cm from top and left
        left = top = Cm(1)

        # Encompass width of all, and 2/3 of height
        width = prs.slide_width - Cm(2)
        height = (prs.slide_height/3)*2 - Cm(2)
        
        # Add lyrics
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.text = hymns[h][i]

        # Change size and font
        tf.paragraphs[0].font.name = 'Arial'
        tf.paragraphs[0].font.size = Pt(30)
        tf.paragraphs[0].font.bold = True

        tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE

    print('{}/{} Powerpoint Finished'.format(h+1, len(hymns)))

    # Save file
    prs.save(argv[2]+'/'+file_names[h])
