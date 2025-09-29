import argparse
from analyzer import analyze_code

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to Python file to review")
    args = parser.parse_args()

    report = analyze_code(args.file)

    output_path = "reports/review_report.txt"
    with open(output_path, "w") as f:
        for line in report:
            f.write(line + "\n")

    print(f"✅ Review report saved at {output_path}")
