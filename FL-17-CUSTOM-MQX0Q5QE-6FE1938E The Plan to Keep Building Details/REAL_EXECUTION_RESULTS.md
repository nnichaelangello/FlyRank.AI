# AI Resume Screener: Real Execution Log

Dokumen ini berisi log terminal asli tanpa rekayasa dari hasil eksekusi prototipe *AI Resume Screener & Skill Matcher* yang telah kita bangun.

## 1. Apa yang Telah Kita Lakukan?
- Kita merakit kode Python ML/NLP menggunakan *Sentence-Transformers* dari HuggingFace (`all-MiniLM-L6-v2`).
- Sistem membaca *Job Description* (berisi syarat Python, ML, Pandas, dll).
- Sistem membedah 5 buah file PDF secara otomatis (termasuk CV asli milik Michael Angello) menggunakan pustaka `PyPDF2`.
- Sistem mengubah teks menjadi vektor semantik dan menghitung jarak *Cosine Similarity* untuk mendapatkan persentase kecocokan.

## 2. Hasil Terminal (Output Nyata)
Berikut adalah *output real* dari terminal ketika sistem mendeteksi keberadaan file-file PDF tersebut dan memprosesnya secara *end-to-end*:

```text
[SYSTEM] Loading AI Model 'all-MiniLM-L6-v2'...
[SYSTEM] Model loaded successfully.

[SCAN] Reading Job Description from: C:\Users\Michael Angello\Documents\Michael\Magang\FlyRank.AI\FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details\job_description.txt
[SCAN] Found 5 resumes. Analyzing semantic match...

==================================================
[*] AI RESUME SCREENING RESULTS [*]
==================================================
                                        Candidate  Match Score (%)   Status
                            Bob_Jones_Backend.pdf            68.52 Analyzed
                               Alice_Smith_ML.pdf            66.61 Analyzed
                         Charlie_Brown_Design.pdf            33.71 Analyzed
                                      Profile.pdf            31.01 Analyzed
CV ATS - Michael Angello Qadosy Riyadi (indo).pdf            23.36 Analyzed
==================================================
[SUCCESS] Results exported to C:\Users\Michael Angello\Documents\Michael\Magang\FlyRank.AI\FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details\screening_report.csv
```

## Analisis Hasil:
Seperti yang terlihat dari *output* asli di atas, sistem berhasil mengidentifikasi dan membedah CV ATS pribadi milik Michael Angello (`CV ATS - Michael Angello Qadosy Riyadi (indo).pdf` dan `Profile.pdf`) secara instan dan memberikan persentase skor kecocokan berdasarkan kedekatan kata kuncinya terhadap parameter *Job Description* yang kita tentukan.
