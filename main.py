import os

from rag import get_rfp_context
from agents import build_agents
from tasks import build_tasks
from crew_run import run_crew
from exporters import export_md_to_csv_korean

# 1. 환경 설정
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 테스트용 제안서 초안 (작성 중인 텍스트)
proposal_draft = """
[제안서] AI 기반 지능형 배관 관리 및 예방정비 솔루션
1. 귀사의 배관 관리, '터지고 나서' 수리하시겠습니까?
대부분의 기업이 배관 내부가 막히거나 녹물이 나온 후에야 막대한 비용을 들여 교체 공사를 진행합니다. 
하지만 사후 대응 방식은 업무 중단, 자산 가치 하락, 그리고 예방 정비 대비 5배 이상의 지출을 초래합니다.
**[A기업]**은 생성형 AI와 정밀 진단 기술을 결합하여, 보이지 않는 배관 속 리스크를 데이터로 관리하고 비용을 혁신적으로 절감해 드립니다.
2. 주요 서비스 내용 (AI 기반 3단계 케어)
① AI 정밀 진단 및 리스크 예측
디지털 내시경 분석: AI가 배관 내부 영상을 분석하여 부식 정도, 슬러지 퇴적률을 수치화합니다.
AI 예측 리포트: 건축물 연식과 사용량을 분석하여 향후 3년간 발생할 수 있는 누수 및 폐쇄 위험도를 예측합니다.
② 맞춤형 지능형 세척 (Smart Flushing)
고압 펄스 공법: 배관에 무리를 주지 않으면서 스케일만 정밀하게 제거하는 최첨단 공법을 적용합니다.
최적 주기 설정: AI가 귀사의 설비 상태에 가장 경제적인 세척 주기를 산출하여 과잉 정비를 방지합니다.
③ 생성형 AI 관리 대시보드
자동 분석 보고서: 복잡한 수치 대신, AI가 생성한 '쉬운 요약 보고서'를 통해 의사결정권자에게 관리 성과를 즉시 보고할 수 있습니다.
24/7 모니터링: 수질 센서와 연동하여 이상 징후 발생 시 즉각 알림을 발송합니다.
3. 도입 시 기대 효과 (Economic Value)
구분도입 전 (사후 수리)도입 후 (AI 예방 정비)
비용 절감노후 배관 전면 교체 (고비용)정기 세척으로 수명 2배 연장 (60% 절감)
업무 연속성누수 시 공장/사무실 폐쇄비가동 시간 최소화 (야간/주말 작업)
관리 편의성문제 발생 시 업체 수동 수수AI 자동 스케줄링 및 리포트 제공
자산 가치설비 노후화로 가치 하락깨끗한 수질 및 관리 이력으로 가치 보존
4. [A기업]만의 차별점
기술력: 업계 최초 생성형 AI 기반 배관 노후도 판독 알고리즘 보유
신뢰성: 공공기관 및 대단지 산업단지 레퍼런스 확보
사후보장: 서비스 후 문제 발생 시 즉각 출동 및 무상 AS 보증 제도 운영
5. 향후 추진 일정
현장 무료 진단: AI 스캐닝 장비를 통한 배관 상태 샘플링 (D-Day)
분석 리포트 제출: 진단 결과 및 예상 절감 비용 제안 (D+3)
연간 케어 계약: 귀사 맞춤형 정기 관리 서비스 개시 (D+7)
"보이지 않는 곳의 관리가 기업의 진정한 경쟁력입니다."
본 제안과 관련하여 상세한 상담이나 무료 현장 진단을 원하시면 언제든 연락 주시기 바랍니다.
[A기업] 사업본부 배상연락처: 02-xxx-xxxx이메일: contact@acorp.ai홈페이지: www.acorp.ai
"""

def main():
    # 4. 데이터 로드 및 태스크 정의
    rfp_content = get_rfp_context("example_rfp_배관관리.pdf")

    extractor, matcher, reviewer = build_agents()
    task1, task2, task3 = build_tasks(extractor, matcher, reviewer, rfp_content, proposal_draft)

    # 실행
    _ = run_crew(extractor, matcher, reviewer, task1, task2, task3)

    # 각 단계별 결과물을 CSV 및 텍스트로 저장
    export_md_to_csv_korean("1_요구사항_체크리스트.md", "1_요구사항_체크리스트.csv")
    export_md_to_csv_korean("2_일치_여부_보고서.md", "2_일치_여부_보고서.csv")

    print("\n" + "="*50)
    print("분석 완료! 다음 파일들이 생성되었습니다.")
    print("1. 1_요구사항_체크리스트.csv")
    print("2. 2_일치_여부_보고서.csv")
    print("3. 3_최종_전략_리포트.txt")
    print("="*50)

if __name__ == "__main__":
    main()
