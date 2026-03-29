const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 490, height: 1136 });
  await page.goto('http://localhost:5176', { waitUntil: 'networkidle2' }).catch(e => console.log('goto error:', e.message));
  
  const bottomNav = await page.evaluate(() => {
    const el = document.querySelector('section.fixed.bottom-0');
    if (!el) return null;
    const rect = el.getBoundingClientRect();
    const style = window.getComputedStyle(el);
    return { rect: rect.toJSON(), display: style.display, visibility: style.visibility, opacity: style.opacity, zIndex: style.zIndex, transform: style.transform };
  });
  
  const whatsappNav = await page.evaluate(() => {
    const el = document.querySelector('a[href^=\"https://wa.me\"]');
    if (!el || !el.parentElement) return null;
    const rect = el.parentElement.getBoundingClientRect();
    const style = window.getComputedStyle(el.parentElement);
    return { rect: rect.toJSON(), display: style.display, visibility: style.visibility, opacity: style.opacity, zIndex: style.zIndex, transform: style.transform };
  });

  console.log(JSON.stringify({ bottomNav, whatsappNav }, null, 2));
  await browser.close();
})();
