**Kita laksanakan sebagai satu siklus perbaikan terkontrol, bukan dengan menambah deretan dokumen baru.** Sasaran akhirnya adalah satu paket CS-AML yang konsisten, sumbernya dapat diperiksa, dan persyaratan pentingnya dapat diuji.

Ada dua pekerjaan yang harus dibedakan:

**Memperbaiki dokumentasi** berarti menghilangkan kesalahan dan ketidakjelasan spesifikasi. **Membuktikan implementasi** berarti menjalankan pengujian terhadap perangkat lunak. Penyelesaian yang pertama tidak otomatis menyelesaikan yang kedua. Register audit saat ini memang masih menandai semua temuan sebagai terbuka; dokumen sumber belum diubah. fileciteturn18file0L11-L19

Berikut cara pelaksanaan yang saya sarankan.

## 1. Amankan baseline lama dan tetapkan sumber acuan

Jangan langsung menimpa semua file `v0.1`. Simpan paket yang diaudit sebagai **arsip baseline lama**, sehingga kita tetap dapat menunjukkan bagian mana yang berubah dan alasannya.

Untuk pekerjaan koreksi, gunakan satu folder atau repositori kerja dengan pembagian sederhana:

```text
CS-AML/
├── archive/         Paket v0.1 yang telah diaudit
├── source/          Isi lengkap dokumen yang sedang diperbaiki
├── contracts/       Registry istilah, requirement, schema, dan API
├── audit/           Register temuan dan catatan keputusan
└── releases/        Paket hasil koreksi yang sudah direview
```

Ini usulan struktur kerja, bukan kewajiban membuat lima dokumen baru.

**Saya menyarankan Markdown lengkap sebagai sumber penyuntingan**, kemudian DOCX dan PDF dihasilkan dari sumber tersebut. Tetapi langkah awalnya harus mengambil isi lengkap dari DOCX—**jangan memakai companion Markdown yang ringkas sebagai pengganti spesifikasi lengkap**. Audit menemukan bahwa sebagian companion memang hanya berisi rangkuman atau rujukan ke DOCX/PDF. fileciteturn18file0L273-L287

Setiap dokumen cukup mempunyai metadata: ID, versi, status, pemilik, reviewer, dan dokumen yang digantikannya. Hindari status “approved” sebelum ada keputusan persetujuan yang tercatat.

**Hasil tahap ini:** tidak ada lagi dua file berbeda yang sama-sama dianggap sebagai acuan aktif tanpa penjelasan.

## 2. Ubah 16 temuan menjadi enam paket pekerjaan

Gunakan **register audit yang sudah ada** sebagai daftar pekerjaan. Jangan membuat ulang daftar temuan dengan nomor baru karena hubungan ke bukti audit harus tetap terjaga.

Saya akan mengelompokkan A01–A16 berikut. Pengelompokan ini adalah usulan pelaksanaan; ID dan masalahnya berasal dari register audit. fileciteturn18file0L46-L65

| Paket | Temuan | Pekerjaan konkret | Bukti penyelesaian |
|---|---|---|---|
| **1. Kendali dokumen** | A01, A12 | Betulkan status kesiapan; tentukan sumber lengkap dan versi aktif; tandai companion ringkas. | Manifest dokumen dan perbandingan isi antarformat. |
| **2. Makna dan model bersama** | A05, A07, A08, A09, A10 | Selaraskan requirement ID, capability, klasifikasi, enum, confidence, serta lifecycle Claim/Fact. | Registry yang konsisten, mapping perubahan, dan contoh data tervalidasi. |
| **3. Kontrak API** | A04, A11 | Perbaiki konflik HTTP; lengkapi schema request/response, autentikasi, idempotency, upload, jobs, dan approval. | OpenAPI, contoh payload, serta hasil pemeriksaan kontrak. |
| **4. Scope dan keselamatan rilis** | A06, A16 | Putuskan jumlah template MVP; batasi pengecualian release. | Scope yang sama pada PRD/SRS/backlog dan kriteria release yang diperbaiki. |
| **5. Dependency dan sumber eksternal** | A02, A03, A13 | Periksa maintenance/lisensi komponen; cocokkan klaim eksternal dengan bagian sumber yang mendukungnya. | Catatan keputusan dependency dan register verifikasi sumber. |
| **6. Contoh dan pemetaan UI** | A14, A15 | Perbaiki arah `DIRECTOR_OF` dan pattern Case Register. | Contoh tervalidasi dan hasil pemeriksaan tampilan/pemetaan. |

Urutannya tidak harus sepenuhnya serial. Paket 1 dimulai pertama; Paket 2 dan 4 menjadi masukan penting untuk Paket 3. Paket 5 dapat berjalan paralel, sedangkan koreksi lokal pada Paket 6 dapat dilakukan lebih awal.

## 3. Pisahkan koreksi langsung dari keputusan yang perlu Anda setujui

**Tidak semua temuan boleh diselesaikan hanya dengan mengganti teks.**

Arah panah yang salah merupakan koreksi. Mengurangi scope MVP atau mengubah model klasifikasi merupakan keputusan produk dan keamanan.

### Koreksi yang dapat disiapkan langsung

Contohnya: membetulkan pemetaan layar, memperbaiki contoh hubungan, menghapus klaim kesiapan yang tidak mempunyai bukti, serta memisahkan dua requirement yang selama ini keliru dipetakan.

Untuk konflik API, penolakan karena **`If-Match` yang sudah kedaluwarsa** perlu konsisten menggunakan **412**, sedangkan **409** dapat digunakan untuk konflik keadaan aplikasi. RFC 9110 membedakan precondition HTTP dan konflik resource; ketentuan tentang request yang aksinya ternyata sudah terpenuhi juga perlu diperhitungkan dalam kontrak retry. ([rfc-editor.org](https://www.rfc-editor.org/rfc/rfc9110.html))

### Keputusan substantif yang harus dicatat

| Keputusan | Usulan saya | Batas keputusan |
|---|---|---|
| **Enam atau tiga template MVP?** | Tiga template dapat menjadi scope awal yang lebih kecil. | Jangan mengubahnya sepihak. Sampai perubahan disetujui, enam template pada SRS tetap merupakan requirement yang belum seluruhnya tercakup backlog. |
| **Model klasifikasi informasi** | Pisahkan tingkat sensitivitas dari pembatasan khusus seperti identitas sumber. | Label lama harus dipetakan; jangan otomatis menyamakan `HIGHLY RESTRICTED` dengan `SOURCE-PROTECTED`. |
| **Enum Value Flow** | Gunakan satu penulisan machine value secara konsisten, misalnya uppercase yang sudah digunakan pada API. | Perubahan harus mencakup schema, contoh, UI, export, dan mapping data lama bila ada. |
| **Confidence** | Representasikan `INSUFFICIENT_BASIS` secara eksplisit, terpisah dari `LOW`. | “Dasar belum cukup” tidak boleh berubah menjadi “keyakinan rendah” tanpa keputusan analitis. |
| **Claim dan Fact** | Pertahankan klaim sumber, lalu catat keputusan verifikasi secara terpisah. | Jangan mengganti klaim sumber dengan kesimpulan analis atau membuat promosi otomatis menjadi fakta. |
| **Autentikasi browser** | Pilih satu kontrak utama untuk MVP, lalu selaraskan frontend dan backend. | Jangan membiarkan engineer menebak antara beberapa alternatif yang belum diputuskan. |

Masalah klasifikasi, confidence, dan Claim/Fact tersebut memang tercatat sebagai ketidakjelasan kontrak, bukan bukti bahwa seluruh konsepnya salah. fileciteturn18file0L190-L254

Untuk setiap keputusan cukup ada catatan singkat:

> Masalah → pilihan → keputusan → alasan → dampak → pemberi persetujuan.

Tidak perlu masing-masing menjadi dokumen puluhan halaman.

## 4. Perbaiki berdasarkan satu temuan, bukan berdasarkan satu dokumen

Ini perubahan cara kerja yang paling penting.

**Jangan memperbaiki SRS sampai selesai, kemudian baru membaca API.** Sebuah temuan dapat memengaruhi beberapa dokumen sekaligus. Perbaikannya harus menjadi satu paket lintas dokumen.

### Contoh: menyelesaikan A05

Audit menemukan bahwa `F-ASM-003` berarti *disconfirming search record*, tetapi SRS memetakannya ke *backward traceability*. Padahal menelusuri sumber dan mencari bukti yang menyangkal kesimpulan adalah dua pekerjaan berbeda. fileciteturn18file0L139-L155

Penyelesaiannya:

1. **Pertahankan makna `F-ASM-003`.** Jangan mengganti arti identifier lama.
2. Tambahkan atau perbaiki requirement SRS untuk pencatatan pencarian bukti yang menyangkal hipotesis. Berikan pemetaan terpisah untuk backward traceability.
3. Sesuaikan backlog, kontrak API, dan layar review yang membutuhkan data tersebut.
4. Buat dua pengujian berbeda: pengujian penelusuran assessment ke evidence, dan pengujian keberadaan catatan disconfirmation sebelum review berdampak tinggi diselesaikan.

Paket perubahan harus menunjukkan **teks sebelum/sesudah, file terdampak, dan pengujian yang berubah**.

Dengan cara ini, kita tidak menghapus kesalahan di satu file lalu meninggalkannya pada lima file lain.

### Status penyelesaiannya juga harus dipisahkan

Saya menyarankan register memiliki dua kolom:

| Dimensi | Contoh status |
|---|---|
| **Koreksi spesifikasi** | Belum diperbaiki → diusulkan → disetujui → diperbaiki → diverifikasi |
| **Pembuktian implementasi** | Belum diimplementasikan → tersedia pada mock → diimplementasikan → diuji |

Dengan demikian, sebuah temuan dapat berstatus:

> **Spesifikasi telah diperbaiki; implementasi belum diuji.**

Itu lebih jujur daripada satu kotak “Done” yang menyamarkan pekerjaan tersisa.

## 5. Verifikasi ulang sumber dan dependency—termasuk kesimpulan audit

**Audit saya sendiri tidak boleh dijadikan sumber kebenaran yang tidak boleh dipertanyakan.** Sebelum menutup temuan, reviewer perlu dapat mereproduksi bukti yang mendasarinya.

Untuk klaim eksternal, gunakan empat kategori:

| Kategori | Perlakuan |
|---|---|
| **Fakta eksternal terverifikasi** | Cantumkan sumber, versi/tanggal, dan section atau halaman pendukung. |
| **Keputusan desain CS-AML** | Cantumkan alasan dan pemilik keputusan; jangan diatribusikan kepada FATF. |
| **Asumsi atau target** | Tandai sebagai sesuatu yang masih perlu diuji. |
| **Belum terverifikasi** | Jangan dipakai sebagai dasar klaim yang kuat sebelum diperiksa. |

Misalnya, pembagian G0–G6 dapat dipertahankan sebagai desain lokal. Tetapi tidak boleh berubah menjadi pernyataan bahwa FATF mewajibkan persis tujuh gate tersebut. Audit sudah membedakan konvensi lokal dari standar eksternal. fileciteturn18file0L359-L367

Untuk dependency, tindakan praktisnya bukan langsung memilih pengganti berdasarkan popularitas. **Periksa produk, versi, lisensi, maintenance, kompatibilitas, dan pemulihan datanya sebagai satu kesatuan.**

Saya memeriksa kembali dua sumber penting: repositori `minio/minio` memang ditandai sebagai arsip, sedangkan halaman lisensi Redis membedakan ketentuan antarversi. Itu mendukung kebutuhan mengevaluasi ulang baseline, tetapi tidak otomatis menetapkan produk pengganti tertentu. ([github.com](https://github.com/minio/minio))

Hasilnya cukup disimpan dalam catatan keputusan teknis dan manifest dependency yang sudah menjadi bagian pekerjaan engineering.

## 6. Buktikan satu alur kecil dengan data sintetis

Setelah kontrak inti diselaraskan, **jangan langsung membangun seluruh 53 layar**. Saya menyarankan satu potongan aplikasi yang dapat menjalankan alur investigasi dari awal sampai akhir:

```text
Case
→ Source / Evidence
→ Claim dan keputusan verifikasi
→ Entity / Relationship
→ Value Flow
→ Hypothesis / Assessment
→ Independent Review
→ Approved Export
```

Ini sejalan dengan rekomendasi audit untuk menguji satu alur lengkap sebelum memperluas implementasi. fileciteturn18file0L435-L441

Gunakan satu kasus rekaan, bukan data sensitif sungguhan. Sertakan kontrak, klaim pembayaran, dua nama yang mirip, bukti yang bertentangan, dan identitas sumber sintetis yang dibatasi.

**Skenario uji minimum yang saya usulkan:**

| Skenario | Hasil yang harus dibuktikan |
|---|---|
| Dua entitas mempunyai nama sama tetapi identifier berbeda. | Sistem tidak melakukan merge otomatis. |
| Sebuah klaim kemudian dibantah bukti baru. | Keputusan verifikasi dapat direvisi; riwayat dan hubungan ke produk terdampak tetap tersedia. |
| Ada kontrak, tetapi bukti pembayaran belum tersedia. | Nilai kontrak tidak ditampilkan sebagai pembayaran aktual. |
| Satu rangkaian mempunyai beberapa kelas Value Flow. | Kelas setiap leg tetap berbeda pada penyimpanan, API, UI, dan export. |
| Pengguna tanpa izin mencoba mencari atau membuka objek. | Konten dan metadata yang dilarang tetap tidak terungkap, termasuk melalui hasil pencarian. |
| Pengguna mencoba export sebelum approval. | Server menolak; bukan sekadar tombol disembunyikan. |
| Reviewer mencoba menyetujui produk yang ia tulis sendiri. | Aturan independensi yang disepakati diterapkan. |
| Data dipulihkan dari backup. | Evidence, referensi, versi, dan catatan keputusan tetap dapat diperiksa. |

Pengujian terhadap mock berguna untuk memeriksa kontrak, tetapi **tidak dihitung sebagai bukti keamanan backend**. Begitu pula keberhasilan menampilkan Storybook tidak membuktikan authorization aplikasi.

Untuk keselamatan rilis, saya menyarankan tidak ada pengecualian administratif selama jalur akses tanpa izin, pengungkapan sumber, approval bypass, atau penghilangan integritas analitis masih aktif. Menonaktifkan fitur berbahaya baru dapat menjadi mitigasi bila ketidaktersediaan jalur tersebut juga dibuktikan. Ini menutup masalah A16. fileciteturn18file0L341-L357

## 7. Tetapkan siapa yang mengerjakan dan siapa yang memeriksa

Tidak perlu langsung membentuk tim besar. Tetapi tanggung jawabnya harus jelas.

| Peran | Tanggung jawab |
|---|---|
| **Anda/pemilik produk** | Menyetujui scope, tujuan, prioritas, dan perubahan makna domain. |
| **Technical lead atau engineer** | Memperbaiki schema, API, dependency, serta dampaknya pada implementasi. |
| **Reviewer domain dan keamanan** | Menguji makna analitis, pembatasan akses, perlindungan sumber, serta aturan release sesuai kompetensinya. |
| **QA atau pemeriksa kedua** | Memeriksa hasil perubahan dan bukti pengujian, bukan hanya menerima pernyataan penulis. |

Dalam tim kecil, beberapa peran dapat dirangkap. Namun saya menyarankan keputusan sensitif tidak dinyatakan lolos hanya berdasarkan pemeriksaan orang yang membuat perubahan.

AI dapat membantu menyusun patch, menemukan ketidaksesuaian, dan membuat calon pengujian. **Persetujuan manusia dan hasil eksekusi tetap harus dicatat sebagai bukti tersendiri**, bukan digantikan dengan jawaban AI “sudah sesuai”.

## Kapan pekerjaan ini dianggap selesai?

Saya akan memakai tiga gerbang yang berbeda:

**Gerbang dokumentasi:** semua temuan kesalahan dan konflik yang relevan telah diperbaiki atau diputuskan, sumber acuan jelas, dan dokumen turunan tidak lagi saling bertentangan.

**Gerbang handoff engineering:** schema, API, contoh, backlog, serta acceptance criteria konsisten untuk scope yang disetujui. Keputusan yang masih terbuka dinyatakan sebagai blocker, bukan disembunyikan sebagai asumsi.

**Gerbang pilot:** alur sintetis berhasil dijalankan, termasuk skenario gagal dan pengujian keamanan. Ini belum sama dengan kesiapan production untuk investigasi nyata.

### Jadi, langkah pertama kita sekarang

**Mulai dari kendali baseline dan registry bersama—bukan menulis spesifikasi baru.** Pilih sumber dokumen aktif, perluas register audit dengan owner/status/bukti penutupan, lalu kerjakan koreksi ID, enum, klasifikasi, Claim/Fact, dan scope MVP.

Hasil pekerjaan berikutnya seharusnya berupa **file yang benar-benar diperbaiki, catatan perubahan, keputusan yang masih membutuhkan persetujuan, serta hasil pemeriksaan**. Bukan tambahan dokumen panjang yang kembali menyatakan semuanya siap.
