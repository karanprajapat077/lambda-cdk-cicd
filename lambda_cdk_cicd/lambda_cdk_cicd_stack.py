from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _lambda_event_sources
)
from constructs import Construct
from .sqs_resource import create_hourglass_queue
class LambdaCdkCicdStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        func = _lambda.Function(
            self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="hourGlass.lambda_handler",
            code=_lambda.Code.from_asset("hourGlassCode/src"),
            function_name="hour-glass-function"
        )

        queue = create_hourglass_queue(self, "hour-glass-queue")

        func.add_event_source(_lambda_event_sources.SqsEventSource(queue)) 
