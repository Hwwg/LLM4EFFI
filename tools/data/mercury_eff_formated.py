import json
from tools.data import get_evalperf_data, get_human_eval_plus, get_mbpp_plus
with open("/tools/formated_data/Mercurry_case.json", "r") as f:
  case_data = json.loads(f.read())

with open("/Users/tlif3./Desktop/all/zju_research/llm_codegeneration/code_gen_1106/cache/self_codegen_qwen2.5-72b-instruct_Mercury_0125_new_cot_1_all.json","r") as f:
  original_data = json.loads(f.read())

"""
"""
cur_dataset = "Mercury"
if cur_dataset=="Mercury":
    new_result = []
    for num in range(0,len(case_data)):
        for key,value in case_data[num].items():
            tmp_result = {}
            tmp_result["task_id"] = key
            tmp_result["prompt"] = value["prompt"]+value["pretty_content"][0]
            tmp_result["entry_point"] = value["entry_point"]
            tmp_result["test"] = value["test"]
            tmp_result["dataset"] = "Mercury"
            tmp_result["open_test_cases"] = value["test"]+f"\ncheck({value['entry_point']})"
            tmp_result["completion"] = {}
            tmp_result["completion"]["code"] = original_data[key][1]["code"][0]
            new_result.append(tmp_result)
    with open("../formated_data/Mercury_qwen2.5-72b-instruct.json", "w+") as f:
        json.dump(new_result,f,indent=4)
elif cur_dataset == "evalperf":
    original_dataset = {**get_human_eval_plus(), **get_mbpp_plus()}
    case_data = {k: original_dataset[k] for k in get_evalperf_data()}
    new_result = []
    for key,value in case_data.items():
        tmp_result = {}
        tmp_result["task_id"] = key
        tmp_result["prompt"] = value["prompt"]
        tmp_result["entry_point"] = value["entry_point"]
        if "HumanEval" in key:
            tmp_result["test"] = value["test"]
            tmp_result["dataset"] = "HumanEval"
            tmp_result["open_test_cases"] = value["test"] + f"\ncheck({value['entry_point']})"
        elif "Mbpp" in key:
            tmp_result["test"] = value["assertion"]
            tmp_result["dataset"] = "Mbpp"
            tmp_result["test_list"] = value["assertion"]
        tmp_result["completion"] = {}
        tmp_result["completion"]["code"] = original_data[key][1]["code"][0]
        new_result.append(tmp_result)
    with open("../formated_data/evalperf_qwen2.5-coder-32b-instruct.json", "w+") as f:
        json.dump(new_result,f,indent=4)
elif cur_dataset=="enamel":
    case_data = get_human_eval_plus()
    new_result = []
    for key,value in case_data.items():
        tmp_result = {}
        tmp_result["task_id"] = key
        tmp_result["prompt"] = value["prompt"]
        tmp_result["entry_point"] = value["entry_point"]
        if "HumanEval" in key:
            tmp_result["test"] = value["test"]
            tmp_result["dataset"] = "HumanEval"
            tmp_result["open_test_cases"] = value["test"] + f"\ncheck({value['entry_point']})"
        elif "Mbpp" in key:
            tmp_result["test"] = value["assertion"]
            tmp_result["dataset"] = "Mbpp"
            tmp_result["test_list"] = value["assertion"]
        tmp_result["completion"] = {}
        tmp_result["completion"]["code"] = original_data[key][1]["code"][0]
        new_result.append(tmp_result)
    with open("HumanEval_qwen2.5-coder-32b-instruct","w+") as f:
        json.dump(new_result,f,indent=4)



