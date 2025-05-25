from aws_cdk import Stage
from constructs import Construct
from .lambda_cdk_cicd_stack import LambdaCdkCicdStack

class MyAppStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        LambdaCdkCicdStack(self, "LambdaStack")
