#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_cdk_cicd.pipeline_stack import PipelineStack


app = cdk.App()
PipelineStack(app, "MyCICDPipelineStack")
app.synth()
