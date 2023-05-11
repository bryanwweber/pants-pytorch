# Pants + Pytorch

This repo produces the following error:

```shell
pants package src:gpu-training

12:16:50.14 [INFO] Completed: Building local_dists.pex
12:17:06.12 [INFO] Completed: Building 3 requirements for src/gpu-training.pex from the 3rdparty/p
ython-gpu-lock.txt resolve: flytekit, loguru, torch==2.0.1+cu118
12:17:06.12 [ERROR] 1 Exception encountered:

Engine traceback:
  in `package` goal

IntrinsicError: Failed to execute: Process {
    argv: [
        "/Users/bweber/Library/Caches/nce/fc197caf7591487de8182f7932e70c61b197372bb3ec4c3ed53f6a8f
eac3234f/bindings/venvs/2.16.0rc1/bin/python",
        "./pex",
        "--tmpdir",
        ".tmp",
        "--jobs",
        "3",
        "--pip-version",
        "23.0.1",
        "--python-path",
        "/Users/bweber/.pyenv/versions/3.10.11/bin:/Users/bweber/.pyenv/versions/3.11.3/bin:/Users
/bweber/.pyenv/versions/3.9.16/bin:/Users/bweber/.local/bin:/Users/bweber/.cargo/bin:/Users/bweber
/go/bin:/Users/bweber/.pyenv/shims:/Users/bweber/.pyenv/bin:/opt/homebrew/bin:/Users/bweber/microm
amba/condabin:/Users/bweber/.local/bin:/Users/bweber/.cargo/bin:/Users/bweber/go/bin:/Users/bweber
/.pyenv/bin:/opt/homebrew/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin
:/sbin:/Applications/Little Snitch.app/Contents/Components:/var/run/com.apple.security.cryptexd/co
dex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr
/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin",
        "--output-file",
        "src/gpu-training.pex",
        "--no-emit-warnings",
        "--include-tools",
        "--requirements-pex",
        "local_dists.pex",
        "--platform",
        "linux_x86_64-cp-310-cp310",
        "--sources-directory=source_files",
        "flytekit",
        "loguru",
        "torch==2.0.1+cu118",
        "--lock",
        "3rdparty/python-gpu-lock.txt",
        "--no-pypi",
        "--index=https://pypi.org/simple/",
        "--index=https://download.pytorch.org/whl/cpu",
        "--index=https://download.pytorch.org/whl/cu118",
        "--manylinux",
        "manylinux2014",
        "--layout",
        "packed",
    ],
    env: {
        "CPPFLAGS": "",
        "LANG": "en_US.UTF-8",
        "LDFLAGS": "",
        "PATH": "/Users/bweber/.local/bin:/Users/bweber/.cargo/bin:/Users/bweber/go/bin:/Users/bwe
ber/.pyenv/shims:/Users/bweber/.pyenv/bin:/opt/homebrew/bin:/Users/bweber/micromamba/condabin:/usr
/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Little Snitch
.app/Contents/Components:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin
:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.c
ryptexd/codex.system/bootstrap/usr/appleinternal/bin",
        "PEX_IGNORE_RCFILES": "true",
        "PEX_PYTHON": "/Users/bweber/Library/Caches/nce/fc197caf7591487de8182f7932e70c61b197372bb3
ec4c3ed53f6a8feac3234f/bindings/venvs/2.16.0rc1/bin/python",
        "PEX_ROOT": ".cache/pex_root",
    },
    working_directory: None,
    input_digests: InputDigests {
        complete: DirectoryDigest {
            digest: Digest {
                hash: Fingerprint<772eccfddcf71013fa8c301a8aed8e0cf2e7f582562347489c9765e1862aefea
>,
                size_bytes: 515,
            },
            tree: "Some(..)",
        },
        nailgun: DirectoryDigest {
            digest: Digest {
                hash: Fingerprint<e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
>,
                size_bytes: 0,
            },
            tree: "Some(..)",
        },
        input_files: DirectoryDigest {
            digest: Digest {
                hash: Fingerprint<4a6729168c7fa29c1fc546019d32cbecf8627e42127dea37d14bcdbbe1da397a
>,
                size_bytes: 419,
            },
            tree: "Some(..)",
        },
        immutable_inputs: {
            RelativePath(
                ".python-build-standalone",
            ): DirectoryDigest {
                digest: Digest {
                    hash: Fingerprint<e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852
b855>,
                    size_bytes: 0,
                },
                tree: "Some(..)",
            },
        },
        use_nailgun: {},
    },
    output_files: {},
    output_directories: {
        RelativePath(
            "src/gpu-training.pex",
        ),
    },
    timeout: None,
    execution_slot_variable: None,
    concurrency_available: 3,
    description: "Building 3 requirements for src/gpu-training.pex from the 3rdparty/python-gpu-lo
ck.txt resolve: flytekit, loguru, torch==2.0.1+cu118",
    level: Info,
    append_only_caches: {
        CacheName(
            "pex_root",
        ): RelativePath(
            ".cache/pex_root",
        ),
    },
    jdk_home: None,
    cache_scope: Successful,
    execution_environment: ProcessExecutionEnvironment {
        name: None,
        platform: Macos_arm64,
        strategy: Local,
    },
    remote_cache_speculation_delay: 0ns,
}

Failed to digest inputs: "Error storing Digest { hash: Fingerprint<4626ecca9d97876686ac89adf4252f9
21617741f8fec8dcb16a8410375d240d8>, size_bytes: 2265668508 }: Invalid argument"
```
