# AtcoderExtractor
---

Batch extraction contest data of Atcoder for a specified group of users.


## How to use

1. Login your Atcoder account, and download the contest json files from `https://atcoder.jp/contests/<contest id>/standings/json/` .
2. Download all the contest json files you need, and save the json files to the son folder `json`.
3. Add the usernames to the `users.csv` file.
4. Run `reporter.py` with the command like `python .\reporter.py`, and wait for it to finish.
5. Then you will get the `result.xlsx`.
