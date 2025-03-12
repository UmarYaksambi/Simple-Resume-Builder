import streamlit as st
import json
import os
from groq import Groq
import time
import base64
from fpdf import FPDF
from dotenv import load_dotenv
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("api_key"))

# Set page configuration
st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

def create_pdf_resume(resume_content):
    pdf = FPDF()
    pdf.add_page()
    
    # Set margins to give more space for content
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_auto_page_break(True, margin=15)
    
    # Set font
    pdf.set_font("Arial", size=11)
    
    # Extract sections
    sections = resume_content.split("\n\n")
    
    for section in sections:
        if section.strip():
            # Check if it's a header
            if section.strip().isupper() or section.startswith("# "):
                pdf.set_font("Arial", 'B', 14)
                clean_header = section.replace("# ", "").strip()
                pdf.cell(0, 10, txt=clean_header, ln=True)
                pdf.set_font("Arial", size=11)
            else:
                # Handle bullet points and regular text
                lines = section.split("\n")
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                        
                    # Handle bullet points with proper indentation
                    if line.startswith("- "):
                        indent_width = 5
                        bullet_text = line[2:]  # Remove the "- " part
                        
                        # Calculate available width and handle wrapping
                        available_width = pdf.w - pdf.l_margin - pdf.r_margin - indent_width
                        
                        pdf.set_x(pdf.l_margin + indent_width)
                        pdf.multi_cell(available_width, 5, txt="• " + bullet_text)
                    else:
                        # Regular text - use multi_cell for automatic text wrapping
                        pdf.multi_cell(0, 5, txt=line)
                    
            pdf.ln(4)
    
    # Save PDF to a temporary file
    pdf_file = "resume.pdf"
    pdf.output(pdf_file)
    
    # Read the PDF file and return as base64
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
    
    os.remove(pdf_file)  # Remove the temporary file
    return base64.b64encode(pdf_bytes).decode()

def generate_resume(personal_info, education, experience, skills, job_description):
    prompt = f"""
    You are a professional resume writer. Create a well-formatted, ATS-friendly resume based on the following information:
    
    Personal Information:
    {personal_info}
    
    Education:
    {education}
    
    Work Experience:
    {experience}
    
    Skills:
    {skills}
    
    Job Description I'm applying for:
    {job_description}
    
    Please tailor this resume to highlight relevant experiences and skills that match the job description.
    Format the resume cleanly with clear sections for Personal Information, Summary, Experience, Education, and Skills.
    Use bullet points for experience and achievements.
    Be concise and focus on accomplishments and measurable results.
    Optimize for ATS systems by incorporating relevant keywords from the job description.
    The output should be in a clean text format (no HTML).
    
    IMPORTANT: Keep all bullet points and text concise. No individual line should exceed 100 characters.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a professional resume writer who creates tailored, ATS-friendly resumes. Keep all text and bullet points concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=4000
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating resume: {str(e)}")
        return None

def main():
    st.title("AI Resume Builder")
    
    st.info("This application helps you create a customized resume that is tailored to a specific job description. Fill in your details and provide the job description to get an optimized resume.")
    
    # Check for API key
    if not os.environ.get("GROQ_API_KEY"):
        st.warning("Please set your GROQ_API_KEY as an environment variable to use this application.")
        api_key = st.text_input("Or enter your Groq API key here:", type="password")
        if api_key:
            os.environ["GROQ_API_KEY"] = api_key
    
    # Create tabs
    tab1, tab2 = st.tabs(["Create Resume", "View Resume"])
    
    with tab1:
        st.header("Enter Your Information")
        
        # Personal Information
        st.subheader("Personal Information")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        location = st.text_input("Location (City, State)")
        linkedin = st.text_input("LinkedIn URL (optional)")
        
        personal_info = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Location: {location}
        LinkedIn: {linkedin}
        """
        
        # Education
        st.subheader("Education")
        education = st.text_area("Education Details", 
                                height=150, 
                                placeholder="Example:\nMaster of Science in Computer Science\nStanford University, 2018-2020\nGPA: 3.8/4.0\n\nBachelor of Engineering in Software Engineering\nMIT, 2014-2018\nGPA: 3.7/4.0")
        
        # Work Experience
        st.subheader("Work Experience")
        experience = st.text_area("Work Experience", 
                                height=250,
                                placeholder="Example:\nSenior Software Engineer, Google, 2020-Present\n- Led development of a new feature that increased user engagement by 25%\n- Managed a team of 5 engineers for a critical project\n- Implemented CI/CD pipeline reducing deployment time by 40%\n\nSoftware Engineer, Facebook, 2018-2020\n- Developed backend APIs serving 1M+ daily active users\n- Reduced server response time by 30% through code optimization")
        
        # Skills
        st.subheader("Skills")
        skills = st.text_area("Skills", 
                            height=100,
                            placeholder="Example:\nTechnical: Python, JavaScript, React, Node.js, SQL, AWS, Docker, Kubernetes\nSoft Skills: Project Management, Team Leadership, Communication, Problem-solving")
        
        # Job Description
        st.subheader("Job Description")
        job_description = st.text_area("Paste the job description you're applying for", 
                                    height=250,
                                    placeholder="Paste the complete job description here to tailor your resume accordingly.")
        
        if st.button("Generate Resume"):
            if not name or not email or not education or not experience or not skills or not job_description:
                st.error("Please fill in all required fields.")
            else:
                with st.spinner("Generating your customized resume... This may take a minute."):
                    # Store the resume in session state
                    st.session_state.resume_content = generate_resume(
                        personal_info, education, experience, skills, job_description
                    )
                    if st.session_state.resume_content:
                        st.success("Resume generated successfully! Go to the 'View Resume' tab to see it.")
    
    with tab2:
        st.header("Your Customized Resume")
        
        if 'resume_content' in st.session_state and st.session_state.resume_content:
            # Display the resume
            st.markdown(st.session_state.resume_content)
            
            col1, col2 = st.columns(2)
            
            # Create PDF
            with col1:
                if st.button("Download as PDF"):
                    try:
                        with st.spinner("Creating PDF file..."):
                            pdf_data = create_pdf_resume(st.session_state.resume_content)
                            
                            # Create download link
                            href = f'<a href="data:application/octet-stream;base64,{pdf_data}" download="resume.pdf">Click here to download your resume as PDF</a>'
                            st.markdown(href, unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error creating PDF: {str(e)}")
                        st.info("The resume might be too complex for PDF conversion. Try using the 'Copy to Clipboard' option instead.")
            
            # Copy to clipboard option
            with col2:
                if st.button("Copy to Clipboard"):
                    st.code(st.session_state.resume_content)
                    st.success("Resume copied to clipboard! You can now paste it elsewhere.")
        else:
            st.info("Generate a resume first to see it here.")

if __name__ == "__main__":
    main()