# ML-07: Baseline Action Score and Top-10 Review

## Apa yang Kita Lakukan?
Pada tugas ini (Fokus: *Core Lane 2 - Content Refresh Opportunity*), kita membangun sebuah model dasar (*Baseline*) berupa **aturan manual berbasis logika manusia** untuk mendeteksi halaman website yang performanya sedang menurun.

Langkah-langkah yang dilakukan:
1. **Audit Sinyal (EDA):** Menguji hipotesis dua sinyal utama terhadap peluang turunnya *traffic* (`trend_direction == 'down'`).
2. **Menyusun Aturan Baseline:** Membuat sebuah formula skoring manual tanpa *Machine Learning*.
3. **Membangun Antrean (Ranked Queue):** Menyortir halaman dari prioritas tertinggi ke terendah dan menyimpannya ke dalam file CSV (`work/outputs/baseline_action_score.csv`).

## Aturan Baseline yang Digunakan
Aturan manual yang kita ciptakan adalah:
> "Tandai halaman untuk di-review jika usianya sudah kusam (**>180 hari sejak update terakhir**), secara historis masih punya visibilitas pencarian (**>500 impresi dalam 90 hari**), namun interaksi/kliknya sangat buruk (**CTR < 2.0%**)."

Untuk halaman yang memenuhi ketiga syarat mutlak di atas, skornya akan dikalikan dengan total impresinya (`impressions_90d`) agar halaman dengan potensi *traffic* terbesar berada di peringkat pertama. 

Halaman yang tertangkap akan diberi:
* **Action Label:** `review_for_refresh`
* **Reason Code:** `stale_high_volume_low_ctr`

## Hasilnya Seperti Apa?
Hasil dari *Baseline Rule* ini sangat memuaskan:
* Dari sekitar 30.000 baris data, aturan manual ini berhasil menyeleksi dan menyaring tepat **17 halaman paling kritis** yang butuh *refresh* konten.
* **Akurasi Tinggi (Precision):** Dari 17 halaman yang ditandai oleh aturan kita, **16 halaman di antaranya memang terbukti sedang anjlok *traffic*-nya** (berdasarkan kolom proxy label `is_declining`). 
* Ini menghasilkan tingkat **Precision mencapai ~94.1%**. 

Menebak dengan akurasi 94% hanya bermodalkan aturan statis (If-Else) membuktikan bahwa logika bisnis kita sudah tepat dan sinyal yang dipilih sangat kuat. Angka inilah yang akan menjadi **Batas Standar (Baseline)** yang wajib dikalahkan oleh algoritma *Machine Learning* kita di minggu-minggu berikutnya.
