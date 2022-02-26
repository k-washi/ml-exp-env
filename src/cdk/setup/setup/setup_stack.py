from constructs import Construct

from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_s3 as _s3
)


class SetupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, cfg,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = cfg.aws_s3_dataset_bucket
        self.dataset_s3 = _s3.Bucket(
            self,
            f"MLFlow_DATASET_BUCKET_{bucket_name}",
            bucket_name=bucket_name,
            auto_delete_objects=True,
            removal_policy=RemovalPolicy.DESTROY
            )

