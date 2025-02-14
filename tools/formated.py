import json
import re
import os
# from sanitize.sanitize import sanitize
import glob

import datasets

from sanitize.sanitize import sanitize

from tools.data import get_evalperf_data, get_human_eval_plus, get_mbpp_plus



def enamel_formatted(data):
    """
    从数据中提取 HumanEval 的 code 字段，并按顺序组合成列表
    :param data: 包含 HumanEval 数据的字典
    :return: 提取的 code 列表
    """
    result = []
    for i in range(165):
        key = f"HumanEval/{i}"
        if key not in data:
            continue  # 跳过缺失的键
        entry = data[key]
        if len(entry) < 2 or "code" not in entry[1]:
            continue  # 跳过无效条目
        code_list = entry[1]["code"]
        result.append(code_list)
    return result

def evalplus_toename(data):
    result = []
    for i in data:
        result.append([i["solution"]])
    return result


def formated_effilearner(data):
    result = []

    for i in range(165):
        try:
            key = f"HumanEval/{i}"
            if key not in data[i]["task_id"]:
                continue  # 跳过缺失的键
            tmp_code = data[i]["tmp_completion"]
            code =  [sanitize(
                       tmp_code, entrypoint=data[i]["entry_point"]
                    )]
            # if len(entry) < 2 or "code" not in entry[1]:
            #     continue  # 跳过无效条目
            # code_list = entry[1]["code"]
            result.append(code)
        except:
            print(i)
    return result
def formated_effilearner_mercury(data):
    result = {}

    for i in range(len(data)):
        try:
            tmp_result = {}
            tmp_code = data[i]["tmp_completion"]
            code =  sanitize(
                       tmp_code, entrypoint=data[i]["entry_point"]
                    )
            tmp_result["task_id"] = data[i]["task_id"]
            tmp_result["completion"] = code
            result[data[i]["task_id"]] = [tmp_result]


        except:
            print(i)
    return result

def formatted_mercury(data):
    result = {}
    for key,value in data.items():
        entry = data[key]
        if len(entry) < 2 or "code" not in entry[1]:
            continue  # 跳过无效条目
        code_list = entry[1]["code"]
        result[key] = [{"task_id":key,"completion":code_list[0]}]
    return result

def formatted_evalplerf(dir_path, output_file="merged.jsonl"):
    """
    dir_path下有很多json文件，我希望能够读取这些json文件，
    这些json文件的格式都是{"HumanEval/0":["HumanEval/0",{"code":["aaa"]}],"HumanEval/1":["HumanEval/1",{"code":["aba"]}]}
    我希望能够提取出所有文件的json数据，并将其键名作为task_id的值，code的值作为solution的值，形成以下Json格式：
    {"task_id":"HumanEval/0","solution":"aaa"}，
    并将所有的值写入到同一个jsonl文件中
    :param dir_path:
    :return:
    """


    all_entries = []

    # 1) 找到 dir_path 下所有 .json 文件
    # json_files = glob.glob(os.path.join(dir_path, "*.json"))

    # 2) 依次读取每个 JSON 文件
    # for file_path in json_files:
    with open(dir_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        # 3) 解析 JSON 文件里的键值对
    for key, value in data.items():
        # 假设格式:  "HumanEval/0": [ "HumanEval/0", {"code":["aaa", ...]} ]
        # 则 value[1] 应该是 {"code":["aaa",...]} 这类字典
        if len(value) < 2:
            # 如果数据格式不符，可根据需要跳过或者 raise
            continue

        meta_info = value[1]  # {"code": [...]} 结构
        # 提取 code 数组
        code_list = meta_info.get("code", [])
        if not code_list:
            code_str = ""  # 如果 code 为空，可自定义处理
        else:
            # 如果确定只有一个字符串，就取第一个
            # 如果 code 里有多行，可用 "\n".join(code_list) 或其他方式组合
            code_str = code_list[0]

        # 4) 组装成 { "task_id": ..., "solution": ... }
        entry = {
            "task_id": key,
            "solution": code_str
        }
        all_entries.append(entry)

    # 5) 将结果写入 JSONL
    with open(output_file, "w", encoding="utf-8") as f:
        for item in all_entries:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")

    print(f"成功处理 个文件，写入 {len(all_entries)} 条记录 -> {output_file}")

def formatted_evalplerf_ecco(data_path,dataset_name, output_file="merged.jsonl"):
    """
    dir_path下有很多json文件，我希望能够读取这些json文件，
    这些json文件的格式都是{"HumanEval/0":["HumanEval/0",{"code":["aaa"]}],"HumanEval/1":["HumanEval/1",{"code":["aba"]}]}
    我希望能够提取出所有文件的json数据，并将其键名作为task_id的值，code的值作为solution的值，形成以下Json格式：
    {"task_id":"HumanEval/0","solution":"aaa"}，
    并将所有的值写入到同一个jsonl文件中
    :param dir_path:
    :return:
    """
    with open(data_path,"r") as f:
        data = eval(f.read())
    result = {}
    data_result = get_data(dataset_name)
    all_entries = []
    for i in range(len(data)):
        tmp_result = {}
        keys_list = list(data_result[i].keys())
        # 假设你只想要第一个 key
        key = keys_list[0]
        # 然后用这个 key 去取 "entry_point"
        entry_point = data_result[i][key]["entry_point"]
        tmp_result["task_id"] = key
        tmp_result["solution"] = sanitize(
            data[i],entrypoint=entry_point
        )
        all_entries.append(tmp_result)
    with open(output_file, "w", encoding="utf-8") as f:
        for item in all_entries:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")

def formatted_evalplerf_effi(data,dataset_name, output_file="merged.jsonl"):
    """
    dir_path下有很多json文件，我希望能够读取这些json文件，
    这些json文件的格式都是{"HumanEval/0":["HumanEval/0",{"code":["aaa"]}],"HumanEval/1":["HumanEval/1",{"code":["aba"]}]}
    我希望能够提取出所有文件的json数据，并将其键名作为task_id的值，code的值作为solution的值，形成以下Json格式：
    {"task_id":"HumanEval/0","solution":"aaa"}，
    并将所有的值写入到同一个jsonl文件中
    :param dir_path:
    :return:
    """
    # with open(data_path,"r") as f:
    #     data = eval(f.read())
    # result = {}
    # data_result = get_data(dataset_name)
    all_entries = []
    for i in range(len(data)):
        tmp_result = {}
        tmp_code = data[i]["tmp_completion"]
        code = sanitize(
            tmp_code, entrypoint=data[i]["entry_point"]
        )
        tmp_result["task_id"] = data[i]["task_id"]
        tmp_result["solution"] = code
        all_entries.append(tmp_result)
    with open(output_file, "a+", encoding="utf-8") as f:
        for item in all_entries:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")
    print("write successful:", output_file)

def formated_original_evalperf(data,output_file):
    data = data["eval"]
    result = []
    for key,value in data.items():
        tmp_result = {}
        tmp_result["task_id"] = key
        for i in range(0,20):
            try:
                tmp_result["solution"] = value["profiled"][i]["solution"]
                result.append(tmp_result)
            except:
                tmp_result["solution"] = ""
                result.append(tmp_result)

    with open(output_file, "w", encoding="utf-8") as f:
        for item in result:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")
    print("write successful:",output_file)
def formated_ecco(dataset,data_path):
    with open(data_path,"r") as f:
        data = eval(f.read())
    result = []
    data_result = get_data(dataset)
    for i in range(0,164):
        result.append(
            [sanitize(data[i],entrypoint=data_result[i][f"HumanEval/{i}"]["entry_point"])]
        )
    return result

def formated_ecco_mercury(dataset,data_path):
    with open(data_path,"r") as f:
        data = eval(f.read())
    result = {}
    data_result = get_data(dataset)
    for i in range(len(data)):
        tmp_result = {}
        keys_list = list(data_result[i].keys())
        # 假设你只想要第一个 key
        key = keys_list[0]
        # 然后用这个 key 去取 "entry_point"
        entry_point = data_result[i][key]["entry_point"]
        tmp_result["task_id"] = key
        tmp_result["completion"] = sanitize(
            data[i],entrypoint=entry_point
        )
        result[key] = [tmp_result]

    return result





def load_json(path):
    """
    加载 JSON 文件
    :param path: JSON 文件路径
    :return: 解析后的字典
    """
    with open(path, "r") as f:
        data = json.load(f)
    return data

def load_data(file_path):
    with open(file_path, "r") as f:
        data = [json.loads(line.strip()) for line in f if line.strip()]
    return data

def main_process(dataset, path,tools):
    """
    主处理函数
    :param dataset: 数据集名称（如 "enamel"）
    :param path: 输入文件路径
    """
    # 提取文件名中的标识符
    file_name_pattern = re.compile(r"self_codegen_(.*?)_all\.json")
    file_name_pattern_2 = re.compile(r"code_gen_1106/cache/(.*?)temp_0\.0\deepseek_coder.jsonl")
    file_name_pattern_3 = re.compile(r"/code_gen_1106/cache/(.*?)\.json")
    file_name_pattern_4 = re.compile(r"self_codegen_(.*?)all")
    file_name_pattern_5= re.compile(r"evalperf/(.*?)_temp_1.0_evalperf_results\.brief\.json")
    file_name_pattern_6 =  re.compile(r"(.*?)_5\.json")
    file_name_pattern_7 =  re.compile(r"refine_raw_(.*?)\.txt")
    # raw_generations_qw_coder_enamel.txt

    # /Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/evalperf_original/evalplus.github.io/results/evalperf/gpt-4o-mini-2024-07-18_openai_temp_1.0_evalperf_results.brief.json
    # 处理数据
    if dataset == "enamel":
        if tools == "Agent":
            result = enamel_formatted(load_json(path))
            match = file_name_pattern.search(path)
            if not match:
                raise ValueError(f"Invalid file name format: {path}")
            filename = match.group(1)
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
        elif tools =="effi":
            result = formated_effilearner(load_json(path))
            match = file_name_pattern_3.search(path)
            if not match:
                raise ValueError(f"Invalid file name format: {path}")
            filename = match.group(1)
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{tools}/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
        elif tools == "ECCO":
            dataset = "humaneval"
            match = file_name_pattern_7.search(path)
            filename = match.group(1)+"_ECCO"
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
            # output_path = os.path.join(output_dir, f"{filename}deepseek_coder.json")
            result = formated_ecco(dataset,path)
    elif dataset == "humaneval":
        result = evalplus_toename(load_data(path))
        # match = file_name_pattern_2.search(path)
        # if not match:
        #     raise ValueError(f"Invalid file name format: {path}")
        filename = "qwen2.5-72b-instruct.json"
        output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
        os.makedirs(output_dir, exist_ok=True)
    elif dataset == "Mercury":
        if tools=="Agent":
            result = formatted_mercury(load_json(path))
            match = file_name_pattern.search(path)
            if not match:
                raise ValueError(f"Invalid file name format: {path}")
            filename = match.group(1)
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
        elif tools == "ECCO":
            dataset = "Mercury"
            match = file_name_pattern_7.search(path)
            filename = match.group(1) +"Mercury_ecco"
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
            # output_path = os.path.join(output_dir, f"{filename}deepseek_coder.json")
            result = formated_ecco_mercury(dataset,path)
        elif tools == "effi":
            result = formated_effilearner_mercury(load_json(path))
            match = file_name_pattern_3.search(path)
            if not match:
                raise ValueError(f"Invalid file name format: {path}")
            filename = match.group(1)
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{tools}/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
    elif dataset == "evalperf":
        if tools=="Agent":
            # file_name_pattern_4
            match = file_name_pattern_4.findall(path)
            filename = match[0]
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{filename}.jsonl")
            result = formatted_evalplerf(path,output_path)
            return
        elif tools=="ECCO":
            match = file_name_pattern_7.findall(path)
            filename = match[0]
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{filename}_ECCO.jsonl")
            result = formatted_evalplerf_ecco(path,dataset,output_path)
            exit()
        elif tools=="effi":
            # file_name_pattern_6
            match = file_name_pattern_6.findall(path)
            filename = match[0]
            output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}/"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{filename}_effi.jsonl")
            result = formatted_evalplerf_effi(load_json(path), dataset, output_path)
            exit()


    elif dataset == "evalperf_originial":
        match = file_name_pattern_5.search(path)
        filename = match.group(1)
        output_dir = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/final_results/{dataset}"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{filename}original.jsonl")
        result = formated_original_evalperf(load_json(path), output_path)
        exit()




    # 确保输出目录存在

    # 保存结果
    output_path = os.path.join(output_dir, f"{filename}.json")
    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)  # 使用 json.dump 而不是 json.dumps
    print(f"Results saved to: {output_path}")

def get_data(dataset):
    version = "default"
    if dataset == "humaneval":
        dataset_dict = get_human_eval_plus(version=version)
    elif dataset == "mbpp":
        dataset_dict = get_mbpp_plus(version=version)
    elif dataset == "evalperf":
        original_dataset = {**get_human_eval_plus(), **get_mbpp_plus()}
        dataset_dict = {k: original_dataset[k] for k in get_evalperf_data()}
        # assert id_range is None, "id_range not supported for evalperf"
    elif dataset == "Mercury":
        dataset_dict = datasets.load_dataset("parquet", data_files="/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/dataset/Mercury/eval-00000-of-00001.parquet", split="train")
        return [{example["slug_name"]:dict(example)} for example in dataset_dict]
    else:
        raise ValueError(f"Invalid dataset {dataset}")
    dataset_list = [{key: value} for key, value in dataset_dict.items()]

    return dataset_list


# 测试

file_path = f"/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/self_codegen_qwen2.5-coder-32b-instruct_Mercury_0125_special1_0_all.json"
main_process("Mercury", file_path,"Agent")