data = {
    "1": {
        "code": "",
        "result": {
            "case_item": "assert()...",
            "pass_result": True,
            "time": "0.12"
        }
    },
    "2": {
        "code": "",
        "result": {
            "case_item": "assert()...",
            "pass_result": True,
            "time": "0.18"
        }
    },
    "3": {
        "code": "",
        "result": {
            "case_item": "assert()...",
            "pass_result": True,
            "time": "0.10"
        }
    }
}

# 对字典按 time 值降序排序
sorted_data = sorted(
    data.items(),
    key=lambda item: float(item[1]["result"]["time"]) if "result" in item[1] and "time" in item[1]["result"] else 0,
    reverse=True
)

# 输出排序后的结果
print(sorted_data)
for key, value in sorted_data:
    print(f"Key: {key}, Time: {value['result']['time']}")