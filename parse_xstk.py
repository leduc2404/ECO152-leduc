import json
import re

def parse():
    with open(r"d:\KTHP 2026\datalab-output-on-tap-mon-xac-suat-thong-ke-30-cau-trac-nghiem_copy.pdf.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Parse multiple choice
    tracnghiem_questions = []
    mc_section = content.split("## 30 câu trắc nghiệm")[1].split("## **10 câu hỏi ngắn**")[0]

    parts = re.split(r'(?:\*\*)?\d+\.\s*\(0\.200\s*Point\)(?:\*\*)?', mc_section)
    parts = [p.strip() for p in parts if p.strip()]

    for i, part in enumerate(parts):
        lines = part.split('\n')
        question_text_lines = []
        options = []
        correct_answer = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            opt_match = re.match(r'^(?:-\s*)?(?:\\\*)?(?:\*)?([A-D])\.\s*(.*)', line)
            if opt_match:
                letter = opt_match.group(1)
                text = opt_match.group(2)
                
                is_correct = False
                if r'\*' in line or line.startswith('*') or line.startswith('- *'):
                    is_correct = True
                
                options.append(f"{letter}. {text}")
                if is_correct:
                    correct_answer = letter
            else:
                question_text_lines.append(line)
                
        q_obj = {
            "id": i + 1,
            "category": "Xác suất thống kê",
            "question": " ".join(question_text_lines),
            "options": options,
            "correct_answer": correct_answer
        }
        tracnghiem_questions.append(q_obj)

    with open(r"d:\KTHP 2026\ECO152-leduc\data\xstk_tracnghiem.json", "w", encoding="utf-8") as f:
        json.dump(tracnghiem_questions, f, ensure_ascii=False, indent=2)

    # Parse short answer
    tuluan_questions = []
    sa_section = content.split("## **10 câu hỏi ngắn**")[1].split("## **ĐÁP ÁN CÂU NGẮN**")[0]

    sa_parts = re.split(r'(?:\*\*)?\d+\.\s*\(0\.400\s*Point\)(?:\*\*)?', sa_section)
    sa_parts = [p.strip() for p in sa_parts if p.strip()]

    answers_section = content.split("## **ĐÁP ÁN PHẦN CÂU HỎI NGẮN**")[1]
    answers_lines = [line.strip() for line in answers_section.split('\n') if line.strip() and line.strip().startswith('|')]

    answers_map = {}
    for line in answers_lines[2:]: 
        parts = line.split('|')
        if len(parts) >= 3:
            q_num = parts[1].strip()
            ans = parts[2].strip()
            if q_num.isdigit():
                answers_map[int(q_num)] = ans

    for i, part in enumerate(sa_parts):
        q_id = i + 31
        q_obj = {
            "id": q_id,
            "category": "Xác suất thống kê",
            "question": part.replace('\n', ' ').strip(),
            "answer": answers_map.get(q_id, "")
        }
        tuluan_questions.append(q_obj)

    with open(r"d:\KTHP 2026\ECO152-leduc\data\xstk_tuluan.json", "w", encoding="utf-8") as f:
        json.dump(tuluan_questions, f, ensure_ascii=False, indent=2)

    print(f"Parsed {len(tracnghiem_questions)} multiple choice questions.")
    print(f"Parsed {len(tuluan_questions)} short answer questions.")

if __name__ == "__main__":
    parse()
