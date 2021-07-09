```
  _                      _                           _
 | |                    (_)                         (_)
 | |__   ___  __ _  __ _ _ _ __     __ _  __ _  __ _ _ _ __
 | '_ \ / _ \/ _` |/ _` | | '_ \   / _` |/ _` |/ _` | | '_ \ 
 | |_) |  __/ (_| | (_| | | | | | | (_| | (_| | (_| | | | | |
 |_.__/ \___|\__, |\__,_|_|_| |_|  \__,_|\__, |\__,_|_|_| |_|
              __/ |                       __/ |
             |___/                       |___/
```

begain again is a Mid-year work summary.

## Tool Kit Show
* [  ] Git: 使用git管理项目,代码存放在企业版的Github, 目前主流的两种Flow管理流程
    - Git Flow: **目前项目使用**
        ![GitFlow](./misc/git/git-flow.png)
        - master: 主仓库分支, 阶段性的特性新增需要创建Tag版本记录
        - hotfix: 快速修复分支, 修复BUG使用, 测试完毕必须合并Master/Develop
        - release: 目前没有完全遵循此方式, 对当前的我们是没有release的概念,后期接入CI/CD,每次完成新特性会合并Master分支进入自动发布流程
        - develop: 开发分支, 项目研发阶段的Base分支, 从master分支创建, 所有的开发人员将会再此分支进行新特性的开发和Bug修复
        - features: 各种项目新功能的研发都将从develop创建,当此分支准备好发布测试将会rebase到develop分支
        - 合并分支创建新的PR(Pull Request)的形式合并, 必须由同事Review和approved之后才能合并Master分支

    - Github Flow
        ![GitHub Flow](./misc/git/Github-Flow.png)
        - Create a branch: 任何时刻都可以创建不同特性目的的分支，你完全掌控当前的分支，只有你准备合并分支的时候需要被你的同事Review并且approved才能合并
        - 分支的概念是Git工具的核心，只需遵循一条规则，Master/Main分支是一个任何时刻的可用稳定分支,由于其他分支都是从Master分支创建
    - ⚠️  注意事项:
        - 常见问题是线上的Hotfix分支需要及时合并到Master和Develop分支, 不然下次Develop合并Master分支的时候会将之前修复的问题覆盖，导致Bug修复重现
* [  ] Dapr:
    - [Install the Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/)
    - [Initialize Dapr in your local environment](https://docs.dapr.io/getting-started/install-dapr-selfhost/) **注意开发代理**
    - [安装过程记录](./docs/tools/dapr/README.md)
   

### More information
* Git
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Pro Git](https://git-scm.com/book/en/v2)

* FastAPI
- [Building a Data API with FastAPI and SQLAlchemy](https://towardsdatascience.com/fastapi-cloud-database-loading-with-python-1f531f1d438a)

* Python Environment
- [An effective Python Environment: Making Yourself at Home](https://realpython.com/effective-python-environment/)
- [Setting Up Python: pyenv, pyenv-virtualenv, poetry](https://duncanleung.com/set-up-python-pyenv-virtualenv-poetry/)