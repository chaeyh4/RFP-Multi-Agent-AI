from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# 2. PDF 기반 RAG 설정 (RFP 내용 추출)
def get_rfp_context(pdf_path):
    print(f"[{pdf_path}] PDF 문서 분석 중...")
    reader = PdfReader(pdf_path)
    raw_text = ""
    # 다이아몬드 기판 등 주요 과제가 포함된 초반 페이지 집중 추출
    for i in range(min(10, len(reader.pages))):
        text = reader.pages[i].extract_text()
        if text: raw_text += text

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.create_documents([raw_text])
    vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

    # 한국어 핵심 키워드로 컨텍스트 검색
    relevant_docs = vectorstore.similarity_search("연구개발 목표, 정량적 성능지표, 기술적 요구사항, 관리지침", k=7)
    return "\n".join([doc.page_content for doc in relevant_docs])
