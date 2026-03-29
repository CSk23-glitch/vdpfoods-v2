import os

files = [
    r"d:\videepthaFoods\VideepthaWeb2\Videeptawebsite-frontend\website-frontend\src\components\Header.tsx",
    r"d:\videepthaFoods\VideepthaWeb2\Videeptawebsite-frontend\website-frontend\src\components\MobileBottomBar.tsx",
    r"d:\videepthaFoods\VideepthaWeb2\Videeptawebsite-frontend\website-frontend\src\components\PromotionSection.tsx"
]

def fix_colors(content):
    # Backgrounds and Borders
    content = content.replace("bg-white/5", "bg-[var(--color-panel)]")
    content = content.replace("bg-white/10", "bg-[var(--color-panel)]")
    content = content.replace("border-white/5", "border-[var(--color-border)]")
    content = content.replace("border-white/10", "border-[var(--color-border)]")
    content = content.replace("bg-[#1a1d18]", "bg-[var(--color-surface)]")
    content = content.replace("bg-[#1a1d17]", "bg-[var(--color-surface)]")
    content = content.replace("bg-black/80", "bg-[var(--color-surface)]/80")

    # Texts
    content = content.replace("text-white", "text-[var(--color-text)]")
    content = content.replace("text-slate-200", "text-[var(--color-text)]/90")
    content = content.replace("text-slate-300", "text-[var(--color-text)]/80")
    content = content.replace("text-slate-400", "text-[var(--color-text)]/60")
    content = content.replace("text-slate-500", "text-[var(--color-text)]/40")
    
    # Specific hover bugs
    content = content.replace("hover:bg-[var(--color-panel)]", "hover:bg-[var(--color-panel)]") # Actually ok

    return content

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = fix_colors(content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Headers and Footers fixed!")
