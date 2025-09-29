# 🛠️ AI Code Reviewer Bot

This project analyzes Python code and generates a **review report** with:  
- Naming conventions  
- Function length / complexity  
- Unused imports  
- Optional AI suggestions  


## 🚀 Features
- Static code analysis using AST
- Optional AI-generated review comments
- Outputs structured report
- Example Python file included


## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
pip install -r requirements.txt
```

## ▶️ Usage
```
python src/pipeline.py --file data/sample_code.py

```

## Output:

Review report saved to reports/review_report.txt

## 📊 Tech Stack

Python

Static analysis: ast, built-in modules

Optional AI: Hugging Face / GPT for natural-language suggestions

## Requirements

```txt
astpretty
flake8
pytest
```


33
