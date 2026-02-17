# Accessibility and Rights Assistant ♿

This project is a web application developed with Streamlit that uses artificial intelligence (Gemini 2.0 Flash) to offer legal and technical guidance on accessibility and inclusion rights in Chile.

## Features

- **Expert Assistant**: Personalized guidance based on the type of user (Citizen/Institution).
- **Chilean Legal Basis**: Uses a provided legal context (`normativa_chile.md`) to support its responses.
- **AI Model**: Implemented with `google-genai` (Gemini 2.0 Flash).

## Requirements

Ensure you have Python installed. The main libraries are:

- `streamlit`
- `google-genai`

You can install them by running:

```bash
pip install streamlit google-genai
```

## Configuration

1. **Clone the repository** and navigate to the project folder.
2. **Configure credentials**:
   - Create a `.streamlit` folder in the project root if it doesn't exist.
   - Create a `secrets.toml` file inside `.streamlit/`.
   - Add your Google API Key:
     ```toml
     GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
     ```

## Execution

To start the application, run the following command in your terminal:

```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main application code.
- `normativa_chile.md`: File containing the legal and normative context.
- `.streamlit/secrets.toml`: Configuration file for keys (not included in the repository for security).

## Notes

This assistant is an informative tool and does not constitute formal legal advice. Always verify information with official sources.
