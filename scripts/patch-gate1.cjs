const fs = require('fs');
const p = 'D:/Calculator/scripts/extract-gate1-inventory.cjs';
let t = fs.readFileSync(p, 'utf8');

const diyStart = t.indexOf('// --- DIYCalcLab ---');
const diyEnd = t.indexOf('// summarize');
if (diyStart < 0 || diyEnd < 0) throw new Error('DIY markers missing');
const diyNew = `// --- DIYCalcLab ---
{
  for(const file of ['calculators.ts','calculators-p2.ts','calculators-p3.ts','calculators-p4.ts']){
    const p=\`D:/diycalclab/src/data/\${file}\`;
    const txt=read(p);
    const re=/id:\\s*'([^']+)'\\s*,\\s*slug:\\s*'([^']+)'\\s*,\\s*category:\\s*'([^']+)'[\\s\\S]*?name:\\s*'([^']+)'/g;
    let m;
    while((m=re.exec(txt))){
      const id=m[1], slug=m[2], category=m[3], name=m[4];
      const idx=m.index;
      const window=txt.slice(idx, idx+2500);
      const fMatch=window.match(/formula:\\s*\\[([^\\]]*)\\]/);
      const formulas=fMatch?fMatch[1].split(',').map(s=>s.trim().replace(/^'|'$/g,'')).filter(Boolean).slice(0,4).join(' | '):'see CalcPage.formula';
      const vMatch=window.match(/variables:\\s*\\[([\\s\\S]*?)\\]\\s*,\\s*assumptions/);
      let vars='see CalcPage.variables';
      if(vMatch){ vars=vMatch[1].replace(/\\s+/g,' ').slice(0,240); }
      add({
        Website:'DIYCalcLab', ToolID:id, ToolName:name,
        ProductionURL: domains.DIYCalcLab + \`/\${category}/\${slug}/\`,
        FormulaOrAlgorithm: formulas,
        VariablesAndUnits: vars,
        SourceCodeLocation: \`D:\\\\diycalclab\\\\src\\\\data\\\\\${file}\`,
        VerificationStatus:'SOURCE_REGISTERED',
        DocumentationStatus:'INLINE_CALC_PAGE_CONTENT',
        LocalPath:'D:\\\\diycalclab',
        Category: category,
      });
    }
  }
}

`;
t = t.slice(0, diyStart) + diyNew + t.slice(diyEnd);

const dfStart = t.indexOf('// --- DataFileLab ---');
const dfEnd = t.indexOf('// --- WaterEngineerLab ---');
if (dfStart < 0 || dfEnd < 0) throw new Error('DataFile markers missing');
const dfNew = `// --- DataFileLab ---
{
  const md=read('D:/DataFileLab/TOOL_REGISTRY.md');
  const sitemap=exists('D:/DataFileLab/preview/sitemap.xml')?read('D:/DataFileLab/preview/sitemap.xml'):'';
  const locs=[...sitemap.matchAll(/<loc>(https:\\/\\/datafilelab\\.com\\/[^<]+)<\\/loc>/g)].map(x=>x[1]);
  const re=/\\|[ \\t]*((?:TOOL|SEO)-\\d+)[ \\t]*\\|[ \\t]*([^|]+?)\\|[ \\t]*([^|]+?)\\|[ \\t]*([^|]+?)\\|/g;
  let m;
  while((m=re.exec(md))){
    const id=m[1].trim(); const name=m[2].trim(); const phase=m[3].trim(); const status=m[4].trim();
    const guess=name.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
    let url=locs.find(u=>u.replace(/\\/$/,'')===domains.DataFileLab+'/'+guess) || '';
    if(!url){
      const tokens=guess.split('-').filter(x=>x.length>3).slice(0,3);
      url=locs.find(u=>tokens.every(tok=>u.includes(tok))) || '';
    }
    if(!url){
      const alias={
        'excel-csv-compare':'compare','data-cleaner-profiler':'clean'
      };
      if(alias[guess]) url=domains.DataFileLab+'/'+alias[guess];
      else url=domains.DataFileLab+'/'+guess;
    }
    add({
      Website:'DataFileLab', ToolID:id, ToolName:name,
      ProductionURL: url,
      FormulaOrAlgorithm: 'CSV/data file transform, validation, or conversion algorithm',
      ApplicableConditions: \`phase=\${phase}; status=\${status}\`,
      SourceCodeLocation:'D:\\\\DataFileLab\\\\TOOL_REGISTRY.md + preview/sitemap.xml',
      VerificationStatus: status.match(/IMPLEMENTED|ACCEPTED/i)?'SOURCE_REGISTERED':'SOURCE_REGISTERED_NON_ACTIVE',
      DocumentationStatus:'REGISTRY_DOC',
      LocalPath:'D:\\\\DataFileLab',
      Notes: locs.includes(url) ? 'URL from sitemap' : 'URL guessed; confirm in GATE2+',
    });
  }
}

`;
t = t.slice(0, dfStart) + dfNew + t.slice(dfEnd);

// PCDog: prefer TOOL_SLUG / title
t = t.replace(
  /const id=\(txt\.match\(\/id:\\s\*\[\\"']\(\[^\\"']\+\)\[\\"']\/\)\|\|\[\]\)\[1\] \|\| path\.basename\(f,'\.tool\.ts'\);\r?\n\s*const slug=\(txt\.match\(\/slug:\\s\*\[\\"']\(\[^\\"']\+\)\[\\"']\/\)\|\|\[\]\)\[1\] \|\| path\.basename\(f,'\.tool\.ts'\);\r?\n\s*const name=\(txt\.match\(\/name:\\s\*\[\\"']\(\[^\\"']\+\)\[\\"']\/\)\|\|\[\]\)\[1\] \|\| slug;\r?\n\s*const status=\(txt\.match\(\/status:\\s\*\[\\"']\(\[^\\"']\+\)\[\\"']\/\)\|\|\[\]\)\[1\] \|\| '';\r?\n\s*const route=\(txt\.match\(\/route:\\s\*\[\\"']\(\[^\\"']\+\)\[\\"']\/\)\|\|txt\.match\(\/path:\\s\*\[\\"']\(\[^\\"']\+\)\[\\"']\/\)\|\|\[\]\)\[1\] \|\| `\/tools\/\${slug}\/`;/,
  `const id=(txt.match(/TOOL_ID\\s*=\\s*[\"']([^\"']+)[\"']/)||txt.match(/id:\\s*[\"']([^\"']+)[\"']/)||[])[1] || path.basename(f,'.tool.ts');
    const slug=(txt.match(/TOOL_SLUG\\s*=\\s*[\"']([^\"']+)[\"']/)||txt.match(/slug:\\s*[\"']([^\"']+)[\"']/)||[])[1] || path.basename(f,'.tool.ts');
    const name=(txt.match(/title:\\s*[\"']([^\"']+)[\"']/)||txt.match(/name:\\s*[\"']([^\"']+)[\"']/)||[])[1] || slug;
    const status=(txt.match(/status:\\s*[\"']([^\"']+)[\"']/)||[])[1] || '';
    const route=\`/tools/\${slug}\`;`
);

fs.writeFileSync(p, t);
console.log('patched ok');
