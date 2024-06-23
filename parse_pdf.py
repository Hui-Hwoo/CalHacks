from PyPDF2 import PdfReader
from openai import OpenAI

from anki.utils import invoke

from dotenv import load_dotenv
import os
import json

load_dotenv()


def extract_text_from_pdf(pdf_path="./sample.pdf"):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    n = max(7, number_of_pages)

    string = ""
    for i in range(n):
        page = reader.pages[i]
        string += page.extract_text()

    return string


def fetch_QAs_from_text(text):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_KEY"),
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            },
            {
                "role": "user",
                "content": """generate question-answer pairs from the text below, \
                            questions should be concepts and answers should be explanations\
                            return in the format:\
                            ```json
                            {"pairs": [{"Qustion":"qustion1", "Answer": "answer1"} ...]}
                            ```
                            """
                + text,
            },
        ],
    )

    message = completion.choices[0].message
    parsed = json.loads(message.content.strip("```").lstrip("json"))
    print(parsed["pairs"])
    return parsed["pairs"]


def main():
    text = extract_text_from_pdf()
    QAs = fetch_QAs_from_text(text[:10000])

    current_deck = {"name": "CalHacks", "id": 1719082606356}
    for QA in QAs:
        Question = QA["Question"]
        Answer = QA["Answer"]
        invoke(
            "addNote",
            note={
                "deckName": current_deck["name"],
                "modelName": "CalHacks",
                "fields": {"Question": Question, "Answer": Answer},
            },
        )


if __name__ == "__main__":
    main()
