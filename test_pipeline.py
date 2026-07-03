from agents.pipeline_agent import PipelineAgent

pipeline = PipelineAgent()

lead = pipeline.process(
    "https://founders.ai"
)

print(lead)