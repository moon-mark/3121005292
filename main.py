import jieba
import sys

# 定义一个函数用于计算两个文本的相似度
def calculate_similarity(orig_path, copy_path):
  # 读取原文本内容
  with open(orig_path, 'r', encoding='utf-8') as f:orig_text = f.read()
  # 读取副本文本内容
  with open(copy_path, 'r', encoding='utf-8') as f:copy_text = f.read()

  # 使用jieba分词工具对原文本和副本文本进行分词，并转换为set用于去重
  orig_words = set(jieba.cut(orig_text))
  copy_words = set(jieba.cut(copy_text))

  # 计算原文本和副本文本的公共单词（即两者都出现的单词）
  common_words = orig_words & copy_words

  # 计算相似度，即公共单词占原文本单词的比例
  return len(common_words) / len(orig_words)

# 主函数
def main():
  # 从命令行参数获取原文本、副本文本和输出文件的路径
  orig_path = sys.argv[1]
  copy_path = sys.argv[2]
  output_path = sys.argv[3]

  # 计算原文本和副本文本的相似度
  similarity = calculate_similarity(orig_path, copy_path)

  # 将相似度写入到输出文件中，保留两位小数
  with open(output_path, 'w', encoding='utf-8') as f:f.write('{:.2f}'.format(similarity))

# 如果此脚本被作为主程序运行，则调用主函数
if __name__ == "__main__":
  main()
