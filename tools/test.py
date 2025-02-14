
data_prompt = """
def count_up_to(n):\n    \"\"\"Implement a function that takes an non-negative integer and returns an array of the first n\n    integers that are prime numbers and less than n.\n    for example:\n    count_up_to(5) => [2,3]\n    count_up_to(11) => [2,3,5,7]\n    count_up_to(0) => []\n    count_up_to(20) => [2,3,5,7,11,13,17,19]\n    count_up_to(1) => []\n    count_up_to(18) => [2,3,5,7,11,13,17]\n    \"\"\"\n```text\n1. The entry point function name is `count_up_to`.\n2. The function takes a single input parameter `n`, which is a non-negative integer.\n3. The function returns a list (array) of integers containing all prime numbers less than `n`.\n4. If `n` is less than or equal to 1, the function returns an empty list.\n5. Edge cases include `n = 0`, `n = 1`, `n = 2`, and `n` being a prime number itself.\n6. The input parameter `n` is expected to be a non-negative integer (`int` type).\n7. The function should handle edge cases appropriately, such as when `n` is 0, 1, or a prime number itself.\n8. The function should efficiently determine prime numbers, especially for larger values of `n`.\n9. The output should be a list of integers in ascending order, containing all prime numbers less than `n`.\n10. The function should not include `n` in the output list, even if `n` is a prime number.\n11. Example behaviors include `count_up_to(5)` returning `[2, 3]`, `count_up_to(11)` returning `[2, 3, 5, 7]`, and `count_up_to(0)` returning `[]`.\n```\n{algorithm key description:this algorithm using the Sieve of Eratosthenes, the key is to efficiently mark non-prime numbers in a boolean array and collect primes less than n}\n{ pseudo algorithm:\n  function count_up_to(n):\n    if n <= 1:\n      return empty list\n    create a boolean array is_prime of size n, initialized to True\n    set is_prime[0] and is_prime[1] to False\n    for i from 2 to sqrt(n):\n      if is_prime[i] is True:\n        for j from i*i to n with step i:\n          set is_prime[j] to False\n    collect all indices i where is_prime[i] is True and i < n\n    return the collected list\n}\n
"""

from prompt.prompt import CodegenPrompt3, CodegenPrompt1
from gpt.gpt_reply import GPTReply

Gptreply = GPTReply("deepseek-coder")
data = additional_cost_knowledge = Gptreply.getreply(CodegenPrompt3.knowledge_databases_system,
                                                                          str(data_prompt), "")
print(data)