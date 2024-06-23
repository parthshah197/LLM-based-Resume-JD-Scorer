# Resume Scorer for Job Descriptions

This project is a Streamlit web app designed to score resumes based on a given job description (JD). Leveraging a powerful language model (LLM) - Meta-Llama-3-8B-Instruct from Hugging Face, it evaluates the resume, assigns a matching percentage, and identifies missing important keywords based on the JD.

### Setup and Installation (without docker)

1. **Clone the Repository:** Get started by cloning the repository to your local machine.

   ```sh
   git clone https://github.com/parthshah197/LLM-based-Resume-JD-Scorer.git
   cd resume-scorer
   ```

2. **Install Required Packages:** 

   ```sh
   pip install -r requirements.txt
   ```

3. **Set Hugging Face Token:** Replace the 'hf_token' variable with your actual Hugging Face API token in the .env file.
   - Refer the below link to figure out how to get the HF token <br>
     https://huggingface.co/docs/hub/en/security-tokens


### Setup and Installation (using docker)

1. **Clone the Repository:** Get started by cloning the repository to your local machine.

   ```sh
   git clone https://github.com/parthshah197/LLM-based-Resume-JD-Scorer.git
   cd resume-scorer
   ```

2. **Set Hugging Face Token:** Replace the 'hf_token' variable with your actual Hugging Face API token in the .env file.
   - Refer the below link to figure out how to get the HF token <br>
     https://huggingface.co/docs/hub/en/security-tokens

3. **Build the docker image**
   
   ```sh
   docker build -t streamlit_llm_app:latest .
   ```
   
4. **Run the docker container** - We need to set the host 8501 while running the container as we've exposed port 8501 in the Dockerfile config for the streamlit app on the local machine
   ```sh
   docker run -p 8501:8501 streamlit_llm_app:latest
   ```

### How it works?
1. Start the Streamlit App:
   If you are not using docker, run the below command to start the streamlit app. If you are ran the docker container, you'll get the local host link for the streamlit app - http://localhost:8501/

   ```sh
   streamlit run app.py
   ```
   
2. Upload Resume: Users will upload their resumes in PDF format.
3. Input Job Description: Users will input the job description for which they want their resume to be evaluated.
4. Submit: Click on the "Submit" button to get the detailed feedback - matching percentage, lists missing top keywords, and gives a profile summary based on the job description. The app uses a Llama-3-8B model to analyze the resume and the job description.


### Contact
For any questions or issues, please open an issue in the repository or contact me at parthshah197@gmail.com
