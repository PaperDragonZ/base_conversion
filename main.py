# Base conversion
# written by Zhao_Zirui

#                             _ooOoo_
#                            o8888888o
#                            88" . "88
#                            (| -_- |)
#                            O\  =  /O
#                         ____/`---'\____
#                       .'  \\|     |//  `.
#                      /  \\|||  :  |||//  \
#                     /  _||||| -:- |||||-  \
#                     |   | \\\  -  /// |   |
#                     | \_|  ''\---/''  |   |
#                     \  .-\__  `-`  ___/-. /
#                   ___`. .'  /--.--\  `. . __
#                ."" '<  `.___\_<|>_/___.'  >'"".
#               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#               \  \ `-.   \_ __\ /__ _/   .-` /  /
#          ======`-.____`-.___\_____/___.-`____.-'======
#                             `=---='
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                     佛祖保佑        永无BUG

# dec-十进位
# bin-二进制
# hex-十六进制

class detection ():    # 比如1111就没办法检测是那种数了 /(ㄒoㄒ)/~~
    def is_de_n(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    def is_bin_n(s):
        for char in s:
            if char not in ('0', '1'):
                return False
        return True

class convert ():
    def dec_to_bin (n):
        if n == 0:
            return "0"
        elif n < 0:
            return "-" + convert.dec_to_bin(-n)
        l = ""
        while n > 0:
            l = str(n % 2) + l
            n = n // 2
        return l

    def bin_to_dec (n):
        dec_n = 0
        for i in n:
            dec_n = dec_n * 2 + int(i)
        return int(dec_n)

if __name__ == "__main__":
    print("1.十进制转二进制(暂时只支持整数)")
    print("2.二进制转十进制")
    while True:
        z = int(input("请输入模式序号\n"))
        if z == 1:
            while True:
                i = int(input("请输入十进制数\n"))
                if detection.is_de_n(i) == True:
                    print(f"十进制数 {i} 转换为二进制是 {convert.dec_to_bin(i)}")
                    break
                else:
                    print("请输入十进制数！！！")
        elif z == 2:
            while True:
                i = str(input("请输入二进制数\n"))
                if detection.is_bin_n(i) == True:
                    print(f"二进制数 {i} 转换为十进制是 {convert.bin_to_dec(i)}")
                    break
                else:
                    print("请输入二进制数！！！")
        else:
            print("你确定有这个数字吗？\n")
        break
    input("按任意键退出")