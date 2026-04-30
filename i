1
1
1
1








curl -fsSL https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260303/chwrdl/openclaw_installer.sh -o openclaw_installer.sh && bash openclaw_installer.sh

1
1
1
1

npm config set registry https://registry.npmmirror.com
from huggingface_hub import snapshot_downloadmodels = [    {        "repo_id": "openai/gpt-oss-120b",        "local_dir": "./gpt-oss-120b"    },    {        "repo_id": "mistralai/Mistral-Medium-3.5-128B",        "local_dir": "./Mistral-Medium-3.5-128B"    },    {        "repo_id": "Qwen/Qwen3.6-35B-A3B",        "local_dir": "./Qwen3.6-35B-A3B"    },    {        "repo_id": "deepseek-ai/DeepSeek-V4-Flash-Base",        "local_dir": "./DeepSeek-V4-Flash-Base"    },    {        "repo_id": "deepseek-ai/DeepSeek-R1",        "local_dir": "./DeepSeek-R1"    }]for model in models:    print(f"Downloading {model['repo_id']}...")    path = snapshot_download(        repo_id=model["repo_id"],        local_dir=model["local_dir"],        local_dir_use_symlinks=False    )    print(f"Model downloaded in: {path}\n")
