const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
  fs.readdirSync(dir).forEach(f => {
    let dirPath = path.join(dir, f);
    let isDirectory = fs.statSync(dirPath).isDirectory();
    isDirectory ? 
      walkDir(dirPath, callback) : callback(path.join(dir, f));
  });
}

walkDir('./src', function(filePath) {
  if (filePath.endsWith('.tsx') || filePath.endsWith('.ts') || filePath.endsWith('.jsx') || filePath.endsWith('.js') || filePath.endsWith('.css')) {
    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;
    
    // Replace Tailwind classes
    content = content.replace(/\[#5c8d37\]/g, '[var(--color-primary)]');
    content = content.replace(/\[#3e5e25\]/g, '[var(--color-primary)]');
    
    // Replace hexes in quotes
    content = content.replace(/'#5c8d37'/g, "'var(--color-primary)'");
    content = content.replace(/"#5c8d37"/g, '"var(--color-primary)"');
    content = content.replace(/'#3e5e25'/g, "'var(--color-primary)'");
    content = content.replace(/"#3e5e25"/g, '"var(--color-primary)"');

    // Edge cases for background gradients
    content = content.replace(/linear-gradient\(135deg, #5c8d37 0%, #3e5e25 100%\)/g, "var(--color-primary)");
    
    // Catch-all
    content = content.replace(/#5c8d37/g, 'var(--color-primary)');
    content = content.replace(/#3e5e25/g, 'var(--color-primary)');

    if (content !== original) {
      fs.writeFileSync(filePath, content, 'utf8');
      console.log('Fixed:', filePath);
    }
  }
});
