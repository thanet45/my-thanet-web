<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔮 เว็บหมอดูไฮเทค v2</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }

        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            max-width: 450px;
            width: 100%;
            text-align: center;
            margin-bottom: 20px;
        }

        h1 { color: #f1c40f; margin-bottom: 10px; }
        
        .form-group {
            margin: 20px 0;
            text-align: left;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #f39c12;
        }

        input[type="text"], input[type="date"] {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            box-sizing: border-box;
            font-size: 16px;
        }

        .crystal-ball {
            font-size: 70px;
            margin: 15px 0;
            transition: transform 0.2s;
        }

        .shake { animation: shake 0.5s; }
        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(0px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            100% { transform: translate(1px, -2px) rotate(-1deg); }
        }

        button {
            background-color: #e74c3c;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            transition: 0.3s;
            font-weight: bold;
            width: 100%;
        }

        button:hover {
            background-color: #c0392b;
            box-shadow: 0 0 15px #e74c3c;
        }

        #result {
            font-size: 18px;
            margin-top: 25px;
            padding: 15px;
            background: rgba(0,0,0,0.3);
            border-radius: 10px;
            border-left: 5px solid #f1c40f;
            display: none;
            text-align: left;
            line-height: 1.6;
        }

        /* โซนแก้ไขคำทำนายด้านล่าง */
        .admin-panel {
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 15px;
            max-width: 450px;
            width: 100%;
            box-sizing: border-box;
        }

        .admin-panel h3 { color: #2ecc71; margin-top: 0; }

        .add-fortune-box {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }

        .add-fortune-box button {
            background-color: #2ecc71;
            width: auto;
            white-space: nowrap;
        }
        .add-fortune-box button:hover { background-color: #27ae60; }

        .fortune-list {
            text-align: left;
            max-height: 150px;
            overflow-y: auto;
            background: rgba(255,255,255,0.05);
            padding: 10px;
            border-radius: 8px;
        }

        .fortune-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            font-size: 14px;
        }

        .delete-btn {
            background: #ff7675;
            color: white;
            border: none;
            padding: 2px 8px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            width: auto;
        }
        .delete-btn:hover { background: #d63031; }
    </style>
</head>
<body>

    <!-- ส่วนที่ 1: หน้าดูดวงสำหรับผู้ใช้ -->
    <div class="container">
        <h1>🔮 มหาหมอดูแม่นยำ</h1>
        <p>กรอกข้อมูลของท่านเพื่อผูกดวงชะตา</p>
        
        <div class="form-group">
            <label>ชื่อ-นามสกุล:</label>
            <input type="text" id="username" placeholder="กรอกชื่อของคุณ">
        </div>

        <div class="form-group">
            <label>วันเดือนปีเกิด:</label>
            <input type="date" id="birthdate">
        </div>
        
        <div id="ball" class="crystal-ball">🔮</div>
        
        <button onclick="fortuneTelling()">ทำนายดวงชะตา</button>
        
        <!-- ส่วนแสดงผลลัพธ์ -->
        <div id="result"></div>
    </div>

    <!-- ส่วนที่ 2: ระบบจัดการคำทำนาย (แก้ไข/เพิ่ม/ลบ) -->
    <div class="admin-panel">
        <h3>🛠️ ระบบจัดการคำทำนาย (สุ่ม)</h3>
        <div class="add-fortune-box">
            <input type="text" id="newFortuneText" placeholder="พิมพ์คำทำนายใหม่ที่นี่...">
            <button onclick="addFortune()">เพิ่ม</button>
        </div>
        <div class="fortune-list" id="fortuneListContainer">
            <!-- รายการคำทำนายจะถูกใส่ด้วย JavaScript ตรงนี้ -->
        </div>
    </div>

    <script>
        // คำทำนายเริ่มต้น (จะเซฟลง LocalStorage เพื่อให้แก้ไขได้ตลอดไป)
        const defaultFortunes = [
            "🟢 วันนี้โชคดีมาก! สิ่งที่หวังไว้จะสำเร็จแบบงงๆ",
            "🔴 ช่วงนี้พักผ่อนน้อยนะ ระวังลืมกระเป๋าตังค์หรือของสำคัญ",
            "🟡 การเงินกำลังจะปัง มีเกณฑ์ได้ลาภลอยแบบไม่คาดฝัน",
            "🔵 ความรักคนโสดจะมีคนทักมา ส่วนคนมีคู่แฟนจะสายเปย์",
            "🟠 วันนี้ทำอะไรก็ราบรื่น ลุยได้เลยลูกพี่!"
        ];

        // โหลดข้อมูลคำทำนายจากเบราว์เซอร์ ถ้าไม่มีให้ใช้ค่าเริ่มต้น
        let fortunes = JSON.parse(localStorage.getItem('myFortunes')) || defaultFortunes;

        // ฟังก์ชันแสดงรายการคำทำนายในระบบจัดการ
        function renderFortuneList() {
            const container = document.getElementById('fortuneListContainer');
            container.innerHTML = '';
            fortunes.forEach((fortune, index) => {
                container.innerHTML += `
                    <div class="fortune-item">
                        <span>${index + 1}. ${fortune}</span>
                        <button class="delete-btn" onclick="deleteFortune(${index})">ลบ</button>
                    </div>
                `;
            });
        }

        // ฟังก์ชันเพิ่มคำทำนายใหม่
        function addFortune() {
            const input = document.getElementById('newFortuneText');
            if (input.value.trim() !== '') {
                fortunes.push(input.value.trim());
                localStorage.setItem('myFortunes', JSON.stringify(fortunes)); // เซฟลงเครื่อง
                input.value = '';
                renderFortuneList();
            } else {
                alert('กรุณาพิมพ์ข้อความคำทำนายก่อนกดเพิ่มครับ');
            }
        }

        // ฟังก์ชันลบคำทำนาย
        function deleteFortune(index) {
            if(fortunes.length <= 1) {
                alert('ต้องเหลือคำทำนายไว้อย่างน้อย 1 ข้อนะครับ!');
                return;
            }
            fortunes.splice(index, 1);
            localStorage.setItem('myFortunes', JSON.stringify(fortunes)); // เซฟลงเครื่อง
            renderFortuneList();
        }

        // ฟังก์ชันคำนวณและสุ่มดวง
        function fortuneTelling() {
            const name = document.getElementById('username').value.trim();
            const birthdate = document.getElementById('birthdate').value;
            const ball = document.getElementById('ball');
            const resultBox = document.getElementById('result');

            // ตรวจสอบว่ากรอกข้อมูลครบไหม
            if (!name || !birthdate) {
                alert('กรุณากรอกชื่อและเลือกวันเดือนปีเกิดก่อนดูดวงครับ!');
                return;
            }

            // แปลงวันที่เพื่อนำมาแสดงโชว์แบบสวยๆ
            const dateObj = new Date(birthdate);
            const formattedDate = dateObj.toLocaleDateString('th-TH', {
                year: 'numeric', month: 'long', day: 'numeric'
            });

            // เอฟเฟกต์เขย่าลูกแก้ว
            ball.classList.add('shake');
            resultBox.style.display = 'none';

            setTimeout(() => {
                ball.classList.remove('shake');
                
                // สุ่มคำทำนายจากรายการที่แก้ไขได้
                const randomIndex = Math.floor(Math.random() * fortunes.length);
                const randomFortune = fortunes[randomIndex];
                
                // แสดงผลลัพธ์ดวงชะตาแบบเจาะจงบุคคล
                resultBox.innerHTML = `
                    <strong>👤 คุณ:</strong> ${name}<br>
                    <strong>📅 เกิดวันที่:</strong> ${formattedDate}<br>
                    <hr style="border: 0.5px solid rgba(255,255,255,0.2); margin: 10px 0;">
                    <strong>🔮 ดวงชะตาของคุณในวันนี้:</strong><br>
                    ${randomFortune}
                `;
                resultBox.style.display = 'block';
            }, 500);
        }

        // สั่งให้แสดงรายการคำทำนายทันทีที่เปิดเว็บขึ้นมา
        renderFortuneList();
    </script>

</body>
</html>
