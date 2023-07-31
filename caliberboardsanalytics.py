import streamlit as st
import plotly.graph_objects as go
from emoji import emojize

title = ("Caliber Boards Analytics " + emojize(":hospital:"))
st.title(title)

st.subheader('Master the Boards: Leveraging Analytics for Exam Excellence')
st.markdown("""
Discover your strengths and pinpoint areas for improvement. With our tailored analytics, chart your journey, one session at a time.
""")
 
# Define the scenarios and scores
scenarios = ['GI - Small Bowel Obstruction', 'Breast - Architectural Distortion', 'Vascular - Dialysis Access', 'Endocrine - Aldosteronoma']
candidate_scores = [35, 72, 46, 90]
average_scores = [50, 50, 50, 50]

# Create the figure
fig = go.Figure(data=[
    go.Bar(name='Candidate', x=scenarios, y=candidate_scores, marker_color='red'),
    go.Bar(name='Average', x=scenarios, y=average_scores, marker_color='#0ae1c8')
])

# Change the bar mode
fig.update_layout(barmode='group')

# Title and labels
fig.update_layout(title_text='Candidate Score Comparison with 50th Percentile (Example)', xaxis_title='Scenarios', yaxis_title='Percentiles')

# Config to remove Plotly options
config = {"displayModeBar": False, "showTips": False}

# Display the figure in Streamlit with specified config
st.plotly_chart(fig, config=config)

st.subheader('Optimize Success: Higher Pass Rates with More Sessions')
st.markdown('**Data based on 2022 ABS Certifying Examination statistics available [here](https://absurgerydata.shinyapps.io/PassRates/)**')

# Define the session groups and pass rates
session_groups = ['1-3', '4-6', '7-9', '10+']
passrate_values = [80, 90, 98, 100]

# Create the figure
fig2 = go.Figure()

# Add the line for candidates
fig2.add_trace(go.Scatter(x=session_groups, y=passrate_values, mode='lines+markers', name='Candidates', marker_color='red', hovertemplate = 'Candidates: %{y}%'))

# Add the average line
avg_pass_rate = 84
fig2.add_shape(
    type='line',
    x0=session_groups[0], y0=avg_pass_rate,
    x1=session_groups[-1], y1=avg_pass_rate,
    line=dict(
        color="#0ae1c8",
        width=2,
        dash="dot",
    )
)

# Add invisible markers for average line hover info
fig2.add_trace(go.Scatter(x=session_groups, y=[avg_pass_rate]*len(session_groups), mode='markers', marker=dict(size=0), hoverinfo='skip', name='Average', hovertemplate = 'Average: 84%'))

# Hide y-axis but set y-axis range
fig2.update_yaxes(visible=True, showticklabels=True, range=[0, max(passrate_values + [avg_pass_rate])])

# Add title and labels
fig2.update_layout(title_text='Pass Rates vs. Number of Sessions', xaxis_title='Number of Sessions')

# Config to remove Plotly options
config2 = {"displayModeBar": False, "showTips": False}

# Display the figure in Streamlit with specified config
st.plotly_chart(fig2, config=config2)

