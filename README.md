<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ดูดวงแม่นยำระดับโปร | โชคชะตาของคุณ</title>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-color: #00f3ff;
            --bg-color: #0d0d12;
            --card-bg: rgba(20, 20, 30, 0.7);
        }
        body {
            font-family: 'Kanit', sans-serif;
            background-color: var(--bg-color);
            background-image: radial-gradient(circle at 50% 0%, #1a1a3a 0%, var(--bg-color) 70%);
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }
        .container {
            background: var(--card-bg);
            padding: 40px 30px;
            border-radius: 24px;
            box-shadow: 0 8px 32px rgba(0, 243, 255, 0.1);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 243, 255, 0.2);
            max-width: 450px;
            width: 100%;
            text-align: center;
            position: relative;
        }
        h1 {
            color: var(--neon-color);
            text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
            margin-bottom: 5px;
            font-weight: 600;
        }
        select, button, input {
            font-family: 'Kanit', sans-serif;
            width: 100%;
            padding: 12px;
            margin-top: 15px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(0,0,0,0.5);
            color: white;
            font-size: 16px;
            outline: none;
            box-sizing: border-box;
        }
        select:focus, input:focus {
            border-color: var(--neon-color);
            box-shadow: 0 0 8px rgba(0, 243, 255, 0.3);
        }
        button.primary-btn {
            background: linear-gradient(90deg, #0052d4, #4364f7, #6fb1fc);
            border: none;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 20px;
        }
        button.primary-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(111, 177, 252, 0.4);
        }
        #result-card {
            display: none;
            margin-top: 25px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            border-left: 4px solid var(--neon-color);
            text-align: left;
            animation: fadeIn 0.5s ease;
        }
        .share-btn {
            background: transparent;
            border: 1px solid var(--neon-color);
            color: var(--neon-color);
            margin-top: 15px;
            cursor: pointer;
            transition: 0.3s;
        }
        .share-btn:hover {
            background: var(--neon-color);
            color: #000;
        }
        
        /* Loading Animation */
        .loader {
            display: none;
            border: 3px solid rgba(255,255,255,0.1);
            border-top: 3px solid var(--neon-color);
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }

        /* Admin Settings Icon */
        .settings-icon {
            position: absolute;
            top: 20px;
            right: 20px;
            cursor: pointer;
            font-size: 20px;
            opacity: 0.6;
            transition: 0.3s;
        }
        .settings-icon:hover {
            opacity: 1;
            color: var(--neon-color);
        }

        /* Admin Modal */
        #admin-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
            z-index: 100;
        }
        .modal-content {
            background: #1a1a2e;
            padding: 30px;
            border-radius: 16px;
            width: 90%;
            max-width: 500px;
            max-height: 80vh;
            overflow-y: auto;
            border: 1px solid #333;
        }
        .fortune-item {
            display: flex;
            justify-content: space-between;
            background: rgba(255,255,255,0.05);
            padding: 10px;
            margin-top: 10px;
            border-radius: 8px;
            font-size: 14px;
        }
        .delete-btn {
            background: #ff4757;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 6px;
            cursor: pointer;
            margin-top: 0;
            width: auto;
        }

        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

    <div class="container">
        <div class="settings-icon" onclick="toggleAdminModal()">⚙️</div>
        <h1>✨ ศาสตร์แห่งดวงดาว</h1>
        <p style="color: #aaa; font-size: 14px;">วิเคราะห์โชคชะตาของคุณในวันนี้</p>
        
        <select id="zodiac-select">
            <option value="" disabled selected>-- กรุณาเลือกราศีของคุณ --</option>
            <option value="มังกร">ราศีมังกร (15 ม.ค. - 12 ก.พ.)</option>
            <option value="กุมภ์">ราศีกุมภ์ (13 ก.พ. - 14 มี.ค.)</option>
            <option value="มีน">ราศีมีน (15 มี.ค. - 12 เม.ย.)</option>
            <option value="เมษ">ราศีเมษ (13 เม.ย. - 14 พ.ค.)</option>
            <!-- สามารถพิมพ์เพิ่มให้ครบ 12 ราศีได้ -->
        </select>
        
        <button class="primary-btn" onclick="predict()">เริ่มต้นอ่านคำทำนาย</button>
        
        <div class="loader" id="loader"></div>
        
        <div id="result-card">
            <h3 style="margin-top: 0; color: var(--neon-color);" id="result-title"></h3>
            <p id="result-text" style="font-size: 16px; line-height: 1.6;"></p>
            <button class="share-btn" onclick="shareResult()">📤 แชร์คำทำนาย</button>
        </div>
    </div>

    <!-- Admin Modal สำหรับแก้ไขคำทำนาย -->
    <div id="admin-modal">
        <div class="modal-content">
            <h2 style="color: var(--neon-color); margin-top: 0;">ตั้งค่าคำทำนาย</h2>
            <div style="display: flex; gap: 10px;">
                <input type="text" id="new-fortune" placeholder="เพิ่มคำทำนายใหม่ที่นี่...">
                <button class="primary-btn" style="width: auto; margin-top: 15px;" onclick="addFortune()">เพิ่ม</button>
            </div>
            <div id="fortune-list" style="margin-top: 20px;"></div>
            <button class="share-btn" onclick="toggleAdminModal()">ปิดหน้าต่าง</button>
        </div>
    </div>

    <!-- พื้นที่สำหรับฝัง Code: LINE Official Account / Facebook Messenger Floating Chat -->
    <!-- นำ Script ของ Social แชทมาวางก่อนปิด </body> ได้เลยครับ -->

    <script>
        // ชุดคำทำนายเริ่มต้น
        const defaultFortunes = [
            "จังหวะชีวิตกำลังขาขึ้น การงานที่ติดขัดจะได้รับการช่วยเหลือจากผู้ใหญ่",
            "ระวังปัญหาการสื่อสารในทีม ควรใช้ความใจเย็นและรับฟังให้มากขึ้นในวันนี้",
            "การเงินโดดเด่น มีโอกาสได้ผลตอบแทนจากการลงทุนหรือโปรเจกต์พิเศษ",
            "ความรักสดใส คนโสดมีเกณฑ์พบคนสไตล์เดียวกันผ่านงานอดิเรก",
            "วันนี้พลังงานคุณอาจลดลง ควรหลีกเลี่ยงการตัดสินใจเรื่องใหญ่ๆ"
        ];

        // โหลดข้อมูลจาก Local Storage หรือใช้ค่าเริ่มต้น
        let fortunes = JSON.parse(localStorage.getItem('fortunes')) || defaultFortunes;

        function saveFortunes() {
            localStorage.setItem('fortunes', JSON.stringify(fortunes));
            renderAdminList();
        }

        // ฟังก์ชันประมวลผลคำทำนาย
        function predict() {
            const zodiac = document.getElementById('zodiac-select').value;
            if(!zodiac) {
                alert("กรุณาเลือกราศีก่อนครับ");
                return;
            }

            const loader = document.getElementById('loader');
            const resultCard = document.getElementById('result-card');
            
            resultCard.style.display = 'none';
            loader.style.display = 'block';
            
            setTimeout(() => {
                loader.style.display = 'none';
                
                // สุ่มคำทำนาย
                const randomIndex = Math.floor(Math.random() * fortunes.length);
                const fortuneText = fortunes[randomIndex];
                
                document.getElementById('result-title').innerText = `ดวงของชาวราศี${zodiac}`;
                document.getElementById('result-text').innerText = fortuneText;
                
                resultCard.style.display = 'block';
            }, 1500); // จำลองเวลาประมวลผล 1.5 วินาที
        }

        // ฟังก์ชันแชร์ (รองรับบนมือถือ)
        async function shareResult() {
            const title = document.getElementById('result-title').innerText;
            const text = document.getElementById('result-text').innerText;
            
            if (navigator.share) {
                try {
                    await navigator.share({
                        title: 'คำทำนายของฉัน',
                        text: `${title}\n"${text}"\nมาดูดวงของคุณบ้างสิ!`,
                        url: window.location.href
                    });
                } catch (err) {
                    console.log('Share canceled or failed', err);
                }
            } else {
                // กรณีใช้บน PC ที่ไม่รองรับ Web Share API ให้คัดลอกลง Clipboard แทน
                navigator.clipboard.writeText(`${title}\n${text}`);
                alert("คัดลอกคำทำนายเรียบร้อยแล้ว! นำไปวางในแชทได้เลย");
            }
        }

        // ---------------- ฟังก์ชันฝั่ง Admin (จัดการข้อความ) ----------------
        
        function toggleAdminModal() {
            const modal = document.getElementById('admin-modal');
            modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex';
            if(modal.style.display === 'flex') renderAdminList();
        }

        function addFortune() {
            const input = document.getElementById('new-fortune');
            if(input.value.trim() !== '') {
                fortunes.push(input.value.trim());
                saveFortunes();
                input.value = '';
            }
        }

        function deleteFortune(index) {
            if(fortunes.length <= 1) {
                alert("ต้องเหลือคำทำนายอย่างน้อย 1 ข้อครับ");
                return;
            }
            fortunes.splice(index, 1);
            saveFortunes();
        }

        function renderAdminList() {
            const list = document.getElementById('fortune-list');
            list.innerHTML = '';
            fortunes.forEach((fortune, index) => {
                list.innerHTML += `
                    <div class="fortune-item">
                        <span style="flex-grow: 1; padding-right: 10px;">${index + 1}. ${fortune}</span>
                        <button class="delete-btn" onclick="deleteFortune(${index})">ลบ</button>
                    </div>
                `;
            });
        }
    </script>
</body>
</html>
