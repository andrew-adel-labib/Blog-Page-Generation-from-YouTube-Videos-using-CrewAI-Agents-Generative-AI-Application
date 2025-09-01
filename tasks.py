from crew import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task = Task(
  description=(
    "Identify the video {topic}. "
    "Get detailed information about the video from the channel."
  ),
  expected_output="A comprehensive report, three paragraphs long, based on the {topic} of the video content.",
  tools=[yt_tool],
  agent=blog_researcher
)

write_task = Task(
  description=(
    "Get the information from the YouTube channel on the topic {topic}."
  ),
  expected_output="Summarize the information from the YouTube channel video on the topic {topic}, and create content for the blog.",
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file="new-blog-post.md"
)