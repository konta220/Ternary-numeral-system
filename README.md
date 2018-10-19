# 1. Ternary-numeral-system
______________________________________________________________________________

[![Turu License](https://img.shields.io/website-turu-license-black-red/http/shields.io.svg?label=license&style=flat-square)](turu-license.md)

English  
Welcome to the Open Source Society. This repository is computer science (CS).
We have written about the ternary-numeral notation.

Japanese  
オープンソース社会へようこそ。このリポジトリはコンピュータサイエンス (CS) です。私たちは、3進数の計算機の世界について書かれています。

______________________________________________________________________________
# 2. 表現

|  Mean     |  Exp  |  Jap  |
| ----      | ----   |  ---  |
|  Binary   |  Bin  |  2進数  |
|  Ternary  |  Ter  |  3進数  |

______________________________________________________________________________
# 3. 進数から３進数への変換

|  2進数 (Bin) |  ３進数 (Ter) |
| ----    | ---- |
|  00     |   0  |
|  01     |  -1  |
|  11     |   0  |
|  10     |   1  |

______________________________________________________________________________
# 4. 3進化２進計算尺

[ここ](https://konta220.github.io/Ternary-numeral-system/index.html) からアクセスし利用できます。

## 4.1. 各ゲート (ABC) の役割
|  記号  |  値  |
| ---- | ---- |
|  A |  0   |
|  B |  1   |
|  C |  -1  |

## 4.2. 計算例


### 4.2.1. ORゲート

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

### 4.2.2. ANDゲート

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
# 5. 今後の方針 (Mission)

1. 文書画像のMarkdown化
    1. JK-FF
    2. 3進化ゲート
    3. 全加算器
2. 3進CPUの作成 (CAD)
    1. ALUの作成
    2. シフタの作成
3. 3進プログラムの作成 (CAD)
    1. 順次実行
    2. 条件分岐
    3. 繰り返し


______________________________________________________________________________
# 6. 回路図作成 - ソフトウェア (CAD)

以下のソフトウェアで無料にて回路図を作成できます。

Quartus Prime Lite Edition (Free)
http://fpgasoftware.intel.com/18.1/?edition=lite

______________________________________________________________________________
# 7. 募集 (Recruitment)

English
- We are looking for opinions and criticisms on the issue of GitHub.
- Who can translate into English and Chinese?
Contact is not required!!

Japanese
- ご意見・ご批判をgithubのissue等で募集中です。
- 英語/中国語に翻訳していただける方を募集しております。連絡は不要です。
