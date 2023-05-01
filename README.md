# Naive GitHub

***

# Catalog

* [1. Preparation](#1-preparation)
* [2. Initialization](#2-initialization)
  * [2.1 git init](#21-git-init)
  * [2.2 create .gitignore](#22-create-gitignore)
  * [2.3 git add .](#23-git-add-)
  * [2.4 git branch -m main](#24-git-branch--m-main)
  * [2.5 create your repository online](#25-create-your-repository-online)
  * [2.6 git remote add origin](#26-git-remote-add)
  * [2.7 git push -u origin main](#27-git-push--u-origin-main)
* [3 Normal Update](#3-normal-update)
* [4 Normal Update](#4-others)
  * [4.1 color of files in PyCharm](#41-color-of-files-in-pycharm-)
  * [4.2 tips](#42-tips)

***

## 1. Preparation

1. Install Git (https://git-scm.com/) and register online
2. Install PyCharm (https://www.jetbrains.com/pycharm/)
3. Create a folder and `cd` into it

---

## 2. Initialization

This process only needs to be done once.

### 2.1 git init

This will create the `.git` folder automatically, which will later save all necessary local information about your repository. 

Hint: To move or remove your local repository info, you can just `rm -rf .git`.

```shell
% git init
```

### 2.2 create .gitignore

`.gitignore` (you CANNOT change any characters in its name) files are very important files that can be used to control whether a file need to be kept in your repo or not.

In `.gitignore`:

1. By default, all files in your repo are considered to be included (tracked) by GitHub.
2. `xxx.yyy` means you want to exclude file xxx.yyy into your repo.
3. `!xxx.yyy` means you want to include file xxx.yyy into your repo.
4. The later lines in this file will overwrite the former lines if they have conflicts.
5. You can use `*` here to represent all matchable files like `*`, `test_*`, `saves/*`, etc.
6. It is recommended that in each folder there is a `.gitignore` file.
7. Usually we list some `xxx.yyy` lines first and then list some `!xxx.yyy` to make some changes.

An example for your highest-level `.gitignore` (directly in your repo folder):

```gitignore
.DS_Store
.idea/*
__pycache__/*
venv/*
```

Where `.DS_Store` is for macOS, `.idea/*` and `__pycache__/*` for PyCharm default compilation files and `venv/*` for your virtual environment.

In this example I exclude `map.png` but track `cat.png` in my repo.

### 2.3 git add .

This will add all your changes in this repo, considering all `.gitignore` files.

Hint: To add specified files, use `git add xxx.yyy` instead.

```shell
% git add .
```

### 2.4 git branch -M main

Update your default branch name from "master" to "main". Although this is not a mandatory step, it is recommended as a good habit.

Hint: You may use `git branch -a` at any time to see all branches and the current branch you are on.

```shell
% git branch -M main
```

### 2.5 create your repository online

Click `New`.


Choose a proper repo name. It can be different from your current folder name, but they are recommended to be the same.


In the instruction page, copy the line `git remote add origin ...` and you will use it later.

### 2.6 git remote add

Paste what you have copied to your terminal. This help to build the connection from your local repo to your online repo.

```shell
% git remote add origin https://github.com/USERNAME/REPONAME.git
```

### 2.7 git push -u origin main

This is a one-time step that push your local repo to online as initialization. Later you need only use simplified `git push` to do any further push operations.

```shell
% git push -u origin main
```

---

## 3. Normal Update

Any time after you have edited your repo and corresponding `.gitignore` files.

```shell
% git add .
% git commit -m "updated xxx"
% git push
```

---

## 4. Others

### 4.1 Color of files in PyCharm:

1. Red files refer to untracked but not excluded by `.gitignore` files;
2. Yellow files refer to excluded files;
3. Blue files refer to tracked files that have been changed;
4. White files refer to tracked files that up to date;

### 4.2 Tips

1. You cannot upload a single file exceeding 100 MB. Consider to exclude it using `.gitignore`.
2. TODO list: requirements.txt and LICENSE

***