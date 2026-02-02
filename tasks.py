from crewai import Task

def build_tasks(extractor, matcher, reviewer, rfp_content, proposal_draft):
    task1 = Task(
        description=(
            f"입력된 RFP PDF 파일의 전수 조사를 통해 발주처가 요구하는 모든 기술적, 관리적, 사업적 요구사항을 추출하세요. "
            f"각 요구사항은 ID를 부여하고, 카테고리(기능, 보안, 유지보수 등), 세부 내용, 중요도를 포함해야 합니다. "
            f"표(Table) 형태로 정리하여 후속 에이전트가 참조할 수 있도록 하세요. 한국어로 답변하세요.\n\n"
            f"[RFP 추출 내용]\n{rfp_content}"
        ),
        expected_output="요구사항 ID, 카테고리, 요구사항 명칭, 상세 내용, 중요도가 포함된 xlsx 테이블 형식의 리스트",
        agent=extractor,
        output_file="1_요구사항_체크리스트.md"
    )

    task2 = Task(
        description=(
            f"extractor가 생성한 요구사항 테이블과 사용자가 작성한 제안서 텍스트를 대조하세요. "
            f"각 요구사항 ID별로 제안서에 내용이 포함되었는지 확인하고, '일치/미흡/누락' 상태를 판정하세요. "
            f"내용이 포함되었다면 제안서의 어느 부분에 해당 내용이 있는지 위치를 명시해야 합니다. 한국어로 답변하세요.\n\n"
            f"[제안서 초안]\n{proposal_draft}"
        ),
        expected_output="요구사항 ID, 일치 여부(O/△/X), 제안서 내 관련 섹션, 검토 의견이 포함된 이행 분석 테이블",
        agent=matcher,
        context=[task1],
        output_file="2_일치_여부_보고서.md"
    )

    task3 = Task(
        description=(
            "사용자의 최종 제안서를 분석하여 독창성을 확인하고, 심사위원의 관점에서 논리적으로 허술하거나 "
            "공격받기 쉬운 '취약한 부분' 3가지를 도출하세요. "
            "단순한 지적에 그치지 않고, 실제 발표(PT) 현장에서 답변할 수 있는 설득력 있는 대응 시나리오를 작성하세요. 한국어로 답변하세요."
        ),
        expected_output="3가지 핵심 취약점 및 각 취약점에 대한 논리적 답변(Q&A)이 포함된 전략 리포트",
        agent=reviewer,
        context=[task2],
        output_file="3_최종_전략_리포트.txt"
    )

    return task1, task2, task3
