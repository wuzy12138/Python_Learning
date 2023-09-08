import argparse

# description参数可以用于插入描述脚本用途的信息，可以为空
parser = argparse.ArgumentParser(description="your script description")        
# 添加--verbose标签，标签别名可以为-v，这里action的意思是当读取的参数中出现--verbose/-v的时候
# 参数字典的verbose建对应的值为True，而help参数用于描述--verbose参数的用途或意义。
# 将变量以标签-值的字典形式存入args字典。
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')   
parser.add_argument("--mike", "-m", required=True, type=int)
# parser.add_argument("filename")
parser.add_argument('file', type=argparse.FileType('r'))                                                                                    
args = parser.parse_args()                                                         
if args.verbose:
    print("Verbose mode on!")
else:
    print("Verbose mode off!")

if args.mike:
    print("input value is", args.mike)

for line in args.file:
    print(line.strip())

