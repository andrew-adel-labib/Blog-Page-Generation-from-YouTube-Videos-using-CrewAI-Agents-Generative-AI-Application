import os 
from dotenv import load_dotenv
from crew import Agent
from tools import yt_tool

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

blog_researcher = Agent(
    role="Blog Researcher for YouTube Videos",
    goal="Retrieve the relevant video transcription for the topic {topic} from the provided YouTube channel.",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos on AI, Data Science, "
        "Machine Learning, and Generative AI, and in providing suggestions."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Write compelling tech stories based on the video {topic} from the YouTube channel.",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)