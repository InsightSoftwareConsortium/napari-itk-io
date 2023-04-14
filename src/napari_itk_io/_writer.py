"""
This module is an example of a barebones writer plugin for napari.

It implements the Writer specification.
see: https://napari.org/plugins/stable/guides.html#writers

Replace code below according to your needs.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, List, Any, Sequence, Tuple, Union

import itk
from itk_napari_conversion import image_from_image_layer
from pathlib import Path
import napari

if TYPE_CHECKING:
    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]


def write_single(path: str, data: Any, meta: dict) -> List[str]:
    """Writes a single layer"""
    pass


def write_multiple(path: str, data: List[FullLayerData]) -> List[str]:
    """Writes multiple layers of different types."""
    written_paths = []
    for i, image_layer_tuple in enumerate(data):
        image_layer = napari.layers.Image(image_layer_tuple[0], metadata=image_layer_tuple[1]['metadata'])
        image = image_from_image_layer(image_layer)

        if len(data) == 1:
            itk.imwrite(image, path)
            written_paths = [path]
        else:
            unique_path = Path(path)
            unique_path = str(Path(unique_path.parent) / (unique_path.stem + "_" + image_layer_tuple[1]['name'] + unique_path.suffix))
            itk.imwrite(image, unique_path)
            written_paths.append(unique_path)

    return written_paths  
