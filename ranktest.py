import random

# 学生の数
NUM_STUDENTS = 20

# 教科名
SUBJECTS = ["国語", "英語", "情報"]

# --- ダミーの氏名リスト ---
DUMMY_NAMES = [
    "山下 斗優太", "鈴木 一郎", "高橋 花子", "田中 次郎", "伊藤 さくら", "渡辺 三郎", "山本 美咲", "中村 四郎", "小林 恵子", "加藤 五郎",
    "吉田 あかり", "山田 六郎", "佐々木 陽菜", "山口 七郎", "松本 凛", "井上 八郎", "木村 結衣", "林 九郎", "斎藤 葵", "清水 十郎"
]
# ダミー名の数が学生数より少ない場合のフォールバック
if len(DUMMY_NAMES) < NUM_STUDENTS:
    DUMMY_NAMES.extend([f"生徒_{i+1:02d}" for i in range(len(DUMMY_NAMES), NUM_STUDENTS)])

# --- 1. ダミーデータの生成 ---
students = []
for i in range(NUM_STUDENTS):
    student_name = DUMMY_NAMES[i] # リストから名前を取得
    scores = {subject: random.randint(60, 100) for subject in SUBJECTS} # 各教科0点から100点のランダムな点数
    student_data = {"名前": student_name}
    student_data.update(scores)
    students.append(student_data)

print("--- 生成されたデータ ---")
for student in students:
    print(student)
print("-" * 20)

# --- 2. 合計点の計算 ---
for student in students:
    total_score = sum(student[subject] for subject in SUBJECTS)
    student["合計点"] = total_score

# --- 3. 順位付け (比較による方法) ---
# 各生徒の順位を一旦1位として初期化
for student in students:
    student["順位"] = 1

# 生徒リストを2重ループで比較
for i in range(NUM_STUDENTS):
    for j in range(NUM_STUDENTS):
        # 自分自身とは比較しない
        if i == j:
            continue
        # 生徒iの合計点が、生徒jの合計点より低い場合、生徒iの順位を下げる
        if students[i]["合計点"] < students[j]["合計点"]:
            students[i]["順位"] += 1
            # 同点の場合、順位は同じになる（自分より点数が高い人の数を数えているため）

print("--- 順位付け後 ---")
# 見やすくするために、順位でソートして表示（これは表示のためであり、順位付けアルゴリズム自体は比較で行っています）
students_sorted_by_rank = sorted(students, key=lambda x: x['順位'])

for student in students_sorted_by_rank:
    print(f"順位: {student['順位']}位, 名前: {student['名前']}, 合計点: {student['合計点']}, 国語: {student['国語']}, 英語: {student['英語']}, 情報: {student['情報']}")

print("\nプログラム完了")