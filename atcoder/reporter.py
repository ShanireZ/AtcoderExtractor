import os
import json
import pandas as pd
from pathlib import Path

# 读取用户列表
users_df = pd.read_csv("users.csv", header=None)
users = users_df[0].tolist()  # 假设username在第一列（A列）

# 初始化结果列表
results = []

# 处理json目录下的所有文件
json_dir = Path("json")
for json_file in json_dir.glob("*.json"):
    # 解析比赛数据
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 提取比赛名称（文件名前缀）
    contest_name = json_file.stem

    # 遍历比赛中的用户数据
    for entry in data.get("StandingsData", []):
        username = entry.get("UserScreenName", "")
        raw_score = entry.get("TotalResult", {}).get("Score") // 100

        if username in users and raw_score != 0:
            # 提取需要统计的字段
            record = {
                "username": username,
                "contest_name": contest_name,
                "Rank": entry.get("Rank"),
                "Rating": entry.get("Rating"),
                "Score": entry.get("TotalResult", {}).get("Score") // 100,
                "Elapsed": entry.get("TotalResult", {}).get("Elapsed") // 1000000000,
                "Accepted": entry.get("TotalResult", {}).get("Accepted"),
                "Penalty": entry.get("TotalResult", {}).get("Penalty"),
            }
            results.append(record)

# 转换为DataFrame并保存
df = pd.DataFrame(results)
df.to_excel(
    "result.xlsx",
    index=False,
    columns=[
        "username",
        "contest_name",
        "Rank",
        "Rating",
        "Score",
        "Elapsed",
        "Accepted",
        "Penalty",
    ],
)
