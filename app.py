import streamlit as st
import random

# ====================
# 1. 頁面設定與 CSS
# ====================
st.set_page_config(page_title="慾望輪盤：最終硬核生理版", page_icon="🔞", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 3.5em; font-size: 18px !important; font-weight: bold; border-radius: 12px; }
    .card-box { padding: 25px; border-radius: 15px; background-color: #262730; border: 2px solid #ff4b4b; margin-bottom: 20px; }
    .punish-box { border-color: #ff0000 !important; background-color: #3d0000 !important; }
    .dom-tag { color: #ff88ff; font-weight: bold; text-decoration: underline; }
    .sub-tag { color: #88ccff; font-weight: bold; text-decoration: underline; }
    .role-indicator { font-size: 16px; padding: 10px; border-radius: 8px; text-align: center; margin-bottom: 15px; border: 1px solid #444; }
    .dom-role { background-color: #4b0082; color: white; }
    .sub-role { background-color: #2e2e2e; color: #aaaaaa; }
    .rest-alert { background-color: #004d40; padding: 15px; border-radius: 10px; text-align: center; border: 2px solid #00bfa5; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# ====================
# 2. 原始指令資料庫 (保持原始文字)
# ====================
levels = {
    'S': [
        "S1: 嗅覺誘惑 - {sub}閉眼，{dom}把遙控跳蛋塞進你騷逼裡開震，同時舔你耳朵說「等下{dom}要操到你噴水求饒」。",
        "S2: 溫度反差 - 用冰塊磨{sub}陰蒂/龜頭，再用熱蠟滴在奶頭和大腿根，讓{sub}爽到哭著叫爸爸。",
        "S3: 沉默的觸摸 - 10分鐘不准出聲，{dom}用指甲刮{sub}屁眼和會陰，誰先浪叫誰就是欠操的母狗。",
        "S4: 濕度評測 - {sub}用騷逼/硬雞巴磨{dom}，直到{dom}說「夠濕了，準備被操爛」為止。",
        "S5: 呼吸控制 - {dom}掐著{sub}脖子狂吻，讓你喘不過氣，臉紅到翻白眼求{dom}幹你。",
        "S6: 專屬氣味 - 戴眼罩的{sub}用舌頭舔{dom}的奶頭、腋下、屁眼，猜出3個最騷的地方才准停。",
        "S7: 專注的口慾 - {sub}給{dom}站好不准動，{dom}舔你奶頭和會陰5分鐘，就是不碰你下面，讓你急到滴水。",
        "S8: 四肢綑綁 - 用手銬把{sub}綁成M字腿騷逼大開，{dom}要慢慢欣賞你發浪。",
        "S9: 羽毛輕拂 - 用羽毛刷{sub}腳底、奶頭、陰囊/陰唇3分鐘，讓你癢到扭腰求{dom}直接插進來。",
        "S10: 情慾繪畫 - 用潤滑液在{sub}身上寫「公用肉便器」「操爛我」「{dom}的專屬雞巴套」，錯一個就用鞭子抽奶頭。",
        "S11: 內衣透視 - 穿開檔情趣內衣+乳夾，{dom}隔著布料用遙控跳蛋震你陰蒂/龜頭3分鐘，讓你浪叫求脫。",
        "S12: 慾望脫線 - 穿開檔內褲，{dom}用手指慢慢掰開{sub}陰唇/包皮，拉長3分鐘，讓騷水流滿地。"
    ],
    'D': [
        "D1: 口頭服從 - {sub}跪下叫十聲「{dom}操我」，然後舔{dom}屁眼或腳趾，像條母狗一樣。",
        "D2: 等待的懲罰 - 快射/噴時{dom}立刻停，逼{sub}在60秒內哭著說「{dom}我錯了，請操爛我的騷逼/雞巴」。",
        "D3: 姿勢鎖定 - 維持狗爬式或M字腿，{dom}用假屌或電擊貼片慢慢玩{sub}騷穴/雞巴。",
        "D4: 發號施令 - 不碰{sub}下面，只用最髒的話命令你自己插肛塞或摳逼，邊做邊說「我好欠操」。",
        "D5: 雙重限制 - {dom}戴眼罩，塞{sub}口球，只靠你扭屁股的程度決定用多大力玩乳夾。",
        "D6: 慾望懲罰 - 接下來10次求饒就用鞭子抽{sub}屁股或滴蠟在奶頭，讓你記住誰是主人。",
        "D7: 完全靜止 - {sub}雙手舉高過頭不准動，{dom}滴蠟滿你奶頭和大腿內側。",
        "D8: 語音剝奪 - 塞口球只准流口水扭逼，表示想被{dom}操爛。",
        "D9: 口頭控制 - {sub}雙手舉高，{dom}命令「把腿張到最大」「翹屁股求插」「叫給{dom}聽」。",
        "D10: 高潮懸崖 - 計時10分鐘，誰先射誰就戴鎖精環+肛塞當一晚肉便器。"
    ],
    'T': [
        "T1: 無手挑戰 - 把跳蛋塞進{sub}騷逼/貼在雞巴上開最大檔5分鐘，{dom}只舔其他地方，讓你爽到發瘋。",
        "T2: 鎖精耐久 - 戴鎖精環+肛塞，{dom}用飛機杯或假屌磨你，就是不讓你射，讓{sub}哭著求饒。",
        "T3: 主人與奴僕 - {dom}戴假屌，{sub}戴眼罩+手銬+口球，跪著用身體磨求{dom}插進去。",
        "T4: 八抓椅極限 - 把{sub}綁在八抓椅上，用跳蛋+假屌+乳夾+電擊貼片同時操爛你。",
        "T5: 振動轉移 - 先用跳蛋震{sub}陰蒂/龜頭3分鐘，再轉移到肛塞，前後一起爽到你失禁。",
        "T6: 飛機杯的試煉 - {sub}自己用飛機杯，{dom}隨時抽走或用鞭子抽，讓你哭著求{dom}讓你射。",
        "T7: 手銬解鎖 - 手銬鎖{sub}，把鑰匙塞{dom}屁眼，讓你用舌頭挖出來舔乾淨。",
        "T8: 假屌感官遊走 - 用假屌頭磨{sub}奶頭、陰蒂、屁眼，就是不插進去，讓你急到發浪。",
        "T9: 道具三明治 - 同時用手、口、跳蛋、假屌、肛塞操{sub}三穴，直到你崩潰噴水。",
        "T10: 雙重振動 - 前面塞跳蛋，後面塞震動肛塞，奶頭夾乳夾，同時開最大檔。",
        "T11: 自慰棒引導 - {dom}用自慰棒狂插{sub}騷逼/屁眼，你必須同時用假屌回操{dom}。",
        "T12: 自慰棒挑戰 - 戴眼罩的{sub}用自慰棒找{dom}身上最敏感的點，找錯就電擊奶頭。",
        "T13: 電玩模式 - 用手機App控制跳蛋+肛塞+電擊貼片，{sub}猜錯模式就加10秒最高檔。"
    ],
    'P': [
        "P1: 核心三連擊 (60秒) - 20秒狂野女上操到子宮 → 20秒背入撞爛屁股 → 20秒側躺插到翻白眼。",
        "P2: 體力流動 (90秒) - 30秒站立後入抬腿深插 → 30秒抱起來操到腿軟 → 30秒頂到最深處。",
        "P3: 視覺衝擊 (120秒) - 40秒面對鏡子看自己被操到哭 → 40秒單膝跪深喉到吐 → 40秒正面狂吻猛幹。",
        "P4: 單點壓力測試 - 選高難姿勢維持3分鐘，{dom}只用假屌頭狂攻G點或前列腺，讓{sub}噴個不停。",
        "P5: 核心位移 (150秒) - 50秒後入猛幹到子宮 → 50秒抱腿式抬高狂頂 → 50秒側躺鎖喉插爛。",
        "P6: 鏡面反射 - 面對鏡子做傳教士，強制{sub}看著自己被操到失神的騷樣3分鐘。",
        "P7: 橋式懸空 - {sub}橋式翹臀，{dom}從下方用假屌狂頂到你腿抖4分鐘。",
        "P8: 69變形 - 側躺69，輪流深喉到噁心乾嘔5分鐘。",
        "P9: 蓮花深融 - 面對面坐姿，{dom}控制深度猛撞到子宮，{sub}只能抱緊哭喊4分鐘。",
        "P10: 牆壁征服 - {sub}靠牆抬雙腿，{dom}站著狂插到你腿軟站不住5分鐘。"
    ],
    'X': [
        "X1: 核心節奏 - 不准出聲，只用眼神呼吸同步猛幹，錯一次停30秒+鞭打{sub}奶頭10下。",
        "X2: 失敗的代價 - 180秒內必須讓{sub}噴/射，失敗就當一晚肉便器。",
        "X3: 共享邊緣極限 - 5分鐘內同時到邊緣，誰先射誰就當晚被綁起來操到天亮。",
        "X4: 凍結與羞辱 - {dom}有3次凍結權，{sub}動一下就電擊奶頭或陰蒂。",
        "X5: 恒定高難度 - 維持極難姿勢5分鐘狂操，姿勢崩就滴蠟+鞭打重來。",
        "X13: 蠟燭滴滿全身 - 邊狂插邊滴蠟滿奶頭、陰蒂、屁股，讓{sub}痛到爽到哭。",
        "X15: 終極性奴之夜 - 綁在八抓椅上，操{sub}三穴到天亮，當{dom}的專屬肉便器。"
    ]
}

punishments = [
    "懲罰1：跪舔屁眼 - {sub}跪下舔{dom}屁眼60秒，邊舔邊哭。",
    "懲罰2：公開自慰 - 當場摳逼/打手槍到邊緣不准射，{dom}全程觀賞。",
    "懲罰3：乳夾+鞭打 - {sub}戴乳夾2分鐘，被鞭子抽屁股20下。",
    "懲罰4：肛塞過夜 - {sub}塞最大號肛塞過夜，明天早上由{dom}拔出。",
    "懲罰5：鏡前辱罵 - 面對鏡子說30句「我是賤貨」「操爛我的騷逼」之類的髒話。"
]

# ====================
# 3. 核心邏輯函數：生理詞彙自動調整
# ====================
def adjust_body_parts(text, sub_gender):
    if sub_gender == "男性":
        # 男生當受方的替換邏輯
        t = text.replace("騷逼", "騷穴")
        t = t.replace("陰蒂", "龜頭/前列腺")
        t = t.replace("子宮", "前列腺")
        t = t.replace("摳逼", "玩弄後穴")
        t = t.replace("噴水", "失禁高潮")
        t = t.replace("陰唇", "陰囊")
        t = t.replace("母狗", "公狗/賤畜")
    else:
        # 女生當受方的替換邏輯 (防止男生關鍵字出現在女生指令)
        t = text.replace("雞巴", "騷逼")
        t = t.replace("陰囊", "陰唇")
    return t

def finalize_text(text, dom, sub, sub_gender):
    # 先做生理替換
    t = adjust_body_parts(text, sub_gender)
    # 再做名字與 HTML 色彩替換
    t = t.replace("{dom}", f"<span class='dom-tag'>{dom}</span>")
    t = t.replace("{sub}", f"<span class='sub-tag'>{sub}</span>")
    return t

# ====================
# 4. 初始化與狀態
# ====================
for key, val in {
    'p1_score': 0, 'p2_score': 0, 'round': 1, 'game_phase': 'ready',
    'level_index': 0, 'turn_owner': 0, 'success_count': 0, 'total_action_count': 0,
    'current_card': "", 'punishment_text': ""
}.items():
    if key not in st.session_state: st.session_state[key] = val

# 側邊欄設定
with st.sidebar:
    st.title("⚙️ 角色資訊設定")
    p1_name = st.text_input("玩家 1 名字", "主人")
    p1_gender = st.selectbox("玩家 1 性別", ["男性", "女性"], index=0)
    st.divider()
    p2_name = st.text_input("玩家 2 名字", "騷貨")
    p2_gender = st.selectbox("玩家 2 性別", ["女性", "男性"], index=0)
    
    if st.button("🔄 重置遊戲進度"):
        for k in st.session_state.keys(): del st.session_state[k]
        st.rerun()

# 分配當前攻受
if st.session_state.turn_owner == 0:
    current_dom, current_sub = p1_name, p2_name
    current_sub_gender = p2_gender
else:
    current_dom, current_sub = p2_name, p1_name
    current_sub_gender = p1_gender

# ====================
# 5. 遊戲頁面呈現
# ====================
st.title("🔞 慾望輪盤：生理客製整合版")

level_order = ['S', 'D', 'T', 'P', 'X']
cur_lvl_key = level_order[st.session_state.level_index]

# 分數面板
c1, c2, c3 = st.columns(3)
c1.metric(p1_name, st.session_state.p1_score)
c2.metric(p2_name, st.session_state.p2_score)
c3.metric("目前等級", cur_lvl_key, f"成功 {st.session_state.success_count}/3")

st.progress(min((st.session_state.level_index * 3 + st.session_state.success_count) / 15, 1.0))
st.divider()

# 休息提醒 (每5次行動)
if st.session_state.total_action_count > 0 and st.session_state.total_action_count % 5 == 0 and st.session_state.game_phase == 'ready':
    st.markdown("<div class='rest-alert'><h3>🧘 安全時間</h3>請確認彼此體力與心理狀態，補充水分。</div>", unsafe_allow_html=True)

# 角色指示器
st.markdown(f"""
<div style="display: flex; gap: 10px;">
    <div style="flex: 1;" class="role-indicator dom-role">👑 攻：{current_dom}</div>
    <div style="flex: 1;" class="role-indicator sub-role">⛓️ 受：{current_sub} ({current_sub_gender})</div>
</div>
""", unsafe_allow_html=True)

# 遊戲主流程
if st.session_state.game_phase == 'ready':
    if st.button(f"🔥 由 {current_dom} 抽取 {cur_lvl_key} 級指令"):
        raw_card = random.choice(levels[cur_lvl_key])
        st.session_state.current_card = finalize_text(raw_card, current_dom, current_sub, current_sub_gender)
        st.session_state.game_phase = 'action'
        st.rerun()

elif st.session_state.game_phase == 'action':
    st.markdown(f"<div class='card-box'><p style='font-size:22px;'>{st.session_state.current_card}</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    if col1.button("✅ 執行成功 (換手)"):
        # 計分
        if st.session_state.turn_owner == 0: st.session_state.p1_score += (st.session_state.level_index + 1)
        else: st.session_state.p2_score += (st.session_state.level_index + 1)
        
        # 升階邏輯 (每3次)
        st.session_state.success_count += 1
        if st.session_state.success_count >= 3:
            if st.session_state.level_index < 4: st.session_state.level_index += 1
            st.session_state.success_count = 0
            
        st.session_state.total_action_count += 1
        st.session_state.turn_owner = 1 - st.session_state.turn_owner
        st.session_state.game_phase = 'ready'
        st.rerun()

    if col2.button("❌ 失敗/拒絕 (懲罰)"):
        raw_p = random.choice(punishments)
        st.session_state.punishment_text = finalize_text(raw_p, current_dom, current_sub, current_sub_gender)
        st.session_state.game_phase = 'punish'
        st.rerun()

elif st.session_state.game_phase == 'punish':
    st.error("⚠️ 任務失敗，必須接受懲罰")
    st.markdown(f"<div class='card-box punish-box'><p style='font-size:22px;'>{st.session_state.punishment_text}</p></div>", unsafe_allow_html=True)
    
    if st.button("😭 接受懲罰並換手"):
        # X 級摔回 D 邏輯
        if cur_lvl_key == 'X':
            st.session_state.level_index = 1 # Index 1 是 D
            st.toast("💀 慘烈！從 X 級摔回 D 級！")
        elif st.session_state.level_index > 0:
            st.session_state.level_index -= 1
        
        st.session_state.success_count = 0
        st.session_state.total_action_count += 1
        st.session_state.turn_owner = 1 - st.session_state.turn_owner
        st.session_state.game_phase = 'ready'
        st.rerun()
