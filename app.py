#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_cdk_cicd.lambda_cdk_cicd_stack import LambdaCdkCicdStack

app = cdk.App()
LambdaCdkCicdStack(app, "LambdaCdkCicdStack")
app.synth()
