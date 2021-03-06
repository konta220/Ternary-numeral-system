Ternary-numeral-system
==============================================================================

[![Turu License](https://img.shields.io/website-turu-license-black-red/http/shields.io.svg?label=license&style=flat-square)](turu-license.md)

English  
Welcome to the Open Source Society. This repository is computer science (CS).
We have written about the ternary-numeral-system.

Chinese  
欢迎来到开源社会。 这个资料库是计算机科学 (CS)。  
我们已经写了关于三元-数字系算器的世界。

Japanese  
オープンソース社会へようこそ。このリポジトリはコンピュータサイエンス (CS) です。  
私たちは、3進数の計算機の世界について書いています。

______________________________________________________________________________
# 1. 表現

|  Mean     |  Exp  |  Japanese  | Chinese |
| ----      | ----   |  ---   |  ---     |
|  Binary   |  Bin   |  2進数  | 二进制数 |
|  Ternary  |  Ter   |  3進数  | 三进制数 |

______________________________________________________________________________
# 2. 2進数から３進数への変換

|  2進数 (Bin) |  ３進数 (Ter) |
| ----    | ---- |
|  00     |   0  |
|  01     |  -1  |
|  11     |   0  |
|  10     |   1  |

______________________________________________________________________________
# 3. 3進化２進計算尺

[ここ](https://konta220.github.io/Ternary-numeral-system/index.html) からアクセスし利用できます。

## 3.1. 各ゲート (ABC) の役割
|  記号  |  値  |
| ---- | ---- |
|  A |  0   |
|  B |  1   |
|  C |  -1  |

## 3.2. 計算例


### 3.2.1. ORゲート

| A + B |   -1 |  0  |  1  |
| ----  | ---- |---- |---- |
|  -1   |  -1  | -1  | 0   |
|   0   |  -1  |  0  | 1   |
|   1   |   0  |  1  | 1   |

計算例
```math
B + C
= (1) + (-1)
= 0
```

### 3.2.2. ANDゲート

| A・B   |   -1 |  0  |  1  |
| ----   | ---- |---- |---- |
|  -1    |  -1  |  0  | -1  |
|   0    |   0  |  0  |  0  |
|   1    |  -1  |  0  |  1  |


計算例
```math
B ・ C 
= (1) ・ (-1) 
= -1
```

______________________________________________________________________________
# 4. コミット方法 (How to commit?)

[コミット方法](how-to/how-to-written.md) を参照

______________________________________________________________________________
# 5. 論理回路 - 環境構築

以下のソフトウェアで無料にて回路図を作成できます。

Quartus Prime Lite Edition (Free)  
http://fpgasoftware.intel.com/18.1/?edition=lite

______________________________________________________________________________
# 6. 今後の方針 (Mission)

1. 文書画像のMarkdown化
    1. How to written?
    2. JK-FF
    3. 3進化ゲート
    4. 全加算器
2. 3進CPUの作成 (CAD)
    1. ALUの作成
    2. シフタの作成
3. 3進プログラムの作成 (CAD)
    1. 順次実行
    2. 条件分岐
    3. 繰り返し

______________________________________________________________________________
# 7. 謝辞 (Special Thanks)

以下のリンクにお世話になったと思う方々について記述してあります。  
[Special-thanks](how-to/Special-thanks.md)

______________________________________________________________________________
# 8. 募集 (Recruitment)

English
- We are looking for opinions and criticisms on the issue of GitHub.
Don't hesitate to write whatever you think.
- Who can translate into English and Chinese?


Chinese
- 我们正在寻找关于GitHub问题的意见和批评。  
不要犹豫，写下你的想法。
- 谁可以翻译成英文和中文？


Japanese
- ご意見・ご批判をGitHubのissue等で募集中です。  
遠慮せずに何でも書いてください。
- 英語/中国語に翻訳していただける方を募集しております。
