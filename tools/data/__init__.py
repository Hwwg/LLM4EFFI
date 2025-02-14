import json

from datasets import load_dataset

from evalplus.data.humaneval import get_human_eval_plus, get_human_eval_plus_hash
from evalplus.data.mbpp import get_mbpp_plus, get_mbpp_plus_hash
from evalplus.data.utils import load_solutions, write_directory, write_jsonl


def get_evalperf_data():
    from datasets import load_dataset
    data_files = [
        "/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/dataset/evalperf/test-00000-of-00002.parquet",
        "/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/dataset/evalperf/test-00001-of-00002.parquet"
    ]
    # 加载多个 JSONL 文件并合并为一个数据集
    dataset = load_dataset("parquet", data_files=data_files, split="train").to_list()
    # dataset = load_dataset("evalplus/evalperf", split="test").to_list()
    for d in dataset:
        d["pe_input"] = json.loads(d["pe_input"])
    return {task["task_id"]: task for task in dataset}
