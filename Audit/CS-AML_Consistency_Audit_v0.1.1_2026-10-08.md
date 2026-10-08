# CS-AML — Audit Konsistensi Lintas Dokumen v0.1.1

**Tanggal pemeriksaan:** 8 Oktober 2026
**Status:** Pemeriksaan internal yang dilakukan oleh AI (Claude). **Bukan verifikasi independen**, bukan sertifikasi, dan bukan bukti bahwa implementasi sudah diuji.
**Perubahan pada dokumen sumber:** Tidak ada. Laporan ini hanya mencatat temuan; koreksi belum dijalankan.

## 1. Cakupan dan metode

Yang diperiksa adalah sumber kanonik v0.1.1: `Documents/*_v0.1.1*.md` (23 dokumen), `schemas/enums.yaml`, `contracts/openapi.yaml`, `sources/typology-source-map.yaml`, `docs/adr/*.md`, `CHANGELOG.md` dan README di `contracts/`, `schemas/` serta `docs/adr/`. DOCX/PDF (legacy) dan `remediation.txt` tidak diperiksa.

`python3 tools/check_consistency.py` lulus (0 error, 0 warning; 50 enum, 88 fitur, 113 ID SRS, 50 story). Pemeriksaan ini mencari hal yang tidak ditangkap skrip tersebut: kontradiksi semantik antardokumen, sisa istilah v0.1, celah traceability, ketidakcocokan API Specification ↔ OpenAPI, serta Markdown yang rusak (jumlah kolom tabel diperiksa dengan skrip; tag di dalam code fence dicari dengan grep). Hitungan di CHANGELOG sudah dicocokkan ulang: 71 path dan 91 operasi OpenAPI, 50 enum dengan 291 nilai, serta 89 indikator di peta sumber, yang sama dengan jumlah baris indikator di Typology Catalogue.

Batasan: pembacaan dilakukan dengan sampel terarah, bukan baris demi baris di seluruh 33.000 baris. Tidak adanya temuan pada suatu bagian tidak membuktikan bagian itu bebas cacat.

## 2. Ringkasan status

| Temuan | Status | Catatan / temuan terkait |
|---|---|---|
| A01 Klaim kesiapan | Terkoreksi konsisten | Status block dan "not validated" ada di ke-23 dokumen. |
| A02 MinIO | Terkoreksi sebagian | ADR-0003 dan ADR-0005 tumpang tindih (C19). |
| A03 Redis → Valkey | Terkoreksi konsisten | — |
| A04 409/412 | Terkoreksi sebagian | `expected_versions` hanya diterapkan di API/OpenAPI (C03–C05). |
| A05 F-ASM-003 | Terkoreksi sebagian | SRS-FR-ASM-004 tidak punya objek data, endpoint, atau bukti sprint (C10). |
| A06 Enam template | Terkoreksi konsisten | PRD, SRS, MVP, Sprint, Screen, Data Model dan OpenAPI (subset 6 dari 8) selaras. |
| A07 Namespace CAP | Terkoreksi konsisten | Crosswalk TA-CAP ↔ CAP lengkap. |
| A08 Klasifikasi | Terkoreksi konsisten | — |
| A09 Enum | Terkoreksi sebagian | Ada state dan relationship type di luar registry (C08, C09, C14, C15). |
| A10 Claim/Fact | Terkoreksi sebagian | Lihat D-A10. |
| A11 Kontrak API | Terkoreksi sebagian | C12, C13, C18. |
| A12 Markdown lengkap | Terkoreksi konsisten | — |
| A13 Sumber | Terkoreksi sebagian | Label sudah ada; pemetaan per indikator masih terbuka dan sudah tercatat di CHANGELOG. Tidak ada temuan baru. |
| A14 DIRECTOR_OF | Terkoreksi konsisten | — |
| A15 Case Register | Terkoreksi konsisten | — |
| A16 Waiver rilis | Terkoreksi konsisten | Daftar invariant sama di Sprint Plan, Framework Expanded, Control Guide, SRS dan MVP. |
| D-A10 (Fact didukung claim, tidak dipromosikan) | Terkoreksi sebagian | C01, C02, C11, C16, C17. |
| D-ER (state vs ResolutionDecision) | Terkoreksi sebagian | C06, C07. |

Jumlah: 19 temuan, terdiri atas 2 Tinggi, 9 Sedang dan 8 Rendah.

## 3. Temuan rinci

### C01 — Decision `CREATE` tidak bisa dibuat sebelum Fact-nya ada
**Tingkat keparahan:** Tinggi.
**Bukti:**
- `Documents/CS-AML_Data_Model_Specification_v0.1.1.md:365` menetapkan `target_ref` sebagai "Claim or Fact the decision applies to". Decision `CREATE` dengan demikian menunjuk ke Fact itu sendiri.
- `Documents/CS-AML_API_Specification_v0.1.1.md:372` mewajibkan `POST /cases/{caseId}/facts` membawa "a VerificationDecision ref; otherwise 422".
- `contracts/openapi.yaml:6464` mendeskripsikan `verification_decision_refs` sebagai "Existing VerificationDecision(s) supporting fact creation".
- Satu-satunya endpoint untuk membuat decision adalah `POST /claims/{claimId}/verification-decisions`, dan endpoint itu hanya menerima nilai untuk claim (`ClaimVerificationDecisionCreate`).

Akibatnya, decision `CREATE` harus sudah ada sebelum Fact yang menjadi targetnya dibuat. Fact tanpa claim, yang hanya didukung evidence, tidak bisa dibuat sama sekali.

**Koreksi:** Tetapkan bahwa server membuat decision `CREATE` secara atomik di dalam `POST /cases/{caseId}/facts`. Request membawa `rationale` dan `evidence_refs` untuk decision tersebut. Hapus `verification_decision_refs` dari `required` di `FactCreate`, atau ubah artinya secara eksplisit menjadi decision claim yang mendukung (opsional). Selaraskan API §16A, Data Model §7.5, SRS-FR-CLM-003 dan MVP ST-E3-07.

### C02 — "Claim dan/atau evidence" bertentangan dengan evidence yang wajib
**Tingkat keparahan:** Sedang.
**Bukti:**
- Evidence diwajibkan oleh Data Model `:323` (`supporting_evidence | ref[] | Y | 1..n`), `:864` DM-I01 ("Every Fact SHALL reference at least one EvidenceItem or EvidenceExtract") dan `contracts/openapi.yaml:6473` (`required: supporting_evidence`).
- Sebaliknya, Data Model `:343`, API `:372`, SRS `:350`, MVP `:480` dan Sprint Plan `:248` menulis "supporting claim references … **and/or** evidence references". Rumusan ini mengizinkan Fact yang hanya didukung claim.

**Koreksi:** Putuskan salah satu, lalu terapkan di semua dokumen. Pilihan pertama: ganti "and/or" menjadi "evidence (wajib) plus claim (opsional)". Pilihan kedua: longgarkan DM-I01 dan `required` di OpenAPI.

### C03 — `expected_versions` belum diterapkan di luar API Specification
**Tingkat keparahan:** Tinggi.
**Bukti:** API `:312` menetapkan bahwa perintah multi-entity memakai body map `expected_versions` dan tidak memakai `If-Match`. Dokumen berikut masih menyatakan aturan tunggal `If-Match` untuk semua mutasi:
- SRS `:852` (SRS-IF-002): "Mutations of versioned resources SHALL use `If-Match`".
- Frontend `:205`: "Every mutation of a versioned resource SHALL send `If-Match`". Pemetaan 412 di `:209` hanya menampilkan `details.current_record_version` (tunggal).
- Technical Stack `:295`, UX `:443` dan Component Inventory `:124` (GEN-028: "412 … (stale If-Match)").
- MVP ST-E4-04 `:570` tidak menyebut `expected_versions` maupun Idempotency-Key.

Padahal CHANGELOG D-A04 mencantumkan Frontend, SRS-IF-002, UX dan Component Inventory sebagai dokumen terdampak.

**Koreksi:** Di setiap lokasi di atas, tambahkan pengecualian: "merge/unmerge/resolution-decision: body `expected_versions`; 412 membawa `details.current_record_versions` (map)". Frontend dan GEN-028 perlu menangani konflik untuk banyak entitas.

### C04 — `expected_versions` wajib menurut skema, sehingga balasannya bisa 422, bukan 428
**Tingkat keparahan:** Sedang.
**Bukti:**
- `contracts/openapi.yaml:6836`, `:6862`, `:6906` dan `:6938` mencantumkan `expected_versions` sebagai `required` di skema body JSON. Validator skema yang umum akan menolak request seperti ini dengan 422 VALIDATION_FAILED.
- Padahal API `:312` dan `openapi.yaml:4746` menetapkan "Missing map … → 428 PRECONDITION_REQUIRED". Urutan evaluasi di API `:192` juga menempatkan 428 sebelum 422.
- Selain itu, `/entity-match-candidates/{id}/decisions` memakai `expected_versions` di OpenAPI, tetapi tidak tercantum dalam daftar Preconditions di API `:312`.

**Koreksi:** Keluarkan `expected_versions` dari `required` dan dokumentasikan bahwa server mengembalikan 428 jika field itu tidak ada. Alternatif: nyatakan di API §9 bahwa field precondition di body diperiksa sebelum validasi skema. Tambahkan endpoint match-candidate ke API §14 Preconditions.

### C05 — `expected_versions` berlabel "Proposed", padahal keputusannya "Adopted"
**Tingkat keparahan:** Rendah.
**Bukti:** `contracts/openapi.yaml:6729` ("Proposed: map <entityId>…"), `:4726` dan `:4746` ("Proposed multi-entity precondition"), serta `contracts/README.md:19`. Di sisi lain, CHANGELOG D-A04 berstatus "Adopted · 2026-10-08" dan API `:312` bersifat normatif tanpa label proposed.
**Koreksi:** Hapus `x-csaml-status: proposed` dan teks "Proposed" pada `ExpectedVersions`, response 412/428 multi-entity, dan README.

### C06 — Pemetaan "unresolved" pada match-candidate bertentangan dengan Methodology
**Tingkat keparahan:** Sedang.
**Bukti:**
- `contracts/openapi.yaml:6910`: "distinct → KEEP_SEPARATE, unresolved → POSSIBLE_MATCH, defer → DEFER".
- `Documents/CS-AML_Investigation_Methodology_v0.1.1.md:378`: "UNRESOLVED → DEFER" (juga CHANGELOG Round 2).
- API `:302` masih memakai kosakata lama "Mark same/distinct/unresolved/defer".

**Koreksi:** Ganti istilah di API §14 dengan nilai wire (`MERGE` via `/entities/merge`, `KEEP_SEPARATE`, `POSSIBLE_MATCH`, `DEFER`) dan hapus pemetaan "unresolved" dari OpenAPI. Jika pemetaan tetap dipertahankan, samakan dengan Methodology (→ `DEFER`).

### C07 — Tabel API §14 rusak, sehingga endpoint relationship/asset masuk ke tabel aturan
**Tingkat keparahan:** Sedang.
**Bukti:** `Documents/CS-AML_API_Specification_v0.1.1.md:308` membuka tabel 2 kolom (`| **Concern** | **Rule** |`). Baris `:314`–`:317` (`| GET/POST | /relationships | First-class relationships. |`, `/relationships/{relationshipId}`, `/assets`, `/assets/{assetId}`) berisi 3 kolom. Akibatnya keempat endpoint itu dirender sebagai baris "Concern" yang kolom ketiganya terpotong.
**Koreksi:** Tutup tabel aturan setelah baris "Re-suggestion", lalu pindahkan keempat endpoint ke tabel `Method | Endpoint | Purpose` yang baru, atau kembalikan ke tabel endpoint di atasnya.

### C08 — SRS Annex B memakai state yang tidak ada di registry
**Tingkat keparahan:** Sedang.
**Bukti:**
- SRS `:1370` "Case: DRAFT → TRIAGE → ACTIVE → REVIEW → APPROVED/CLOSED → …". Nilai registry `case_status` dan Data Model `:203` adalah DRAFT → AUTHORIZED → ACTIVE → REVIEW → CLOSED → MONITORING → REOPENED: TRIAGE dan APPROVED tidak ada di sana, sedangkan AUTHORIZED tidak muncul di SRS.
- SRS `:1381` "Intelligence product: DRAFT → IN_REVIEW → CHANGES_REQUESTED → APPROVED → DISSEMINATED → SUPERSEDED/CORRECTED". Registry `product_approval_state` berisi DRAFT, REVIEWED, APPROVED, DISSEMINATED, WITHDRAWN.
- SRS `:1390` "PROVISIONAL → ESTABLISHED → DISPUTED | SUPERSEDED" tidak memuat transisi PROVISIONAL→DISPUTED dan DISPUTED→SUPERSEDED, padahal keduanya ada di Data Model §7.5.

**Koreksi:** Turunkan Annex B dari `schemas/enums.yaml` dan lifecycle di Data Model. Jika state proses (triage, changes requested) memang dibutuhkan, daftarkan dulu di registry.

### C09 — Relationship type di Methodology, IA dan Framework berada di luar registry
**Tingkat keparahan:** Sedang.
**Bukti:**
- Methodology `:405`–`:411`: SHAREHOLDER_OF, AUTHORIZED_SIGNATORY_OF, LENDER_TO, BORROWER_FROM, OWNS_ASSET, USES_ASSET, ACQUIRED_FROM, RELATIVE_OF, SHARES_DOMAIN_WITH, TRANSFERRED_VALUE_TO, RECEIVED_VALUE_FROM.
- IA `:318`–`:320`: MANAGES, USES, RELATIVE_OF.
- Framework Expanded `:586`: COMMISSIONER_OF, REPRESENTS, SHARES_CONTACT_WITH, LOANED_TO, LEASED_TO, DONATED_TO, FUNDED_BY, ACTS_FOR.

Tak satu pun nilai di atas terdaftar di `relationship_type` dalam `schemas/enums.yaml` atau di Data Model Annex B. Ini bertentangan dengan D-A09 ("All wire enums … registered").

**Koreksi:** Daftarkan nilai yang memang dipakai ke Annex B dan registry, atau tandai daftar di atas sebagai contoh tampilan yang dipetakan ke nilai registry (misalnya SHAREHOLDER_OF → OWNS + `ownership_type`).

### C10 — SRS-FR-ASM-004 tidak punya objek data maupun endpoint, dan titik penegakannya berbeda
**Tingkat keparahan:** Sedang.
**Bukti:**
- SRS `:606`–`:613` mensyaratkan "recorded disconfirming-search entry … before a high-impact or adverse assessment/product can pass review".
- Data Model §13.3 (`:678`–`:692`) dan §15.2 tidak punya field atau objek untuk catatan ini, juga tidak punya penanda "high-impact adverse".
- API Specification tidak punya endpoint untuk mencatatnya.
- OpenAPI `:3348` justru menegakkannya saat `POST /assessments/{id}/finalize` (409), bukan saat review.
- Traceability MVP E6 `:726` belum memuat SRS-FR-ASM-004 (hanya tabel epic `:50` yang memuatnya). Sprint 5 tidak punya exit criterion maupun bukti untuk aturan ini (bagian bukti sprint di sekitar `:402`).

**Koreksi:** Tambahkan objek atau field (misalnya `Assessment.disconfirming_search` dan penanda high-impact) di Data Model, buat endpoint dan skema di API/OpenAPI, dan pilih satu titik penegakan: review atau finalize. Tambahkan SRS-FR-ASM-004 ke MVP `:726` serta ke exit criteria dan bukti Sprint 5.

### C11 — Uji dependent flagging dijadwalkan di Sprint 2, padahal Assessment dan Product baru dibangun kemudian
**Tingkat keparahan:** Sedang.
**Bukti:**
- Sprint Plan `:260` mensyaratkan bukti Sprint 2 berupa "Claim/fact lifecycle test (… dependent flagging)". MVP `:498` mensyaratkan "flags dependent assessment/product, leaves published product unchanged".
- Assessment baru dibangun di Sprint 5 (ST-E6-06, Sprint Plan `:380`), sedangkan Product dan Review di Sprint 7 (ST-E8-01…06, `:462`–`:472`).

**Koreksi:** Batasi bukti Sprint 2 pada claim, decision dan transisi fact. Pindahkan uji dependent flagging ke exit criteria Sprint 5 (assessment) dan Sprint 7 (product dan correction task), sebagai regresi atas ST-E3-07.

### C12 — OpenAPI disebut "generated from the implementation", padahal kontraknya contract-first
**Tingkat keparahan:** Sedang.
**Bukti:**
- API `:544`: "An OpenAPI 3.1 document SHALL be generated from the implementation, committed as `contracts/openapi.yaml`".
- API `:558`, SRS `:852` dan `contracts/README.md` menyatakan bahwa file ini ditulis tangan (contract-first), sedangkan skema hasil generate cukup dibandingkan (di-diff) dengan file ini di CI.
- SRS `:852` juga memuat kalimat rusak: "An The OpenAPI 3.1 contract …".

**Koreksi:** Ubah API `:544` menjadi "maintained contract-first in `contracts/openapi.yaml`; the schema generated from the implementation SHALL be diffed against it in CI", dan perbaiki "An The" di SRS `:852`.

### C13 — Nama resource di SRS Annex C berbeda dari API/OpenAPI
**Tingkat keparahan:** Rendah.
**Bukti:**
- SRS `:1403` `/evidence-extracts` (API: `/evidence/{evidenceId}/extracts`).
- SRS `:1425` `/gaps` (API: `/intelligence-gaps`).
- `/claims` (API: `/cases/{caseId}/claims` untuk list dan create).
- Aturan "exact REST/GraphQL design may vary" bertentangan dengan SRS-IF-002, yang mewajibkan kepatuhan pada `contracts/openapi.yaml`.

**Koreksi:** Samakan Annex C dengan path API §12–§20 dan hapus frasa "REST/GraphQL may vary", atau beri label informatif yang tunduk pada OpenAPI.

### C14 — Contoh query API memakai nilai di luar registry
**Tingkat keparahan:** Rendah.
**Bukti:** API `:148` `GET /api/v1/entities?…&type=COMPANY&status=CONFIRMED…`. `COMPANY` adalah `organization_type`, bukan `entity_type`. `CONFIRMED` adalah istilah v0.1 yang sekarang menjadi `RESOLVED`. Di OpenAPI, parameter `type` dan `status` pada `GET /entities` hanya bertipe string tanpa enum.
**Koreksi:** Ubah contoh menjadi `type=ORGANIZATION&resolution_status=RESOLVED`, lalu beri parameter OpenAPI tersebut nama dan `x-csaml-enum` yang tepat (`entity_type`, `entity_resolution_status`).

### C15 — Komentar usang di OpenAPI
**Tingkat keparahan:** Rendah.
**Bukti:**
- `contracts/openapi.yaml:5308`: "The API Specification §16 calls the rationale `confidence.rationale`". API `:350` kini memakai `confidence.basis`.
- `:6293`: "(API §16A also lists claim_status under PATCH)". API `:359` kini menyatakan "`claim_status` is read-only here".

**Koreksi:** Hapus kedua kalimat tersebut.

### C16 — Sisa istilah "promotion" dan "verified" pada Fact
**Tingkat keparahan:** Rendah.
**Bukti:**
- Control Implementation Guide `:1420`: "Require source-level human verification before promotion to Claim/Fact".
- UX `:155` mendefinisikan Fact sebagai "Verified/time-bounded proposition", padahal Fact `PROVISIONAL` belum ditetapkan (established).

**Koreksi:**
- Control Guide: "…before a Claim is recorded or a Fact is created through a VerificationDecision".
- UX: "Proposition, time-bounded, … status Provisional/Established/…", tanpa kata "Verified".

### C17 — Frontend dan Component Inventory belum memuat artefak A10/ER
**Tingkat keparahan:** Rendah.
**Bukti:**
- Frontend §22 (`:400`–`:409`) dan struktur `features/` (`:80`–`:105`) tidak punya pemilik untuk claims, facts, verification decisions atau resolution decisions.
- Component Inventory tidak punya komponen untuk `claim_status`/`fact_status`, riwayat decision, maupun penanda `review_required`. Satu-satunya yang terkait adalah ANA-001 di `:130`.
- HiFi `:237` merujuk `MergeDecisionPanel`, `CompareColumn` dan `RationaleField`, padahal ketiganya tidak ada di inventory.

CHANGELOG D-A10/D-ER mencantumkan "UX/UI" sebagai dokumen terdampak.

**Koreksi:** Tambahkan pemilik fitur dan query key untuk claim, fact dan resolution di Frontend, serta komponen P0 (status badge, decision history, review-required flag) di inventory. Alternatif: petakan nama-nama di HiFi ke ID komponen yang sudah ada.

### C18 — Ketidakcocokan kecil API Specification ↔ OpenAPI
**Tingkat keparahan:** Rendah.
**Bukti:**
- API §13 mencantumkan `PUT/POST /evidence/uploads/{uploadId}/content`, sedangkan OpenAPI hanya punya `PUT` (proposed).
- OpenAPI mewajibkan `If-Match` pada `POST /claims/{claimId}/verification-decisions`, tetapi API `:375` hanya menyebut "`PATCH /claims/{claimId}` and every fact command".

**Koreksi:** Pilih satu method upload dan samakan di kedua sisi. Di API §16A, sebutkan secara eksplisit bahwa `If-Match` wajib untuk verification decision pada claim.

### C19 — Kebersihan Markdown dan ADR
**Tingkat keparahan:** Rendah.
**Bukti:**
- Tag `[v0.1.1 · ER]` dan `[v0.1.1 · A10]` berada di dalam code fence pada Technology Architecture `:385` dan `:1172`, sehingga ikut tercetak sebagai bagian diagram atau trace.
- `contracts/README.md:30` dan `:37` memuat dua heading `## Validation` yang isinya tumpang tindih.
- Technical Stack `:580` mencantumkan `0003-s3-evidence-storage.md` di samping `0005-object-storage.md`, sehingga ada dua ADR untuk keputusan object storage.

**Koreksi:**
- Pindahkan tag ke bawah fence.
- Gabungkan kedua bagian Validation.
- Satukan ADR-0003 dan ADR-0005 (atau batasi ADR-0003 pada pola penyimpanan dan ADR-0005 pada pemilihan produk), lalu perbarui `docs/adr/README.md`.

## 4. Catatan

- Hal yang sudah tercatat sebagai terbuka di CHANGELOG ("Still open") tidak dilaporkan ulang sebagai temuan. Contohnya: label tampilan entitas candidate/probable, tumpang tindih endpoint match-candidate, verifikasi sumber A13, `unregistered_fields`, dan cara SPA memperoleh token CSRF.
- Status "Terkoreksi konsisten" berarti tidak ditemukan kontradiksi dalam pemeriksaan ini. Status itu tidak berarti spesifikasi sudah divalidasi atau diimplementasikan.
- Pemeriksaan ini dilakukan oleh AI dan tidak menggantikan review oleh product owner, technical lead, atau pihak independen.
