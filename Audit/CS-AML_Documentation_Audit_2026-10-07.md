# CS-AML — Audit Dokumentasi, Konsistensi, dan Sumber

**Tanggal pemeriksaan:** 7 Oktober 2026  
**Status:** Hasil review; bukan sertifikasi, legal opinion, atau bukti kelulusan aplikasi.  
**Perubahan pada dokumen sumber:** Tidak ada. Semua temuan tetap terbuka sampai koreksi dan verifikasinya dilakukan.

## Ringkasan keputusan

Paket CS-AML tidak perlu dibuang, tetapi belum layak diperlakukan sebagai baseline implementasi final yang sudah tervalidasi. Sejumlah rujukan eksternal yang sempat tampak berisiko ternyata benar-benar ada. Masalah terbesar adalah drift antarspesifikasi, kontrak implementasi yang belum lengkap, pemilihan dependency yang perlu dimutakhirkan, dan bahasa kesiapan yang terlalu kuat dibanding bukti yang tersedia.

Jawaban saya sebelumnya terlalu yakin ketika menyebut rangkaian ini matang atau siap untuk handoff. Penulisan dokumen, penggunaan SHALL/MUST, dan pemeriksaan tampilan PDF tidak membuktikan efektivitas metodologi, keamanan aplikasi, kompatibilitas library, atau penerimaan pihak berwenang. Beberapa dokumen sebenarnya sudah memasukkan disclaimer yang benar; disclaimer itu perlu menjadi batas konsisten seluruh paket.

Audit ini mencatat **16 temuan**: 9 prioritas tinggi, 6 sedang, dan 1 rendah. Prioritas adalah urutan koreksi dokumen, **bukan CVSS, skor keamanan aplikasi, atau persentase halusinasi**. Temuan dibedakan antara kesalahan yang terlihat langsung dan kesenjangan/keputusan yang masih perlu dikunci.

## 1. Cakupan dan keterbatasan pemeriksaan

Diperiksa 23 DOCX utama, 21 companion Markdown, dan 26 representasi PDF untuk judul yang sama. Satu PDF utama per DOCX berjumlah 576 halaman. Framework original dan Expanded dihitung sebagai dua dokumen karena keduanya masih ada. `AML-brainstrom.md` diperiksa sebagai bahan historis tambahan.

Seluruh teks paragraf dan tabel DOCX diekstrak untuk pemeriksaan registry, jumlah ID, enum, istilah, referensi, dan hubungan antarbagian. Pembacaan mendalam difokuskan pada keputusan yang berpengaruh pada keselamatan, data, audit, scope MVP, dan kontrak engineer. PDF dicocokkan secara tekstual; halaman penting API, Data Model dan beberapa tabel dipilih untuk pemeriksaan visual. Ini **bukan pemeriksaan visual ulang setiap halaman PDF**.

Sumber primer eksternal utama dibuka atau dicari ulang. Keberadaan publikasi diverifikasi terpisah dari dukungan terhadap kalimat tertentu. Pemeriksaan ini tidak mengklaim telah memverifikasi setiap kalimat, setiap indikator tipologi, seluruh hukum yang berlaku, maupun setiap versi library. Tidak ada aplikasi, repository implementasi CS-AML, hasil CI, atau Storybook berjalan yang diuji. Karena itu tidak diberikan angka seperti “95% akurat” atau “tingkat halusinasi 2%”.

**Cara membaca bukti:** kode `Pxxxx` di register adalah nomor record hasil ekstraksi berurutan (paragraf atau baris tabel), bukan nomor halaman cetak. Nama file dan judul section disertakan agar temuan dapat dicari pada sumber asli. Hash file tersedia di register JSON pendamping.

## 2. Hal yang terkonfirmasi dan layak dipertahankan

FATF Recommendations amended June 2026, Wolfsberg RBA June 2026, dan publikasi PPATK mengenai Klinik Dumas pada November 2025 terverifikasi pada sumber resmi [S01-S03]. Jadi menyatakan semua rujukan 2026 sebagai karangan adalah keliru. Dukungan informasi CSO kepada otoritas dan kehati-hatian terhadap generalisasi risiko NPO juga mempunyai sumber yang relevan [S03,S07]. Namun sumber tersebut tidak mengesahkan taxonomy, level conformance, atau arsitektur aplikasi CS-AML.

Pilihan desain berikut konsisten secara konseptual dan tidak ditemukan alasan untuk dibuang: case sebagai konteks; canonical record berbeda dari search/graph projection; evidence asli berbeda dari derivative; entity merge harus bisa ditinjau; typology match bukan bukti kejahatan; unknown tidak diubah menjadi nol; keputusan pengungkapan berdampak tinggi memerlukan review manusia. Ini penilaian desain, bukan hasil pengujian implementasi.

| Katalog | Hasil hitung dari isi dokumen | Catatan |
|---|---:|---|
| Product features | 87 | 54 P0, 26 P1, 7 P2; jumlah benar. |
| Screen IDs | 53 | 50 layar kerja dan 3 system-state screens; bukan 50 total. |
| Shared component IDs | 65 | Jumlah benar; bukan 65 komponen yang terbukti sudah diimplementasikan. |
| Typology IDs | 20 | Jumlah benar; taxonomy adalah katalog CS-AML, bukan daftar resmi FATF berisi tepat 20 entri. |

## 3. Ringkasan temuan

| ID | Prioritas | Kategori | Temuan |
|---|---|---|---|
| A01 | Tinggi | Klaim kesiapan / tata kelola | Normative baseline tidak sama dengan baseline yang telah divalidasi |
| A02 | Tinggi | Ketidakmutakhiran rekomendasi teknologi | MinIO Community direkomendasikan tanpa caveat maintenance |
| A03 | Sedang | Dependensi / lisensi | Redis 7.x terlalu luas untuk baseline open-source |
| A04 | Tinggi | Kontradiksi teknis | If-Match gagal: 409 pada contoh, 412 pada tabel |
| A05 | Tinggi | Traceability drift | F-ASM-003 berganti arti pada SRS |
| A06 | Sedang | Scope drift | Enam template pada SRS, tiga pada breakdown MVP |
| A07 | Sedang | Tabrakan identifier | Namespace CAP-10 dipakai untuk capability berbeda |
| A08 | Tinggi | Ketidakjelasan policy model | Klasifikasi informasi belum mempunyai mapping lintas dokumen |
| A09 | Tinggi | Kontrak data / serialisasi | Flow class dan confidence tidak konsisten |
| A10 | Tinggi | Kelengkapan handoff | Claim dan Fact belum punya jalur implementasi eksplisit yang lengkap |
| A11 | Tinggi | Kelengkapan kontrak implementasi | API masih baseline naratif, belum kontrak executable penuh |
| A12 | Sedang | Document control | Banyak Markdown adalah companion, bukan salinan penuh |
| A13 | Sedang | Sumber / verifikasi metodologis | Referensi nyata belum selalu mempunyai dukungan per klaim |
| A14 | Sedang | Kesalahan contoh / visual | DIRECTOR_OF terbalik pada contoh Data Model |
| A15 | Rendah | Inkonsistensi pemetaan UI | Case Register memakai pattern detail |
| A16 | Tinggi | Governance release / kontradiksi keselamatan | Pengecualian release bisa terbaca terlalu luas |

## 4. Temuan rinci dan koreksi yang dibutuhkan

### A01 — Normative baseline tidak sama dengan baseline yang telah divalidasi

**Prioritas:** Tinggi. **Jenis:** Klaim kesiapan / tata kelola. **Keyakinan atas temuan:** Tinggi.

Sejumlah dokumen dan jawaban pengantar memakai istilah approved, implementable, resmi, atau siap engineering handoff. Paket berisi persyaratan, template, dan kriteria penerimaan; tidak berisi bukti adopsi bernama, hasil uji implementasi CS-AML, atau audit independen yang memenuhi kriteria itu. Ini terutama koreksi atas tingkat kepastian jawaban saya sebelumnya. Bukan berarti semua dokumen mengaku sebagai standar FATF: parent framework justru memuat disclaimer yang benar.

**Bukti yang diperiksa:**
- `CS-AML_Framework_v0.1_Expanded.docx`, 40. Annex H — External Standards Mapping, `P0791`: The mapping is informative. Compliance with CS-AML does not imply compliance with FATF Recommendations, national AML law, regulated-entity obligations, or professional standards.
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, Front matter, `P0004`: Document statusNormative software baseline for MVP 0.1 implementation. This SRS translates the approved PRD, Product & Feature Specification, Data Model Specification, Control Implementation Guide, Investigation Methodology, and Technology Architecture into testable software requirements.
- `CS-AML_Component_Inventory_and_Storybook_Implementation_Specification_v0.1.docx`, 18. Security and Privacy in Storybook, `P0283`: CISB-082 — Authorization behavior MAY be simulated through safe decorators/fixtures, but Storybook SHALL NOT be treated as proof of server-side authorization.

**Dampak:** Tim dapat menyamakan selesai menulis dengan selesai memvalidasi. Hal ini membuat keputusan domain dan keamanan yang masih terbuka terlihat sudah disahkan.

**Koreksi yang disarankan:** Gunakan status Draft for Review atau Proposed Internal Baseline sampai ada owner, tanggal keputusan, reviewer, dan evidence penerimaan. Bedakan specification, implementation, dan verified implementation di register dokumen. Pertahankan disclaimer bahwa CS-AML bukan standar atau sertifikasi eksternal.

**Verifikasi setelah koreksi — belum dijalankan:** Periksa bahwa setiap klaim approved/conformant mempunyai record persetujuan atau hasil uji yang dirujuk; jika tidak, ubah statusnya. Tidak diperlukan dokumen teori baru.

### A02 — MinIO Community direkomendasikan tanpa caveat maintenance

**Prioritas:** Tinggi. **Jenis:** Ketidakmutakhiran rekomendasi teknologi. **Keyakinan atas temuan:** Tinggi.

Technical Stack menggunakan MinIO sebagai reference object store dan menampilkan layanan itu dalam deployment. Pada tanggal audit, repositori upstream minio/minio telah diarsipkan sejak 25 April 2026 dan README menyatakan tidak lagi dipelihara. Kapabilitas S3-compatible tetap masuk akal; rekomendasi default produk perlu dievaluasi ulang.

**Bukti yang diperiksa:**
- `CS-AML_Technical_Stack_and_Repository_Specification_v0.1.docx`, 3. MVP Reference Stack, `P0038`: Object storage | S3-compatible store (MinIO reference) | Original/derivative evidence objects, versioning | Required capability
- `CS-AML_Technical_Stack_and_Repository_Specification_v0.1.docx`, 18. Container and Runtime Topology, `P0150`: compose project (reference deployment)├── nginx├── web          (Django/Gunicorn)├── worker       (Celery)├── scheduler    (Celery beat, only if required)├── postgres├── redis├── object-store (MinIO reference / external S3 supported)└── telemetry    (deployment-specific collectors)External or separately managed:└── Keycloak / OIDC IdP

**Dampak:** Pemilihan penyimpanan evidence dapat dimulai dari komponen dengan jalur maintenance yang tidak lagi sesuai asumsi. Ini tidak membuktikan instance pengguna rentan; tidak ada instance yang diuji.

**Koreksi yang disarankan:** Pertahankan requirement S3-compatible, tetapi jangan mengunci MinIO Community sebagai default production tanpa keputusan risiko/maintenance. Evaluasi penyedia/implementasi yang dipelihara, versi, lisensi, migrasi, dan dukungan. Bedakan MinIO Community dengan AIStor atau produk lain.

**Verifikasi setelah koreksi — belum dijalankan:** ADR penyimpanan memuat rilis yang dipilih, status maintenance, jalur patch, bukti compatibility test, dan restore test.

**Sumber eksternal:** [S04].

### A03 — Redis 7.x terlalu luas untuk baseline open-source

**Prioritas:** Sedang. **Jenis:** Dependensi / lisensi. **Keyakinan atas temuan:** Tinggi.

Redis 7.x dijadikan required reference. Rentang ini mencakup batas lisensi yang berbeda: versi 7.2 dan 7.4 tidak mempunyai pilihan lisensi yang sama. Ini bukan library fiktif, tetapi spesifikasi versi dan lisensinya belum cukup pasti.

**Bukti yang diperiksa:**
- `CS-AML_Technical_Stack_and_Repository_Specification_v0.1.docx`, 3. MVP Reference Stack, `P0037`: Broker/cache | Redis 7.x | Task broker, bounded cache, transient coordination | Required reference

**Dampak:** Engineer dapat memilih minor release yang memenuhi teks spesifikasi tetapi tidak memenuhi keputusan lisensi organisasi.

**Koreksi yang disarankan:** Tetapkan release line dan pilihan lisensi eksplisit; simpan dalam dependency manifest/ADR. Jangan mengartikan semua 7.x sebagai BSD atau menyamakan source-available dengan open-source tanpa memeriksa lisensinya.

**Verifikasi setelah koreksi — belum dijalankan:** Dependency manifest, image digest, SBOM dan catatan lisensi merujuk versi yang sama.

**Sumber eksternal:** [S05].

### A04 — If-Match gagal: 409 pada contoh, 412 pada tabel

**Prioritas:** Tinggi. **Jenis:** Kontradiksi teknis. **Keyakinan atas temuan:** Tinggi.

API section 9 menyebut 412 untuk kegagalan If-Match/ETag, tetapi section 10 menunjukkan If-Match: "7" terhadap versi 8 menghasilkan 409 VERSION_CONFLICT. Dua engineer dapat menerapkan perilaku berbeda berdasarkan dokumen yang sama.

**Bukti yang diperiksa:**
- `CS-AML_API_Specification_v0.1.docx`, 9. Error Model, `P0086`: 412 | PRECONDITION_FAILED | If-Match/ETag failed.
- `CS-AML_API_Specification_v0.1.docx`, 10. Concurrency and Record Versioning, `P0098`: PATCH /api/v1/assessments/{id}If-Match: "7"{ "record_version": 7, "judgement": "..." }→ 409 VERSION_CONFLICT if current version is 8

**Dampak:** Frontend conflict handling, generated client, dan contract test tidak memiliki satu expected response.

**Koreksi yang disarankan:** Untuk penolakan stale HTTP If-Match tetapkan 412 PRECONDITION_FAILED. Cadangkan 409 untuk konflik workflow atau body-version aplikasi sesuai kontrak. Definisikan urutan pemeriksaan jika body dan header sama-sama ada. RFC melarang penerapan method saat If-Match false dan mempunyai pengecualian untuk request yang aksinya sudah terpenuhi; kontrak harus menangani hal tersebut secara konsisten.

**Verifikasi setelah koreksi — belum dijalankan:** Contract tests: stale header -> 412; konflik business state -> 409; tidak ada silent overwrite. Contoh, tabel, frontend error mapping dan OpenAPI harus sama.

**Sumber eksternal:** [S06].

### A05 — F-ASM-003 berganti arti pada SRS

**Prioritas:** Tinggi. **Jenis:** Traceability drift. **Keyakinan atas temuan:** Tinggi.

Feature catalogue memberi F-ASM-003 arti Disconfirming search record. SRS-FR-ASM-003 berjudul Backward traceability tetapi dipetakan ke F-ASM-003. Kedua kebutuhan penting, namun tidak ekuivalen.

**Bukti yang diperiksa:**
- `CS-AML_Product_and_Feature_Specification_v0.1.docx`, CAP-09 — Hypothesis & Assessment, `P0171`: F-ASM-003 | Disconfirming search record | P0 | Reviewer | Document what was done to search for evidence that weakens adverse findings. | Review,Hypothesis | HYP-02,QUA-01 | High-impact product cannot pass review if no disconfirmation record/rationale.
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, SRS-FR-ASM-003 — Backward traceability, `P0327`: SRS-FR-ASM-003 — Backward traceability
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, SRS-FR-ASM-003 — Backward traceability, `P0328`: Requirement | The system SHALL allow a reviewer to traverse an assessment backward through hypotheses/indicators/facts/evidence/sources.
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, SRS-FR-ASM-003 — Backward traceability, `P0332`: Traceability | F-ASM-003

**Dampak:** Checklist coverage dapat tampak lengkap walaupun kewajiban mencari bukti yang melemahkan hipotesis belum diimplementasikan atau dites.

**Koreksi yang disarankan:** Pertahankan stable meaning F-ASM-003; buat requirement SRS yang secara eksplisit menguji disconfirming search. Beri backward traceability ID tersendiri atau mapping lain yang benar. Jangan mengganti arti ID lama diam-diam.

**Verifikasi setelah koreksi — belum dijalankan:** Satu test menolak review adverse/high-impact tanpa catatan disconfirmation yang diperlukan; test terpisah menelusuri assessment ke evidence. Traceability membedakan kedua test.

### A06 — Enam template pada SRS, tiga pada breakdown MVP

**Prioritas:** Sedang. **Jenis:** Scope drift. **Keyakinan atas temuan:** Tinggi.

Feature catalogue dan SRS mensyaratkan enam template: Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, Case Report. ST-E8-01 pada engineering breakdown hanya merinci tiga. Dalam paket yang diperiksa tidak ada perubahan scope eksplisit yang menghubungkan pengurangan ini.

**Bukti yang diperiksa:**
- `CS-AML_Product_and_Feature_Specification_v0.1.docx`, CAP-11 — Intelligence Products & Review, `P0182`: F-PRD-001 | Intelligence product templates | P0 | Analyst | Generate Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package and Case Report. | IntelligenceProduct | ASM-01,DIS-01 | Product embeds version, classification, author/reviewer and evidence index.
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, SRS-FR-PRD-001 — Product templates, `P0354`: Requirement | The system SHALL generate Financial Intelligence Note, Entity Profile, Asset Profile, Network Analysis, Referral Package, and Case Report from canonical objects.
- `CS-AML_MVP_Engineering_Breakdown_v0.1.docx`, ST-E8-01 — Intelligence product templates, `P0440`: Templates: Financial Intelligence Note, Referral Package, Case Report

**Dampak:** MVP dapat dinyatakan selesai berdasarkan backlog, tetapi belum memenuhi SRS yang dijadikan acuan penerimaan.

**Koreksi yang disarankan:** Putuskan scope enam atau tiga melalui change record. Bila tiga dipilih, ubah prioritas/template scope pada Feature, PRD, SRS dan acceptance matrix; jangan sekadar mengubah backlog.

**Verifikasi setelah koreksi — belum dijalankan:** Jumlah dan nama template sama pada requirement, backlog, screen create-product dan acceptance tests.

### A07 — Namespace CAP-10 dipakai untuk capability berbeda

**Prioritas:** Sedang. **Jenis:** Tabrakan identifier. **Keyakinan atas temuan:** Tinggi.

Technology Architecture menggunakan CAP-10 untuk Hypothesis & assessment. Product & Feature Specification memakai CAP-10 untuk Search / Graph / Analytics. Perubahan grouping boleh dilakukan, tetapi penggunaan ID sama tanpa namespace atau crosswalk tidak aman untuk traceability otomatis.

**Bukti yang diperiksa:**
- `CS-AML_Technology_Architecture_v0.1.docx`, 4. Capability Architecture, `P0106`: CAP-10 | Hypothesis & assessment | Competing hypotheses, support/contradiction, gaps, confidence
- `CS-AML_Product_and_Feature_Specification_v0.1.docx`, 7. Product Capability Map, `P0093`: CAP-10 | Search / Graph / Analytics | Full-text, faceted search, graph navigation, paths, clusters, network analytics

**Dampak:** Pemetaan capability ke feature/story dapat menunjuk fungsi yang salah meskipun identifier tampak cocok.

**Koreksi yang disarankan:** Pilih satu capability registry bersama atau pisahkan namespace TA-CAP dan PROD-CAP dengan crosswalk eksplisit. Bekukan makna ID saat dijadikan referensi lintas dokumen.

**Verifikasi setelah koreksi — belum dijalankan:** Validator menolak satu global ID dengan lebih dari satu makna; migration/crosswalk mencakup semua referensi CAP lama.

### A08 — Klasifikasi informasi belum mempunyai mapping lintas dokumen

**Prioritas:** Tinggi. **Jenis:** Ketidakjelasan policy model. **Keyakinan atas temuan:** Tinggi.

Framework Expanded menyarankan PUBLIC, INTERNAL, RESTRICTED, HIGHLY RESTRICTED. Data Model memakai PUBLIC, INTERNAL, SENSITIVE, RESTRICTED, SOURCE-PROTECTED. Keduanya boleh sebagai desain lokal, tetapi mapping dan aturan konflik belum dikunci. Source protection juga bukan otomatis sekadar level tertinggi dalam satu urutan.

**Bukti yang diperiksa:**
- `CS-AML_Framework_v0.1_Expanded.docx`, 6.4 Case sensitivity, `P0208`: Public: information safe for broad release;
- `CS-AML_Framework_v0.1_Expanded.docx`, 6.4 Case sensitivity, `P0209`: Internal: routine investigative material;
- `CS-AML_Framework_v0.1_Expanded.docx`, 6.4 Case sensitivity, `P0210`: Restricted: sensitive personal, legal, partner, or unpublished material;
- `CS-AML_Framework_v0.1_Expanded.docx`, 6.4 Case sensitivity, `P0211`: Highly Restricted: source-identifying information, severe physical-security risk, legally privileged material, or comparable sensitivity.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 16. Privacy, Classification, and Access-Control Metadata, `P0424`: PUBLIC | Suitable for public release after normal review.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 16. Privacy, Classification, and Access-Control Metadata, `P0425`: INTERNAL | Routine internal operational information.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 16. Privacy, Classification, and Access-Control Metadata, `P0426`: SENSITIVE | Could create privacy, reputational, safety, or investigative harm if disclosed.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 16. Privacy, Classification, and Access-Control Metadata, `P0427`: RESTRICTED | High-risk information requiring named-role or case-specific authorization.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 16. Privacy, Classification, and Access-Control Metadata, `P0428`: SOURCE-PROTECTED | Information whose disclosure could identify or endanger a confidential source.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 16. Privacy, Classification, and Access-Control Metadata, `P0429`: Access labels MAY add purpose, jurisdiction, source-protection, embargo, legal-review, or compartment restrictions. Implementations SHALL enforce the most restrictive applicable label.

**Dampak:** Authorization, pewarisan label, export, dan retention dapat berbeda antar-engineer. Ini adalah risiko spesifikasi, bukan bukti bypass pada aplikasi yang belum diuji.

**Koreksi yang disarankan:** Tetapkan model klasifikasi yang authoritative. Pisahkan level sensitivitas dari compartment/source-protection bila dipilih. Buat mapping eksplisit untuk label lama; jangan otomatis mengubah HIGHLY RESTRICTED menjadi SOURCE-PROTECTED.

**Verifikasi setelah koreksi — belum dijalankan:** Policy tests mencakup case/entity/evidence lintas label, sumber terlindungi, export turunan, dan perubahan akses. Unknown label fail-closed sesuai kontrak.

### A09 — Flow class dan confidence tidak konsisten

**Prioritas:** Tinggi. **Jenis:** Kontrak data / serialisasi. **Keyakinan atas temuan:** Tinggi.

Data Model mewajibkan kelas flow uppercase pada teks, tetapi tabel field, Annex A dan contoh JSON menggunakan lowercase. SRS/API menggunakan uppercase. Data Model confidence.level hanya low/moderate/high, sementara SRS dan Design System mempunyai Insufficient Basis. Ini memerlukan satu schema wire dan mapping, bukan sekadar penyamaan label visual.

**Bukti yang diperiksa:**
- `CS-AML_Data_Model_Specification_v0.1.docx`, 11. Value-Flow Model, `P0285`: Mandatory distinction / Every ValueFlow SHALL carry an epistemic class: DIRECT, DOCUMENTED, RECONSTRUCTED, or HYPOTHETICAL. Systems SHALL preserve this distinction in storage, APIs, exports, and visualizations.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 11.1 ValueFlow, `P0289`: flow_class | enum | Y | 1 | direct, documented, reconstructed, hypothetical
- `CS-AML_Data_Model_Specification_v0.1.docx`, 14.1 Confidence, `P0384`: level | enum | Y | 1 | low, moderate, high
- `CS-AML_Data_Model_Specification_v0.1.docx`, Annex A. Controlled Enumerations (Baseline), `P0525`: flow_class | direct, documented, reconstructed, hypothetical
- `CS-AML_Data_Model_Specification_v0.1.docx`, Annex A. Controlled Enumerations (Baseline), `P0526`: confidence.level | low, moderate, high
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, SRS-FR-ASM-002 — Confidence model, `P0322`: Requirement | The system SHALL support High, Moderate, Low, and Insufficient Basis (or configured equivalent) with rationale.
- `CS-AML_UI_Design_System_Specification_v0.1.docx`, 10.2 Confidence, `P0166`: Insufficient basis | Neutral warning-style label | Must not look like adverse result

**Dampak:** Enum validation dapat gagal; keadaan insufficient-basis dapat hilang atau terpaksa diubah menjadi low, padahal maknanya berbeda.

**Koreksi yang disarankan:** Bekukan machine enum dan versioning dalam schema. Tetapkan bagaimana Insufficient Basis direpresentasikan, termasuk null/unknown jika relevan. Pisahkan label terjemahan dari nilai wire. Generate referensi enum dokumen dari registry yang sama.

**Verifikasi setelah koreksi — belum dijalankan:** Round-trip semua kelas dan confidence melalui DB/API/UI/export. Test menolak normalisasi yang menaikkan kepastian; unknown tidak menjadi low atau zero tanpa aturan eksplisit.

### A10 — Claim dan Fact belum punya jalur implementasi eksplisit yang lengkap

**Prioritas:** Tinggi. **Jenis:** Kelengkapan handoff. **Keyakinan atas temuan:** Tinggi.

Data Model mendefinisikan Claim dan Fact, dan keduanya pusat rantai analitis. Breakdown menyebut link extract ke claims/facts, tetapi tidak merinci lifecycle verifikasi/promosi sebagai story tersendiri. API mencantumkan banyak endpoint namun tidak menjelaskan kontrak create/read/update/verify/supersede untuk Claim/Fact, baik sebagai resource sendiri maupun embedded command. Tidak disimpulkan bahwa implementasi mustahil; kontraknya belum tertulis.

**Bukti yang diperiksa:**
- `CS-AML_Data_Model_Specification_v0.1.docx`, 7.4 Claim, `P0159`: 7.4 Claim
- `CS-AML_Data_Model_Specification_v0.1.docx`, 7.4 Claim, `P0160`: Represents a proposition asserted by a source or person. A Claim is not automatically accepted as fact.
- `CS-AML_Data_Model_Specification_v0.1.docx`, 7.5 Fact, `P0172`: 7.5 Fact
- `CS-AML_Data_Model_Specification_v0.1.docx`, 7.5 Fact, `P0178`: fact_status | enum | Y | 1 | provisional, established, superseded, disputed
- `CS-AML_Data_Model_Specification_v0.1.docx`, Normative rules:, `P0182`: Fact status SHALL be revisable when materially new evidence emerges.
- `CS-AML_MVP_Engineering_Breakdown_v0.1.docx`, ST-E3-04 — Evidence extracts and citations, `P0212`: Link extract to claims/facts
- `CS-AML_MVP_Engineering_Breakdown_v0.1.docx`, ST-E8-02 — Evidence index generation, `P0448`: Generate index from linked facts/assessments

**Dampak:** Tim dapat kembali menyimpan klaim/fakta dalam notes atau mempromosikan extract menjadi fact tanpa keputusan yang dapat direview.

**Koreksi yang disarankan:** Tambahkan requirement, task, endpoint atau command eksplisit untuk provenance-backed claim/fact lifecycle. Tetapkan siapa boleh memverifikasi, apa bukti keputusan, dan bagaimana koreksi mempengaruhi assessment/product terdahulu.

**Verifikasi setelah koreksi — belum dijalankan:** Pilot: source claim dibuat; diterima sementara; dibantah; fact berubah disputed/superseded; produk terdampak ditandai tanpa kehilangan riwayat.

### A11 — API masih baseline naratif, belum kontrak executable penuh

**Prioritas:** Tinggi. **Jenis:** Kelengkapan kontrak implementasi. **Keyakinan atas temuan:** Tinggi.

Dokumen API berisi konvensi dan endpoint catalogue yang berguna, tetapi belum menyediakan schema request/response lengkap per operasi dan artefak OpenAPI. OIDC session/bearer masih alternatif. Idempotency memuat REQUIRED/recommended tanpa scope key, TTL, payload conflict dan race semantics yang terkunci. Sejumlah aksi seperti task update, komentar review dan lifecycle jobs masih perlu kontrak rinci. Hal ini harus disebut gap, bukan dianggap fitur sudah berfungsi.

**Bukti yang diperiksa:**
- `CS-AML_API_Specification_v0.1.docx`, 28. API Schema and OpenAPI Requirements, `P0273`: An OpenAPI 3.1-equivalent schema SHOULD be generated/published for v1.
- `CS-AML_API_Specification_v0.1.docx`, 4. Authentication and Principal Context, `P0041`: Authentication | OIDC-authenticated session/bearer mechanism approved by security architecture.
- `CS-AML_API_Specification_v0.1.docx`, 11. Idempotency, `P0103`: Evidence ingest finalization | Idempotency key REQUIRED/recommended to avoid duplicate completion after retry.

**Dampak:** Backend/frontend belum dapat sepenuhnya bekerja independen dengan generated client dan contract tests yang deterministik.

**Koreksi yang disarankan:** Lengkapi OpenAPI/schema P0 dari keputusan domain yang sudah diselaraskan. Kunci model login browser, respons error, nullability, pagination envelope, upload/job/approval preconditions dan policy response. Gunakan mock API berbasis schema; bukan menambah daftar endpoint generik saja.

**Verifikasi setelah koreksi — belum dijalankan:** Lint/validate OpenAPI, generated TypeScript, request/response contract suite, concurrent mutation tests, serta negative authorization tests berjalan terhadap implementation atau contract mock yang jelas diberi label.

### A12 — Banyak Markdown adalah companion, bukan salinan penuh

**Prioritas:** Sedang. **Jenis:** Document control. **Keyakinan atas temuan:** Tinggi.

Terdapat 21 companion Markdown untuk 23 DOCX. SRS Markdown sekitar 148 kata, API sekitar 171, Data Model sekitar 405; beberapa berisi See normative DOCX/PDF for full requirements. Ini bukan kesalahan karena banyak memang disebut companion. Kesalahannya terjadi jika file ringkas itu dipakai seolah seluruh specification atau dianggap setara dengan DOCX saat membuat dokumen turunan.

**Bukti yang diperiksa:**
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.md`, Seluruh file, `MD`: Requirement families dan MVP release gate; tidak memuat seluruh requirement rinci DOCX.
- `CS-AML_Data_Model_Specification_v0.1.md`, Bagian-bagian field model, `MD`: See normative DOCX/PDF for full field-level requirements.

**Dampak:** Detail guardrails dan acceptance criteria dapat hilang pada handoff atau penggunaan coding agent; koreksi pada DOCX belum tentu sampai ke companion.

**Koreksi yang disarankan:** Pilih satu canonical source. Generate DOCX/PDF/MD penuh dari sumber yang sama, atau beri nama *.summary.md dan larang penggunaannya sebagai satu-satunya input implementasi. Manifest menyimpan hashes, versi dan status legacy/current.

**Verifikasi setelah koreksi — belum dijalankan:** CI dokumentasi membandingkan ID requirement dan enum pada semua format; companion jelas dikecualikan dari klaim full specification.

### A13 — Referensi nyata belum selalu mempunyai dukungan per klaim

**Prioritas:** Sedang. **Jenis:** Sumber / verifikasi metodologis. **Keyakinan atas temuan:** Tinggi.

FATF, Wolfsberg dan PPATK yang utama terverifikasi. Namun beberapa entri katalog hanya menunjuk FATF Methods and Trends atau PPATK risk assessments tanpa halaman/section/versi spesifik. Link UNODC yang dikutip terindeks di domain resmi, tetapi pembukaan PDF penuh gagal pada alat audit, sehingga wording dan lokasi halaman klaim spesifik belum dikukuhkan. Kegagalan akses tidak dinyatakan sebagai sumber palsu.

**Bukti yang diperiksa:**
- `CS-AML_Typology_Catalogue_v0.1.docx`, Primary reference lineage, `P0239`: FATF Methods and Trends
- `CS-AML_Typology_Catalogue_v0.1.docx`, Primary reference lineage, `P0423`: FATF Methods and Trends case studies
- `CS-AML_Framework_v0.1_Expanded.docx`, 42. Annex J — Normative and Informative References, `P0820`: 4. UNODC, Civil Society Guide to the United Nations Convention against Corruption, including civil-society roles in asset tracing, public information, financial investigation, forensic auditing, and legal analysis.  

**Dampak:** Daftar pustaka yang valid dapat memberi kesan setiap indikator, ambang penilaian dan kewajiban lokal berasal langsung dari otoritas, padahal sebagian adalah desain CS-AML.

**Koreksi yang disarankan:** Buat pemetaan klaim/indikator -> sumber -> section/halaman -> catatan adaptasi. Labeli keputusan lokal, contoh hipotetis, dan klaim belum terverifikasi. Untuk sumber yang tidak dapat dibuka, simpan status pending-verification dan jangan menguatkan klaim.

**Verifikasi setelah koreksi — belum dijalankan:** Reviewer dapat menelusuri tiap klaim eksternal material tanpa menebak dokumen atau paragraf; sampel indikator dinilai oleh investigator/AML specialist.

**Sumber eksternal:** [S01], [S02], [S03], [S10].

### A14 — DIRECTOR_OF terbalik pada contoh Data Model

**Prioritas:** Sedang. **Jenis:** Kesalahan contoh / visual. **Keyakinan atas temuan:** Tinggi.

Section 19 benar menampilkan Person -> DIRECTOR_OF -> Organization. Annex D justru memulai hubungan Company A --DIRECTOR_OF--> Person B. Render PDF juga membuat susunan dua kolom contoh sulit dibaca. Ini kesalahan contoh yang nyata; skema relasi yang benar ada di bagian lain.

**Bukti yang diperiksa:**
- `CS-AML_Data_Model_Specification_v0.1.docx`, 19. Canonical Graph Mapping, `P0470`: (:Person)-[:DIRECTOR_OF {relationship_id,...}]->(:Organization)(:Person)-[:BENEFICIAL_OWNER_OF {ownership_interest_id,...}]->(:Organization)(:Organization)-[:AWARDED_CONTRACT]->(:Contract)(:Organization)-[:ACQUIRED]->(:Asset)(:Entity)-[:VALUE_FLOW {value_flow_id, flow_class,...}]->(:Entity)
- `CS-AML_Data_Model_Specification_v0.1.docx`, Annex D. Example Analytical Chain, `P0554`: SOURCE  Government procurement portal       |       vEVIDENCE  Contract award record       |       vFACT  Company A received Contract X on 12 May       |       +---------------------------+       |                           |       v                           vENTITY / RELATIONSHIP          EVENT  Company A --DIRECTOR_OF-->   Contract award  Person B       |       vINDICATOR  Related entity acquired property shortly after award       |       vHYPOTHESIS  Value may have been diverted through related entity       |       vVALUE FLOW (RECONSTRUCTED)  Contract -> Company A -> related entity -> asset       |       vASSESSMENT  Pattern is consistent with procurement-value diversion;  settlement route remains unknown.       |       vINTELLIGENC...

**Dampak:** Contoh yang dipakai sebagai fixture atau petunjuk graph dapat menghasilkan edge terbalik dan salah arti.

**Koreksi yang disarankan:** Perbaiki contoh menjadi Person B --DIRECTOR_OF--> Company A, atau gunakan inverse relation yang eksplisit. Rapikan diagram menjadi bentuk yang tidak menukar endpoint dengan Event.

**Verifikasi setelah koreksi — belum dijalankan:** Validator domain/range relasi menguji contoh; review visual halaman contoh memastikan arah dan endpoint tidak ambigu.

### A15 — Case Register memakai pattern detail

**Prioritas:** Rendah. **Jenis:** Inkonsistensi pemetaan UI. **Keyakinan atas temuan:** Tinggi.

Wireframe section 3 mendefinisikan WF-PAT-01 sebagai Register/List dan WF-PAT-02 sebagai Canonical Object Detail. Mapping SCR-CASE-001 Case Register memakai WF-PAT-02. Screen yang sama pada HiFi dijelaskan sebagai register/list.

**Bukti yang diperiksa:**
- `CS-AML_Wireframe_Specification_v0.1.docx`, 4. Wireframe Pattern Library, `P0027`: WF-PAT-01 | Register/List | Header + filters + sortable result list/table + empty state + primary create action.
- `CS-AML_Wireframe_Specification_v0.1.docx`, 4. Wireframe Pattern Library, `P0028`: WF-PAT-02 | Canonical Object Detail | Context header + summary block + local tabs + main object facts + provenance rail + backlinks.
- `CS-AML_Wireframe_Specification_v0.1.docx`, 5. Screen-to-Wireframe Mapping, `P0037`: SCR-CASE-001 | Case Register | WF-PAT-02 | default, empty, no-access, filtered

**Dampak:** Perbedaan pola dapat menyebabkan desain/frontend mengikuti template yang salah.

**Koreksi yang disarankan:** Ubah mapping Case Register ke WF-PAT-01 atau dokumentasikan pengecualian yang benar-benar disengaja. Tidak perlu membuat screen ID baru.

**Verifikasi setelah koreksi — belum dijalankan:** Screen -> pattern mapping tervalidasi lintas inventory, wireframe, HiFi dan component composition.

### A16 — Pengecualian release bisa terbaca terlalu luas

**Prioritas:** Tinggi. **Jenis:** Governance release / kontradiksi keselamatan. **Keyakinan atas temuan:** Tinggi.

Sprint Plan menyatakan unresolved high-severity security/data-integrity defects memblokir promotion. Namun tabel High memasukkan export without approval, flow-class confusion dan broken audit history, lalu mengizinkan fixed or formally waived. Sebagian adalah pelanggaran invariant inti, bukan kekurangan kosmetik. Teks perlu membedakan waiver aman dari kondisi yang tidak boleh dirilis.

**Bukti yang diperiksa:**
- `CS-AML_Sprint_and_Milestone_Plan_v0.1.docx`, 1.1 Planning principles, `P0018`: Unresolved high-severity security or data-integrity defects block promotion to the next release milestone.
- `CS-AML_Sprint_and_Milestone_Plan_v0.1.docx`, 7.2 Release-blocking defect classes, `P0304`: Critical | Authorization bypass; source identity exposure; evidence corruption; unrecoverable DB/evidence mismatch | Immediate block
- `CS-AML_Sprint_and_Milestone_Plan_v0.1.docx`, 7.2 Release-blocking defect classes, `P0305`: High | Incorrect merge/unmerge; direct/reconstructed flow confusion; export without approval; broken audit history | Block M4 until fixed or formally waived by accountable authority
- `CS-AML_Software_Requirements_Specification_SRS_v0.1.docx`, SRS-FR-DIS-001 — Dissemination approval, `P0378`: Requirement | The system SHALL block external export until required handling classification, recipient, purpose, and approval are recorded.

**Dampak:** Keputusan administratif dapat terlihat membolehkan release dengan kontrol pengungkapan atau integritas analitis yang gagal.

**Koreksi yang disarankan:** Definisikan non-waivable invariants: akses tanpa izin, exposure sumber, hilangnya provenance/integrity kritis, certainty promotion, approval bypass. Untuk fitur berbahaya yang dinonaktifkan sebagai mitigasi, bukti non-reachability harus ada; ini bukan membiarkan cacat tetap dapat digunakan.

**Verifikasi setelah koreksi — belum dijalankan:** Uji bahwa release gate gagal saat invariant dilanggar. Exception hanya lulus untuk batasan yang tidak mengaktifkan jalur bahaya dan mempunyai compensating control teruji.

## 5. Catatan desain yang perlu keputusan, bukan tuduhan halusinasi

### N01 — Konvensi CS-AML adalah desain lokal, bukan otomatis standar internasional

G0-G6, A-F/1-6, keluarga 20 tipologi, empat kelas value flow, maturity levels, dan pemisahan state UI dapat berguna. Keputusan-keputusan ini perlu rationale, owner, versioning dan uji penerapan. Tidak ada alasan menyebutnya halusinasi hanya karena baru kita desain; yang tidak boleh adalah mengatribusikannya sebagai kewajiban FATF tanpa sumber.

### N02 — Rantai analitis jangan dipaksakan menjadi mekanisme kenaikan kepastian

Parent Expanded mengatakan tidak ada tahap yang boleh dilewati pada kesimpulan material. Data Model Assessment mengizinkan supporting_refs langsung ke facts/indicators/evidence. Selaraskan ini sebagai provenance graph dan workflow yang bisa berulang, bukan mesin yang menjadikan setiap claim pasti fact atau memaksa setiap assessment melalui tipologi. Ini catatan desain yang memerlukan keputusan domain, bukan koreksi fakta eksternal.

### N03 — Kontrak per-leg perlu dipertegas, tanpa menghapus field yang sudah ada

Common Object Envelope sudah mempunyai confidence conditional; jadi tidak benar mengatakan Data Model sama sekali tidak mempunyai confidence untuk leg. Namun section ValueFlowLeg tidak menjelaskan kondisi kewajiban per kelas, sedangkan SRS meminta confidence/evidence per leg. Tambahkan invariant eksplisit tentang direct/documented/reconstructed/hypothetical leg, reconstruction basis dan inheritance, lalu tes mixed-class chain.

### N04 — Kontrak/award tidak sama dengan settlement

Data Model sudah menyatakan DOCUMENTED dapat membuktikan obligation tanpa settlement. Pertahankan pembedaan tersebut sampai UI, kalkulasi dan export. Jangan menjumlahkan contract award sebagai pembayaran aktual atau menyimpulkan asal dana pembelian dari urutan waktu semata.

### N05 — Hash bukan validasi kebenaran isi

Hash dan immutability berguna untuk mendeteksi perubahan terhadap bytes yang dicatat. Catatan asal, autentisitas, atribusi, keterbatasan dan review tetap dibutuhkan. Jangan menampilkan hash verified sebagai fact verified. Ini penegasan interpretasi, bukan tuduhan bahwa seluruh dokumen telah menyamakan keduanya.

### N06 — Estimasi sprint/latensi adalah target, bukan hasil pengukuran

Sprint Plan menandai kapasitas dan cadence sebagai asumsi. Itu wajar untuk perencanaan, bukan halusinasi. Tanpa estimasi tugas, velocity, benchmark dan profil beban nyata, waktunya tidak boleh dipresentasikan sebagai janji tervalidasi. Begitu pula RPO/RTO, latensi dan accessibility adalah target sampai diuji.

### N07 — Spesifikasi UI bukan mockup atau implementasi

Dokumen HiFi berisi aturan komposisi dan ukuran. Component/Storybook berisi requirements, bukan bukti bahwa 65 komponen telah dibuat. Target WCAG, pemeriksaan render dokumen dan test suite aplikasi harus dipisahkan. Audit ini tidak menguji aplikasi atau Storybook yang berjalan.

### N08 — Riwayat versi perlu satu authority

Terdapat Framework original dan Expanded dengan versi sama-sama 0.1. Tiga judul juga mempunyai dua PDF di lokasi berbeda. Dua pasang PDF mempunyai text digest sama; HiFi berbeda dalam page breaks/repeated headers. Jangan menyimpulkan perubahan substansi dari hash file saja. Tetapkan canonical file, supersedes, release manifest dan tanggal review.

## 6. Hasil per dokumen

Status berikut menunjukkan hasil review dan pekerjaan tersisa, bukan cap “lulus audit”. Dokumen yang tidak mempunyai kesalahan unik tetap bergantung pada koreksi kontrak bersama.

| No. | Dokumen | Halaman PDF utama | Status / tindak lanjut |
|---|---|---:|---|
| 1 | Framework | 30 | **Arsipkan sebagai legacy setelah keputusan eksplisit.** Ada Expanded dengan versi sama; jangan menjadi baseline paralel. A01, A12, A13. |
| 2 | Framework v0.1 Expanded | 36 | **Pertahankan dengan koreksi.** Prinsip cukup jelas dan disclaimer eksternal sudah ada; selaraskan klasifikasi, strict chain dan source lineage. A01, A08, A13; N01-N02. |
| 3 | Framework Goals and Non-Goals | 8 | **Pertahankan; validasi outcome.** Tidak ditemukan kesalahan faktual spesifik pada goals dalam audit ini. Goal adalah niat produk, bukan efektivitas terukur. A01; N06. |
| 4 | Typology Catalogue | 54 | **Review sumber dan domain.** 20 ID valid dihitung; mapping per indikator/halaman dan empirical calibration belum tervalidasi. A13; N01. |
| 5 | Investigation Methodology | 29 | **Pertahankan; harmonisasi.** Peran non-koersif dan disclaimer ada. Verifikasi rujukan rinci dan selaraskan state/evidence/flow. A08-A09, A13; N02-N05. |
| 6 | Data Model Specification | 33 | **Prioritas perbaikan.** Authority model belum konsisten pada enum/confidence/classification; contoh edge salah; lifecycle perlu lengkap. A08-A10, A14; N03. |
| 7 | Control Implementation Guide | 41 | **Perbaiki policy exceptions.** Owner/evidence/test distinctions baik. Control efficacy belum dibuktikan; pengecualian release harus dibatasi. A01, A16. |
| 8 | Technology Architecture | 26 | **Harmonisasi registry.** Canonical versus derived konsisten. Capability namespace bertabrakan dengan Feature. A07, A08; N01. |
| 9 | Product and Feature Specification | 25 | **Perbaiki traceability downstream.** 87 fitur = 54 P0 + 26 P1 + 7 P2 terkonfirmasi. F-ASM-003 dan template perlu dipertahankan maknanya. A05-A07. |
| 10 | Product Requirements Document PRD | 24 | **Tetap baseline rencana.** Arah dan non-goals jelas; problem/JTBD/outcome belum hasil user research. Samakan scope dengan SRS/backlog. A01, A05-A06, A12. |
| 11 | Software Requirements Specification SRS | 36 | **Prioritas perbaikan.** Requirement IDs berguna, tetapi F-ASM mapping, enum dan output scope belum konsisten. A04-A06, A08-A11, A16. |
| 12 | MVP Engineering Breakdown | 25 | **Perbaiki sebelum estimasi rinci.** Story breakdown belum menutup Claim/Fact; template hanya tiga. A05-A06, A10; N06. |
| 13 | Technical Stack and Repository Specification | 23 | **Revalidasi dependency baseline.** MinIO Community maintenance dan Redis release/licence harus diputuskan ulang; model auth browser belum final. A02-A03, A11. |
| 14 | Sprint and Milestone Plan | 16 | **Rebaseline setelah koreksi scope.** Cadence adalah asumsi, bukan guarantee; waiver high-risk tidak boleh melemahkan invariant. A06, A16; N06. |
| 15 | UX Specification | 20 | **Pertahankan; belum uji pengguna.** Uncertainty dan safety principles kuat; butuh prototype/usability/accessibility evidence, bukan tambah klaim lulus. A01, A08-A09; N07. |
| 16 | Information Architecture Specification | 22 | **Harmonisasi identifiers/labels.** Case-as-context dan permission-aware findability baik; normalisasi canonical enums, mapping role/classification. A07-A09. |
| 17 | Screen Inventory | 23 | **Pertahankan angka aktual.** 53 ID terdiri 50 screen kerja + 3 system-state screens. Klaim chat 50 total harus diberi batas hitung. A15; N07. |
| 18 | Wireframe Specification | 11 | **Koreksi mapping spesifik.** Case Register salah pattern detail. Review screen-pattern links sebelum implementasi. A15. |
| 19 | UI Design System Specification | 25 | **Pertahankan; selaraskan schema.** No guilt-by-color dan non-color cues konsisten; Insufficient Basis harus didukung model. Belum klaim WCAG conformance. A09; N07. |
| 20 | High-Fidelity UI Specification | 20 | **Reference komposisi, bukan UI jadi.** Jangan menganggap prose layout sebagai completed mockup/testing. Selaraskan canonical states dan versi PDF. A01, A09, A15; N07-N08. |
| 21 | Component Inventory and Storybook Implementation Specification | 17 | **Inventory valid; implementasi belum dibuktikan.** 65 ID benar. Storybook security disclaimer baik. Tidak ada hasil code/interaction/axe/visual regression dalam corpus. A01; N07. |
| 22 | Frontend Architecture and State Management Specification | 15 | **Lengkapi kontrak lintas tim.** State ownership baik; login model, cache-revocation behavior dan API conflict semantics belum locked. A04, A08-A09, A11. |
| 23 | API Specification | 17 | **Prioritas perbaikan.** 409/412 konflik nyata; schema/operasi/Claim-Fact/auth-idempotency belum kontrak executable lengkap. A04, A08-A11. |

**Bahan tambahan:** `AML-brainstrom.md` tetap sebagai histori percakapan, bukan sumber kontrak implementasi. Angka aset, perusahaan anonim dan flow ilustratif di dalamnya bukan hasil investigasi nyata. Rujukan AHU yang dikutip adalah artikel 16 Desember 2025; jangan disajikan sebagai angka terbaru 2026 tanpa pembaruan [S12].

## 7. Urutan perbaikan yang direkomendasikan

### Gelombang 1 — Hentikan drift sebelum coding domain

Bekukan penambahan dokumen spesifikasi baru. Tetapkan register dokumen authoritative, status legacy, pemilik keputusan dan change log. Selesaikan A04-A11: namespace capability, makna F-ASM-003, template MVP, classification, enum/confidence, Claim/Fact lifecycle dan kontrak API. Keputusan berubah harus menghasilkan errata atau versi 0.1.1, bukan menimpa file v0.1 tanpa jejak.

### Gelombang 2 — Validasi dependency dan invariant keselamatan

Selesaikan keputusan object store/Redis dan login browser; kunci versi yang dipelihara dan lisensinya. Tetapkan invariant yang tidak bisa di-waive. Jalankan validator schema/example, negative authorization, stale-write, entity merge/unmerge, flow mixed-class, approval/export dan evidence round-trip. Gunakan data sintetis; belum perlu data kasus sensitif.

### Gelombang 3 — Buktikan satu vertical slice

Implementasikan satu alur kecil: case -> source/evidence -> claim/fact -> entity/relationship -> hypothesis/assessment -> independent review -> approved export. Ukur apa yang benar-benar terjadi, bukan hanya checklist yang direncanakan. Model yang belum perlu untuk slice tidak perlu ditambah dokumen turunannya. Review domain, privacy dan keamanan dilakukan atas contoh kerja tersebut.

### Gerbang untuk menyebut baseline siap handoff

Baseline baru layak dibekukan ketika tidak ada ID yang berubah arti tanpa mapping; enums dan states konsisten; scope P0 sama pada PRD/SRS/backlog; OpenAPI/examples tervalidasi; reference URLs material mempunyai lokasi dukungan atau label pending; source-of-truth dokumen jelas; dan keputusan keselamatan mempunyai tests yang dapat dieksekusi. “Siap handoff” masih berbeda dari “siap production”.

## 8. Register verifikasi sumber eksternal

### [S01] FATF Recommendations

Terverifikasi: halaman resmi mencantumkan amended June 2026.

**Batas verifikasi:** Keberadaan/versi standar dan konteks risk-based approach; bukan validasi semua kontrol CS-AML.

Sumber: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html

### [S02] Wolfsberg Guidance on the Risk-Based Approach, June 2026

Terverifikasi: guidance resmi Juni 2026.

**Batas verifikasi:** Proportionality, prioritisation, effectiveness; ditujukan kepada financial institutions, diadaptasi oleh CS-AML.

Sumber: https://wolfsberg-group.org/resources/202/205

### [S03] PPATK Klinik Dumas Special Edition

Terverifikasi: publikasi 26 November 2025; acara 25 November 2025.

**Batas verifikasi:** Peran informasi NGO/CSO dan kualitas pendukung pengaduan; tidak membuktikan adanya persetujuan PPATK terhadap framework kita.

Sumber: https://www.ppatk.go.id/news/read/1570/klinik-dumas-special-edition-ppatk-dan-ngocso-perkuat-aduan-tppu-melalui-peluncuran-laporppatkgoid.html

### [S04] MinIO upstream repository

Terverifikasi: diarsipkan 25 April 2026; README menyatakan tidak lagi dipelihara.

**Batas verifikasi:** Repositori MinIO Community yang dirujuk; bukan pernyataan bahwa seluruh produk/vendor MinIO berhenti beroperasi.

Sumber: https://github.com/minio/minio

### [S05] Redis licenses

Terverifikasi: batas versi mengubah pilihan lisensi.

**Batas verifikasi:** Redis <=7.2 BSD-3; Redis 7.4 RSALv2/SSPLv1; Redis 8 menambah pilihan AGPLv3. Bukan pendapat hukum lisensi implementasi tertentu.

Sumber: https://redis.io/legal/licenses/

### [S06] RFC 9110, HTTP Semantics, section 13.1.1

Terverifikasi: conditional request If-Match dan penanganan precondition.

**Batas verifikasi:** False If-Match tidak boleh diterapkan; 412 adalah respons kegagalan precondition yang relevan. RFC memuat pengecualian respons sukses untuk aksi yang sudah terpenuhi; jangan mengganti semua konflik aplikasi menjadi 412.

Sumber: https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1

### [S07] FATF Non-Profit Organisations

Terverifikasi: pendekatan targeted, proportionate, risk-based.

**Batas verifikasi:** Mendukung guardrail terhadap over-application AML/CFT, tidak menetapkan taxonomy atau maturity CS-AML.

Sumber: https://www.fatf-gafi.org/en/topics/non-profit-organisations.html

### [S08] FATF Investigating Professional Money Laundering, Underground Banking, Hawala and HOSSPs

Terverifikasi: publikasi 2026 memang ada.

**Batas verifikasi:** Keberadaan dan ruang lingkup laporan, bukan validasi indikator lokal per entri.

Sumber: https://www.fatf-gafi.org/en/publications/Methodsandtrends/pml-underground-banking-hawala-hossps.html

### [S09] FATF Cyber-Enabled Fraud

Terverifikasi pada sumber resmi: publikasi 2026 ada.

**Batas verifikasi:** Tidak semua narasi angka/kasus pada chat terdahulu diaudit dalam pemeriksaan dokumen ini.

Sumber: https://www.fatf-gafi.org/en/publications/Methodsandtrends/cyber-enabled-fraud-digitalisation-ml-tf-pf-risks.html

### [S10] UNODC civil-society/UNCAC guide, URL yang dikutip

Parsial: URL dan teks terindeks ditemukan pada domain resmi; pembukaan langsung gagal pada alat audit.

**Batas verifikasi:** Judul bibliografis serta lokasi halaman untuk klaim spesifik tentang asset tracing, forensic auditing, dan legal analysis belum dapat dikukuhkan dari PDF penuh. Ini bukan bukti sumber fiktif.

Sumber: https://www.unodc.org/documents/NGO/Corruption/251113-CSU-UNCAC_Guide-Web.pdf

### [S11] UU No. 27 Tahun 2022, JDIH BPK

Terverifikasi: peraturan ada; abstrak memuat catatan kejahatan dan data keuangan pribadi sebagai data spesifik.

**Batas verifikasi:** Tidak merupakan legal opinion tentang dasar pemrosesan kasus tertentu atau audit kepatuhan penuh CS-AML.

Sumber: https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022

### [S12] AHU, Penguatan Transparansi Pemilik Manfaat Korporasi

Terverifikasi: artikel 16 Desember 2025 memuat keterbatasan jumlah/kualitas pelaporan dan self-declaration.

**Batas verifikasi:** Catatan historis, bukan statistik terbaru 2026. Klaim jumlah absolut harus disertai sumber jumlah, bukan disimpulkan dari persentase saja.

Sumber: https://portal.ahu.go.id/id/detail/75-berita-lainnya/6150-ditjen-ahu-dorong-penguatan-transparansi-pemilik-manfaat-korporasi

### [S13] AHU pencarian profil pemilik manfaat

Terverifikasi: halaman pencarian tersedia dan menjelaskan asal data pelaporan.

**Batas verifikasi:** Tidak berarti izin scraping massal atau jaminan kebenaran setiap laporan.

Sumber: https://www.ahu.go.id/pencarian/profil-pemilik-manfaat

### [S14] KPK e-LHKPN portal/FAQ

Terverifikasi: pengumuman dan pencarian tahun lapor tersedia bagi masyarakat melalui e-Announcement.

**Batas verifikasi:** Akses/form/captcha tetap berlaku; adanya sumber publik tidak membuktikan akses otomatis atau atribut aset lengkap.

Sumber: https://elhkpn.kpk.go.id/portal

### [S15] OWASP ASVS

Terverifikasi: versi stabil 5.0.0 ditampilkan.

**Batas verifikasi:** Rujukan valid; tidak ada bukti pengujian aplikasi CS-AML terhadap ASVS dalam paket yang diperiksa.

Sumber: https://owasp.org/projects/asvs

### [S16] SLSA v1.2

Terverifikasi: versi 1.2 berstatus approved.

**Batas verifikasi:** Rujukan valid; bukan bukti build CS-AML memenuhi level SLSA.

Sumber: https://slsa.dev/spec/v1.2/

### [S17] Django downloads/support schedule

Terverifikasi: Django 5.2 adalah LTS dengan extended support sampai April 2028.

**Batas verifikasi:** Pemilihan lini LTS bukan kesalahan hanya karena ada versi fitur lebih baru; patch/dependency tetap perlu dipatok dan diuji.

Sumber: https://www.djangoproject.com/download/

### [S18] WCAG 2.2

Rujukan resmi dapat diperiksa.

**Batas verifikasi:** Target aksesibilitas dalam spesifikasi bukan bukti pemenuhan kriteria aktual.

Sumber: https://www.w3.org/TR/WCAG22/

## 9. Kesimpulan akhir

Yang paling perlu dikoreksi bukan gagasan dasar CS-AML, melainkan kepastian yang dilekatkan kepadanya dan konsistensi kontrak saat gagasan itu diterjemahkan ke banyak dokumen. Referensi eksternal yang valid tidak otomatis memvalidasi desain lokal. Spesifikasi yang panjang tidak otomatis lengkap. Kriteria test bukan bukti test telah lulus.

Rekomendasi audit: pertahankan arah produk, hentikan ekspansi dokumentasi sementara, terbitkan koreksi terkoordinasi untuk temuan prioritas tinggi, dan gunakan satu vertical slice dengan data sintetis untuk menguji framework. Jangan memakai paket v0.1 yang sekarang sebagai bukti kepatuhan, sertifikasi, atau kesiapan production.

---
Register JSON pendamping menyimpan temuan, kutipan/section sumber, inventory, dan SHA-256 file input. Dokumen asli tidak diubah.
