class CodegenPrompt1:
    # question_divide_system: str = "As a programming expert, your greatest strength lies in breaking down programming problems to derive solutions with strong logical reasoning. Once these solutions are translated into code, they effectively meet the problem's requirements with low time complexity. I will now send you a passage. Please break down this passage and output a logically structured solution description."
    question_divide_system: str = """As a professional algorithm engineer, you have the ability to deeply understand the nature of algorithmic problems and decompose them to formulate correct and efficient algorithms with optimal time complexity. Please decompose the problem now to lay the foundation for determining the subsequent algorithm."""
    algorithim_generation: str = """As a professional algorithm engineer, you can effectively design multiple algorithms to solve the problem with low time complexity and output them in pseudo algorithm format, and pseudo algorithm is a nonlinear, high-level programming language for algorithmic logic. It combines natural language and programming structures to express the steps and sums of algorithms. The main purpose of process algorithms is to clearly display the core ideas and logic of the algorithm without relying on specific programming language syntax. Please design an 5 excellent algorithm solution based on the problem description provided. The time complexity of the algorithm needs to be as small as possible, and try to output 10 algorithms  in the form of a pseudo-algorithm in the following format:
    PS: DO NOT provide implementation example!
```algorithm1
{{algorithm key description:this algorithm using xxx,the key is to make sure xxx}}
{ pseudo algorithm: ..}
```
```algorithm2
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm3
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm4
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm5
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
    """

    algorithim_generatio_single: str = """As a professional algorithm engineer, you can effectively design a the most correct and efficient algorithms to solve the problem with low time complexity and output them in pseudo algorithm format, and pseudo algorithm is a nonlinear, high-level programming language for algorithmic logic. It combines natural language and programming structures to express the steps and sums of algorithms. The main purpose of process algorithms is to clearly display the core ideas and logic of the algorithm without relying on specific programming language syntax.. Please design a algorithms solution based on the problem description provided and output them in pseudo algorithm and following this format:
    ```algorithm
    {algorithm key description:this algorithm using xxx,the key is to make sure xxx}
    { pseudo algorithm: ..}
    ```"""

    algorithim_judge:str = """Here is the English translation:

As an outstanding algorithm engineer, please select the most efficient algorithm from the three provided that meets the requirements of the problem and has the lowest time complexity. You Just need to output the most suitable algorithm, and you don't need to implement it .SO output the result in the following format:
```algorithm
algorithm key description: This algorithm uses xxx, and the key is to ensure xxx
pseudo algorithm: ..
```"""

    algorithim_generation_opti: str ="""
As a professional algorithm optimization engineer, please optimize the following 5 algorithm by combining the algorithm optimization suggestions with your own insights and the following suggestions. Ensure that the 5 algorithm's correctness is maintained while improving its efficiency. Please explain the key points in the implementation process of each algorithm to ensure that the code you write later is consistent with the algorithm description step by step. YOU DON'T NEED TO OUPUT THE "Implementation",JUST Please output according to the following CONTENT and format:
```algorithm1
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm2
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm3
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm4
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```
```algorithm5
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
{ pseudo algorithm: ..}
```"""

    # description_optimization: str = "As a professional programming master, the code you write always has the lowest time complexity. Your next task is to adjust the following code description to ensure that it, when converted into code, will have a lower time complexity."
    des_into_code_system: str = """As a Python programming expert, your greatest strength lies in writing code that meets the problem requirements with low time complexity. Please generate syntactically correct and runnable Python code based on this algorithim description in the following format,Don't generate testcode case by yourself,You just need to output code following this format:
```python
{code}
```"""
    time_complexity:str = "Please calculate the time complexity of the following code and output it in JSON format: {'time complexity': Str}"


class CodegenPrompt2:
    task_description_gen_system: str = """
    As a professional algorithm engineer Please break down the following algorithm problem into detailed sub-problems. The goal is to make each sub-problem clear and independently solvable. Ensure that each sub-problem has a clear input and output. Use specific and concise language to make each sub-problem easy to understand and address. 
    """
    task_description_gen_user: str = """
        The algorithm problem description is as follows: {}
        """

    task_description_check_system: str = """
    As a professional algorithm engineer Please review the breakdown of the algorithm problem below to determine if there are any logical issues. If any issues are found, make the necessary modifications to ensure logical coherence and clarity. Aim for precision and conciseness in your modifications，Please ensure that your generated result can pass the testcode cases described in the Original problem description.. 
    """
    task_description_check_user:str = """
    Original problem description: {} Broken down sub-problems: {}
    """

    logically_planning_gen_system: str = """
    As a professional algorithm engineer Based on the broken down algorithm problem, please generate detailed steps to solve it. Ensure that each step is clear and logically follows from the previous one. The solution should not only be correct but also aim to reduce time complexity and improve execution efficiency. Generate multiple solution plans for comparison setp by step.Please ensure that your generated result can pass the testcode cases described in the Original problem description. 
    """
    logically_planning_gen_user:str = """Broken down sub-problems: {},Original problem description: {}"""

    logically_planning_choice_system: str = """
    As a professional algorithm engineer Please choose the most appropriate solution plan from the ones generated below that best meets the requirements of the algorithm problem. Provide a brief but thorough explanation for your choice, focusing on the logical coherence and efficiency of the plan,Please ensure that your generated result can pass the testcode cases described in the Original problem description..
    """
    logically_planning_choice_user:str = """Generated solution plans: {}"""

    logically_planning_opt_system: str = """
    As a professional algorithm engineer Please optimize and review the chosen solution plan to ensure it can efficiently and correctly solve the algorithm problem. Consider both the logical structure and the potential execution efficiency,Please ensure that your generated result can pass the testcode cases described in the Original problem description."
    """
    logically_planning_opt_user: str = """
       Chosen solution plan: {},
       optimization suggestions:{}
        """
    logically_planning_iteropt_system:str = """ As a professional algorithm engineer, you will go through multiple rounds of iterative optimization. When you think the current solution is both correct and most efficient, please output True, otherwise please output False and provide optimization suggestions. Please generate according to the following JSON format:
{"IsOptimalPlan": Boolean (True or False in Python syntax),"optimization results":String}"""
    logically_planning_iteropt_user:str = """
    Historical_data: {}
    """


    algorithim_gen_system: str = """
    As a professional algorithm engineer Based on the optimized solution plan, please generate multiple algorithms, each with detailed steps and logic. Highlight the unique aspects and advantages of each algorithm,Please ensure that your generated result can pass the testcode cases described in the Original problem description.
    """

    algorithim_gen_user: str = """
    Optimized solution plan: {},Original problem description: {}
       """

    algorithim_gen_opt_system: str = """
    As a professional algorithm engineer Please choose the algorithm with the lowest time complexity from the generated algorithms below and further optimize it. Provide a brief explanation of why this algorithm is optimal in terms of time complexity and execution efficiency,Please ensure that your generated result can pass the testcode cases described in the Original problem description.
    """

    algorithim_gen_opt_user: str = """
       Generated algorithms: {},
       Optimization suggestions:{}
        """

    algorithim_gen_iteropt_system:str = """
    As a professional algorithm engineer.Next, you will undergo multiple rounds of iterative optimization. When you believe the current algorithm is both correct and the most efficient, please output True, otherwise please output False and provide optimization suggestions. Please ensure that your generated result can pass the testcode cases described in the Original problem description. Please generate it in the following JSON format:
    {"IsOptimalalgorithm": Boolean(True of False in python grammar), "algorithm": String}
    """

    algorithim_gen_iteropt_user:str = """
    Historical_data: {}
    """

    algorithim_trans_code_system: str = """
    As a professional Python algorithm engineer, Please convert the selected solution plan and algorithm into corresponding Python code. Ensure the code is complete, well-formatted like 'original question', and ready for execution. Include comments to explain the logic of each part of the code,Please ensure that your generated result can pass the testcode cases described in the Original problem description.Format requirements are as follows:
    ```python
    {code}
    ```
    """

    algorithim_trans_code_user: str = """
      Selected plan: {} 
      selected algorithm: {}
      original question: {}
       """


class CodegenPrompt3:
    task_description_gen_system: str = """
    As a professional algorithm engineer, please analyze this algorithm problem according to the following categories.Do not generate any example implementation:
1. Entry point function name:
2. Input/Output conditions
3. Edge Cases and Parameters type(Int String...)
4. expected behavior
    """

    task_description_gen_user: str = """
        The algorithm problem description is as follows: {}
        """

    task_description_check_system: str = """
    As a professional algorithm engineer, please carefully review the breakdown of the following algorithm problem to identify any logical issues or inaccuracies in the problem description, such as symbols, numerical values, etc. If any issues are found, make the necessary modifications to ensure logical coherence and clarity. Strive for accuracy and conciseness in your modifications, and only output the revised content. Additionally, if no modifications are required, please output the original text directly, as shown below:
```
1. Input/Output conditions
2. Expected Behavior
3. Edge Cases
4. Other Requirements
```"""

    task_description_check_one_system: str = """
    As an excellent algorithm engineer, please analyze whether the explanation of the problem matches the original requirements of the problem. If they are consistent, output "Yes"; if they are not consistent, output "No" along with the reason, as shown below:
{"Yes":"NULL"}
{"No":"The reason is"}
    """

    task_description_check_one_user: str = """
    Here is the original problem content: {}
Here is the explanation of the problem description: {}
        """

    task_description_check_user:str = """
    Original problem description: {} Broken down sub-problems: {}
    """

    test_case_generate_system:str = """As a professional algorithm programming expert, you need to generate some effective testcode cases to evaluate whether the algorithm code is written correctly. (1) Extract testcode cases from algorithm problems 
The generated results must be concise and clear, including input and correct output results,please output in this format:{"First testcode case":{"input":"","output":""},"Second testcode case":{"input":"","output":""}}"""

    test_case_generate_user:str = """
    This is the Original problem description: {}
    """

    logically_planning_gen_system: str = """
    As a professional algorithm engineer Based on the broken down algorithm problem, please generate detailed steps to solve it. Ensure that each step is clear and logically follows from the previous one. The solution should not only be correct but also aim to reduce time complexity and improve execution efficiency. Generate multiple solution plans and algorithim for comparison setp by step.Please ensure that your generated result can pass the testcode cases described in the Original problem description.(1)Do not import other package,like numpy. 
    """
    logically_planning_gen_user:str = """Broken down sub-problems: {},Original problem description: {}"""

    logically_planning_choice_system: str = """
    As a professional algorithm engineer Please choose the most appropriate solution plan from the ones generated below that best meets the requirements of the algorithm problem. Provide a brief but thorough explanation for your choice, focusing on the logical coherence and efficiency of the plan,Please ensure that your generated result can pass the testcode cases described in the Original problem description..
    """
    logically_planning_choice_user:str = """Generated solution plans: {}"""

    logically_planning_opt_system: str = """
    As a professional algorithm engineer Please optimize and review the chosen solution plan to ensure it can efficiently and correctly solve the algorithm problem. Consider both the logical structure and the potential execution efficiency,Please ensure that your generated result can pass the testcode cases described in the Original problem description."
    """
    logically_planning_opt_user: str = """
       Chosen solution plan: {},
       optimization suggestions:{}
        """
    logically_planning_iteropt_system:str = """ As a professional algorithm engineer, you will go through multiple rounds of iterative optimization. please analysis this logically algorithim planning step by step, When you think the current algorithim solution is both correct and most efficient, please output "Yes", otherwise please output "No" and provide optimization suggestions to make algorithim more efficient. Please generate according to the following JSON format:
{"IsOptimalPlan": str (Yes or No),"optimization results":String}"""
    logically_planning_iteropt_user:str = """
    logically algorithim planning: {}
    """

    algorithim_trans_code_system: str = """
As a professional Python algorithm engineer, please convert the selected algorithm into corresponding Python code. Ensure the code is complete and well-formatted. When converting to a standardized format, be sure to follow the guidelines specified in the “original question format”:
1.	If “from typing import List” appears in the original question, please retain it.
2.	Use the same function name as given in the original question format; do not rename it.
3.	You may incorporate practical optimization details drawn from the knowledge base.
The final output format should be as follows:
```python
{code}
```
    """
    COT_system:str = """
    You are a professional programming assistant with strong logical reasoning and optimization capabilities. You need to perform a detailed reasoning process (Chain-of-Thought) internally under a given requirement, and then output a correct and efficient solution code. But please note: only use step-by-step analysis in your internal reasoning, and do not expose all the reasoning details in the final answer.

When you receive a question, please:

1. Summarize the requirements or problem goals in concise language first.

2. Perform detailed logical reasoning internally (find the correct algorithm, data structure and potential optimization methods, etc.).

3. Produce a runnable and efficient code as the final answer.

4. Output a small amount of explanatory text only when necessary, and do not display all ideas or reasoning processes directly to the user.
    """
    varient_1_get_code_system:str = """
     As a professional Python algorithm engineer, please solve the algorithms problem and generate a solution code. The final output format should be as follows:
```python
{code}
```
    
    """

    special_1_get_code_system: str = """
         As a professional Python algorithm engineer, please solve the algorithms problem and generate 5 solution code, Please improve the efficiency of the code as much as possible while ensuring the correctness of the code.. The final output format should be as follows:
    ```python1
    {code}
    ```
    ```python2
    {code}
    ```
    ```python3
    {code}
    ```
    ```python4
    {code}
    ```
    ```python5
    {code}
    ```

        """

    algorithim_trans_code_user: str = """
      Selected plan and algorithm: {} 
      original question format: {}
       """
    algorithim_trans_choose_system:str = """As a professional Python programming expert, please select the most efficient and stable code from the provided options, and output it in the following format:
    ```python
    {code}
    ```
    """

    result_checker_system = """
    As a professional algorithm programming master, your task is to determine whether the output results of each testcode case meet the expected output results. Next, please combine the executed code, execution results and testcode cases to make a judgment.(1)judge the ouput is correct,if the output is correct the "Meets the expected output result" should be "True" in the foloow ouuput format,or should be false(2) Output which testcode case has an error and all the original execution results(3)Please distinguish between input and output.(4)sometimes the output may be '',''is not none and use the Json return format:
{"Meets the expected output result":Boolean(True or False),"error results":String(description the specific error),"all execution results":String(description all original results)}
    """
    result_checker_user:str = """
    This is the execution result output:{},
    This is the executed code:{},
    """

    code_false_analysis_system:str = """As a professional Python programming expert, your task is to analyze the reasons why the code produces incorrect results.  You should analyze the execution data flow of the code step by step and explain why these testcode case failed.When you are analyzing, please analyze each element in the code, including whether the encapsulation function used is used correctly, whether there are other alternative methods, and avoid some edge cases that cannot pass this algorithm problem. Keep the code as concise as possible Please re-analyze and find new reasons for the wrong results."""
    code_false_analysis_user:str = """Here is the executed code:{}
Here is the wrong output:{}
Historical modification record: {}
"""

    code_iteration_system:str = """As a professional code programming algorithm expert, your task is to correct the code and ensure that the code is fixed without impacting its time complexity or practical efficiency. Then I will provide you with specific code and test cases. Based on the algorithm requirements:
If the code is correct but the test case is wrong, please output the unmodified code directly.
If the test case is correct but the code is wrong, please modify the code.
Important Notes:
1.	Do not alter the algorithm itself—maintain minimal time complexity.
2.	Do not change the format, such as the function name.
3.	Please output in the specified format.
3.  Ensure there are no syntax errors.
please output in this format:
    ```python
    {code}
    ```
    """
    code_iteration_system2: str = """As a professional Python code programming expert, your task is to analyze the code and improve its correctness, such as (1) Understand the core of the problem: identify the input, output, and the key concepts or data structures involved.
(2) Identify constraints: Consider any constraints and edge cases in the problem to ensure that the algorithm can handle special and extreme inputs
(3) Do not change the algorithm to ensure efficiency.
(4) Do not change the format, such as function names, just keep it in the "original algorithm format"
Please refer to the provided input and output to step by step analyze the execution data flow of the code to ensure the correctness of the code. Please output in this format:
```python
{code}
```
        """

    code_iteration2_system:str = """As a professional Python code programming expert, Your task is to modify the original code implementation according to the modification suggestions.format:
    ```python
    {code}
    ```
    """

    code_iteration2_user:str = """
    original execution code: {}
    modification suggestions: {}
    original algorithm format:{}
    """
    code_iteration_user_2:str = """
    This is the input and output of a reference code, please refer to modify your code: {}
    original execution code: {}
    original algorithm problem format:{}
    """

    code_iteration_user:str = """
    Don't change the algorithm!
    This is the algorithm problem description:{}
    This is the wrong code: {}
    This is the correct case and output: {}
    """

    code_modify_Summarize_system:str = """As a professional Python code programming expert, please summarize your opinions and content for this modification as feedback for the next code modification. The output format is:
{"Historical modification record":""}
    """


    code_format_system:str = """As a professional Python programming expert, you JUST need to remove the example cases in the form of `print()`. For example:
Example 1:  
**INPUT:**  
```python
from xxx import xxx  
def functionname():  
    xxxx  
print(xxxx)  # Example  
```  
**OUTPUT:**  
```python
from xxx import xxx  
def functionname():  
    xxxx  
```  
Example 2:  
**INPUT:**  
```python
def functionname():  
    xxxx  
print(xxxx)  # Example  
```  
**OUTPUT:**  
```python
def functionname():  
    xxxx  
```  
Example 3:  
**INPUT:**  
```python
def functionname():  
    xxxx  
xxxx  # 
```  
**OUTPUT:**  
```python
def functionname():  
    xxxx  
```
"""


    code_format_user:str = """
    This is the generated code:{}
    """
    code_format_check_system = """
    Please help me check whether the following code meets the writing standards of the algorithm question, focusing on the input and output data formats, as well as the entry function names. If not, please output the modified results. If it is compliant, please directly output the original code content. PS: Do'not add any test case by using `print()` or somethingelse.Please output in the following format:
```python
{code}
```
    """
    code_format_check_user = """
    This is the code:{}
        """
    code_check_system:str = """"As a professional algorithm programming expert, you excel at analyzing algorithmic problems and determining whether the corresponding solutions are reasonable. Next, based on the input and output of the reference test cases, please judge whether the generated code is correct. If it is incorrect, output 'No' and explain the reason step by step; if it is correct, output 'Yes'. Please strictly follow the format below for the output:
{"IsCodecorrect":str('Yes' or 'No'),"Optimization_strategy":str}"
    """
    code_check_user:str = """
    This is the generated code:{}
    This is the test case analysis:{}
    """
    package_system:str = """
Now you need to restructure the following information. Specifically, you should integrate the problem description and algorithm description into the original problem content. The output should follow this format:
Example:
Input:
Original problem content:
```python
def rounded_avg(n, m):
    \"\"\"You are given....
     \"\"\"
    return binary_representation
```
Problem description: xxx  
Algorithm description: xxx  

Output:
```python
def rounded_avg(n, m):
    \"\"\"You are given....
    \"\"\"
    return binary_representation
This is the Problem description: xxx
Here is the algorithm you need to reference: xxx
``` """

    package_user:str = """
    Original problem content:{}
    Problem description:{}
    Algorithm description:{}
    """

    algorithim_description_check_system:str = """
    As a professional algorithm engineer, please ensure that the algorithm meets the problem requirements. If the algorithm satisfies the requirements, output "Yes." If it does not, input "No" and provide a detailed reason step by step. Please consider all possible scenarios for the algorithm and outline its logic as thoroughly as possible.
Output format:
```json
{
  "No": "Reason....."
}
{
  "Yes": "Null"
}
```
    """

    algorithim_description_check_user:str = """
    This is the description of the problem: {},
    This is the Algorithm that you need to check :{}
    """

    algorithim_description_adjust_system:str = """
    As an excellent algorithm engineer, you excel at solving various algorithm problems. Based on the suggestions for algorithm optimization, please modify the original algorithm and ensure the lowest time complexity and space complexity of your algorithm .Please output the updated algorithm in the following format,You DON'T NEED TO OUPUT THE Implementation:
    ```Algorithm
Algorithm Description:
Algorithm Optimization Suggestions:
pseudo algorithm:
```
    """

    algorithim_description_adjust_user:str = """
    This is the Algorithm  Modify comments:{}
    This is the Algorithm that you need to modify:{}
    """

    algorithim_description_iterchose_system:str = """
    As a professional algorithm engineer, I will provide you with multiple algorithms. Please select the most efficient algorithm with the lowest time and space complexity from these options.Please output as the following format,do not output the implementation:
        ```Algorithm
Algorithm Description:
Algorithm Optimization Suggestions:
pseudo algorithm:
```
    """

    code_check_withques_system:str = """
    As an excellent algorithm engineer, you are best at solving various algorithm problems. Now please check whether the generated code meets the requirements of the algorithm question. If yes, please output "Yes", if not, please output "No", and describe the modification plan in detail step by step:
{"Yes":"Null"},
{"No":"Suggested Modifications"}
    """

    code_check_withques_user: str = """
    This is the code that you need to analysis:{},
    This is the Algorithm Problem Description:{}
        """

    code_modify_system:str = """As a professional Python algorithm engineer, please modify the code according to the modification suggestions and output it in the required format:
```python
{code}
```
    """

    code_modify_user:str = """
    This is the code that you need to modify:{}
    This is the Suggested Modifications:{}
        """

    code_evaluate_system:str = """
    As a professional algorithm engineer, please evaluate whether the following algorithm meets the problem requirements and is the correct and most efficient code. Consider both time complexity and space complexity. If it is, please output "Yes"; otherwise, output "No" and explain the reason. Please format the output as follows:
```json
{"Yes":"Null"},
{"No":"Reason"}
```
    """

    code_evaluate_user:str = """
    This is the algorithm problem:{}
    This is the code that you need to evaluate:{},
    """

    code_evaluate2_system:str = """
    As a professional Python algorithm engineer, I will provide you with two code.Please analysis the time complexity and space complexity of these codes step by step and the choose the most effciency code  which is fully meeting the algorithm problem’s requirements.Do not output example case like print and make sure all package is imported in the code.
    YOU just need to output the most effective and correct code directly(Final code reuslt) in the following format:
    ```python
{code}
```
    """

    code_evaluate2_user:str = """
    This is the algorithm problem:{}
    This is the code1:{}
    This is the code2:{}
    """

    code_evaluate2_t_system: str = """
    As a professional algorithm engineer, you need to compare the two pieces of code below to determine which one meets the requirements of the algorithm task, while having the lowest time complexity and space complexity. Please analyze step by step, and output the most efficient code directly.Do not output example case like print and make sure all package is imported in the code. Please follow the format below for the output:
    ```python
    {code}
    ```
        """

    code_evaluate2_t_user: str = """
        This is the algorithm problem:{}
        This is the code1:{}
        This is the code2:{}
        """

    code_evaluate3_system: str = """
    As a professional Python algorithm engineer, I will provide you with two code.Please analysis the time complexity and space complexity of these codes step by step and the choose the most effciency code and using the others code to improve the correctness making the code highly accurate, fully meeting the algorithm problem’s requirements.Do not output example case like print and make sure all package is imported in the code.
    YOU just need to output the most effective and correct code directly(Final code reuslt) in the following format:
    ```python
{code}
```
    """

    code_evaluate3_user:str = """
    This is the algorithm problem:{}
    This is the code1:{}
    This is the code2:{}
    """

    case_check_agent_system:str = """
As a professional algorithm programming master, please help me step by step check whether the input and output of this test case meet the requirements of the algorithm question based on the question. If yes, please output "Yes", otherwise output "No"
    """

    case_check_agent_user:str = """
    This is the requirements:{}
    This is the wrong case:{}
    """

    case_summarize_system:str = """As a professional algorithm programming master, you are good at analyzing whether the test cases meet the input and output requirements of the question and summarizing the reasons for the script execution errors. Next, I will give you some test cases and the reasons for their execution errors. Please help me summarize the types of these failed test cases and return them in the following format:
```json
{
"1":{"failed_case": "assert....","failed_Reason":"...."},
"2":{"failed_case": "assert...","failed_Reason":"...."}
}
```
    """

    case_summarize_user: str = """
    This is the algorithm problem:{}
    This is the wrong case:{}
        """

    code_iter_practice_system:str = """
As a professional Python engineer, you are familiar with the time cost of various codes in Python and can effectively modify the code to avoid unnecessary time cost. Please  optimize the following code step by step from the implementation level to make it more efficient and output the results in the form of ```python\n{code}```.
    """
    code_iter_practice_user:str = """
    Here are some optimization suggestions for reference::{}
    This is the code:{}
    """

    fask_code_choice_system:str = """
As a professional Python algorithm engineer, please help me choose the most efficient Python code from the following codes. It is worth mentioning that it is necessary to consider the time complexity and practical level comprehensively:
INPUT:
{"1":"def ...()....",
"2": "def ...()..."
}
OUTPUT:
```text
{key}
EXAMPLE:
INPUT:
{"1":"def ...()....",
"2": "def ...()..."
}
OUTPUT:
```text
1
``` 
    """
    additional_cost_analysis_system:str ="""
    As a professional Python algorithm engineer, please generate a code practice optimization knowledge base based on the following Python code implementation method, and accurately explain which implementations in Python syntax are more efficient without changing the correctness of the original code.
  """
    knowledge_databases_system:str = """
As a professional Python algorithm programming expert, please provide suggestions for improving code efficiency based on the potential inefficiencies mentioned above. For example:
1.	Using xxx instead of xxx can significantly improve code efficiency.
Please provide at least 20 suggestions.
    """
    knowledge_databases_user:str = """
    This is the algorithm:{}
    """

    case_extraction_system:str = """
    """
# Additional_cost_analysis
class caseGen:

    #1.拆分问题，然后提取题目中的测试用例
    #2.根据题目，确定可以输入的测试用例类型（需要细化）、边界数值
    #3.根据题目以及类型分析生成测试用例（具体的值），总共n个 or #4.生成generator
    #5.让LLM直接基于题意，针对输入的测试用例进行分析推理演化拿到正确的执行结果 6. 根据演化的过程转化为对应的代码，作为正确测试用例执行结果生成的代码
    #7.得到输入和输出用例

    pro_description_case:str ="""
As a professional algorithm engineer, please analyze the given algorithmic problem by clearly identifying the data types of the input and the expected output, including expected behavior, edge cases, and the provided reference test cases. You may refer to the following format:
1. Input/Output conditions: Please extract and explain the data types required for input as described in the problem.
2. Expected Behavior: Please describe the process that the algorithm needs to accomplish.
3. Test Cases: Please extract the test cases provided in the problem, including both input and output.
"""

    edge_case_description_system:str = """As a professional algorithm programming expert, you excel in analyzing and constructing complex algorithmic problems. Your next task is to analyze the following algorithmic problem and, based on its description, generate relevant explanations for the test cases. The purpose of this task is JUST to construct input test cases to verify the robustness of the problem solver's code,So you don't need to generate the output case. Therefore, you need to analyze the following aspects:
1. Input test case data types analysis (e.g., str, list, dict, bool, etc.): To ensure that the problem solver considers some edge cases, please identify all possible data types in Syntax structure of Python that the algorithm can accept and provide examples,please analysis step by step.
2. Input test case value types (e.g., odd numbers, even numbers, prime numbers, letters, Chinese characters, etc.): Please specify the types of values that the algorithm can accept and analysis step by step.
"""
    edge_case_description_user: str = """
        This is the algorithmic description:{},
        This is  the ini algorithmic problem:{}
          """

    inputcase_generator_system: str = """
    As a professional algorithm programming expert, you excel at constructing test cases to verify the robustness of code. Next, based on the algorithmic problem, please generate 10 correct and useful test cases as a list according to the following format:
Example:
INOUT:
def funtion(args):
    xxxx
OUTPUT:
["assert (funtion(arguments1) == result1),'Explain what this test case does'",
"assert (funtion(arguments2) == result2),'Explain what this test case does'"]
```python
["assert (function_name(arguments1) == result1),'Explain what this test case does'",
"assert (function_name(arguments2) == result2),'Explain what this test case does'"]
```
"""
    inputcase_generator_user: str = """
    This is  the ini algorithmic problem:{}
      """

    inputcase_generator_system1:str = """
    As a Python tester, your task is to create 10 comprehensive test cases for the function given the definition and docstring. These test cases should encompass Basic and Edge scenarios to ensure the code's robustness and reliability.Please output as an array following the  OUTPUT format.
    """

    inputcase_generator_user1:str = """
    EXAMPLES:
Function:
```python
from typing import List
def find_the_median(arr: List[int]) -> float:
 \"\"\"
 Given an unsorted array of integers `arr`, find the median of the array.
 The median is the middle value in an ordered list of numbers.
 If the length of the array is even, then the median is the average of the two middle numbers.
 \"\"\"
```
Test Cases(OUTPUT Format):
```python
["assert find_the_median([3, 1, 2]) == 2,'basic test cases:Explain what this test case does'",
"assert find_the_median([1, 3, 2, 5]) == 2.5,'basic test cases:Explain what this test case does'",
"assert find_the_median([1]) == 1,'edge test cases:Explain what this test case does'",
"assert find_the_median([-1, -2, -3, 4, 5]) == -1,'edge test cases:Explain what this test case does'",
"assert find_the_median([4, 4, 4]) == 4,'edge test cases:Explain what this test case does'"]
```
END OF EXAMPLES.
    """


    outputcase_analysis_system:str = """As a professional expert in algorithmic logic programming, you excel at analyzing complex algorithmic problems and can deduce the expected output test cases step by step based on the input. Next, please generate the corresponding output cases for these input cases based on the given algorithmic problem.please Output in this format:
    ```inputcase1
    input case:xxx
    analysis step by step:
    output case:xx
    ```
    ```inputcase2
    input case:xxx
    analysis step by step:
    output case:xx
    ```
"""
    outputcase_analysis_user:str = """
    This is the algorithmic problem description:{},
    This is the input test cases:{}
    """

    case_formated_system:str = """
    As a professional text analyst familiar with Python, you can accurately extract text content and integrate it to generate formatted data,Please note that unnecessary carriage return and line feed characters should be identified and removed. Next, please extract the input case and output case in the 'case example' and construct them according to the data transmission method described in the function body in the algorithm question.and output them in the following Json format:
{ "1":{"input_case": "xxx","output_case":"xxx"},
"2":{"input_case": "xxx","output_case":"xxx"}
}
    """

    case_formated_user: str = """
  This is the algorithmic problem:{},
  This is the case example:{}
        """

    case_check_system:str = """As a professional Python algorithm engineer, you are best at analyzing the content of the algorithm question and checking whether the input and output are correct. Next, please check whether the following input and output are correct in combination with the algorithm question. If they are all correct, please output "Right", if not, please output "mistake", and re-output the results and analysis process step by step, and output in the following format:
Right
or
Mistake
```inputcase1
input case:xxx
analysis step by step:
output case:xx
```
```inputcase2
input case:xxx
analysis step by step:
output case:xx
```"""

    designer_agent_system:str = """
    As a Python tester, your task is to create comprehensive test inputs for the function given the deinition and docstring. These test inputs should be Edge scenarios to ensure the code's robustness and reliability.Plese  output {} edge test cases which cover all required parameters type in a single line and start with a `input:`.
    PS: DON't generate too long!!!
    """
    designer_agent_user:str = """
    EXAMPLES:
Function:
```python
from typing import *
def find_the_median(arr: List[int]) -> float:
 \"\"\"
 Given an unsorted array of integers `arr`, find the median of the array.
 The median is the middle value in an ordered list of numbers.
 If the length of the array is even, then the median is the average of the two middle numbers.
 \"\"\"
```
Test Inputs(OUTPUT format):
```text 
input: [1] 
input: [-1, -2, -3, 4, 5] 
input: [4, 4, 4] 
input: [....]
input: [....]
```
END OF EXAMPLES.
Function:
{}
    """

    designer_agent_complexity_system:str = """
As a Python tester, your task is to create highly complex and computationally intensive test inputs for the function based on its definition and docstring. These test inputs should push the function’s limits, covering all required parameter types and edge cases, while maximizing computational load to thoroughly test its efficiency and scalability. Please JUST output {} test cases in a single line starting with input:. Ensure the generated cases are diverse and represent extreme scenarios to effectively stress test the function. """

    calculator_agent_system:str = """
    As a Python programmer, your task is to calculate the test output and write the test case statement corresponding to the test input for the function given the definition and docstring. Write each test case with a single line of assert statement. You have access to a Python interpreter, allowing you to execute any Python code snippets that assist in calculating the test cases. 
    Use the following format: 
    Function: The function definition and docstring 
    Test Input: One test input to the function 
    Thought: You should always think about what to do 
    Code: The Python code you want to execute 
    Observation: The execute result of the Python code ... (this Thought/Code/Observation can repeat N times) Thought: I now know the final answer. 
    Test Case: The test case statement 
    Begin!
    """

    calculator_agent_nopy_system: str = """
        As a Python programmer, your task is to calculate all the test outputs and write the test case statement corresponding to the test input for the function given the definition and docstring. Write One test cases with a single line of assert statement.
        """

    input_constructor_system:str = """
You are tasked to write a Python test case constructor for the given algorithm problem. The constructor should generate as complex as possible test cases tailored to the provided problem.

Requirements:

	1.	Write a Python function named generate_test_cases that can dynamically create 10 diverse test cases for the specified algorithm problem.
	2.	The constructor should:
		Accept the name of the function being tested (e.g., function_name).
		Generate random inputs with varying types and complexities (e.g., integers, floats, nested lists).
		Support additional parameters specific to the algorithm.
		Handle constraints such as input size, value ranges, or specific patterns.
	3.	The output of the constructor function should be a LIST of formatted test cases like(DO NOT USING 'for' to output the case):

['print(function_name(case1))', 'print(function_name(case2))', ...]


	4.	Ensure that the constructor can adapt to any algorithm problem provided.

Input Example:

Algorithm problem description:
“Write a function has_close_elements that checks if any two elements in a list are closer to each other than a given threshold.”
Example Function Signature:

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    pass

Output Example:

The constructor code should look like this:

import random
from typing import List, Callable, Any, Tuple

def generate_test_cases(
    func_name: str,
    num_cases: int = 10,
    list_length_range: Tuple[int, int] = (...),
    value_generators: List[Callable[[], Any]] = [lambda: random.randint(0, 100)],
    additional_params: List[Callable[[], Any]] = []
) -> List[str]:
    test_cases = []
    for _ in range(num_cases):
        main_list = [random.choice(.......)]
        params = [.......]
        test_cases.append(f"print({func_name}({', '.join(params)}))")
    return test_cases

# Example Usage
if __name__ == "__main__":
    cases = generate_test_cases(
        func_name="has_close_elements",
        num_cases=10,
        list_length_range=(....),
        value_generators=[
            lambda: random.randint(....),
            lambda: round(random.uniform(...), ...)
        ],
        additional_params=[lambda: round(random.uniform(...), ....)]
    )
    print(cases)

Expected Output:

[
    "print(has_close_elements(....))",
    "print(has_close_elements(....))",
    ...
]
    """

    input_constructor_user: str = """
    This is the algorithmic problem:{}
    """


    calculator_agent_agent_fewshot_system: str = """
      As a Python programmer, your task is to calculate one test output and write the test case statement corresponding to the test input for the function given the definition and docstring. Then, I will give you some correct test case based on this function, you can refer to it. Write all JUST 20 test cases with a single line of assert statement.
        This is the correct example test case:
        {}
    """

    calculator_agent_nopy_user: str = """
EXAMPLES: 
Function: 
```python 
from typing import List 
def find_the_median(arr: List[int]) -> float: 
    \"\"\" Given an unsorted array of integers `arr`, find the median of the array. The median is the middle value in an ordered list of numbers. If the length of the array is even, then the median is the average of the two middle numbers. 
    \"\"\" 
``` 
Test Input: 
```text 
input: [1, 3, 2, 5] 
...
``` 
Test Case: 
```python 
assert find_the_median([1, 3, 2, 5]) == 2.5 
``` 
END OF EXAMPLES.
FUNCTION:
{}
```
Test Input: 
```text 
{} 
```
```python
assert....
```
        """

    calculator_agent_fewshot_user: str = """
    EXAMPLES: 
Function: 
```python 
from typing import List 
def find_the_median(arr: List[int]) -> float: 
    \"\"\" Given an unsorted array of integers `arr`, find the median of the array. The median is the middle value in an ordered list of numbers. If the length of the array is even, then the median is the average of the two middle numbers. 
    \"\"\" 
``` 
Test Input: 
```text 
input: [1, 3, 2, 5] 
...
``` 
Test Case: 
```python 
assert find_the_median([1, 3, 2, 5]) == 2.5 
assert ...
``` 
END OF EXAMPLES.
FUNCTION:
{}
```
Test Input: 
```text 
{} 
```
```python
assert....
```
    """

    case_extraction_system = """
    As a professional Python code testing expert, you excel at extracting all test cases from problem descriptions and converting them into the required format. Following the example below, please extract all the test cases from algorithm problems in the specified format,Please carefully analyze the problem, extract all the test cases, and convert them into assert statements. If the format of the problem does not match the example below, independently analyze it step by step and follow this format:
    ```python
    assert xxx()==()
    ```

EXAMPLE1:
```python
```:

INPUT:
```python
def parse_music(music_string: str) -> List[int]:
    \"\"\" 
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    \"\"\"
```
OUTPUT:
```python
assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
EXAMPLE2:
INPUT
```python
def tri(n):
    \"\"\"
    Everyone knows the Fibonacci sequence, which has been deeply studied by mathematicians
    in the last couple of centuries. However, what people don't know is the Tribonacci sequence.
    
    The Tribonacci sequence is defined by the recurrence:
    
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8
    
    You are given a non-negative integer number n, and you have to return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    
    Examples:
    tri(3) = [1, 3, 2, 8]
    \"\"\"
```
OUTPUT:
```python
assert tri(3)==[1, 3, 2, 8]
....
```
EOF EXAMPLE

    """

    case_checkwithcode_system:str = """
    As a professional Python algorithm engineer, your expertise lies in analyzing code based on the problem requirements and determining whether the test cases meet those requirements. Next, I will provide you with several pieces of code and test cases, along with their corresponding execution results. Please help me delete the test cases or code where the execution failed.

Therefore, your tasks may include:

	1. If the test case results are judged to be correct, modify the code to ensure it can successfully pass the test cases.
2. If the code results are judged to be correct, simply delete the wrong test case based on the error which is in the reason.
	This is a example：
INPUT
{ '1':
{
'passwd':False,
'reason': "assert(testcase1) error"
'code': "def function():
	xxx
assert(testcase1)
assert(testcase2)
"
}
}

Output example1 (if the code is wrong):
{'1':{code:"def function():
	{code after modified}
assert(testcase1)
assert(testcase2)"}}

Output example2 (if the case is wrong):
{'1':{code:"def function():
	{code after modified}
assert(testcase2)"}}
    """

    case_checkwithcode_user:str = """
    Here is the algorithm problem:{}
Here is the code and test cases you need to modify, as well as the corresponding errors encountered during execution:{}
    """

    case_extraction_in_code_system:str = """
    Please help me extract the test cases from the code and return them in the following format:
```python
assert...
```
    """

    false_reason_check_system:str = """
    As a professional Python code tester, please determine whether the following error is caused by incorrect code or incorrect test cases. If the code is incorrect, output `{"code":"No","case":"Yes"}`. If the test case is incorrect, output `{"code":"Yes","case":"No"}`.

Output in the following format:
```json
{"code":String(Yes or No),"case":String(Yes or No)}
```
    """
    case_delete_system:str = """
    
    
    """