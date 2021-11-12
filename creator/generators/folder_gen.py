import os

news = "assistant director handed Alec Baldwin a prop firearm and yelled before the actor fired and killed cinematographer Halyna Hutchins and injured director Joel Souza, according to a court document.The cold gun remark was meant to indicate that the weapon did not have live rounds, according to affidavit for a search warrant for the movie set filed by the Santa Fe County Sheriff's Office and obtained by CNN affiliate KOAT.According to the affidavit, Baldwin was handed one of three prop guns by assistant director David Halls that were set up in a cart by an armorer.Halls did not know there were live rounds in the gun, the affidavit said."

folder_names = list(set(news.split(" ")))+['Bonk']

parent_dir = "../TrashFolder"

for directory in folder_names:
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    f = open(path+"/README.md", "x")
    f = open(path+"/apology", "x")