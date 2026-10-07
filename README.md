# CS-AML All Documents Package

**Civil Society Anti-Money Laundering & Financial Intelligence Framework**

Paket dokumentasi lengkap CS-AML versi **v0.1** (Oktober 2026): kerangka metodologi, spesifikasi produk, rekayasa, dan antarmuka untuk aplikasi intelijen keuangan berbasis masyarakat sipil, beserta hasil audit dokumentasinya.

> **Status: Normative Draft v0.1 — belum tervalidasi.**
> Audit 7 Oktober 2026 mencatat 16 temuan terbuka (9 tinggi, 6 sedang, 1 rendah). Paket ini belum layak diperlakukan sebagai baseline implementasi final. Lihat [`Audit/`](Audit/) sebelum memakai dokumen ini sebagai acuan.

## Rantai analitis inti

```
SOURCE → EVIDENCE → FACT → INDICATOR → HYPOTHESIS → ASSESSMENT → INTELLIGENCE PRODUCT
```

## Struktur repositori

```
.
├── Documents/     23 dokumen spesifikasi (DOCX, PDF, dan sebagian Markdown)
├── Audit/         Laporan audit dokumentasi, register temuan, dan rencana perbaikan
└── MANIFEST.txt   Daftar seluruh file dalam paket
```

## Daftar dokumen

Setiap dokumen tersedia dalam format **DOCX** (sumber normatif) dan **PDF**. Sebagian besar juga punya file **Markdown**, tetapi banyak di antaranya hanya *companion* ringkas, bukan salinan penuh (temuan audit A12). Untuk isi lengkap, gunakan DOCX.

### Kerangka & metodologi

| Dokumen | MD |
|---|:-:|
| CS-AML Framework | ✓ |
| CS-AML Framework (Expanded) | ✓ |
| Framework Goals and Non-Goals | — |
| Investigation Methodology | ✓ |
| Typology Catalogue | — |
| Control Implementation Guide | ✓ |

### Produk & kebutuhan

| Dokumen | MD |
|---|:-:|
| Product Requirements Document (PRD) | ✓ |
| Product and Feature Specification | ✓ |
| Software Requirements Specification (SRS) | ✓ |

### Arsitektur & rekayasa

| Dokumen | MD |
|---|:-:|
| Technology Architecture | ✓ |
| Technical Stack and Repository Specification | ✓ |
| Data Model Specification | ✓ |
| API Specification | ✓ |
| Frontend Architecture and State Management Specification | ✓ |
| MVP Engineering Breakdown | ✓ |
| Sprint and Milestone Plan | ✓ |

### UX & antarmuka

| Dokumen | MD |
|---|:-:|
| UX Specification | ✓ |
| Information Architecture Specification | ✓ |
| Screen Inventory | ✓ |
| Wireframe Specification | ✓ |
| High-Fidelity UI Specification | ✓ |
| UI Design System Specification | ✓ |
| Component Inventory and Storybook Implementation Specification | ✓ |

Nama file mengikuti pola `CS-AML_<Judul>_v0.1.<ext>`.

## Audit

| File | Isi |
|---|---|
| [`CS-AML_Documentation_Audit_2026-10-07.md`](Audit/CS-AML_Documentation_Audit_2026-10-07.md) | Laporan audit konsistensi, sumber, dan kesiapan paket |
| [`CS-AML_Audit_Register_2026-10-07.json`](Audit/CS-AML_Audit_Register_2026-10-07.json) | Register temuan A01–A16 beserta bukti dan hash file |
| [`audit-cs-ml.md`](Audit/audit-cs-ml.md) | Rencana siklus perbaikan dokumentasi |

Dokumen sumber belum diubah sejak audit; semua temuan masih berstatus terbuka.

## Catatan penggunaan

- Dokumen ini adalah spesifikasi, bukan sertifikasi, opini hukum, atau bukti bahwa aplikasi sudah berjalan atau aman.
- Kecocokan tipologi adalah indikator, bukan bukti kejahatan. Struktur graf menghasilkan petunjuk, bukan kesimpulan bersalah.
- Rujukan ke FATF, Wolfsberg, dan PPATK tidak berarti lembaga tersebut mengesahkan taksonomi atau arsitektur CS-AML.
