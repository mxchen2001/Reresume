import requests
import dotenv
import os

dotenv.load_dotenv()
def query_gpt(prompt, model="gpt-3.5-turbo-0613", max_tokens=1024):
    # Replace YOUR_API_KEY with your actual OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=data
    )

    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()        
        return response_json.get("choices", [{}])[0].get("message", {}).get("content")
    else:
        return f"Error: {response.status_code}"


def expansion(text):
    prompt = f"Give me some targeted buzzwords for a {text} position. Give me as a list of comma-separated words."
    response_text = query_gpt(prompt)
    return response_text

# Example usage
prompt = """I want to apply for a product design position format the following resume to fit the job description. Remove irrelevant information. Return the response as a Markdown with styling.

Last Updated on January 12th, 2024
Matty Doe
§ github.com/mattyDoe Ð mattydoe.com ï linkedin.com/in/mattydoe # mattydoe@gmail.com
Education
College University
June 2026
B.S. Computer Science
Current GPA: 4.0/4.0
Little High School (Dual Enrollment at Mission Community College)
June 2022
GPA: 4.44/4.0
Coursework
Courses: Object-Oriented Programming, Data Structures & Algorithms, Embedded Systems, Discrete Math,
Linear Algebra, Calculus, Physics, Probability & Statistics
Awards: Dean’s Honor List (3x), AP Scholar with Distinction (2x), World Language History Award (Spanish)
Skills
Languages: C/C++, Python, Java, JavaScript/TypeScript, HTML/CSS, LATEX
Tools: Git/GitHub, Unix Shell, Webpack, VS Code, IntelliJ CLion/PyCharm/IDEA, Atom
Projects
Carbon | Flutter, Dart, Supabase, APIs (INRIX, Google Maps), Git, Unix Shell, VS Code
Nov. 2023
• Team project for the INRIX Hack 2023 Hackathon, earned Honorable Mention
• Developed a social media mobile app to gamify eco-friendliness using the INRIX API
• Learned how to use Flutter in conjunction with backend databases and APIs
ChatBuzz | TypeScript, HTML/CSS, Webpack, API (Twitch), Git, Unix Shell, VS Code
May 2023 – Present
• Developed a full-stack web application for Twitch livestreamers to display repeated chat messages on OBS
• Experimented with Twitch API’s OAuth Access Tokens to get chat data from the given channel
• Collaborated with livestreamers to get feedback and suggested features
• Solved problems relating to asynchronous tasks
FoodDropper | Java, Maven, API (Spigot), Git, IntelliJ IDEA
Aug. 2022
• Developed a Minecraft server plugin to limit players to one way of replenishing their hunger bar
• Used persistent data containers to save and load data, ensuring that it persists across plugin resets
• Optimized UX e.g. sound design, food drop timing, supplied saturation level, and addressed potential workarounds
Experience
Competitive Programming Club | Member
Sept. 2023 – Present
Involved in the club centered around Competitive Programming
Apex Tutoring | Tutor
2019 – Present
Routinely tutor K–12 students in math, coding, etc.
Luigi Team Charity | Volunteer, Manager
2018 – Present
Earned an award for philanthropic hours spent, still giving away 100 stocked backpacks a year
Hobbies
Playing the Drums
2013 – 2019
Played the drums in symphonic, jazz, and marching bands
3rd Place Time Keeping Challenge Championship (Time Keeping Assocation)
Feb. 2022 – May 2022
Won $1500 nationally competing against high school students in counting seconds and minutes

"""
response_text = query_gpt(prompt)
print(response_text)


