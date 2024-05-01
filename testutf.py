import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

file_path = 'F:\研\读研事务\课程\人工智能\AI-V1\RD.txt'
encoding = detect_file_encoding(file_path)
print(f'The detected encoding of file is: {encoding}')
