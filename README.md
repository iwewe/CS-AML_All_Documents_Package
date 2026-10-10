# CS-AML All Documents Package

**Civil Society Anti-Money Laundering & Financial Intelligence Framework**

Paket dokumentasi lengkap CS-AML: kerangka metodologi, spesifikasi produk, rekayasa, dan antarmuka untuk aplikasi intelijen keuangan berbasis masyarakat sipil, beserta hasil audit dokumentasinya.

> **Status: v0.1.4 — Approved Internal Specification Baseline (tag `v0.1.4-spec`, 10 Oktober 2026; menggantikan `v0.1.3-spec`).**
> v0.1.4 memuat 14 change request (CR-N-01…CR-N-14) dari tindak lanjut pasca-MVP: alur kerja kasus (charter, gate G0–G6, task, aktivitas), OCR / ekstraksi teks dan terjemahan mesin offline (DerivedText), serta MFA step-up untuk aksi berisiko tinggi. Semua rekomendasi disetujui product owner pada 2026-10-10 tanpa perubahan perilaku implementasi. Beberapa hal ditunda ke v0.2: status MONITORING/reopen, konfigurasi gate per organisasi/tingkat risiko, konfigurasi step-up per deployment dan faktor tahan-phishing (WebAuthn), filter aktivitas di server dan tampilan auditor, tautan task ke objek.
> v0.1.3 memuat 30 change request (CR-I5-01…CR-I7-08) yang muncul saat implementasi increment I5–I7 (search & graph, produk/review/diseminasi, retensi/hardening). Semua rekomendasi disetujui product owner pada 2026-10-09 tanpa perubahan. Dua syarat: celah timing pada search (CR-I5-08) hanya diterima untuk MVP dengan data sintetis dan wajib ditinjau ulang sebelum data nyata diproses; disposisi ANONYMIZE dan DELETE seluruh kasus (CR-I7-05) ditunda ke v0.2.
> v0.1.2 memuat 52 change request (CR-I1-01…CR-I4-14) dari increment I1–I4. Dua keputusan v0.1.2 masih perlu review eksternal: CR-I4-03 (ambang konsistensi tipologi, oleh spesialis AML) dan CR-I1-10 (model clearance, oleh reviewer keamanan). Ini bukan review independen. Lihat [`CHANGELOG.md`](CHANGELOG.md).

## Kapan sebuah rilis spesifikasi dianggap selesai

> A specification release is considered complete when all release-blocking semantic, safety, traceability, and contract inconsistencies are resolved; automated consistency checks pass; remaining limitations are explicitly documented; and unresolved non-blocking items are assigned to a future release. Absence of known imperfections is not required.

Artinya: spesifikasi tidak harus bebas kekurangan, tetapi harus bebas dari kekurangan yang membuat implementasi berbahaya, ambigu, atau tidak dapat diuji. Setelah sebuah tag spesifikasi, dokumen tidak diaudit ulang kecuali ada perubahan substantif. Masalah yang ditemukan saat implementasi masuk sebagai issue → change request → rilis berikutnya (v0.1.2 adalah rilis pertama lewat jalur ini, v0.1.3 yang kedua, v0.1.4 yang ketiga).

## Panduan untuk programmer

- **Gunakan file Markdown versi terbaru setiap dokumen** (lihat tabel *Daftar dokumen*: delapan dokumen kini `*_v0.1.4*.md`, tiga tetap `*_v0.1.2.md`, sisanya tetap `*_v0.1.1*.md` karena tidak berubah). Setiap dokumen hanya punya satu file Markdown yang berlaku; versi lama tersimpan di git (`git log --follow`, tag `v0.1.1-spec`, `v0.1.2-spec`, `v0.1.3-spec`).
- Rujukan "<dokumen> v0.1.1", "v0.1.2" atau "v0.1.3" di dalam dokumen yang tidak berubah berarti versi terbaru dokumen tersebut.
- **DOCX dan PDF adalah arsip v0.1 lama.** Isinya belum memuat koreksi v0.1.1/v0.1.2, jadi jangan dipakai sebagai acuan implementasi.
- Setiap bagian yang berubah ditandai `*[v0.1.1 · Axx]*` (Axx = ID temuan di [`Audit/`](Audit/)), `*[v0.1.2 · CR-xx-yy]*`, `*[v0.1.3 · CR-xx-yy]*` atau `*[v0.1.4 · CR-N-xx]*` (ID change request di `CHANGELOG.md`).
- Untuk kerangka, gunakan `CS-AML_Framework_v0.1.4_Expanded.md`. File `CS-AML_Framework_v0.1.1.md` berstatus *legacy*.
  > `CS-AML_Framework_v0.1.4_Expanded.md` is the authoritative framework document. The non-expanded Framework is retained for historical reference only.
- Kontrak API ada di `contracts/openapi.yaml` (OpenAPI 3.1, versi 0.1.4: 146 path, 190 operasi; ekstensi I3–I7, case-workflow dan N1 sudah digabung). Nilai enum ada di `schemas/enums.yaml` (registry 0.1.4, 87 enum), dan keputusan arsitektur di `docs/adr/`.
- Sebelum commit perubahan spesifikasi, jalankan `python3 tools/check_consistency.py`. Hasilnya harus 0 error.
- Hal-hal yang belum selesai tercantum di bagian **Still open after v0.1.4** dan **Deferred to v0.2** pada `CHANGELOG.md`.

## Rantai analitis inti

```
SOURCE → EVIDENCE → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT
```

## Struktur repositori

```
.
├── Documents/      23 dokumen: Markdown v0.1.4/v0.1.2/v0.1.1 (acuan) + DOCX/PDF v0.1 (arsip)
├── Audit/          Laporan audit, register temuan, rencana perbaikan
├── contracts/      OpenAPI 3.1 (v0.1.4)
├── schemas/        Registry enum (enums.yaml)
├── sources/        Peta sumber indikator tipologi (verifikasi A13)
├── docs/adr/       Architecture Decision Records (0004–0006)
├── tools/          Konverter DOCX → Markdown dan pengecek konsistensi
├── CHANGELOG.md    Register keputusan dan perubahan (v0.1.4, v0.1.3, v0.1.2, v0.1.1)
└── MANIFEST.txt    Daftar seluruh file
```

## Daftar dokumen

Nama file mengikuti pola `CS-AML_<Judul>_v<versi>.md` (acuan) dan `CS-AML_<Judul>_v0.1.docx/.pdf` (arsip). Kolom **Versi** menunjukkan versi Markdown yang berlaku.

### Kerangka & metodologi

| Dokumen | Versi | Catatan |
|---|---|---|
| CS-AML Framework (Expanded) | **0.1.4** | Kerangka induk (v0.1.4: hanya §5.9 baru) |
| CS-AML Framework | 0.1.1 | *Legacy*, digantikan versi Expanded |
| Framework Goals and Non-Goals | 0.1.1 | |
| Investigation Methodology | **0.1.4** | |
| Typology Catalogue | **0.1.2** | 20 tipologi; katalog CS-AML, bukan daftar resmi FATF |
| Control Implementation Guide | **0.1.4** | |

### Produk & kebutuhan

| Dokumen | Versi | Catatan |
|---|---|---|
| Product Requirements Document (PRD) | 0.1.1 | |
| Product and Feature Specification | 0.1.1 | 88 fitur (55 P0, 26 P1, 7 P2) |
| Software Requirements Specification (SRS) | **0.1.4** | |

### Arsitektur & rekayasa

| Dokumen | Versi | Catatan |
|---|---|---|
| Technology Architecture | 0.1.1 | Kapabilitas memakai namespace `TA-CAP-xx` |
| Technical Stack and Repository Specification | **0.1.4** | |
| Data Model Specification | **0.1.4** | Registry enum (Annex A) |
| API Specification | **0.1.4** | |
| Frontend Architecture and State Management Specification | **0.1.2** | |
| MVP Engineering Breakdown | 0.1.1 | |
| Sprint and Milestone Plan | 0.1.1 | |

### UX & antarmuka

| Dokumen | Versi | Catatan |
|---|---|---|
| UX Specification | 0.1.1 | |
| Information Architecture Specification | **0.1.4** | |
| Screen Inventory | 0.1.1 | 53 ID layar (50 layar kerja + 3 layar status sistem) |
| Wireframe Specification | 0.1.1 | |
| High-Fidelity UI Specification | 0.1.1 | |
| UI Design System Specification | **0.1.2** | |
| Component Inventory and Storybook Implementation Specification | 0.1.1 | 65 komponen |

## Keputusan utama v0.1.4

| Topik | Keputusan |
|---|---|
| Change request | 14 CR pasca-MVP (CR-N-01…CR-N-14) disetujui product owner (2026-10-10) tanpa perubahan perilaku implementasi |
| Kontrak | Ekstensi `case-workflow.yaml` dan `n1.yaml` digabung ke `contracts/openapi.yaml` 0.1.4: riwayat versi charter, detail/ubah task, OCR / ekstraksi teks, terjemahan offline, DerivedText; `STEP_UP_REQUIRED` (403) pada 13 operasi berisiko tinggi; field sesi `auth_level`/`auth_time`/`step_up`; parameter login `acr`; `authCallback` gagal → 303 `/?login_error=…` |
| Registry | 9 enum baru (`investigation_question_priority`, `gate_status`, `task_type`, `task_status`, `derived_text_transformation`, `derived_text_status`, `text_page_method`, `derivation_type` (terbuka), `job_type`); `DERIVED_TEXT` / `DERIVED` di search |
| Kebijakan | Status kasus hanya berubah lewat gate yang disetujui (G0 DRAFT→AUTHORIZED, G1 AUTHORIZED→ACTIVE, G4 ACTIVE→REVIEW, G6 ACTIVE/REVIEW→CLOSED); gate hanya mengendalikan siklus hidup kasus; pemutus ≠ pengaju; semua mesin otomasi (OCR, MT, AI) wajib offline; 11 aksi step-up (ACR 2 = password + TOTP, 900 s) |
| Ditunda ke v0.2 | MONITORING/reopen; konfigurasi gate per organisasi/tingkat risiko; step-up per deployment dan WebAuthn/passkey; filter aktivitas di server dan tampilan auditor; tautan task ke objek; ekstraksi DOCX/XLSX |

## Keputusan utama v0.1.3

| Topik | Keputusan |
|---|---|
| Change request | 30 CR dari implementasi I5–I7 disetujui product owner (2026-10-09) tanpa perubahan |
| Kontrak | Ekstensi I5/I6/I7 digabung ke `contracts/openapi.yaml` 0.1.3: search, graph query/paths, template & versi produk, koreksi/withdraw, review kinds, diseminasi & export package, retensi/legal hold/disposisi; baru `GET /evidence-extracts/{extractId}` dan `GET /health` (`/metrics` internal, di luar API); `generateExportPackage` selalu 202 |
| Registry | 18 enum baru (mis. `search_object_type`, `review_kind`, `dissemination_status`, `export_package_format`, `job_status`, `retention_target_type`, `disposition_status`) |
| Kebijakan | SOURCE_PROTECTED di search hanya dengan opt-in eksplisit + grant per kasus; rilis SOURCE_PROTECTED hanya dengan `source_protected_release` oleh approver ber-grant; disposisi selalu lewat keputusan LEAD (bukan pengusul), ditolak saat legal hold aktif |
| Syarat | CR-I5-08: celah timing search ditinjau ulang sebelum data nyata; CR-I7-05: ANONYMIZE dan DELETE seluruh kasus ditunda ke v0.2 |

## Keputusan utama v0.1.2

| Topik | Keputusan |
|---|---|
| Change request | 52 CR dari implementasi I1–I4 disetujui product owner (2026-10-09); CR-I4-10 diubah: disconfirming search boleh ditambahkan setelah finalize sampai review approval |
| Kontrak | Ekstensi I3/I4 digabung ke `contracts/openapi.yaml` 0.1.2; membership kasus, back-channel logout, provenance trace; `/entity-match-candidates/{id}/decisions` deprecated |
| Registry | 10 enum baru (mis. `case_membership_role`, `risk_rating`, `upload_session_status`, `envelope_status`, `credibility_grade`, `hypothesis_link_effect`) |
| Kebijakan | Semua merge/unmerge high-impact (wajib reviewer ≠ decider → 409); reklasifikasi kasus hanya oleh LEAD (upgrade saja); aturan competing hypotheses ditegakkan saat finalize |
| Perlu review eksternal | CR-I4-03 (ambang konsistensi, spesialis AML), CR-I1-10 (model clearance, keamanan) |

## Keputusan utama v0.1.1

| Topik | Keputusan |
|---|---|
| Template produk MVP | 6: Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report |
| Klasifikasi | `PUBLIC`, `INTERNAL`, `SENSITIVE`, `RESTRICTED`, `SOURCE_PROTECTED`; label tak dikenal → akses ditolak (fail closed) |
| Object storage | S3-compatible; produk dipilih lewat ADR-0005 (MinIO Community bukan lagi default) |
| Broker/cache | Valkey 8.x (BSD-3-Clause), versi dikunci (ADR-0006) |
| Autentikasi browser | Session cookie di server (BFF) lewat OIDC Keycloak; token tidak pernah sampai ke JavaScript |
| Konflik versi | `If-Match` usang → 412, tanpa `If-Match` → 428, konflik workflow → 409. Perintah multi-entity (merge, unmerge, resolution decision) memakai `expected_versions` di body, bukan `If-Match` |
| Enum | `UPPER_SNAKE_CASE`; confidence `HIGH/MODERATE/LOW/INSUFFICIENT_BASIS` |
| Claim/Fact | Claim permanen; Fact objek terpisah yang *didukung* claim/evidence + VerificationDecision (disetujui 2026-10-08) |
| Entity resolution | Status entity (`resolution_status`) dipisah dari ResolutionDecision (MERGE/KEEP_SEPARATE/POSSIBLE_MATCH/DEFER/UNMERGE) (disetujui 2026-10-08) |

## Audit

| File | Isi |
|---|---|
| [`CS-AML_Documentation_Audit_2026-10-07.md`](Audit/CS-AML_Documentation_Audit_2026-10-07.md) | Laporan audit konsistensi, sumber, dan kesiapan paket v0.1 |
| [`CS-AML_Audit_Register_2026-10-07.json`](Audit/CS-AML_Audit_Register_2026-10-07.json) | Register temuan A01–A16 beserta bukti dan hash file |
| [`audit-cs-ml.md`](Audit/audit-cs-ml.md) | Rencana siklus perbaikan dokumentasi |

File audit 2026-10-07 tidak diubah dan tetap menggambarkan kondisi v0.1. Status perbaikan setiap temuan ada di `CHANGELOG.md`. Hasil pemeriksaan konsistensi v0.1.1 ada di `CS-AML_Consistency_Audit_v0.1.1_2026-10-08.md`; pemeriksaan ini dilakukan oleh AI, bukan pihak independen.

## Catatan penggunaan

- Dokumen ini adalah spesifikasi, bukan sertifikasi, opini hukum, atau bukti bahwa aplikasi sudah berjalan atau aman.
- Kecocokan tipologi adalah indikator, bukan bukti kejahatan. Struktur graf menghasilkan petunjuk, bukan kesimpulan bersalah.
- Rujukan ke FATF, Wolfsberg, dan PPATK tidak berarti lembaga tersebut mengesahkan taksonomi atau arsitektur CS-AML.
