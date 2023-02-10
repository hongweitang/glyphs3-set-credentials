#MenuTitle: Set Font Credentials
__doc__="""
Sets copyright metadata to Hongwei Tang.
"""

import time

thisFont = Glyphs.font # Assigns active font in Glyphs (The active GSFont object)
thisYear = time.gmtime()[0] # returns current year, remove if you don't wanna set year

thisFont.designer = "Hongwei Tang"
thisFont.designerURL = "https://hongweitang.com/"

thisFont.manufacturer = "Hongwei Tang"
thisFont.manufacturerURL = "https://hongweitang.com/"
thisFont.copyright = "Copyright © %i by Hongwei Tang. All rights reserved." % thisYear