========================================================================
             RAG Pipeline with Docling & LangChain
========================================================================

Follow these quick instructions to get the project up and running.

------------------------------------------------------------------------
1. FIRST TIME USE / INITIAL SETUP
------------------------------------------------------------------------
Before running the pipeline for the first time, you need to create the 
virtual environment and install all necessary dependencies. 

Simply double-click or run the setup batch script from your terminal:

    setup.bat

This script will automatically:
- Create a local '.venv' folder.
- Bootstrap and upgrade 'pip'.
- Install all required libraries listed in 'requirements.txt'.


------------------------------------------------------------------------
2. NEXT TIME ONWARDS (DAILY USE)
------------------------------------------------------------------------
Once the setup has been run successfully once, you DO NOT need to run 
'setup.bat' again. Going forward, just activate the environment and 
run your script.

Step 1: Open your terminal and activate the virtual environment:
        
        Windows (Command Prompt):
        .venv\Scripts\activate.bat

        Windows (PowerShell):
        .venv\Scripts\Activate.ps1

        Git Bash / Linux / macOS:
        source .venv/Scripts/activate  (or bin/activate for macOS/Linux)

Step 2: Set your Groq API Key (if not already set in your system):
        
        set GROQ_API_KEY=your_actual_api_key_here

Step 3: Run your Python script:

        python rag_pipeline.py --query "Your question here"


------------------------------------------------------------------------
3. PIPELINE USAGE EXAMPLES
------------------------------------------------------------------------
Ingest a new file and query it simultaneously:
python rag_pipeline.py --document "AtliqAI_HR_Policies.pdf" --query "What is the probation period?"

Query the existing/saved vector database directly:
python rag_pipeline.py --query "What is the policy on casual leaves?"
========================================================================