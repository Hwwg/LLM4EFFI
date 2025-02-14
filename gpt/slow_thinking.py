import json

from gpt.gpt_reply import  GPTReply
import re
from prompt.slow_reasoning import slow_prompt

from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import threading
from tools.sanitize.sanitize import sanitize
# from tools import code_gen_v6
from tools.data import get_evalperf_data, get_human_eval_plus, get_mbpp_plus
class slow_thinking:
    def __init__(self, model):
        self.model = model
        self.gpt = GPTReply(model)
        self.prompt = slow_prompt()

    def slow_thinking_process(self,systemprompt,user1prompt,user2prompt):
        problem_item = self.problem_item_gen(systemprompt,user1prompt,user2prompt)
        problem_solved_result = self.problem_solved_chains(problem_item,user1prompt)
        final_result = self.format_ensure(problem_solved_result)
        return final_result

    def format_ensure(self,formate_prompt,beformat_result):
        return self.gpt.getreply(formate_prompt,"This is the content:"+beformat_result,"")

    def step_extractor(self,problem_description):
        problem_item = {}
        for i in range(1,20):
            try:
                code_regexp_pattern = re.compile(rf"```step{i}\n(.*?)```", re.DOTALL)
                matches = re.findall(code_regexp_pattern, problem_description)
                problem_item[str(i)] = matches[0]
            except:
                break
        return problem_item

    def problem_item_gen(self,systemprompt,user1prompt,user2prompt):
        ini_problem = systemprompt+user1prompt+user2prompt
        problem_step = self.gpt.getreply(self.prompt.problem_thinking,"This is the task that you need to split："+ini_problem,"")
        problem_step_dic = self.step_extractor(problem_step,)
        return problem_step_dic


    def problem_solved_chains(self,problem_item,task_description):
        pre_answer = ""
        temp_step = ""
        for key,value in problem_item.items():
            try:
                temp_step = self.gpt.getreply(self.prompt.algorithms_template.format(value),task_description,pre_answer)
                pre_answer = temp_step
            except:
                temp_step = self.gpt.getreply(self.prompt.algorithms_template.format(value),task_description, pre_answer)
                pre_answer = temp_step

        return temp_step

    def json_extract(self, data):
        try:
            code_regexp_pattern = re.compile(r"```json\n(.*?)```", re.DOTALL)
            matches = re.findall(code_regexp_pattern, data)
            if matches:
                # Ensure the JSON string is properly formatted
                return json.dumps(json.loads(matches[0]))
            else:
                raise ValueError("No JSON data found in the input string.")
        except Exception as e:
            print(f"Error extracting JSON: {e}")
            raise

    def max_score(self,score):
        try:
            max_key = max(score, key=lambda k: int(score[k]["score"]))
            return max_key
        except:
            raise RuntimeError


    def evaluate_code_process(self, task, code_dict,entry_point):
        code_score = {}
        try:
            def process_code_item(key, value):
                """单独处理每个 code_item 的任务"""
                partial_scores = {}
                # 多次调用 GPT 以获取评分
                for i in range(0, 1):
                    score_value = self.gpt.getreply(
                        self.prompt.evaluate_expert,
                        self.prompt.evaluate_expert_user.format(task, value),
                        ""
                    )
                    partial_scores[str(i)] = score_value

                # 获取最终得分

                final_score = self.gpt.getreply(
                    self.prompt.final_expert.format(task),
                    self.prompt.final_expert_user.format(str(partial_scores)),
                    ""
                )
                return key, final_score,value

            # 使用线程池并发执行
            with ThreadPoolExecutor() as executor:
                futures = []
                for code_item in code_dict:
                    for key, value in code_item.items():
                        futures.append(executor.submit(process_code_item, key, value))

                # 等待所有任务完成并收集结果
                for future in as_completed(futures):
                    key, final_score,code = future.result()
                    code_score[key] = {}
                    code_score[key]['comment'] = final_score
                    # code_score[key]['code'] = code

            # 找到得分最高的 key
            summrise_comment = self.gpt.getreply(
                self.prompt.summaries_code_system.format(task),
                self.prompt.summaries_code_user.format(code_score),
                ""
            )

            # fast_code_key = code_score
            final_score = self.gpt.getreply(
                self.prompt.candi_code.format(task),
                self.prompt.candi_code_user.format(summrise_comment),
                ""
            )
            suggestion = ""


            sanitized_solution = sanitize(
                final_score, entrypoint=entry_point
            )


            # final_code = [d[fast_code_key] for d in code_dict if fast_code_key in d][0]
            return sanitized_solution
        except:
            raise RuntimeError

# File lock for thread-safe file writing
file_lock = threading.Lock()


def key_exists_in_file(key, output_file):
    """检查指定的 key 是否已经存在于输出文件中"""
    try:
        with open(output_file, "r") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get("task_id") == key:
                        return True
                except json.JSONDecodeError:
                    continue  # 跳过损坏的 JSON 行
    except FileNotFoundError:
        pass  # 如果文件不存在，则视为 key 不存在
    return False

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
    else:
        raise ValueError(f"Invalid dataset {dataset}")
    dataset_list = [{key: value} for key, value in dataset_dict.items()]
    return dataset_list
def process_task(key, value, slthinking, output_file,que_data):
    """处理单个任务，如果 key 已存在于 output_file，则跳过"""
    if key_exists_in_file(key, output_file):
        print(f"Task {key} already exists in {output_file}. Skipping.")
        return
    if value["compare_code"] =='':
        print("ok",key)
    else:
        for i in que_data:
            if key in i.keys():
                entry_point = i[key]['entry_point']
                task_description = i[key]['disprompt'].strip() + "\n"
                break
        while True:
            try:
                result = {
                    "task_id": key,
                    "solution": slthinking.evaluate_code_process(task_description, value["compare_code"],entry_point)
                }
                print(result)
                with file_lock:  # 确保线程安全的文件写操作
                    with open(output_file, "a") as f:
                        f.write(json.dumps(result) + "\n")
                print(f"Processed task {key}")
                break
            except Exception as e:
                print(f"Error processing task {key}: {e}")

def main():
    try:
        # Load the data

        data_ini = get_data("evalperf")

        with open("../cache/backup/self_codegen_deepseek-coder_evalperf_1226_2_all.json", "r") as f:
            data = json.load(f)

        # Initialize the slow_thinking object
        slthinking = slow_thinking("deepseek-coder")

        # Define the output file
        output_file = "../cache/slow_thinking_9.jsonl"

        # Use ThreadPoolExecutor to manage tasks
        with ThreadPoolExecutor(max_workers=1) as executor:  # Limit the number of concurrent threads
            futures = [executor.submit(process_task, key, value, slthinking, output_file,data_ini) for key, value in data.items()]

            # Wait for all tasks to complete
            for future in as_completed(futures):
                future.result()  # Raise any exceptions that occurred in the thread

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()













