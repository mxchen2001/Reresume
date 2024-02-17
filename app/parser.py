import fitz  # PyMuPDF
import markdown
import pdfkit
from uuid import uuid4

def parse_pdf(pdf_bytes):
    # Open the PDF file
    document = fitz.Document(stream=pdf_bytes, filetype="pdf")
    
    # Initialize a variable to store text
    full_text = ""
    
    # Iterate through each page of the PDF
    for page_num in range(len(document)):
        page = document.load_page(page_num)  # Load the current page
        text = page.get_text()  # Extract text from the page
        full_text += text + "\n"  # Append text to the full_text variable
    
    document.close()  # Close the document
    return full_text


md_string = """# Matty Doe

[github.com/mattyDoe](github.com/mattyDoe) • [mattydoe.com](mattydoe.com) • [linkedin.com/in/mattydoe](linkedin.com/in/mattydoe) • mattydoe@gmail.com

---

## Education

**College University**
June 2026

- B.S. Computer Science
- Current GPA: 4.0/4.0

**Little High School (Dual Enrollment at Mission Community College)**
June 2022

- GPA: 4.44/4.0

---

## Coursework

- Object-Oriented Programming
- Data Structures & Algorithms
- Embedded Systems
- Discrete Math
- Linear Algebra
- Calculus
- Physics
- Probability & Statistics

---

## Skills

- Languages: C/C++, Python, Java, JavaScript/TypeScript, HTML/CSS, LATEX
- Tools: Git/GitHub, Unix Shell, Webpack, VS Code, IntelliJ CLion/PyCharm/IDEA, Atom

---

## Projects

**Carbon | Flutter, Dart, Supabase, APIs (INRIX, Google Maps), Git, Unix Shell, VS Code**
Nov. 2023

- Developed a social media mobile app to gamify eco-friendliness using the INRIX API
- Learned how to use Flutter in conjunction with backend databases and APIs

**ChatBuzz | TypeScript, HTML/CSS, Webpack, API (Twitch), Git, Unix Shell, VS Code**
May 2023 – Present

- Developed a full-stack web application for Twitch livestreamers to display repeated chat messages on OBS
- Experimented with Twitch API’s OAuth Access Tokens to get chat data from the given channel
- Collaborated with livestreamers to get feedback and suggested features

**FoodDropper | Java, Maven, API (Spigot), Git, IntelliJ IDEA**
Aug. 2022

- Developed a Minecraft server plugin to limit players to one way of replenishing their hunger bar
- Used persistent data containers to save and load data, ensuring that it persists across plugin resets
- Optimized UX e.g. sound design, food drop timing, supplied saturation level, and addressed potential workarounds

---

## Experience

**Competitive Programming Club | Member**
Sept. 2023 – Present

- Involved in the club centered around Competitive Programming

**Apex Tutoring | Tutor**
2019 – Present

- Routinely tutor K–12 students in math, coding, etc.

---

## Hobbies

- Playing the Drums (2013 – 2019)"""

def markdown_to_pdf(md_text, pdf_filepath):    
    # Convert Markdown to HTML
    html_text = markdown.markdown(md_text)

    
    # check if the file exists
    try:
        with open(pdf_filepath, 'w') as f:
            pass
    except:
        raise Exception("The file path is invalid")
    
    
    # Convert HTML to PDF
    pdfkit.from_string(html_text, pdf_filepath)
    
def markdown_to_html(md_text):
    return markdown.markdown(md_text)
    
    
    
# Example usage
markdown_to_pdf(md_string, "resume.pdf")

    