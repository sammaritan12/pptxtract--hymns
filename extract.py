from glob import glob
from sys import argv

from pptx import Presentation
from pptx.enum.text import MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Cm, Inches, Pt
from pptx.dml.color import RGBColor


def list_filenames(dirpath, file_type):
    if type(dirpath) is not str or type(file_type) is not str:
        raise TypeError('dirpath and filetype must both be strings')

    return glob(dirpath + '/**/*.' + file_type, recursive=True)

def filenames_only(filenames):
    named_files = []
    for i in filenames:
        for j in range(len(i)):
            if i[j] == '/':
                named_files.append(i[j+1:])
                continue
            elif i[j] == '\\':
                named_files.append(i[j+1:])
                continue
    return named_files
                

if len(argv) < 5:
    print("Enter a directory to extract, and directory to place")
    print("extract.py <dir to extract> <dir to place> <background images> <text colour>")
    quit()

pptx_file_dir = list_filenames(argv[1], 'pptx')
pptx_file_names = filenames_only(pptx_file_dir)
images_path = list_filenames(argv[3], 'jpg')
hymns = []
text_colour = RGBColor(255, 255, 255) if argv[4].lower() == 'white' else RGBColor(0,0,0)

for i in range(len(pptx_file_dir)):
    current_hymn = []
    prs = Presentation(pptx_file_dir[i])

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            if not shape.text == '':
                current_hymn.append(shape.text)
    hymns.append(current_hymn)

for j in range(len(hymns)):
    if len(hymns[j]) == 0:
        print(pptx_file_names[j], "Length: 0")

for h in range(len(hymns)):

    prs = Presentation()

    # Create Title Slide
    title_slide_layout = prs.slide_layouts[0]
    title_slide = prs.slides.add_slide(title_slide_layout)

    # Add title
    title = title_slide.shapes.title
    title.text = hymns[h][0]
    title.text_frame.paragraphs[0].font.name = 'Arial'
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.color.rgb = text_colour

    # Add picture
    pic = title_slide.shapes.add_picture(images_path[h % len(images_path)], 0, 0)
    pic.height = prs.slide_height
    pic.width = prs.slide_width

    # Put background in back
    title_slide.shapes._spTree.remove(pic._element)
    title_slide.shapes._spTree.insert(2, pic._element)


    for i in range(1, len(hymns[h])):
        # Create Blank slide
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)

        # Add background image
        pic = slide.shapes.add_picture(images_path[h % len(images_path)], 0, 0, width=prs.slide_width , height=prs.slide_height)

        # 1 cm from top and left
        left = top = Cm(1)

        # Encompass width and height of all
        width = prs.slide_width - Cm(2)
        height = prs.slide_height- Cm(2)
        
        # Add lyrics
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.text = hymns[h][i]

        # Change size, font and colour
        tf.paragraphs[0].font.name = 'Arial'
        tf.paragraphs[0].font.size = Pt(34)
        tf.paragraphs[0].font.color.rgb = text_colour
        tf.paragraphs[0].font.bold = True
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER   

    print('{}/{} {} Processed'.format(h+1, len(hymns), pptx_file_names[h]))

    # Save file
    prs.save(argv[2]+'/'+pptx_file_names[h])
