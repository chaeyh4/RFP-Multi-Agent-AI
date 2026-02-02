import pandas as pd

# 5. 크루 실행 및 결과 저장 함수 (CSV 변환 로직 포함)
def export_md_to_csv_korean(md_file, csv_file):
    try:
        # 다양한 인코딩으로 읽기 시도
        for enc in ['utf-8', 'cp949', 'euc-kr']:
            try:
                with open(md_file, 'r', encoding=enc) as f:
                    lines = [l.strip() for l in f.readlines() if "|" in l]
                if lines: break
            except UnicodeDecodeError: continue

        if len(lines) > 2:
            data = [[cell.strip() for cell in row.split("|") if cell.strip()] for row in lines]
            df = pd.DataFrame(data[2:], columns=data[0])
            # utf-8-sig: 엑셀에서 한글이 깨지지 않게 하는 인코딩
            df.to_csv(csv_file, index=False, encoding='utf-8-sig')
            print(f"✅ 파일 생성 완료: {csv_file}")
    except Exception as e:
        print(f"❌ 파일 변환 중 오류 발생: {e}")
