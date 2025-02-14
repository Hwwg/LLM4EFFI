class multi_prompt:
    diff_gen:str = """
   Please analyze the following text content step by step and help me extract the text fragments with different semantics or the text fragments lacking such semantics in the candidate text. And return it in the following format:
EXAMPLE
INPUT:{
"0": "This is a book,is written by weiwei,he is from china",
"1": "This is a book,is written by a chinese",
"2": "This is a book,is written by a man,who is a chinese"
}
OUTPUT:
```text
1. the name of the book's author is weiwei
2. The book's author is a man
```
OUTPUT FORMAT:
```text
1.xxxxx
2.xxxx
3.xxxx
```
    """

    same_gen:str = """
    Please analyze the following text content step by step and help me extract the same content in the following candidate texts. And return it in the following format:
EXAMPLE
INPUT:{
"0": "This is a book,is written by weiwei,he is from china",
"1": "This is a book,is written by a chinese",
"2": "This is a book,is written by a man,who is a chinese"
}
OUTPUT:
```text
This is a book and the author is a chinese
```
OUTPUT FORMAT:
```text
{content}
``` 
    """

    check_contents:str = """
    Please help me filter out the text content that does not meet the requirements of the question step by step, and return the filtered results directly
    """

    combine_result:str = """
    Please help me put the following together logically without adding any extra statements
    """



class slow_prompt:
    problem_thinking:str = """
Please step by step split the task description into multiple steps and restate the disprompt content as a new complete and logical disprompt. It is important to note that the steps you split need to have complete context.
EXAMPLE:
INPUT:
please using A to output C
```step1
using A output B
```
```step2
Using B output C
```


Please return in the following format:
```step1
{task description}
```
```step2
{task description}
```
```step3
{task description}
```
.....
    """

    algorithms_template:str = """
    As a professional algorithm engineer,please help me {}
    """

    algorithms_template_user:str = """
    This is the task description:{}
    """

    algorithms_format_template:str = """
    Please convert the following content into this format output:
        PS: DO NOT provide implementation example!
```algorithm1
algorithm key description:this algorithm using xxx,the key is to make sure xxx
 pseudo algorithm: 
```
```algorithm2
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
 pseudo algorithm: 
```
```algorithm3
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
 pseudo algorithm: 
```
```algorithm4
{algorithm key description:this algorithm using xxx,the key is to make sure xxx}
 pseudo algorithm: 
```
```algorithm5
algorithm key description:this algorithm using xxx,the key is to make sure xxx
 pseudo algorithm: 
```
    """

    evaluate_expert:str = """
    As a professional Python algorithm competition judge,Please analyze whether the following code meets the requirements of the question and whether it misinterprets the meaning of the question. If so, please output the problems in the code.
If the code perfectly meets the requirements of the question and is efficient, please explain its advantages in detail.
The output of the above content is to guide the writing of better code.
    """

    evaluate_expert_user:str = """
    This is the algorith problem:{}
    This is the candidate codes:{}
    """

    final_expert:str = """
As a professional Python algorithm judge, you will receive three explanations about the code corresponding to this algorithm question: {}, which contains some disadvantages and advantages. Next, based on the explanation of the code, please analyze step by step what algorithm and implementation method should be used for this algorithm question to obtain efficient and correct code.    """

    final_expert_user:str = """
    This is the all comments:{}
    """

    rethinking_system:str = """
    As a professional algorithm programming master, please step by step reflect again whether the code you just generated based on the algorithm question is correct: {}, please avoid the problems mentioned before.
    """

    rethinking_user:str = """
    This is the code:{}
    """

    summaries_code_system:str = """
    As a professional Python algorithm programming master, next, I need you to integrate all the code review records based on this problem:{}\n. Please describe these records logically, first describe the algorithms used, then describe the time complexity of each algorithm, then describe the optimization and advantages of each code in practice, and then describe the content of each code that does not meet the requirements of the question. This report is to guide students to better write efficient and correct code. You only need to output a text description report without outputting sample code
    """
    summaries_code_user:str = """
    This is all code comment:{}
    """

    candi_code:str = """
    As a professional Python algorithm programming master, please give the best code based on this algorithm question and the contestants' answers, taking into account both correctness and efficiency.
    """
    candi_code_user:str = """
    This is the algorithm problem:{}
    This is the all comments:{}
    """

