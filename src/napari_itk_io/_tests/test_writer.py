from napari_itk_io import write_multiple #, write_single
import numpy as np
import itk

def test_write_single_image(tmp_path):
    # write fake data
    original_data = np.random.rand(20, 20)
    original_metadata = {'name': 'test_layer', 'metadata': {}}
    filepath = str(tmp_path / "test_file.nii")
    written_filepaths = write_multiple(filepath, [(original_data, original_metadata, 'image')])
    assert filepath == written_filepaths[0]

    # read it back
    image = itk.imread(filepath)
    np.testing.assert_allclose(original_data, image)


def test_write_multiple_images(tmp_path):
    # write fake data
    original_data = (np.random.rand(20, 20), np.random.rand(20, 20))
    original_metadata = ({'name': 'test_layer1', 'metadata': {}},
                        {'name': 'test_layer2', 'metadata': {}})
    filepath = str(tmp_path / "test_file.nii")
    written_filepaths = write_multiple(filepath, [(original_data[0], original_metadata[0], 'image'),
                                                  (original_data[1], original_metadata[1], 'image')])
    assert(len(written_filepaths) == 2)

    # read them back
    for i, written_filepath in enumerate(written_filepaths):
        assert original_metadata[i]['name'] in written_filepath 
        image = itk.imread(written_filepath)
        np.testing.assert_allclose(original_data[i], image)



