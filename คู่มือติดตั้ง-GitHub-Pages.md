# คู่มือติดตั้ง NOIR HOST LIVE ลง GitHub Pages (ภาษาไทย)

## 1) ตรวจไฟล์ก่อนอัปโหลด
ภายใน ZIP นี้ประกอบด้วย:

```text
index.html                  หน้าเว็บหลัก (ต้องอยู่ root)
style.css                   ธีมดำ-ทอง รองรับมือถือ
app.js                      ฟังก์ชันหน้าเว็บและ Firebase
firebase-config.js          ค่าเชื่อมต่อ Firebase ที่ต้องกรอกเอง
.nojekyll                   ปิด Jekyll สำหรับ GitHub Pages
.gitignore                  ป้องกันการ commit ไฟล์เฉพาะเครื่อง
firestore.rules             กฎแชตและโปรไฟล์
storage.rules               กฎรูปภาพ
firebase.json               กำหนด Firebase CLI สำหรับ deploy rules
README.md                   ข้อมูลโครงการ
คู่มือติดตั้ง-GitHub-Pages.md   คู่มือฉบับนี้
```

**ไฟล์ที่อัปโหลดต้องอยู่ใน repository root** ไม่ใช่โฟลเดอร์ซ้อน เช่น `repo/NOIR_HOST_GITHUB_PAGES/index.html` เพราะจะทำให้ลิงก์ GitHub Pages ที่ root แสดงหน้าไม่ถูกต้อง

## 2) สร้าง Firebase ก่อนเปิดเว็บจริง
1. ไป https://console.firebase.google.com/ > สร้าง Project
2. Authentication > Sign-in method > เปิด Email/Password
3. Firestore Database > Create database (เลือกภูมิภาคตามต้องการ)
4. Storage > Get started (อาจมีเงื่อนไขการเปิดการเรียกเก็บเงินตามโปรเจ็กต์)
5. Project settings > Your apps > เพิ่ม Web app และคัดลอก firebaseConfig
6. เปิดไฟล์ `firebase-config.js` กรอกค่า 6 ตัวจาก Firebase **ห้ามใช้ข้อความ PASTE เดิม** และอย่าลบ `export const firebaseConfig`

Firebase Web API key สามารถอยู่ฝั่งหน้าเว็บได้ แต่ต้องใช้ Firebase Security Rules จำกัดสิทธิ์ ไม่ควรใส่ private key หรือ service account ในไฟล์นี้

## 3) นำกฎความปลอดภัยขึ้น Firebase (ทำก่อนแชร์เว็บ)
ติดตั้ง Node.js LTS จาก https://nodejs.org/ แล้วเปิด Terminal ที่โฟลเดอร์ซึ่งมี `firebase.json` จากนั้นรัน:

```sh
npm install -g firebase-tools
firebase login
firebase use --add
firebase deploy --only firestore:rules,storage
```

คำสั่ง `firebase use --add` ให้เลือกโปรเจ็กต์ Firebase ของคุณ; ไฟล์ `.firebaserc` ถูก ignore โดย Git. ตรวจสอบใน Firebase Console ว่ากฎถูกเผยแพร่เรียบร้อย **ห้ามใช้กฎแบบ `allow read, write: if true`**

## 4) สร้างบัญชีแอดมินคนแรก
1. Firebase Console > Authentication > Users > Add user สร้างอีเมล/รหัสผ่านแอดมิน (อย่างน้อย 8 ตัวอักษรสำหรับฟอร์มเว็บนี้)
2. คัดลอก UID ของบัญชีนั้น
3. Firestore Database > Data > Start collection: `admins`
4. Document ID คือ UID ตรงตัว เพิ่ม field `role` ชนิด string ค่า `admin` และ Save
5. ผู้มี UID ใน collection `admins` จะดูแชตทั้งหมดและแก้ไขโปรไฟล์ได้ เก็บบัญชีนี้ให้ปลอดภัย

## 5) อัปโหลดขึ้น GitHub
1. เข้า https://github.com/new สร้าง Repository ชื่อ `noir-host-live` เลือก Public หากใช้ Pages แบบ Public
2. เปิด Repo > Add file > Upload files
3. แตก ZIP **ก่อน** แล้วเลือกไฟล์ที่อยู่ภายในโฟลเดอร์ `NOIR_HOST_GITHUB_PAGES` ทั้งหมด รวม `.nojekyll` ถ้า file picker แสดงไฟล์ซ่อน
4. กด Commit changes; เปิด repo แล้วตรวจว่ามี `index.html` อยู่ชั้นแรก
5. ไป Settings > Pages > Source: Deploy from a branch > Branch: `main` > Folder: `/(root)` > Save
6. ดูสถานะที่ Actions/Pages; URL ปกติคือ `https://YOUR_USERNAME.github.io/noir-host-live/`

**ข้อสังเกต:** GitHub Pages เป็น static hosting: ไม่ใช่เซิร์ฟเวอร์ Firebase. การแก้ไขไฟล์ผ่าน GitHub อาจต้องรอการเผยแพร่รอบถัดไปจึงจะเห็นหน้าเว็บใหม่

## 6) เพิ่มโดเมนที่อนุญาตให้ล็อกอิน
ใน Firebase Console > Authentication > Settings > Authorized domains กดเพิ่ม `YOUR_USERNAME.github.io` (ไม่ใส่ `https://` หรือ `/noir-host-live/`). ถ้าใช้โดเมนส่วนตัวให้เพิ่มโดเมนนั้นด้วย

## 7) ทดสอบออนไลน์
- เปิดลิงก์ GitHub Pages ในเบราว์เซอร์; ห้ามทดสอบผ่าน `file://`
- ล็อกอินเป็นแอดมิน เพิ่มโปรไฟล์ #01 รูป JPEG/PNG/WebP ไม่เกิน 10 MB ต่อภาพ
- เปิดโหมดไม่ระบุตัวตน สมัครเป็นสมาชิกคนละบัญชี เลือกเบอร์และส่งข้อความ
- กลับไปหน้าแอดมิน > กล่องข้อความ > เปิดแชต > ตอบกลับ ตรวจว่าอีกหน้าต่างเห็นข้อความ
- หากแชตไม่ทำงาน ให้เปิด Developer Tools > Console และตรวจ `firebase-config.js`, กฎ Firestore, Authorized domains, และ Firebase billing/Storage

## 8) ข้อจำกัดและความปลอดภัยก่อนใช้จริง
- ระบบนี้ให้สมาชิกส่งแชตถึง **แอดมิน** ไม่ใช่แชตไปยังเจ้าของรูปโดยตรง
- สมาชิกที่สมัครใหม่ยังไม่มีการยืนยันอีเมลหรือระบบจำกัดสแปม ควรเสริม Firebase App Check, moderation, rate limiting ก่อนเผยแพร่กว้าง
- กฎแชตป้องกันผู้ใช้ทั่วไปอ่านห้องคนอื่น แต่ต้องตรวจเพิ่มเติมตามความเสี่ยงสำหรับธุรกิจจริง
- ภาพโปรไฟล์ที่อัปโหลดเผยแพร่สู่สาธารณะและลิงก์ภาพสามารถแชร์ได้ ควรขอความยินยอมและจัดทำนโยบายส่วนตัว
- ลบโปรไฟล์จากหน้าแอดมินแล้ว **ยังไม่ลบไฟล์ภาพเก่าจาก Storage** และห้องแชตเดิมไม่ได้ถูกลบ
- ไม่มีระบบ backup อัตโนมัติหรือหน้าจัดการลบข้อความตามคำร้อง ต้องเพิ่มก่อนใช้เป็น production
- GitHub repo สาธารณะ: ห้าม commit private keys, service account, password หรือ secrets
- ตรวจข้อกำหนดผู้ให้บริการและข้อกฎหมายท้องถิ่น โดยเฉพาะการใช้ภาพและบริการสำหรับผู้ใหญ่

## 9) เมื่อเปลี่ยนโค้ด
แก้ไฟล์และ commit ไปยัง `main` จากนั้นรอ GitHub Pages deploy; ส่วน `firestore.rules` และ `storage.rules` **ไม่เปลี่ยนใน Firebase โดยอัตโนมัติ** ต้องรัน `firebase deploy --only firestore:rules,storage` ใหม่ทุกครั้งที่แก้กฎ
