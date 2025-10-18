import os

from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

mask = np.array(Image.open(path.join(d, "mask_2.png")))

# Read the whole text.
text = open(path.join(d, 'bsh.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(
    background_color=None, 
    mode="RGBA", 
    mask=mask
).generate(text)

# Save as SVG
svg_content = wordcloud.to_svg()
with open(path.join(d, "wordcloud_masked.svg"), 'w') as f:
    f.write(svg_content)

