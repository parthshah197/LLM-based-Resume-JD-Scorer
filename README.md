# Resume Scorer for Job Descriptions

This project is a Streamlit web app designed to score resumes based on a given job description (JD). Leveraging a powerful language model (LLM) - Meta-Llama-3-8B-Instruct from Hugging Face, it evaluates the resume, assigns a matching percentage, and identifies missing important keywords based on the JD.

### Setup and Installation

1. **Clone the Repository:** Get started by cloning the repository to your local machine.

   ```sh
   git clone https://github.com/parthshah197/LLM-based-Resume-JD-Scorer.git
   cd resume-scorer
   ```

2. **Install Required Packages:** 

   ```sh
   pip install -r requirements.txt
   ```

3. **Set Hugging Face Token:** Replace the 'hf_token' variable with your actual Hugging Face API token.
   - Refer the below link to figure out how to get the HF token <br>
     https://huggingface.co/docs/hub/en/security-tokens


### How it works?
1. Start the Streamlit App:
   
   ```sh
   streamlit run app.py
   ```
   
2. Upload Resume: Users will upload their resumes in PDF format.
3. Input Job Description: Users will input the job description for which they want their resume to be evaluated.
4. Submit: Click on the "Submit" button to get the detailed feedback - matching percentage, lists missing top keywords, and gives a profile summary based on the job description. The app uses a Llama-3-8B model to analyze the resume and the job description.


### Contact
For any questions or issues, please open an issue in the repository or contact me at parthshah197@gmail.com
