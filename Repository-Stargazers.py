from github import Github
g_credential = Github("<Insert Your Token Here>")
f_repository = input("Enter repository name to see its stars (User/Repository): ")
repo = g_credential.get_repo(f_repository)
print(repo.stargazers_count)
