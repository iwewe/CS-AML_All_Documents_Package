# CS-AML All Documents Package

**Civil Society Anti-Money Laundering & Financial Intelligence Framework**

Paket dokumentasi lengkap CS-AML: kerangka metodologi, spesifikasi produk, rekayasa, dan antarmuka untuk aplikasi intelijen keuangan berbasis masyarakat sipil, beserta hasil audit dokumentasinya.

> **Status: v0.1.1 — Approved Internal Specification Baseline (tag `v0.1.1-spec`, 8 Oktober 2026).**
> Keenam release gate terpenuhi: konsistensi domain, invariant keselamatan, traceability, kontrak mesin, keputusan blocking, dan keterbatasan yang tercatat. Spesifikasi ini dibekukan sebagai acuan implementasi. Belum ada review independen, implementasi, atau pengujian yang membuktikan isinya. Lihat [`CHANGELOG.md`](CHANGELOG.md).

## Kapan sebuah rilis spesifikasi dianggap selesai

> A specification release is considered complete when all release-blocking semantic, safety, traceability, and contract inconsistencies are resolved; automated consistency checks pass; remaining limitations are explicitly documented; and unresolved non-blocking items are assigned to a future release. Absence of known imperfections is not required.

Artinya: spesifikasi tidak harus bebas kekurangan, tetapi harus bebas dari kekurangan yang membuat implementasi berbahaya, ambigu, atau tidak dapat diuji. Setelah tag `v0.1.1-spec`, dokumen tidak diaudit ulang kecuali ada perubahan substantif. Masalah yang ditemukan saat implementasi masuk sebagai issue → change request → v0.1.2.

## Panduan untuk programmer

- **Gunakan file Markdown `Documents/*_v0.1.1*.md`.** File-file ini berisi teks lengkap setiap dokumen beserta koreksi audit, dan menjadi sumber acuan utama.
- **DOCX dan PDF adalah arsip v0.1 lama.** Isinya belum memuat koreksi v0.1.1, jadi jangan dipakai sebagai acuan implementasi.
- Setiap bagian yang berubah ditandai `*[v0.1.1 · Axx]*`. Axx adalah ID temuan di [`Audit/`](Audit/).
- Untuk kerangka, gunakan `CS-AML_Framework_v0.1.1_Expanded.md`. File `CS-AML_Framework_v0.1.1.md` berstatus *legacy*.
  > `CS-AML_Framework_v0.1.1_Expanded.md` is the authoritative framework document. The non-expanded Framework is retained for historical reference only.
- Kontrak API ada di `contracts/openapi.yaml` (OpenAPI 3.1, P0 vertical slice). Nilai enum ada di `schemas/enums.yaml`, dan keputusan arsitektur di `docs/adr/`.
- Sebelum commit perubahan spesifikasi, jalankan `python3 tools/check_consistency.py`. Hasilnya harus 0 error.
- Hal-hal yang belum selesai (OpenAPI, ADR, beberapa enum) tercantum di bagian **Still open** pada `CHANGELOG.md`.

## Rantai analitis inti

```
SOURCE → EVIDENCE → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT
```

## Struktur repositori

```
.
├── Documents/      23 dokumen: Markdown v0.1.1 (acuan) + DOCX/PDF v0.1 (arsip)
├── Audit/          Laporan audit, register temuan, rencana perbaikan
├── contracts/      OpenAPI 3.1 (P0 vertical slice)
├── schemas/        Registry enum (enums.yaml)
├── sources/        Peta sumber indikator tipologi (verifikasi A13)
├── docs/adr/       Architecture Decision Records (0004–0006)
├── tools/          Konverter DOCX → Markdown dan pengecek konsistensi
├── CHANGELOG.md    Register keputusan dan perubahan v0.1.1
└── MANIFEST.txt    Daftar seluruh file
```

## Daftar dokumen

Nama file mengikuti pola `CS-AML_<Judul>_v0.1.1.md` (acuan) dan `CS-AML_<Judul>_v0.1.docx/.pdf` (arsip).

### Kerangka & metodologi

| Dokumen | Catatan |
|---|---|
| CS-AML Framework (Expanded) | Kerangka induk |
| CS-AML Framework | *Legacy*, digantikan versi Expanded |
| Framework Goals and Non-Goals | |
| Investigation Methodology | |
| Typology Catalogue | 20 tipologi; katalog CS-AML, bukan daftar resmi FATF |
| Control Implementation Guide | |

### Produk & kebutuhan

| Dokumen | Catatan |
|---|---|
| Product Requirements Document (PRD) | |
| Product and Feature Specification | 88 fitur (55 P0, 26 P1, 7 P2) |
| Software Requirements Specification (SRS) | |

### Arsitektur & rekayasa

| Dokumen | Catatan |
|---|---|
| Technology Architecture | Kapabilitas memakai namespace `TA-CAP-xx` |
| Technical Stack and Repository Specification | |
| Data Model Specification | Registry enum (Annex A) |
| API Specification | |
| Frontend Architecture and State Management Specification | |
| MVP Engineering Breakdown | |
| Sprint and Milestone Plan | |

### UX & antarmuka

| Dokumen | Catatan |
|---|---|
| UX Specification | |
| Information Architecture Specification | |
| Screen Inventory | 53 ID layar (50 layar kerja + 3 layar status sistem) |
| Wireframe Specification | |
| High-Fidelity UI Specification | |
| UI Design System Specification | |
| Component Inventory and Storybook Implementation Specification | 65 komponen |

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
