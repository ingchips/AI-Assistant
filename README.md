# INGCHIPS AI-Assistant

# 安装

安装前请确认运行环境符合要求：

1. Windows 10 及以上的 x64 版本；
2. 最少 8GB 内存，建议 16GB 以上

**声明**: 语言模型通过学习大量的文本来生成内容，无法理解、表达观点，也无法进行价值判断，
它所输出的任何内容都不代表我们或者模型开发者的观点和立场。用户在使用模型生成的内容时，应自行负责对其进行评估和验证。
请充分了解此信息，然后下载、安装本程序。

将本仓库克隆到本地。

## 运行

运行 _app/run.exe_。

初次运行时，程序会自动下载所需要的几个大语言模型及知识库。总大小约 13GB，请等待下载完成。
本助手使用了 [Streamlit](https://streamlit.io/)，初次运行时，会要求填写 E-mail 地址，直接回车即可。

在启动页面可根据运行环境选择不同的模型设置。

答案后面附带了对应的参考资料，方便开发者进一步了解：

可用中文或英文提问。对于英文资料，也会用中文回答。答案倾向于使用 _Markdown_ 排版。

## 致谢

本程序基于下列公司（组织）提供的开源 LLM 构建：

* 网易有道：BCE-Embedding, BCE-Reranker
* 北京智源：BGE-M3, BGE-Reranker-M3
* OpenBMB：MiniCPM
* 阿里云：通义千问 MoE
* Google：Gemma

## 局限性

* 只支持单人使用，不可作为支持多人对话的服务器；
* 不支持 GPU 加速；
* 对于某些问题，可能无法检索到正确的资料；
* 大模型存在幻觉问题。
