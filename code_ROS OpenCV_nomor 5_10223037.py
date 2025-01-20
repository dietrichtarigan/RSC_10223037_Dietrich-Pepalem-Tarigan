import numpy as np
import cv2

# Membaca gambar query dan train
# Pastikan file 'query.jpg' dan 'train.jpg' berada di direktori yang sama dengan skrip ini
query_img = cv2.imread('query.png')
train_img = cv2.imread('train.jpg')

# Memeriksa apakah gambar berhasil dibaca
if query_img is None:
    print("Gagal membaca 'query.jpg'. Pastikan file tersebut ada di direktori yang sama.")
    exit()
if train_img is None:
    print("Gagal membaca 'train.jpg'. Pastikan file tersebut ada di direktori yang sama.")
    exit()

# Konversi gambar ke grayscale
query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

# Inisialisasi detektor ORB
orb = cv2.ORB_create()

# Deteksi keypoints dan compute deskriptornya untuk gambar query dan train
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw, None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw, None)

# Inisialisasi Brute Force Matcher dengan NORM_HAMMING karena ORB menggunakan deskriptor biner
# crossCheck=True memastikan bahwa hanya matches terbaik yang dipertimbangkan
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Melakukan pencocokan deskriptor antara gambar query dan train
matches = matcher.match(queryDescriptors, trainDescriptors)

# Mengurutkan matches berdasarkan jarak (lower distance lebih baik)
matches = sorted(matches, key=lambda x: x.distance)

# Menggambar 20 matches terbaik
final_img = cv2.drawMatches(
    query_img, queryKeypoints,
    train_img, trainKeypoints,
    matches[:20], None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Mengubah ukuran gambar hasil agar lebih mudah dilihat
final_img = cv2.resize(final_img, (1000, 650))

# Menampilkan gambar hasil pencocokan
cv2.imshow("Matches", final_img)

# Menunggu hingga ada tombol yang ditekan
cv2.waitKey(0)

# Menutup semua jendela OpenCV
cv2.destroyAllWindows()