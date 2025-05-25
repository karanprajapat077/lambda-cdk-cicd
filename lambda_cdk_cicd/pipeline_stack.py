from aws_cdk import Stack, SecretValue
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct
from .my_stage import MyAppStage

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        pipeline = CodePipeline(self, "Pipeline",
            pipeline_name="LambdaPipeline",
            synth=ShellStep("Synth",
                input=CodePipelineSource.git_hub(
                    "karanprajapat077/lambda-cdk-cicd",  # Example: "johnsmith/my-cdk-repo"
                    "dev",
                    authentication=SecretValue.secrets_manager("GITHUB_TOKEN")  # store GitHub PAT in Secrets Manager
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m venv .venv",y
                    "source .venv/bin/activate",
                    "pip install -r requirements.txt",
                    "cdk synth"
                ]
            )
        )

        pipeline.add_stage(MyAppStage(self, "DeployLambda"))
