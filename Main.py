import os
import sys

from PIL import Image # Pillow library for image processing
from reportlab.lib.pagesizes import letter # ReportLab library for PDF generation
from reportlab.pdfgen import canvas # ReportLab library for PDF generation

SPPORTED_IMAGE_FORMATS = ('.jpg', '.jpeg', '.png', '.bmp',)#NO gif or webp because of transparency issues

PAGE_WIDTH, PAGE_HEIGHT = letter #612, 792
PAGE_MARGIN = 36 # better layout and less ugly

# thats all for the base
