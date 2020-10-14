# tb8xmlCN
解决TheBrain 8 中导出为Brain XML格式的文件中文字符显示问题。

TheBrain 11 无法直接打开 TheBrain 8 创建的脑图。可在 TheBrain 8 中导出为Brain XML格式的文件。但对于节点含有中文字符的脑图，导出后中文字符全部变成十进制的Unicode码，TheBrain 11导入后，依然是Unicode码，而无法显示成中文。

`tb8xmlCN` 将导出后的中的Unicode码转换成中文字符，再导入 TheBrian11，可以解决上述问题。
