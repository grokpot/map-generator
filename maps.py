
# Allan Jacobs

# Installation
# https://www.citylab.com/equity/2017/01/x-ray-your-citys-street-network-with-a-bit-of-code/512714/?ct=t(Teleport_Trail_week_195_8_2017)&goal=0_8238077a1e-e423d31670-240024073
# http://geoffboeing.com/2016/11/osmnx-python-street-networks/
# pip install geopandas
# pip install rtree
# pip install osmnx
# $ brew install spacialindex
# https://github.com/gboeing/osmnx/issues/45

# Latlong Finder: https://mynasadata.larc.nasa.gov/latitudelongitude-finder/


# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python
import matplotlib as mpl
mpl.use('TkAgg')

import osmnx as ox


# G = ox.graph_from_point((32.730869, -96.81765), distance=50000, network_type='drive')

G = ox.graph_from_address('1410 Arizona Ave, Dallas, TX', distance=750, distance_type='network', network_type='drive')
fig, ax = ox.plot_graph(G, dpi=600, bgcolor='#333333', edge_color="#666666", node_size=0, edge_linewidth=3.5, show=False, save=True, filename='network', file_format='svg')


# How to draw a hexagon in Illustrator:
# https://www.youtube.com/watch?v=SkhSRNbVqCs

# How to color drop a color outside of illustrator:
# http://www.laughing-lion-design.com/2013/10/how-to-pick-a-colour-outside-of-photoshop-using-the-eyedropper-tool/

# How to Bevel
# https://astutegraphics.com/blog/how-to-create-the-bevel-emboss-effects-for-editable-text-in-adobe-illustrator/

# How to color a symbol
# https://graphicdesign.stackexchange.com/questions/8199/illustrator-change-the-colors-of-a-symbol

# Color swatches
# https://helpx.adobe.com/illustrator/using/using-creating-swatches.html