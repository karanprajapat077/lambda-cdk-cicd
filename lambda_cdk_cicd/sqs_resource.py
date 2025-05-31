from aws_cdk import aws_sqs as sqs
from constructs import Construct

def create_hourglass_queue(scope: Construct, queue_name: str) -> sqs.Queue:
    """
    Create an SQS queue for the Hourglass application.

    :param scope: The scope in which to define this resource.
    :param queue_name: The name of the SQS queue.
    :return: An instance of the created SQS queue.
    """
    return sqs.Queue(
        scope,
        "HourglassQueue",
        queue_name=queue_name,
        visibility_timeout=sqs.Duration.seconds(300),
        retention_period=sqs.Duration.days(4)
    )