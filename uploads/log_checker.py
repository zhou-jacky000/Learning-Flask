import os
import csv

# 可自訂關鍵字
KEYWORDS = ["FAIL", "ERROR", "ASSERT", "PANIC"]

def scan_log_file(file_path):
    issues = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f, start=1):
            for kw in KEYWORDS:
                if kw in line:
                    issues.append((i, kw, line.strip()))
    return issues

def scan_selected_then_all(folder_path, primary_log_name="pretest.log", output_csv=False):
    primary_log_path = os.path.join(folder_path, primary_log_name)

    if not os.path.exists(primary_log_path):
        print(f"❌ 無法找到主 log：{primary_log_path}")
        return

    print(f"🔍 優先分析主 log：{primary_log_name}\n")
    primary_issues = scan_log_file(primary_log_path)

    if not primary_issues:
        print("✅ 主 log 無異常，停止後續分析。")
        return

    print(f"🚨 主 log 發現異常，繼續分析其他 log...\n")
    print(f"🔧 {primary_log_name} 異常摘要：")
    for line_num, kw, content in primary_issues:
        print(f"  ➤ [{kw}] 第 {line_num} 行：{content}")

    summary = [{
        "File": primary_log_name,
        "Keyword Hits": len(primary_issues),
        "Details": primary_issues
    }]

    # 開始分析其他 log 檔案
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file == primary_log_name or not file.endswith((".log", ".txt")):
            continue
        result = scan_log_file(full_path)
        if result:
            print(f"\n🚨 發現異常：{file}")
            for line_num, kw, content in result:
                print(f"  ➤ [{kw}] 第 {line_num} 行：{content}")
            summary.append({
                "File": file,
                "Keyword Hits": len(result),
                "Details": result
            })

    if output_csv:
        csv_path = os.path.join(folder_path, "log_summary.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["File", "Line", "Keyword", "Content"])
            for entry in summary:
                for line_num, kw, content in entry["Details"]:
                    writer.writerow([entry["File"], line_num, kw, content])
        print(f"\n📁 匯出報表：{csv_path}")

    print(f"\n✅ 分析完成，共 {len(summary)} 筆異常 log 檔。")

# ===== 主程式執行區 =====
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="先分析主 log，再視狀況分析其他 log")
    parser.add_argument("folder", help="log 資料夾路徑")
    parser.add_argument("--primary", default="Summary-Run-QuickStress.log", help="主 log 檔名（預設：pretest.log）")
    parser.add_argument("--csv", action="store_true", help="是否匯出分析報表 (CSV)")
    args = parser.parse_args()

    scan_selected_then_all(args.folder, args.primary, args.csv)
