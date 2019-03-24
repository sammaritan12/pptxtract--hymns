# pptxtract-hymns

Extracts the texts from church powerpoint hymns, and places them into a new blank powerpoint.

Will only work if powerpoint file is `.pptx`, and the powerpoint layout is as follows:

- First slide is a title slide containing only one textbox with title of hymn
- Subsequent slides contain only 1 text box which contains the lyrics
- All pictures and blank text boxes are ignored

## Converting PPT to PPTX

To convert multiple PPT files to PPTX, you must download LibreOFfice and run the following command on to your terminal and it will create a PPTX file for every ppt file within the current working directory.

```bash
libreoffice --headless --convert-to pptx *.ppt
```

## Dependencies

In order to run, you will need to use Python 3 and `python-pptx`, run the following in the terminal to install.

```bash
pip install python-pptx
```

## How to run

```bash
extract.py <dir to extract> <dir to place> <background images> <text colour> <wide/normal>
```
