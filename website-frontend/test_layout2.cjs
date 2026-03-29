const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 360, height: 760 });
  await page.goto('http://localhost:5176/products');
  await new Promise(r => setTimeout(r, 2000));
  
  const bottomBar = await page.evaluate(() => {
    const el = document.querySelector('.lg\\:hidden.fixed.bottom-0');
    if (!el) return null;
    const rect = el.getBoundingClientRect();
    const style = window.getComputedStyle(el);
    return { 
        className: el.className,
        visible: style.display !== 'none' && style.visibility !== 'hidden',
        rect: { top: rect.top, bottom: rect.bottom, height: rect.height, y: rect.y },
        zIndex: style.zIndex
    };
  });

  const whatsapp = await page.evaluate(() => {
    const el = document.querySelector('.bg-\\[\\#25D366\\]') || document.querySelector('a[href*="wa.me"]');
    if (!el) return null;
    const parent = el.closest('.fixed');
    if (!parent) return null;
    const rect = parent.getBoundingClientRect();
    const style = window.getComputedStyle(parent);
    return {
        visible: style.display !== 'none' && style.visibility !== 'hidden',
        rect: { top: rect.top, bottom: rect.bottom, height: rect.height, y: rect.y },
        zIndex: style.zIndex
    };
  });

  console.log(JSON.stringify({ bottomBar, whatsapp }, null, 2));
  await browser.close();
})();
