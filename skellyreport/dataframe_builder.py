import numpy as np
import pandas as pd
from pathlib import Path
from typing import Union

class DataFrameBuilder:
    def __init__(self, marker_list: list, data_3d_array: np.ndarray = None, path_to_data: Union[Path, str] = None):
        if data_3d_array is not None and path_to_data is not None:
            raise ValueError("Only one of data_array or path_to_data should be provided, not both.")
        if data_3d_array is None and path_to_data is None:
            raise ValueError("One of data_array or path_to_data must be provided.")
        
        self.marker_list = marker_list
        self._data_array = data_3d_array
        self.path_to_data = Path(path_to_data) if path_to_data else None
        self._data_loaded = False if path_to_data else True

    @property
    def data_array(self):
        if not self._data_loaded:
            self.load_data_from_file()
        return self._data_array

    def load_data_from_file(self):
        if self.path_to_data and self.path_to_data.exists():
            self._data_array = np.load(self.path_to_data)
            self._data_loaded = True
        else:
            raise FileNotFoundError("The specified path to data does not exist or is not provided.")

    def _convert_3d_array_to_dataframe(self):
        """
        Convert the FreeMoCap data from a numpy array to a pandas DataFrame. 
        """
        data_array = self.data_array
        num_frames, num_markers, _ = data_array.shape
        frame_list, marker_names, x_list, y_list, z_list = [], [], [], [], []

        for frame in range(num_frames):
            for marker in range(num_markers):
                frame_list.append(frame)
                marker_names.append(self.marker_list[marker])  
                x_list.append(data_array[frame, marker, 0])
                y_list.append(data_array[frame, marker, 1])
                z_list.append(data_array[frame, marker, 2])

        data_frame = pd.DataFrame({
            'frame': frame_list,
            'marker': marker_names,
            'x': x_list,
            'y': y_list,
            'z': z_list
        })

        return data_frame

    def get_dataframe(self):
        """
        Public method to access the converted DataFrame.
        Ensures data is loaded and converts it to a DataFrame.
        """
        if not self._data_loaded:
            raise RuntimeError("Data is not loaded yet.")
        return self._convert_3d_array_to_dataframe()



if __name__ == '__main__':
    from mediapipe_marker_list import mediapipe_markers
    # Example usage
    # data_builder_direct = DataBuilder(marker_list=[...], data_3d_array=np.array([...]))
    data_builder_from_path = DataFrameBuilder(marker_list=mediapipe_markers, path_to_data=r"D:\2023-05-17_MDN_NIH_data\1.0_recordings\calib_3\sesh_2023-05-17_13_48_44_MDN_treadmill_2\mediapipe_output_data\mediapipe_body_3d_xyz.npy")

    # Accessing the data (will load from file if not already loaded)
    data = data_builder_from_path.data_array
    df = data_builder_from_path.get_dataframe()
    print(df.head())
    f = 2