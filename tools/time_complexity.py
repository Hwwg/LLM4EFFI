from gpt.gpt_reply import GPTReply

import json
with open("../cache/backup/sorted_results.json", "r") as f:
    data = json.load(f)
print(data[0])

result = {}
failed_result = []
GptReply = GPTReply("gpt-4o-mini")
for i in range(0,20):
    try:
        time_complexity_result = GptReply.getreply("Please output the time complexity of the following code and use it. You only need to output a few results, for example: O(n)",
                                                   str(data[i]),"")
        result[str(i)] = time_complexity_result
        # print(time_complexity_result)

    except:
        failed_result.append(i)

print(json.dumps(result))
with open("time_result3.json","w+") as f:
    f.write(json.dumps(result))