class Solution1:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        res = ''
        n = len(s)
        for i in range(0, n + 1):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
        res = res.replace('#', '')
        print(res)
        return res

    def helper(self, s, l, h):
        while l >= 0 and h < len(s) and s[l] == s[h]:
            l -= 1
            h += 1
        return s[l + 1:h]


# 伪代码编程法解决
class Solution2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 将奇偶数长度的s转换成同一种情况
        s = ''.join(['#', '#'.join(s), '#'])

        # 需要一个容器保存临时最长回文串
        oldstr = ''
        # 遍历字符串s
        # 由于需要index，所以用enumerate
        for i, v in enumerate(s):
            n = len(oldstr)
            # 从遍历经过的当前字符向左右扩展
            # 向左向右扩展都有边界
            # 向左扩展的边界是到最左，范围是0到当前字符的index
            left_range = i
            # 向右扩展的边界是到最右，范围当前字符的index到len(s)
            right_range = len(s) - i - 1
            # 取左右范围中小的为扩展范围
            rng = min(left_range, right_range)
            # 判断当前字符串是否为回文，如果是，继续扩展
            for k in range(rng + 1):

                # 此处优化，不计算比当前短的字符串以节省时间
                if 2 * k + 1 < n:
                    continue
                if self.is_pal(s[i - k:i + k + 1]):
                    newstr = s[i - k: i + k + 1]
                    oldstr = self.cmp_update_lgstr(
                        newstr, oldstr)
                else:
                    # 如果不是回文, break
                    break
                    # 如果不是，和临时最长对比并更新
            # 继续向右
        # 返回临时最长回文串
        oldstr = oldstr.replace('#', '')
        return oldstr

    # 需要一个函数判断当前字串是否为回文
    def is_pal(self, ss):
        return ss == ss[::-1]

    # 需要一个比较长度并更新的函数
    def cmp_update_lgstr(self, old, new):
        old = old if len(old) > len(new) else new
        return old


# s = "cwziydanrqvsdtvnnqgjnbrvvwxwqojeqgxhwxdoktjktulemwpbeqscbbtbfvkxsrjetfdrovcrdwzfmnnihtgxybuairswfewvpuscocqifuwylhssldpjrawqdrbvkykpaggspbfrulcktpbofchzikhzxhpocgvdbwpewpywsgqbczmamprklaoovcfecwchhmsaqkhvuvvzjblmgvqpqtnlipgqsanvovylpmxlmxvymppdykphhaamtxjnnlsqfwjwhyywgurteaummwhvavxbcpgrfffxrowluqmqjaugryxdmwvyokdcfcvcytxpixbvwrdgzctejdoaavgtezexmvxgrkpnayvfarkyoruofqmpnsqdzojxqrjsnfwsbzjmaoigytygukqlrcqaxazvmytgfghdczvzphfdbnxtklaiqqsotavdmhiaermluafheowcobjqmrkmlzyas"
# s = 'abaabb'
s = "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
sol = Solution2()
res = sol.longestPalindrome(s)
print(res)
