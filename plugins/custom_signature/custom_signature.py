# 2021 Humberto Garza
# https://github.com/humberto-garza/gimp_python_plugins

import os 
import sys

from gimpfu import *

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

COLOR_OPTIONS = ["White", "Black"] 

def custom_signature(color_option, image) :

    signature_file_name = "{}.png".format(COLOR_OPTIONS[color_option])
    signature_file_path = os.path.join(CURRENT_PATH, "signatures", signature_file_name)

    # Open the signature on the current Image
    layer = pdb.gimp_file_load_layer(
        image,
        signature_file_path)
    layer.name = "Signature"

    # Insert the layer to the image
    image.insert_layer (layer)

    # Scale the layer
    aspect = float(layer.width) / float(layer.height)
    new_layer_width = image.width / 2
    difference = layer.width - new_layer_width
    new_layer_height = layer.height - difference / aspect
    pdb.gimp_layer_scale(
        layer,
        new_layer_width,
        new_layer_height,
        1
    )

    # Position to bottom right corner
    width_midway = image.width / 2
    height_midway = image.height / 2
    pdb.gimp_layer_set_offsets(
        layer,
        image.width - layer.width,
        image.height- layer.height
    )

    gimp.displays_flush()

register(
    "python_fu_custom_signature",
    "Custom Signature",
    "Add a Signature to an image",
    "Humberto Garza",
    "Humberto Garza",
    "2021",
    "Custom Signature",
    "",
    [
        (PF_OPTION, "string", "Color", 0, COLOR_OPTIONS),
        (PF_IMAGE, "image", "Input Image", None)
    ],
    [],
    custom_signature, menu="<Image>/Tools")

main()
