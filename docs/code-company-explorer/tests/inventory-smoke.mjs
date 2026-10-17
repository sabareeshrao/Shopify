import { chromium } from 'playwright';
import assert from 'node:assert/strict';

const browser = await chromium.launch({headless:true,args:['--no-sandbox']});
const page = await browser.newPage({viewport:{width:1440,height:900}});
const errors=[];
page.on('pageerror',e=>errors.push(String(e)));
try {
  await page.goto('http://127.0.0.1:8123/code-company-explorer/index.html#company-176',
                  {waitUntil:'domcontentloaded',timeout:30000});
  await page.waitForFunction(()=>document.querySelector('.repo-meta')?.textContent?.includes('7720'),
                             {timeout:60000});
  assert.match(await page.locator('.repo-meta').innerText(),/7720 companies indexed/);
  assert.match(await page.locator('.repo-meta').innerText(),/176 taught/);
  assert.match(await page.locator('#maincontent .hero h1').innerText(),/Company 176\b/);
  assert.match(await page.locator('.learning-card.question').innerText(),/IQ-176/);
  await page.locator('#next-company').click();
  assert.match(await page.locator('#maincontent .hero h1').innerText(),/Company 177\b/);
  assert.match(await page.locator('.learning-card.sequence').innerText(),/YouTube-style explanation pending/);
  assert.match(await page.locator('.learning-card.question').innerText(),/NOT WRITTEN/);
  await page.waitForFunction(()=>document.querySelectorAll('#current-code .code-row').length>0,
                             {timeout:30000});
  assert.match(await page.locator('#current-code').innerText(),/main/);

  await page.locator('#search').fill('7720');
  await page.locator('#search-results button[data-company="company-7720"]').click();
  assert.match(await page.locator('#maincontent .hero h1').innerText(),/Company 7720\b/);
  assert.equal(await page.locator('#next-company').isDisabled(),true);
  assert.match(await page.locator('.learning-card.question').innerText(),/NOT WRITTEN/);

  await page.setViewportSize({width:425,height:860});
  await page.locator('#menu').click();
  await page.waitForTimeout(400);
  const aligned=await page.evaluate(()=>{
    const nav=document.querySelector('.side-body');
    const active=document.querySelector('#tree [data-company="company-7720"]');
    if(!nav||!active)return false;
    const a=active.getBoundingClientRect(),b=nav.getBoundingClientRect();
    return a.top>=b.top-3&&a.bottom<=b.bottom+3;
  });
  assert.equal(aligned,true,'Mobile sidebar selected company should be visible');
  await page.screenshot({path:'/tmp/inventory-mobile.png',fullPage:false});
  assert.deepEqual(errors,[],'Uncaught JavaScript exceptions');
  console.log(JSON.stringify({passed:true,companyTotal:7720,existingLesson:176,
                              testedPending:[177,7720],sourceLoaded:true,mobileSelection:true}));
} finally {
  await browser.close();
}
