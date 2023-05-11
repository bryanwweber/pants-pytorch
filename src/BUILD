__defaults__(all={"resolve": parametrize("python-default", "cpu", "gpu")})

python_requirements(name="requirements", source="pyproject.toml")
python_requirement(
    name="torch-default",
    requirements=["torch==2.0.1,!=2.0.1+cpu,!=2.0.1+cu118"],
    resolve="python-default",
)

python_requirement(
    name="torch-cpu",
    requirements=["torch==2.0.1+cpu"],
    resolve="cpu",
)

python_requirement(
    name="torch-gpu",
    requirements=["torch==2.0.1+cu118"],
    resolve="gpu",
)
pex_binary(
    name="gpu-training",
    layout="packed",
    include_tools=True,
    dependencies=["./ackbar/workflows/utils.py"],
    platforms=["linux_x86_64-cp-310-cp310"],
    resolve="gpu",
)
