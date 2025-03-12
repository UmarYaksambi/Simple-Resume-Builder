# AI Resume Builder 📄

Welcome to the **AI Resume Builder**, an innovative application that leverages cutting-edge Large Language Models (LLMs) and API integrations to create professional, ATS-friendly resumes in minutes!

> **Presented at:** Code Sprint Workshop, **RVITM**
>
> **Purpose:** Demonstrating the power of LLMs and APIs in real-world applications.

## 🔍 About the Project
This project showcases how AI, specifically LLMs, can be integrated into applications to automate complex tasks like resume writing. The AI Resume Builder simplifies the process of creating tailored resumes by:

- Accepting personal details, education, experience, skills, and job descriptions.
- Using the Groq API with LLaMA-3 model to generate professional, concise resumes optimized for ATS systems.
- Offering download options in PDF format or copying the resume directly to the clipboard.

This project serves as a live demonstration of how APIs can be harnessed to create intelligent, user-friendly applications that solve real-world problems.

## 🔧 Features
- **Customized Resume Creation**: Tailor resumes based on user inputs and job descriptions.
- **PDF Export**: Download your generated resume as a PDF.
- **Clipboard Copy**: Copy the resume content to your clipboard for easy use.
- **User-Friendly UI**: Built with Streamlit for an intuitive interface.
- **Environment Variables**: Secure handling of API keys using environment variables.

## 🔧 Technologies Used
- **Python**
- **Streamlit** for web interface
- **Groq API** with LLaMA-3 model for AI-powered text generation
- **FPDF** for PDF creation
- **dotenv** for environment variable management

## 🕹þ How to Run the Project
1. **Clone the repository**:
```bash
git clone https://github.com/UmarYaksambi/Simple-Resume-Builder
cd Simple-Resume-Builder
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set Up Environment Variables**:
Create a `.env` file in the root directory and add your Groq API key:
```env
api_key=your_groq_api_key_here
```

4. **Run the Application**:
```bash
streamlit run app.py
```

## 🌍 How It Works
1. **Input Your Details**: Fill in personal information, education, experience, skills, and the job description.
2. **Generate Resume**: Click the **"Generate Resume"** button and let the AI do its magic.
3. **View & Download**: Preview the generated resume, download it as a PDF, or copy it to your clipboard.

## 🌟 Why This Project?
This application was crafted to demonstrate:
- The integration of **LLMs** and **APIs** in building intelligent applications.
- Real-world usage of **Streamlit** for rapid UI development.
- Best practices in API key management and data security.
- How AI can be leveraged to automate mundane tasks, enhancing productivity.

## 🔒 Security
- API keys are handled securely using environment variables with Python's `dotenv`.
- Temporary files are cleaned up post-PDF generation to avoid data leaks.

## 🚀 Future Enhancements
- Integrate more AI models for diversified resume styles.
- Allow customization of resume templates.
- Add error analysis and suggestions for improving resumes.
- Optimize PDF generation for more complex content structures.

## 🎓 About the Workshop
This project was presented at the **Code Sprint Workshop** conducted at **RVITM**, aimed at showcasing the practical applications of **Large Language Models (LLMs)** and API integrations. The workshop highlighted how AI can automate complex tasks and be easily incorporated into real-world solutions.

## 📢 Feedback & Contributions
We welcome feedback and contributions to improve this project further. Feel free to fork the repository and raise pull requests!

---

Built with 💜 for the future of intelligent automation!

