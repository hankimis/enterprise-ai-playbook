<h1 align="center">Enterprise AI Adoption Playbook (2026)</h1>

<p align="center">
  <em>어떤 모델·에이전트·세팅으로 효율을 극대화하는가. 일반 기업용, 벤더 중립, 정직한 트레이드오프.</em>
</p>

<p align="center">
  <img alt="status" src="https://img.shields.io/badge/status-living%20document-2e6fb0">
  <img alt="scope" src="https://img.shields.io/badge/scope-dev%20·%20design%20·%20ops%20·%20governance-c9962a">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-2a7f3f">
  <img alt="sourced" src="https://img.shields.io/badge/method-deep--research%20%2B%20adversarial%20verify-c0392b">
</p>

<p align="center"><strong>IOV Labs (아이오브연구소)</strong> · 출처 기반·정직한 기업 AI 도입 플레이북</p>

---

## 한 줄 결론

> **도구는 이미 성숙했다. ROI를 가르는 건 도구가 아니라 통제 시스템이다.** 파일럿은 쉽고, 프로덕션·ROI는 어렵다.

## 무엇인가

일반 기업(중소~중견)이 AI를 실제로 도입·운영해 생산성을 극대화하기 위한 실전 가이드. 4개 영역을 상황별로 디테일하게 다루며, 모든 핵심 수치에 출처와 **검증 상태**를 표기한다.

- 📄 **전체 문서(한국어)**: [`PLAYBOOK.ko.md`](PLAYBOOK.ko.md)
- 📑 **발행용 PDF**: [`paper/paper.pdf`](paper/paper.pdf) (9pp)

## 핵심 발견 (검증된 숫자만)

| 지표 | 수치 | 출처 |
|---|---|---|
| AI 업무 사용률 | 90%, 생산성 체감 80%+ | DORA 2025 |
| AI 코드 신뢰 | 30%가 거의/전혀 불신 | DORA 2025 |
| 체감 vs 실제 | 숙련 개발자 RCT에서 **19% 더 느려짐**, 본인은 20% 빨라졌다 착각 | METR 2025 |
| 조직 AI 프로젝트 폐기 | 2025년 **42%**가 대부분 폐기 (전년 2배+) | S&P Global |
| 유의미 ROI | 생성형 29% / 에이전트 23% | WRITER 2026 |
| M365 Copilot 파일럿→대규모 배포 | 단 **6%** | Gartner 2025 |
| RAG도 환각함 (법률 AI) | Lexis+ 17% / Westlaw 33% | Stanford RegLab |

> 흔히 인용되는 "MIT 95% 파일럿 실패", "IBM CEO 25% ROI" 같은 통계는 적대적 검증에서 **출처 추적 불가/과장으로 기각**했다. 사용하지 않는다.

## 목차

1. 현실 점검 (정직한 숫자)
2. **소프트웨어 개발·코딩** — 난이도별 모델, 가격, 오케스트레이션, "AI 같지 않은 코드" 리뷰 체크리스트
3. **디자인·콘텐츠·마케팅** — "AI 티" 제거(디자인 시스템 템플릿, 판별 체크리스트), 도구
4. **업무 자동화·운영** — RAG 도구·가격, 환각 통제, 빌드 vs 바이, 유스케이스 4종 레시피
5. **도입 전략·ROI·거버넌스·호스팅** — 측정 지표, CDAO 조직, AI 스프롤, 온프레 vs 클라우드, 로드맵
6. **보안·프라이버시·규제** — OWASP LLM Top 10, NIST AI RMF, EU AI Act·GDPR·한국 PIPA 37조의2
7. 빠른 의사결정 치트시트
8. 출처

## 방법론·정직성

- **deep-research 하네스** 5개 패스(다중 소스 검색 → 소스 수집 → 적대적 3표 교차검증) + 핵심 수치 직접 스팟 검증.
- 각 항목에 `[검증완료]` / `[스팟확인]` / `[출처·미검증]` 상태 표기.
- 과장 통계는 기각하고, 디자인·노코드 ROI 등 1차 출처가 약한 영역은 **약함을 명시**한다.
- 가격·모델 수치는 2026년 5~6월 기준이며 빠르게 변한다.

## 인용

```bibtex
@misc{kim2026enterpriseai,
  title  = {Enterprise AI Adoption Playbook},
  author = {Kim, Han},
  year   = {2026},
  note   = {IOV Labs. https://github.com/hankimis/enterprise-ai-playbook}
}
```

## 라이선스

MIT (see [LICENSE](LICENSE)).
