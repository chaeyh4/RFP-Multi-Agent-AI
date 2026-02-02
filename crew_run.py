from crewai import Crew

def run_crew(extractor, matcher, reviewer, task1, task2, task3):
    # 실행 및 저장
    proposal_crew = Crew(
        agents=[extractor, matcher, reviewer],
        tasks=[task1, task2, task3],
        verbose=True
    )

    print("\n### 통합 분석 시스템을 가동합니다 ###")
    result = proposal_crew.kickoff()
    return result
