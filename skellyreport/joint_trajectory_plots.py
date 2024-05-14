import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def create_joint_trajectory_subplot(marker, dataframe_of_3d_data, color_of_cards='white'):
    df_marker = dataframe_of_3d_data[dataframe_of_3d_data['marker'] == marker]
    
    # Create a subplot with 1 column and 3 rows
    fig = make_subplots(rows=3, cols=1, subplot_titles=("X Axis Trajectory", "Y Axis Trajectory", "Z Axis Trajectory"),
                        vertical_spacing=0.1, shared_xaxes=True)
    
    # Plot X trajectory
    fig.add_trace(
        go.Scatter(x=df_marker['frame'], y=df_marker['x'], name='X Position', mode='lines', line=dict(color='blue')),
        row=1, col=1
    )
    
    # Plot Y trajectory
    fig.add_trace(
        go.Scatter(x=df_marker['frame'], y=df_marker['y'], name='Y Position', mode='lines', line=dict(color='blue')),
        row=2, col=1
    )
    
    # Plot Z trajectory
    fig.add_trace(
        go.Scatter(x=df_marker['frame'], y=df_marker['z'], name='Z Position', mode='lines', line=dict(color='blue')),
        row=3, col=1
    )
    
    # Update y-axes titles
    fig.update_yaxes(title_text="X Position (mm)", row=1, col=1)
    fig.update_yaxes(title_text="Y Position (mm)", row=2, col=1)
    fig.update_yaxes(title_text="Z Position (mm)", row=3, col=1)

    # Update layout
    fig.update_layout(height=700, showlegend=True, paper_bgcolor=color_of_cards)
    # Update x-axes titles only for the last plot
    fig.update_xaxes(title_text="Frame", row=3, col=1)

    return fig
