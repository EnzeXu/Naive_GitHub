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
<img width="1035" alt="Screenshot 2023-05-01 at 10 49 47 AM" src="https://user-images.githubusercontent.com/90367338/235484279-a58af348-de8c-45f5-910a-8a1b40eee3c9.png">

---

## 2. Initialization

This process only needs to be done once.

### 2.1 git init

This will create the `.git` folder automatically, which will later save all necessary local information about your repository. 

Hint: To move or remove your local repository info, you can just `rm -rf .git`.

```shell
% git init
```
<img width="609" alt="Screenshot 2023-05-01 at 10 50 08 AM" src="https://user-images.githubusercontent.com/90367338/235484331-d2d7bc1a-fcee-4715-bb65-278ccabcfaaa.png">

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
<img width="401" alt="Screenshot 2023-05-01 at 10 50 45 AM" src="https://user-images.githubusercontent.com/90367338/235484389-e397626d-6ea9-4a24-bad8-9c0c22272c3d.png">
<img width="695" alt="Screenshot 2023-05-01 at 10 52 01 AM" src="https://user-images.githubusercontent.com/90367338/235484417-1ba6fc87-a6a4-4d4e-ba3b-5791b73de04c.png">
<img width="441" alt="Screenshot 2023-05-01 at 10 53 07 AM" src="https://user-images.githubusercontent.com/90367338/235484437-7a3d2c8a-73aa-44f8-8b95-f88fe9136b2b.png">
<img width="955" alt="Screenshot 2023-05-01 at 10 53 26 AM" src="https://user-images.githubusercontent.com/90367338/235484466-ae15ab0a-8f2a-4528-aba6-52d205e7fdc2.png">

After I edit the `.gitignore` file in `figure/`, the color of file `map.png` changes in the left side bar. 

<img width="871" alt="Screenshot 2023-05-01 at 10 53 58 AM" src="https://user-images.githubusercontent.com/90367338/235484539-09c5bf9b-eb1c-456f-a7a8-cab6971509ec.png">

In this example I exclude `map.png!` but track `cat.png` in my repo.

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
<img width="418" alt="Screenshot 2023-05-01 at 10 56 46 AM" src="https://user-images.githubusercontent.com/90367338/235484569-5564f1de-4e12-4c0d-bd57-3fabcf641f9f.png">

### 2.5 create your repository online
<img width="969" alt="Screenshot 2023-05-01 at 10 54 46 AM" src="https://user-images.githubusercontent.com/90367338/235484617-15948f78-47b4-4c57-9dc7-1d81c95eecc6.png">

Click `New`.
<img width="1008" alt="Screenshot 2023-05-01 at 10 55 18 AM" src="https://user-images.githubusercontent.com/90367338/235484640-c078fc88-a267-4932-a1c3-183f52311c09.png">



Choose a proper repo name. It can be different from your current folder name, but they are recommended to be the same.
<img width="1419" alt="Screenshot 2023-05-01 at 10 55 33 AM" src="https://user-images.githubusercontent.com/90367338/235484677-76c742f1-ac0e-450b-91c5-5751cad3a35a.png">


In the instruction page, copy the line `git remote add origin ...` and you will use it later.

### 2.6 git remote add

Paste what you have copied to your terminal. This help to build the connection from your local repo to your online repo.

```shell
% git remote add origin https://github.com/USERNAME/REPONAME.git
```
<img width="695" alt="Screenshot 2023-05-01 at 12 09 19 PM" src="https://user-images.githubusercontent.com/90367338/235484806-14dcf10c-fa3d-4b3d-8938-5e69ff6039b1.png">

### 2.7 git push -u origin main

This is a one-time step that push your local repo to online as initialization. Later you need only use simplified `git push` to do any further push operations.

```shell
% git push -u origin main
```
<img width="484" alt="Screenshot 2023-05-01 at 10 57 28 AM" src="https://user-images.githubusercontent.com/90367338/235484833-e06b52fb-0e8e-46e4-bf39-6e2d51f4d381.png">
<img width="450" alt="Screenshot 2023-05-01 at 10 57 45 AM" src="https://user-images.githubusercontent.com/90367338/235484871-cf48f532-7839-422f-bd61-3e116063f681.png">
<img width="1298" alt="Screenshot 2023-05-01 at 10 58 41 AM" src="https://user-images.githubusercontent.com/90367338/235484898-18262a25-d6dc-4e20-8242-3ad180ca459a.png">

---

## 3. Normal Update

Any time after you have edited your repo and corresponding `.gitignore` files.

```shell
% git add .
% git commit -m "updated xxx"
% git push
```
<img width="421" alt="Screenshot 2023-05-01 at 10 58 51 AM" src="https://user-images.githubusercontent.com/90367338/235484973-048e5334-d4af-4961-96c1-a9006cf58e0f.png">
<img width="1012" alt="Screenshot 2023-05-01 at 11 10 25 AM" src="https://user-images.githubusercontent.com/90367338/235484983-f603227d-c45f-4872-a0f7-e904ee20d09e.png">
<img width="534" alt="Screenshot 2023-05-01 at 11 11 04 AM" src="https://user-images.githubusercontent.com/90367338/235485007-8d44ad76-3818-4dfb-a33f-df866dc4cfe5.png">

In this example I write the README.md file and push it.

---

## 4. Others

### 4.1 Color of files in PyCharm:

1. Red files refer to untracked but not excluded by `.gitignore` files;
2. Yellow files refer to excluded files;
3. Blue files refer to tracked files that have been changed;
4. White files refer to tracked files that up to date;

### 4.2 Tips

1. You cannot upload a single file exceeding 100 MB. Consider to exclude it using `.gitignore`.
2. Every time before you do the `push` operation, it is very recommended to use a `git status` command to check the status of your repo.

3. Go ahead and be careful!

***

[//]: # ( TODO list: requirements.txt and LICENSE)