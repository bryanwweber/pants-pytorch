import torch
from flytekit import Resources, task, workflow
from loguru import logger


@task(
    requests=Resources(gpu="1"),
    container_image="570266238963.dkr.ecr.us-gov-west-1.amazonaws.com/ml-ackbar:gpu-test-0",
)
def get_gpu_task() -> str:
    use_cuda = torch.cuda.is_available()
    logger.info(f"Using CUDA: {use_cuda}")
    device = torch.device("cuda" if use_cuda else "cpu")

    return str(device)


@workflow
def gpu_test() -> str:
    return get_gpu_task()


if __name__ == "__main__":
    device = gpu_test()
    print(device)
