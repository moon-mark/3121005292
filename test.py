import unittest
import os

from main import calculate_similarity

class TestCalculateSimilarity(unittest.TestCase):
  #设置原始文件路径，及其对应的测试文件路径
  def setUp(self):
    self.orig_path = 'orig.txt'
    self.copy_paths = [
      'orig_0.8_add.txt',
      'orig_0.8_del.txt',
      'orig_0.8_dis_1.txt',
      'orig_0.8_dis_10.txt',
      'orig_0.8_dis_15.txt'
    ]

  def test_calculate_similarity(self):
    for copy_path in self.copy_paths:
      with self.subTest(copy_path=copy_path):
        similarity = calculate_similarity(self.orig_path, copy_path)
        print(f" {self.orig_path}对于 {copy_path}相似度为 {similarity:.2f}")
        # 输出保留两位小数的相似度

if __name__ == '__main__':
  unittest.main()
