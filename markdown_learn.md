 * [Markdown 语法](#markdown-语法)
      * [1.标题（#和标题之间留一个空格）](#1标题和标题之间留一个空格)
      * [2.段落 （使用空白行对文本进行分隔）](#2段落-使用空白行对文本进行分隔)
      * [3.换行 (在末尾添加两个空格或HTMLd的br标签，即可换行)](#3换行-在末尾添加两个空格或htmld的br标签即可换行)
      * [4.强调语法](#4强调语法)
      * [5.引用语法](#5引用语法)
      * [6.有序和无序列表](#6有序和无序列表)
         * [有序列表(数字加英文的点，即可形成有序列表)](#有序列表数字加英文的点即可形成有序列表)
         * [无序列表（在列表项前添加 或-或*；缩进两个空格，即可形成嵌套）](#无序列表在列表项前添加或-或缩进两个空格即可形成嵌套)
      * [7.代码语法](#7代码语法)
      * [8.分隔线语法](#8分隔线语法)
      * [9.超链接语法](#9超链接语法)
      * [10.图片语法](#10图片语法)
      * [11.表格语法](#11表格语法)
      * [12.目录语法](#12目录语法)
# Markdown 语法  
## 1.标题（#和标题之间留一个空格）  
 一级标题  一个#       
 二级标题  二个#       
 三级标题  三个#  
 四级标题  四个#  
 五级标题  五个#  
 六级标题  六个#  

## 2.段落 （使用空白行对文本进行分隔）
I really like using   
Markdown.

I think I'll use it to   
format all of my documents   
rom now on.  

## 3.换行 (在末尾添加两个空格或HTMLd的br标签，即可换行)
This is the first line.  
And this is the second line.<br>

## 4.强调语法
    **I just love bold text.**  粗体，在单词或语句前后各添加两个星号或下划线<br>      	
    *I just love bold text.*  斜体，在单词或语句前后各添加一个星号或下划线<br>	
    ***I just love bold text.***  斜体加粗体，在单词或语句前后各添加三个星号或下划线<br>  

## 5.引用语法
    1.单个段落的块引用（在段落前添加 > ） 
    
    > Dorothy followed her through many of the beautiful rooms in her castle.  
     
    2.多个段落的块引用（在段落前添加 > ）
    
    > Dorothy followed her through many of the beautiful rooms in her castle.
    >
    > The Witch bade her clean the pots and kettles and sweep the floor.
       
    3.嵌套块引用(在嵌套的段落前添加>>)  
    
    > Dorothy followed her through many of the beautiful rooms in her castle.
    >
    >> The Witch bade her clean the pots and kettles and sweep the floor.

## 6.有序和无序列表
### 有序列表(数字加英文的点，即可形成有序列表)
    1. First item
    2. Second item
    3. Third item
    4. Fourth item  

### 无序列表（在列表项前添加+或-或*；缩进两个空格，即可形成嵌套）
    - First item  
    - Second item
    - Third item
        - Indented item
        - Indented item
    - Fourth item  

> 注：在无序列表中嵌套代码块，需要缩进8个空格或两个制表符

## 7.代码语法
1.单词或短语表示为代码，可以使用反引号   
2.转义反引号，单词或短语有反引号，使用双反引号  
3.显示代码块，需要缩进4个空格或一个制表符  

## 8.分隔线语法
在单独一行使用三个或多个星号（***）或破折号（---）或下划线（___）,同一行内不能有其他内容   

## 9.超链接语法
    `[超链接显示名](超链接地址 "超链接title")`  

## 10.图片语法
    `![图片名字](图片地址 "图片title")`

## 11.表格语法
    1. 行首和行尾使用|，同行之间分割不同的行使用|
    2. 同一张表格，各行的列数要相同
    3. 第一行是表头
    4. 第二行是将表头与普通单元格分隔，每一列要填写大于等于三个破折号-
    5. 左对齐:---,居中:---:,右对齐---:

| 次数  | 时间(min)  |
|:---:|:---:|
| 1  |  20 |

## 12.目录语法
    * [标题1](#标题1)