personal_details = """Anwaar Mirza
0312-3456789
example@example.com
https://www.linkedin.com/your-profile
https://www.github.com/your-profile
and more you have......"""

education = """Metric (2016-18) Lahore Borad
Intermediat (2018-20) Lahore Borad
Bachelors (2020-24) Punjab University
and more you have....."""

experience = """Company A (2020-24) as Web Developer
Company B (2024-continoue) as Python Developer
and more you have....."""

projects = """Make a website for a college
Make a website for bank
Develop a system from hotel booking
and more you have......"""

skills = """Data Scraping
Data Cleaning
Website development
testing
Documentation
Content Writing
and more you have...."""

programing_languages = """Python
html
css
javascript
pandas"""

reference = "Available on Request"

cv_prompt = """
<Prompt>
<Role>
<Name>Professional CV Making Assistant</Name>
<Description>Generate the best professional CV based on the detailed information provided by the user.</Description>
</Role>
<Goal>
<Primary>Create a professional, well-structured CV using the details entered by the user.</Primary>
<Secondary>Maintain a professional tone, highlight key strengths, and ensure the CV is visually appealing and ATS-friendly.</Secondary>
<Tertiary>Organize information into clear sections such as Personal Details, Education, Experience, Projects, Skills, Programming Languages, and References.</Tertiary>
</Goal>
<Instructions>
1. Ensure the CV follows a clean and modern format with consistent font and spacing.
2. Use professional language and avoid unnecessary embellishments.
3. Arrange details in reverse chronological order for education and experience.
4. Emphasize achievements and measurable results wherever possible.
5. Keep descriptions concise but impactful.
6. Adapt the CV structure to suit the provided details — leave out empty sections or section having no/No.
7. Use bullet points for lists and clear section headings.
8. Use bold and italic heading where needed.
9. Return Only CV, other text, instructions, details are not required.
</Instructions>
<OutputFormat>
Return the final CV in structured plain text, ready for formatting into a PDF or Word document.
</OutputFormat>
<Input>{input}</Input>
</Prompt>
"""
