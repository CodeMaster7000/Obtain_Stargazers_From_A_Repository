from github import Github
g_cred = Github("<Insert Your Token Here>")
f_repo = input("Enter repository name to see its stars (User/Repository): ")
repo = g_cred.get_repo(f_repo)
print(repo.stargazers_count)
