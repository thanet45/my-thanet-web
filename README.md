# NOIR HOST LIVE — GitHub Pages

เว็บหน้าเดียว (static) แบบดำ–ทอง ใช้ Firebase Authentication, Cloud Firestore และ Cloud Storage เป็นบริการหลังบ้าน

**การทำงาน**: ผู้ใช้สมัคร/ล็อกอิน เลือกหมายเลขและส่งข้อความหาแอดมิน; แอดมินจัดการโปรไฟล์ อัปโหลดภาพหลายรูป และตอบแชตเรียลไทม์ **ไม่ได้แชตกับเจ้าของแต่ละโปรไฟล์โดยตรง**

## ขั้นตอนสั้น

1. สร้าง Firebase project, เปิด Email/Password Auth, Firestore และ Storage
2. เพิ่มเว็บแอป Firebase แล้วนำค่าที่ได้รับลง `firebase-config.js` (แทนที่ `PASTE_...` ทั้งหมด)
3. ติดตั้ง Firebase CLI: `npm install -g firebase-tools`, `firebase login`, `firebase use --add`
4. ลงกฎ **ก่อนเปิดเว็บ**: `firebase deploy --only firestore:rules,storage`
5. ตั้งแอดมินครั้งแรก: ใน Authentication สร้างบัญชี จากนั้นเพิ่ม Firestore document `admins/{UID}` ค่า `role` = `admin`
6. อัปโหลดไฟล์ในโฟลเดอร์นี้ไปยัง **root** ของ GitHub repository (ให้ `index.html` อยู่ระดับบนสุด)
7. GitHub > Settings > Pages > Deploy from a branch > `main` > `/(root)` > Save
8. Firebase Authentication > Settings > Authorized domains > เพิ่ม `YOUR_USERNAME.github.io` (ไม่ใส่ https หรือ path)
9. เปิด `https://YOUR_USERNAME.github.io/REPOSITORY_NAME/` และทดสอบบัญชีผู้ใช้ 2 บัญชี

ดูคำอธิบายละเอียดใน [`คู่มือติดตั้ง-GitHub-Pages.md`](คู่มือติดตั้ง-GitHub-Pages.md)

**สำคัญ**: Firebase web config ไม่ใช่ server secret แต่กฎ Firestore/Storage ต้องปลอดภัย ห้ามอัปโหลด service-account JSON, private key, `.env` หรือรหัสผ่านจริงเข้า GitHub. การอัปโหลดรูปสาธารณะต้องได้รับสิทธิ์และความยินยอมจากเจ้าของภาพ.
