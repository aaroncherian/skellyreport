
from pathlib import Path
import numpy as np
from mediapipe_marker_list import mediapipe_markers
from dataframe_builder import DataFrameBuilder
from report_builder import generate_html_report

def main(path_to_recording_folder:Path):

    from dataframe_builder import DataFrameBuilder
    # from skellyreport.report_builder import ReportBuilder


    path_to_numpy_3d = path_to_recording_folder / "output_data"/'mediapipe_body_3d_xyz.npy'
    data_3d = np.load(path_to_numpy_3d)

    # Load the data from the specified folder
    data_builder = DataFrameBuilder(data_3d_array=data_3d, marker_list=mediapipe_markers)
    data_frame = data_builder.get_dataframe()
    f = 2 
    html_report = generate_html_report(position_dataframe_of_3d_data=data_frame)
    html_report_path = path_to_recording_folder / "report.html"
    with open(html_report_path, "w") as file:
        file.write(html_report)
    
    # Save the report
    # report_builder.save_report()


if __name__ == "__main__":
    main(Path(r'C:\Users\aaron\FreeMocap_Data\recording_sessions\freemocap_sample_data'))