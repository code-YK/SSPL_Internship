EXTRACTION_PROMPT = """
You are a data extraction engine.

TASK:
Extract structured profile information from the text below.

RULES (IMPORTANT):
- Output MUST be valid JSON
- Output MUST start with {{ and end with }}
- Do NOT include markdown
- Do NOT include explanations
- Do NOT include code fences
- Use double quotes for keys and values

TEXT:
{profile_text}

JSON SCHEMA:
{{
  "name": string | null,
  "education": string | null,
  "skills": array of strings,
  "experience": string | null
}}
"""

VALIDATION_QUESTION = """
I extracted the following profile information:

{extracted_content}

Is this correct? 
Reply with:
- yes
- or provide corrected dictionary
"""

ASSISTANT_PROMPT = """
You are an assistant.
User profile memory:
{memory}
"""
