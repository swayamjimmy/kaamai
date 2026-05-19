import streamlit as st
import os
from src.job_research_crew.crew import JobResearchCrew

# Configure the page title, icon, and layout
st.set_page_config(page_title="AI Job Research Crew", page_icon=":robot_face:", layout="wide")

# Display the app header and description
st.title("\U0001F916 AI Job Research Crew")
st.markdown("Three AI agents collaborate to research a company and prepare you for your job application.")

# Create a two-column layout for the input fields
col1, col2 = st.columns(2)
with col1:
    company = st.text_input("Company Name", placeholder="e.g. Flipkart, Razorpay, Google")
with col2:
    role = st.text_input("Target Role", placeholder="e.g. Software Engineer, Data Scientist")

if st.button(":rocket: Run Research Crew", type="primary"):
    # Validate that both fields have values
    if not company or not role:
        st.warning("Please enter both a company name and a target role.")
    else:
        # Show a status container while agents work
        with st.status("AI Agents are working...", expanded=True) as status:
            st.write(":mag: **Company Researcher** is gathering intelligence...")
            st.write(":bar_chart: **Role Analyst** is mapping skills to requirements...")
            st.write(":pencil2: **Report Writer** is creating your brief...")

            # Run the crew with user inputs
            os.makedirs('output', exist_ok=True)
            inputs = {'company': company, 'role': role}
            result = JobResearchCrew().crew().kickoff(inputs=inputs)

            status.update(label="Research complete!", state="complete", expanded=False)

        # Display the generated report
        st.markdown("---")
        st.markdown("## :clipboard: Your Company Research Brief")
        st.markdown(result.raw)

        # Offer a download button for the report
        st.download_button(
            label=":inbox_tray: Download Report as Markdown",
            data=result.raw,
            file_name=f"{company.lower().replace(' ', '_')}_research_brief.md",
            mime="text/markdown"
        )
