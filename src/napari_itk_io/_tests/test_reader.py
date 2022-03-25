import numpy as np
from napari_itk_io import napari_get_reader
import itk

# tmp_path is a pytest fixture
def test_reader(tmp_path):
    # write some fake data using your supported file format
    my_test_file = str(tmp_path / "myfile.mha")
    original_data = np.random.rand(20, 20)
    image = itk.image_view_from_array(original_data)
    itk.imwrite(image, my_test_file)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_tuple = layer_data_list[0]
    assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])

def test_reader_channel_axis(tmp_path):
    my_test_file = str(tmp_path / "myfile.mha")
    original_data = np.random.rand(20, 20, 2).astype(np.float32)
    image = itk.image_view_from_array(original_data, is_vector=True)
    itk.imwrite(image, my_test_file)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    layer_data_tuple = layer_data_list[0]

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])
    assert layer_data_tuple[1]['channel_axis'] == 2
    assert layer_data_tuple[1]['rgb'] == False

def test_reader_rgb(tmp_path):
    my_test_file = str(tmp_path / "myfile.png")
    original_data = np.random.randint(256, size=(20, 20, 3), dtype=np.uint8)
    ImageType = itk.Image[itk.RGBPixel[itk.UC], 2]
    image = itk.image_view_from_array(original_data, ttype=ImageType)
    itk.imwrite(image, my_test_file)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    layer_data_tuple = layer_data_list[0]

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])
    assert layer_data_tuple[1]['channel_axis'] == 2
    assert layer_data_tuple[1]['rgb'] == True

def test_reader_metadata(tmp_path):
    # write some fake data using your supported file format
    my_test_file = str(tmp_path / "myfile.mha")
    original_data = np.random.rand(20, 20)
    image = itk.image_view_from_array(original_data)
    image['units'] = 'mm'
    image['flavor'] = 'tasty'
    itk.imwrite(image, my_test_file)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    layer_data_list = reader(my_test_file)
    layer_data_tuple = layer_data_list[0]

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])
    assert layer_data_tuple[1]['metadata']['units'] == 'mm'
    assert layer_data_tuple[1]['metadata']['flavor'] == 'tasty'

def test_reader_scale(tmp_path):
    # write some fake data using your supported file format
    my_test_file = str(tmp_path / "myfile.mha")
    original_data = np.random.rand(20, 20)
    image = itk.image_view_from_array(original_data)
    spacing = [3.0, 4.0]
    image.SetSpacing(spacing)
    itk.imwrite(image, my_test_file)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    layer_data_list = reader(my_test_file)
    layer_data_tuple = layer_data_list[0]

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])
    np.testing.assert_allclose(np.array(spacing)[::-1], layer_data_tuple[1]['scale'])

def test_reader_translate(tmp_path):
    # write some fake data using your supported file format
    my_test_file = str(tmp_path / "myfile.mha")
    original_data = np.random.rand(20, 20)
    image = itk.image_view_from_array(original_data)
    origin = [3.0, 4.0]
    image.SetOrigin(origin)
    itk.imwrite(image, my_test_file)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    layer_data_list = reader(my_test_file)
    layer_data_tuple = layer_data_list[0]

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])
    np.testing.assert_allclose(np.array(origin)[::-1], layer_data_tuple[1]['translate'])

def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None