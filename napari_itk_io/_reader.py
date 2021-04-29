"""
This module provides itk-based file reading functionality in a reader plugin for napari.

"""
import numpy as np
import itk
from itk_napari_conversion import image_layer_from_image
from napari_plugin_engine import napari_hook_implementation

@napari_hook_implementation
def napari_get_reader(path):
    """An itk implementation of the napari_get_reader hook specification.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    if isinstance(path, list):
        # reader plugins may be handed single path, or a list of paths.
        # if it is a list, it is assumed to be an image stack...
        # so we are only going to look at the first file.
        path = path[0]

    # if we know we cannot read the file, we immediately return None.
    image_io = itk.ImageIOFactory.CreateImageIO(path, itk.CommonEnums.IOFileMode_ReadMode)
    if not image_io:
        return None

    # otherwise we return the *function* that can read ``path``.
    return reader_function


def reader_function(path):
    """Take a path or list of paths and return a list of LayerData tuples.

    Readers are expected to return data as a list of tuples, where each tuple
    is (data, [add_kwargs, [layer_type]]), "add_kwargs" and "layer_type" are
    both optional.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples where each tuple in the list contains
        (data, metadata, layer_type), where data is a numpy array, metadata is
        a dict of keyword arguments for the corresponding viewer.add_* method
        in napari, and layer_type is a lower-case string naming the type of layer.
        Both "meta", and "layer_type" are optional. napari will default to
        layer_type=="image" if not provided
    """
    # handle both a string and a list of strings
    image = itk.imread(path)

    image_layer = image_layer_from_image(image)
    components = image.GetNumberOfComponentsPerPixel()
    if components == 1:
        channel_axis = None
    else:
        channel_axis = image_layer.data.ndim - 1

    # optional kwargs for the corresponding viewer.add_* method
    add_kwargs = {
            'channel_axis': channel_axis,
            'rgb': image_layer.rgb,
            }

    layer_type = "image"  # optional, default is "image"
    return [(image_layer.data, add_kwargs, layer_type)]
