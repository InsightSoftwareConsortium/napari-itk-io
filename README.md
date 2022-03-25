# napari-itk-io

[![License](https://img.shields.io/pypi/l/napari-itk-io.svg?color=green)](https://github.com/InsightSoftwareConsortium/napari-itk-io/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-itk-io.svg?color=green)](https://pypi.org/project/napari-itk-io)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-itk-io.svg?color=green)](https://python.org)
[![tests](https://github.com/InsightSoftwareConsortium/napari-itk-io/workflows/tests/badge.svg)](https://github.com/InsightSoftwareConsortium/napari-itk-io/actions)
[![codecov](https://codecov.io/gh/InsightSoftwareConsortium/napari-itk-io/branch/master/graph/badge.svg)](https://codecov.io/gh/InsightSoftwareConsortium/napari-itk-io)

File IO with [itk](https://itk.org) for [napari](https://napari.org).

Image metadata, e.g. the pixel spacing, origin, and metadata tags, are preserved and passed into napari.

Supported image file formats:

- [BioRad](http://www.bio-rad.com/)
- [BMP](https://en.wikipedia.org/wiki/BMP_file_format)
- [DICOM](http://dicom.nema.org/)
- [DICOM Series](http://dicom.nema.org/)
- [ITK HDF5](https://support.hdfgroup.org/HDF5/)
- [JPEG](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format)
- [GE4,GE5,GEAdw](http://www3.gehealthcare.com)
- [Gipl (Guys Image Processing Lab)](https://www.ncbi.nlm.nih.gov/pubmed/12956259)
- [LSM](http://www.openwetware.org/wiki/Dissecting_LSM_files)
- [MetaImage](https://itk.org/Wiki/ITK/MetaIO/Documentation)
- [MINC 2.0](https://en.wikibooks.org/wiki/MINC/SoftwareDevelopment/MINC2.0_File_Format_Reference)
- [MGH](https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/MghFormat)
- [MRC](http://www.ccpem.ac.uk/mrc_format/mrc_format.php)
- [NifTi](https://nifti.nimh.nih.gov/nifti-1)
- [NRRD](http://teem.sourceforge.net/nrrd/format.html)
- [Portable Network Graphics (PNG)](https://en.wikipedia.org/wiki/Portable_Network_Graphics)
- [Tagged Image File Format (TIFF)](https://en.wikipedia.org/wiki/TIFF)
- [VTK legacy file format for images](http://www.vtk.org/VTK/img/file-formats.pdf)

For DICOM Series, select the folder containing the series with *File -> Open
Folder...*. The first series will be selected and sorted spatially.

## Installation

You can install `napari-itk-io` via [pip]:

    pip install napari-itk-io

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

Follow the [itk contributing
guidelines](https://github.com/InsightSoftwareConsortium/ITK/blob/master/CONTRIBUTING.md)
and the [itk code of
conduct](https://github.com/InsightSoftwareConsortium/ITK/blob/master/CODE_OF_CONDUCT.md).

## License

Distributed under the terms of the [Apache Software License 2.0] license,
"napari-itk-io" is free and open source software.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/InsightSoftwareConsortium/napari-itk-io/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/