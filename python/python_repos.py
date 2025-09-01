import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
response_dict = r.json()
#查看有多少python仓库
print("Total repositories:", response_dict['total_count'])
#items是列表包含字典即python仓库信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
repo_dict=repo_dicts[0]
print("Keys():",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
