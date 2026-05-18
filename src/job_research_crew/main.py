#!/usr/bin/env python
import os
from job_research_crew.crew import JobResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)


def run():
    """
    Run the Job Research Crew.
    """
    inputs = {
        'company': 'Flipkart',
        'role': 'Software Engineer'
    }

    # Create and run the crew
    result = JobResearchCrew().crew().kickoff(inputs=inputs)

    print("\n\n========================")
    print("## Research Brief Generated")
    print("========================\n")
    print(result.raw)
    print("\n\nReport saved to: output/report.md")