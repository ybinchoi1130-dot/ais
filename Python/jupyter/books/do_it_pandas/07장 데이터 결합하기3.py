



from pathlib import Path
#%%
#현재 폴더에 있는 모든 파일 목록 출력
current_path = Path(".")
for filename in current_path.glob("*.*"): # 모든 파일
    print(filename)




#%%
# 현재 폴더에서 확장자(py)인 모든 파일을 탐색
python_code_files = (
    Path(".")
    .glob("*.py")
)
# 파일목록을 리스트로 변환하여
# 내림차순으로 정렬하여 저장
python_code_files = sorted(list(python_code_files))
print(python_code_files)

#%%

python_code_files2 = sorted(python_code_files)
print(python_code_files2)