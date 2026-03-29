import os

file_path = r"d:\videepthaFoods\VideepthaWeb2\Videeptawebsite-frontend\website-frontend\src\pages\ProductDetailPage.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make bulk replacements
# General Backgrounds and Borders
content = content.replace("bg-white/5", "bg-[var(--color-panel)]")
content = content.replace("border-white/10", "border-[var(--color-border)]")
content = content.replace("bg-black/50", "bg-[var(--color-surface)]")
content = content.replace("border-white/5", "border-[var(--color-border)]")

# Typography
content = content.replace("text-slate-200", "text-[var(--color-text)]")
content = content.replace("text-slate-300", "text-[var(--color-text)]/90")
content = content.replace("text-slate-400", "text-[var(--color-text)]/70")
content = content.replace("text-slate-500", "text-[var(--color-text)]/50")
content = content.replace("text-slate-600", "text-[var(--color-text)]/40")

# Primary Headers (Carefully avoid replacing the button gradient text-white)
content = content.replace("text-white mb-6", "text-[var(--color-text)] mb-6")
content = content.replace("text-white mb-8", "text-[var(--color-text)] mb-8")
content = content.replace("text-white mb-2", "text-[var(--color-text)] mb-2")
content = content.replace("text-white mb-1", "text-[var(--color-text)] mb-1")
content = content.replace("text-white italic", "text-[var(--color-text)] italic")
content = content.replace("text-white hover", "text-[var(--color-text)] hover")
content = content.replace("text-white\">Fast Delivery", "text-[var(--color-text)]\">Fast Delivery")
content = content.replace("text-white\">Pure Organic", "text-[var(--color-text)]\">Pure Organic")
content = content.replace("text-white\">Farm Fresh", "text-[var(--color-text)]\">Farm Fresh")

# Specifically fixing the heart button (the unclickable / invisible issue)
content = content.replace(
    "'bg-[var(--color-panel)] border-[var(--color-border)] text-white hover:bg-white/10'",
    "'bg-[var(--color-panel)] border-[var(--color-border)] text-[var(--color-text)] hover:bg-[var(--color-border)] z-10 relative'"
)

# And fix any leftover button styles that used white
content = content.replace(
    "hover:bg-white/10",
    "hover:bg-[var(--color-text)]/10"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Styles updated successfully!")
