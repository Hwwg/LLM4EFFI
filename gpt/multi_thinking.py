from gpt.gpt_reply import  GPTReply
from prompt.slow_reasoning import multi_prompt
import concurrent.futures
class MultiThinking:
    def __init__(self, model):
        self.model = model
        self.gpt = GPTReply(model)
        self.prompt = multi_prompt()

    def multi_reason_candidate(self,systemprompt,user1prompt,user2prompt):
        num = 3
        candidate_result = {}
        for i in range(0,num):
            candidate_result[str(i)] = self.gpt.getreply(systemprompt,user1prompt,user2prompt)
        return candidate_result

    import concurrent.futures

    def multi_reason_candidate_thread(self, systemprompt, user1prompt, user2prompt):
        num = 3
        candidate_result = {}

        # 使用 for 循环来顺序执行任务
        for i in range(num):
            try:
                # 调用 getreply 方法并获取结果
                result = self.gpt.getreply(systemprompt, user1prompt, user2prompt)
                candidate_result[str(i)] = result
                # print(result)
            except Exception as e:
                print(f"Task {i} generated an exception: {e}")

        return candidate_result

    def difsame_result_gen(self,candidate_result):

        differ_content = self.gpt.getreply(self.prompt.diff_gen,candidate_result,"")
        same_content = self.gpt.getreply(self.prompt.same_gen,candidate_result,"")

        # print("same_content",same_content)
        # filterd_result = self.gpt.getreply(self.disprompt.check_contents,differ_content,"")
        consis_result = self.gpt.getreply(self.prompt.combine_result,same_content,differ_content)
        # print("consis_result",consis_result)
        return consis_result


    def main_process(self,systemprompt,user1prompt,user2prompt):

        candidate_result = self.multi_reason_candidate_thread(systemprompt,user1prompt,user2prompt)

        combine_result = self.difsame_result_gen(str(candidate_result))
        # print("combine_result")

        return combine_result





