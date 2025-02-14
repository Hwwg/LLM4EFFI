import json
import datasets
from gpt.gpt_reply import GPTReply
import re
import concurrent.futures
from tqdm import tqdm
prompt = """
请帮我整理以下测试用例，使其成为规范可执行的测试用例。并按照如下格式输入：
```python
<code>
```
这是一个例子：
输入
entry point:
class Solution(object):
    def numDistinct(self, s, t):
        \"\"\"
        :type s: str
        :type t: str
        :rtype: int
        \"\"\"
case:
Input: s = "rabbbit", t = "rabbit"\nOutput: 3

输出:
```python
def check(candidate):
    sol = Solution()
    assert candidate(sol,"rabbbit","rabbit") == 3
```
"""
prompt2 = """
entry point name:
{}
case:
{}
"""
def data_formted():
    dataset_dict = datasets.load_dataset("parquet", data_files="/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/dataset/Mercury/eval-00000-of-00001.parquet", split="train")
    return [{example["slug_name"]:dict(example)} for example in dataset_dict]


def text_extract(data):
    code_key_pattern = re.compile(r"```python\n(.*?)```", re.DOTALL)
    found = re.findall(code_key_pattern, data)

    # 确保找到了内容，避免 index out of range 错误
    if found:
        return found[0]
    else:
        # 如果没有找到，返回一个空字符串或其他合适的默认值
        print("No match found in text extract.")
        return ""


def process_item(num, key, value, gptreply, prompt, prompt2):
    try:
        raw_case = value["pretty_content"]
        case = gptreply.getreply(prompt, prompt2.format(value["prompt"], raw_case), "")

        # 检查返回值是否有效
        if case:
            formated_case = text_extract(case)
            return num, key, formated_case
        else:
            print(f"Empty response for key: {key}")
            return num, key, None
    except Exception as e:
        print(f"Error: {e}")
        print(f"Problematic key: {key}")
        return num, key, None


def process_data(data_dict, gptreply, prompt, prompt2):
    results = []

    # 使用 ThreadPoolExecutor 来并行处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        # 使用 tqdm 来显示进度条
        futures = {
            executor.submit(process_item, num, key, value, gptreply, prompt, prompt2): (num, key)
            for num in range(len(data_dict))
            for key, value in data_dict[num].items()
        }

        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            num, key, formated_case = future.result()
            if formated_case is not None:
                data_dict[num][key]["test"] = formated_case

    return data_dict


# Example of running the process with multi-threading and progress bar
gptreply = GPTReply("gpt-4o-mini")
data_dict = data_formted()

data_dict = process_data(data_dict, gptreply, prompt, prompt2)

# Save the processed data to a file
with open("../formated_data/Mercurry_case.json", "w+") as f:
    json.dump(data_dict, f, indent=4)