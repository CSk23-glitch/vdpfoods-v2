import os
import re

def fix_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replacements for Tailwind classes
    replacements = [
        (r'bg-\[\#0b0a08\]', r'bg-[var(--color-bg)]'),
        (r'bg-\[\#0a0d08\]', r'bg-[var(--color-bg)]'),
        (r'text-white([^\w/-])', r'text-[var(--color-text)]\1'),
        (r'text-white/40', r'text-[var(--color-text)] opacity-60'),  # Muted text
        (r'text-white/30', r'text-[var(--color-text)] opacity-50'),
        (r'text-white/20', r'text-[var(--color-text)] opacity-40'),
        (r'text-white/10', r'text-[var(--color-text)] opacity-30'),
        (r'text-white/70', r'text-[var(--color-text)] opacity-80'),
        (r'bg-white/\[0\.03\]', r'bg-[var(--color-surface)] border border-[var(--color-primary)]/10 shadow-sm'),
        (r'bg-white/5', r'bg-[var(--color-surface)] border border-[var(--color-primary)]/10'),
        (r'bg-white/10', r'bg-[var(--color-surface)] border border-[var(--color-primary)]/20'),
        (r'border-white/5', r'border-[var(--color-primary)]/10'),
        (r'border-white/10', r'border-[var(--color-primary)]/20'),
        (r'border-white/20', r'border-[var(--color-primary)]/30'),
        (r'hover:bg-white/5', r'hover:bg-[var(--color-primary)]/5'),
        (r'hover:border-white/10', r'hover:border-[var(--color-primary)]/30'),
    ]

    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)

    # Specific Checkout.tsx inline styles replacements
    if 'Checkout.tsx' in filepath:
        content = content.replace("backgroundColor: '#0a0d08'", "backgroundColor: 'var(--color-bg)'")
        content = content.replace("color: '#f1f5f9'", "color: 'var(--color-text)'")
        content = content.replace("color: '#ffffff'", "color: 'var(--color-text)'")
        content = content.replace("color: '#94a3b8'", "color: 'var(--color-text)', opacity: 0.6")
        content = content.replace("background: 'rgba(255, 255, 255, 0.02)'", "background: 'var(--color-surface)'")
        content = content.replace("border: '1px solid rgba(255, 255, 255, 0.05)'", "border: '1px solid rgba(0,0,0,0.05)'")
        content = content.replace("border: '1px solid rgba(255, 255, 255, 0.1)'", "border: '1px solid rgba(0,0,0,0.1)'")
        content = content.replace("backgroundColor: 'rgba(255, 255, 255, 0.03)'", "backgroundColor: 'var(--color-surface)'")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filepath}")

base_dir = r"d:\videepthaFoods\VideepthaWeb2\Videeptawebsite-frontend\website-frontend\src\pages"
fix_file(os.path.join(base_dir, "Account.tsx"))
fix_file(os.path.join(base_dir, "Checkout.tsx"))
