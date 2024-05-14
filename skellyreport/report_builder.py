
from scatter_plot_3d import create_3d_scatter_from_dataframe
from joint_trajectory_plots import create_joint_trajectory_subplot
import plotly.io as pio
from report_styles import styles




def generate_navigation_links(unique_markers):
    navigation_html = "<div class='navigation'>"
    for marker in unique_markers:
        navigation_html += f"<a href='#{marker}'>{marker}</a> "
    navigation_html += "</div>"
    return navigation_html


    

def generate_marker_specific_html(marker, position_dataframe_of_3d_data):

    marker_specific_html = f"<div class='marker-section' id='{marker}'><center><h1>{marker}</h1></center>"
    marker_specific_html += f"<center><h2> Position (mm) </h1></center>"
    figure = create_joint_trajectory_subplot(marker, position_dataframe_of_3d_data, color_of_cards='white')
    marker_specific_html += fig_to_html(figure)

    marker_specific_html += "</div>"  # Ends the section for a specific marker

    return marker_specific_html


def generate_3d_scatter_plot_html(position_dataframe_of_3d_data):
    scatter_plot_html = ""
    print('creating 3d scatter plot')
    scatter_plot = create_3d_scatter_from_dataframe(dataframe_of_3d_data=position_dataframe_of_3d_data[position_dataframe_of_3d_data['frame']%3==0])
    print('scatter created, converting to html')
    scatter_plot_html += fig_to_html(scatter_plot)
    print('html scatter created')
    return scatter_plot_html

def generate_html_report(position_dataframe_of_3d_data, recording_name = None):
    unique_markers = position_dataframe_of_3d_data['marker'].unique()

    # Start of the HTML content with included CSS for styling
    if recording_name is not None:
        html_content = f"<html><head><title>{recording_name} FreeMoCap Report </title>{styles}</head><body>"
        report_title = f"Recording: {recording_name}"

    else:
        html_content = f"<html><head><title>FreeMoCap Report</title>{styles}</head><body>"
        report_title = f"Error Metrics Report"
    
    html_content += f"<h1 style='text-align: center; margin-top: 50px;'>{report_title}</h1>"
    
    html_content += generate_navigation_links(unique_markers)

    # html_content += generate_overall_rmse_indicators_html(position_rmse_dataframe, type = 'position')

    # html_content += generate_overall_rmse_indicators_html(velocity_rmse_dataframe, type = 'velocity')

    html_content += generate_3d_scatter_plot_html(position_dataframe_of_3d_data)

    # html_content += generate_overall_joint_rmse_bar_plot(position_rmse_dataframe, velocity_rmse_dataframe)

    for marker in unique_markers:
        html_content += generate_marker_specific_html(marker, position_dataframe_of_3d_data)

    html_content += "</body></html>"

    return html_content



def fig_to_html(fig):
    return pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
