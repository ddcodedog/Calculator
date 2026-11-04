const fs = require('fs');
const path = require('path');

function read(p){ return fs.readFileSync(p,'utf8'); }
function exists(p){ try{ fs.accessSync(p); return true; } catch{ return false; } }
function listDirs(p){ try{ return fs.readdirSync(p,{withFileTypes:true}).filter(d=>d.isDirectory()).map(d=>d.name);}catch{return[];} }
function listFiles(p, pred){ try{ return fs.readdirSync(p).filter(pred);}catch{return[];} }
function walkFiles(root, pred, acc=[], depth=0){
  if(depth>6) return acc;
  let ents; try{ ents=fs.readdirSync(root,{withFileTypes:true}); }catch{ return acc; }
  for(const e of ents){
    if(e.name==='node_modules'||e.name==='.git'||e.name==='.next'||e.name==='dist'||e.name==='out') continue;
    const full=path.join(root,e.name);
    if(e.isDirectory()) walkFiles(full,pred,acc,depth+1);
    else if(pred(full,e.name)) acc.push(full);
  }
  return acc;
}

const domains = {
  NetEngineerLab: 'https://netengineerlab.com',
  PCDog: 'https://pcdog.com',
  AIMarkTool: 'https://aimarktool.com', // verify later
  PowerEngineerLab: 'https://powerengineerlab.com',
  HVACEngineerLab: 'https://hvacengineerlab.com',
  PrivacyFileLab: 'https://privacyfilelab.com',
  DataFileLab: 'https://datafilelab.com',
  WaterEngineerLab: 'https://waterengineerlab.com',
  StructuralEngineerLab: 'https://structuralengineerlab.com',
  DevEngineerLab: 'https://devengineerlab.com',
  DIYCalcLab: 'https://diycalclab.com',
};

const tools = [];
function add(t){
  tools.push({
    Website: t.Website,
    ToolID: t.ToolID || t.id || '',
    ToolName: t.ToolName || t.name || '',
    ProductionURL: t.ProductionURL || '',
    FormulaOrAlgorithm: t.FormulaOrAlgorithm || 'PENDING_SOURCE_REVIEW',
    VariablesAndUnits: t.VariablesAndUnits || 'PENDING_SOURCE_REVIEW',
    ApplicableConditions: t.ApplicableConditions || t.status || '',
    SourceCodeLocation: t.SourceCodeLocation || '',
    VerificationStatus: t.VerificationStatus || 'UNVERIFIED',
    DocumentationStatus: t.DocumentationStatus || 'NONE',
    LocalPath: t.LocalPath || '',
    Category: t.Category || '',
    Notes: t.Notes || '',
  });
}

// --- NetEngineerLab ---
{
  const p='D:/NetEngineerLab-V173-GitHub/src/registry/tool-registry.json';
  const arr=JSON.parse(read(p));
  for(const t of arr){
    const route=(t.routes&&t.routes.en)||`/tools/${t.id}/`;
    add({
      Website:'NetEngineerLab', ToolID:t.id, ToolName:(t.translations&&t.translations.en&&t.translations.en.name)||t.id,
      ProductionURL: domains.NetEngineerLab + route,
      FormulaOrAlgorithm: (t.capabilities||[]).includes('calculate') ? 'math/engineering calculator (see source)' : `capabilities: ${(t.capabilities||[]).join(',')||'n/a'}`,
      ApplicableConditions: `status=${t.status}; maturity=${t.maturity||''}; category=${t.category||t.domain||''}`,
      SourceCodeLocation: `D:\\NetEngineerLab-V173-GitHub\\src\\registry\\tool-registry.json + website/tools/${t.id}`,
      VerificationStatus: t.status==='active'?'SOURCE_REGISTERED':'SOURCE_REGISTERED_NON_ACTIVE',
      DocumentationStatus: 'REGISTRY_ONLY',
      LocalPath: 'D:\\NetEngineerLab-V173-GitHub',
      Category: t.category||t.domain||'',
    });
  }
}

// --- PCDog ---
{
  const files=walkFiles('C:/Users/Administrator/Documents/pcdog/domains', (f,n)=>n.endsWith('.tool.ts'));
  for(const f of files){
    const txt=read(f);
    const id=(txt.match(/export const [A-Z0-9_]+_TOOL_ID\s*=\s*["']([^"']+)["']/)||[])[1]
      || (txt.match(/\bid:\s*["'](tool\.[^"']+)["']/)||[])[1]
      || path.basename(f,'.tool.ts');
    const slug=(txt.match(/export const [A-Z0-9_]+_TOOL_SLUG\s*=\s*["']([^"']+)["']/)||[])[1]
      || (txt.match(/\bslug:\s*["']([^"']+)["']/)||[])[1]
      || path.basename(f,'.tool.ts');
    const name=(txt.match(/\btitle:\s*["']([^"']+)["']/)||[])[1]
      || (txt.match(/\bshortTitle:\s*["']([^"']+)["']/)||[])[1]
      || slug;
    const status=(txt.match(/\bstatus:\s*["']([^"']+)["']/)||[])[1] || '';
    const route='/tools/'+slug;
    add({
      Website:'PCDog', ToolID:id, ToolName:name,
      ProductionURL: domains.PCDog + route,
      FormulaOrAlgorithm: 'browser measurement / network / display diagnostic algorithm (not necessarily closed-form math)',
      ApplicableConditions: status,
      SourceCodeLocation: f,
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'C:\\Users\\Administrator\\Documents\\pcdog',
      Category: f.includes('\\display\\')||f.includes('/display/')?'display':f.includes('\\network\\')||f.includes('/network/')?'network':f.includes('\\mobile\\')||f.includes('/mobile/')?'mobile':f.includes('\\wifi\\')||f.includes('/wifi/')?'wifi':'other',
    });
  }
}

// --- AIMarkTool ---
{
  const inv=read('D:/aimarktool/docs/TOOL-INVENTORY.md');
  // rows like: | A | **Name** | `slug` |
  const re=/\|[^\n|]*\|\s*\*\*([^*]+)\*\*\s*\|\s*`([^`]+)`/g;
  let m; const seen=new Set();
  while((m=re.exec(inv))){
    const name=m[1].trim(); const slug=m[2].trim();
    if(seen.has(slug)) continue; seen.add(slug);
    add({
      Website:'AIMarkTool', ToolID:slug, ToolName:name,
      ProductionURL: domains.AIMarkTool + `/tools/${slug}`,
      FormulaOrAlgorithm: slug.includes('calculator')?'marketing math / KPI formulas':'rule/hybrid marketing algorithm or template',
      SourceCodeLocation:'D:\\aimarktool\\core\\registry\\tool-registry.ts + docs\\TOOL-INVENTORY.md',
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'INVENTORY_DOC',
      LocalPath:'D:\\aimarktool',
    });
  }
  // fallback from tool-registry.ts slugs if inventory sparse
  if(seen.size<10){
    const ts=read('D:/aimarktool/core/registry/tool-registry.ts');
    const re2=/slug:\s*["']([^"']+)["']/g; let m2;
    while((m2=re2.exec(ts))){
      const slug=m2[1]; if(seen.has(slug)) continue; seen.add(slug);
      add({Website:'AIMarkTool',ToolID:slug,ToolName:slug,ProductionURL:domains.AIMarkTool+`/tools/${slug}`,SourceCodeLocation:'D:\\aimarktool\\core\\registry\\tool-registry.ts',VerificationStatus:'SOURCE_REGISTERED',DocumentationStatus:'REGISTRY_ONLY',LocalPath:'D:\\aimarktool'});
    }
  }
}

// --- PowerEngineerLab ---
{
  const calcRoot='D:/Calculator/_audit_PowerEngineerLab/app/(en)/calculators';
  const dirs=listDirs(calcRoot);
  for(const slug of dirs){
    const calcFile=`D:/Calculator/_audit_PowerEngineerLab/lib/calculation`;
    const matching=listFiles(calcFile,n=>n.startsWith('tool-')&&n.endsWith('.ts')&&!n.includes('adapter'));
    add({
      Website:'PowerEngineerLab', ToolID:slug, ToolName:slug.split('-').map(s=>s[0].toUpperCase()+s.slice(1)).join(' '),
      ProductionURL: domains.PowerEngineerLab + `/calculators/${slug}/`,
      FormulaOrAlgorithm: 'electrical/energy engineering formula (see lib/calculation/tool-*.ts)',
      SourceCodeLocation: `D:\\Calculator\\_audit_PowerEngineerLab\\app\\(en)\\calculators\\${slug} + lib\\calculation\\`,
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'D:\\Calculator\\_audit_PowerEngineerLab',
      Notes:'Local audit clone of github.com/ddcodedog/PowerEngineerLab (no D:\\PowerEngineerLab tree).',
    });
  }
}

// --- HVACEngineerLab ---
{
  const dirs=listDirs('D:/HVACEngineerLab/src/app/tools');
  for(const slug of dirs){
    add({
      Website:'HVACEngineerLab', ToolID:slug, ToolName:slug.split('-').map(s=>s[0].toUpperCase()+s.slice(1)).join(' '),
      ProductionURL: domains.HVACEngineerLab + `/tools/${slug}/`,
      FormulaOrAlgorithm: 'HVAC engineering formula/algorithm (psychrometrics, load, duct/pipe, energy)',
      SourceCodeLocation: `D:\\HVACEngineerLab\\src\\app\\tools\\${slug} (+ src\\tools impl)`,
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'D:\\HVACEngineerLab',
    });
  }
}

// --- PrivacyFileLab ---
{
  const md=read('D:/PrivacyFileLab/docs/core/06_TOOL_REGISTRY.md');
  const re=/\|[ \t]*(T\d+)[ \t]*\|[ \t]*([^|]+?)\|[ \t]*P\d+/g;
  let m;
  const slugMap={
    'T01':'scan','T02':'ai-upload','T03':'pdf','T04':'photo','T05':'photo','T06':'pdf','T07':'office','T08':'text-redactor','T09':'clean-file-verifier','T10':'metadata-diff','T11':'hash','T12':'ocr'
  };
  while((m=re.exec(md))){
    const id=m[1].trim(); const name=m[2].trim();
    const folder=slugMap[id]||id.toLowerCase();
    add({
      Website:'PrivacyFileLab', ToolID:id, ToolName:name,
      ProductionURL: domains.PrivacyFileLab + `/${folder}/`,
      FormulaOrAlgorithm: 'privacy scanning / metadata cleaning / hashing / OCR algorithm (not closed-form math)',
      SourceCodeLocation: `D:\\PrivacyFileLab\\docs\\core\\06_TOOL_REGISTRY.md; apps\\app\\app\\${folder}`,
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_DOC',
      LocalPath:'D:\\PrivacyFileLab',
    });
  }
}

// --- DataFileLab ---
{
  const md=read('D:/DataFileLab/TOOL_REGISTRY.md');
  const sitemap=exists('D:/DataFileLab/preview/sitemap.xml')?read('D:/DataFileLab/preview/sitemap.xml'):'';
  const locs=[...sitemap.matchAll(/<loc>(https:\/\/datafilelab\.com\/[^<]+)<\/loc>/g)].map(x=>x[1]);
  const re=/\|[ \t]*((?:TOOL|SEO)-\d+)[ \t]*\|[ \t]*([^|]+?)\|[ \t]*([^|]+?)\|[ \t]*([^|]+?)\|/g;
  let m;
  while((m=re.exec(md))){
    const id=m[1].trim(); const name=m[2].trim(); const phase=m[3].trim(); const status=m[4].trim();
    const guess=name.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
    let url=locs.find(u=>u.replace(/\/$/,'')===domains.DataFileLab+'/'+guess) || '';
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
      ApplicableConditions: `phase=${phase}; status=${status}`,
      SourceCodeLocation:'D:\\DataFileLab\\TOOL_REGISTRY.md + preview/sitemap.xml',
      VerificationStatus: status.match(/IMPLEMENTED|ACCEPTED/i)?'SOURCE_REGISTERED':'SOURCE_REGISTERED_NON_ACTIVE',
      DocumentationStatus:'REGISTRY_DOC',
      LocalPath:'D:\\DataFileLab',
      Notes: locs.includes(url) ? 'URL from sitemap' : 'URL guessed; confirm in GATE2+',
    });
  }
}

// --- WaterEngineerLab ---
{
  const ts=read('D:/WaterEngineerLab/src/core/registry/tools.ts');
  const re=/\{id:"([^"]+)",slug:"([^"]+)",name:"([^"]+)",hubIds:\[([^\]]*)\],status:"([^"]+)"\}/g;
  let m;
  while((m=re.exec(ts))){
    add({
      Website:'WaterEngineerLab', ToolID:m[1], ToolName:m[3],
      ProductionURL: domains.WaterEngineerLab + `/tools/${m[2]}/`,
      FormulaOrAlgorithm: 'hydraulics / stormwater / pipe flow engineering formula',
      ApplicableConditions: `status=${m[5]}; hubs=${m[4]}`,
      SourceCodeLocation:'D:\\WaterEngineerLab\\src\\core\\registry\\tools.ts',
      VerificationStatus: m[5]==='closed'?'SOURCE_REGISTERED_CLOSED':'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'D:\\WaterEngineerLab',
    });
  }
}

// --- StructuralEngineerLab ---
{
  const frozen=read('D:/StructuralEngineerLab/src/registry/tool-registry.ts');
  const planned=read('D:/StructuralEngineerLab/src/registry/planned-tool-registry.ts');
  const re1=/\{ id: "([^"]+)", slug: "([^"]+)", name: "([^"]+)",[^}]*status: "([^"]+)"/g;
  let m;
  while((m=re1.exec(frozen))){
    add({
      Website:'StructuralEngineerLab', ToolID:m[1], ToolName:m[3],
      ProductionURL: domains.StructuralEngineerLab + `/tools/${m[2]}/`,
      FormulaOrAlgorithm: 'structural mechanics formula (beam/section/column)',
      ApplicableConditions: `status=${m[4]}`,
      SourceCodeLocation:'D:\\StructuralEngineerLab\\src\\registry\\tool-registry.ts',
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'D:\\StructuralEngineerLab',
    });
  }
  const re2=/\{ id: "([^"]+)", slug: "([^"]+)", name: "([^"]+)", route: "([^"]+)"/g;
  while((m=re2.exec(planned))){
    add({
      Website:'StructuralEngineerLab', ToolID:m[1], ToolName:m[3],
      ProductionURL: domains.StructuralEngineerLab + m[4],
      FormulaOrAlgorithm: 'structural mechanics formula/report tool (planned registry)',
      ApplicableConditions:'status=planned',
      SourceCodeLocation:'D:\\StructuralEngineerLab\\src\\registry\\planned-tool-registry.ts',
      VerificationStatus:'SOURCE_REGISTERED_PLANNED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'D:\\StructuralEngineerLab',
      Notes:'Listed in planned-tool-registry; may also have app/tools page.',
    });
  }
}

// --- DevEngineerLab ---
{
  const arr=JSON.parse(read('D:/DevEngineerLab/src/registries/data/tools.json'));
  for(const t of arr){
    add({
      Website:'DevEngineerLab', ToolID:t.id, ToolName:t.name||t.slug,
      ProductionURL: domains.DevEngineerLab + `/tools/${t.slug}/`,
      FormulaOrAlgorithm: 'developer utility / transform / API tooling algorithm',
      ApplicableConditions: `status=${t.status}; seoStatus=${t.seoStatus||''}; runtime=${t.runtime||''}`,
      SourceCodeLocation:'D:\\DevEngineerLab\\src\\registries\\data\\tools.json',
      VerificationStatus: t.status==='ready'?'SOURCE_REGISTERED':'SOURCE_REGISTERED_NON_READY',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'D:\\DevEngineerLab',
      Category:t.topicId||'',
    });
  }
}

// --- DIYCalcLab ---
{
  for(const file of ['calculators.ts','calculators-p2.ts','calculators-p3.ts','calculators-p4.ts']){
    const p=`D:/diycalclab/src/data/${file}`;
    const txt=read(p);
    const re=/id:\s*'([^']+)'\s*,\s*slug:\s*'([^']+)'\s*,\s*category:\s*'([^']+)'[\s\S]*?name:\s*'([^']+)'/g;
    let m;
    while((m=re.exec(txt))){
      const id=m[1], slug=m[2], category=m[3], name=m[4];
      const idx=m.index;
      const window=txt.slice(idx, idx+2500);
      const fMatch=window.match(/formula:\s*\[([^\]]*)\]/);
      const formulas=fMatch?fMatch[1].split(',').map(s=>s.trim().replace(/^'|'$/g,'')).filter(Boolean).slice(0,4).join(' | '):'see CalcPage.formula';
      const vMatch=window.match(/variables:\s*\[([\s\S]*?)\]\s*,\s*assumptions/);
      let vars='see CalcPage.variables';
      if(vMatch){ vars=vMatch[1].replace(/\s+/g,' ').slice(0,240); }
      add({
        Website:'DIYCalcLab', ToolID:id, ToolName:name,
        ProductionURL: domains.DIYCalcLab + `/${category}/${slug}/`,
        FormulaOrAlgorithm: formulas,
        VariablesAndUnits: vars,
        SourceCodeLocation: `D:\\diycalclab\\src\\data\\${file}`,
        VerificationStatus:'SOURCE_REGISTERED',
        DocumentationStatus:'INLINE_CALC_PAGE_CONTENT',
        LocalPath:'D:\\diycalclab',
        Category: category,
      });
    }
  }
}

// summarize
const bySite={};
for(const t of tools){ bySite[t.Website]=(bySite[t.Website]||0)+1; }

const report={
  generatedAt: new Date().toISOString(),
  timezoneNote: 'Box/report timestamps; user zone Asia/Shanghai',
  gate: 'GATE1',
  domainsAssumed: domains,
  localRoots: {
    NetEngineerLab:'D:\\NetEngineerLab-V173-GitHub',
    PCDog:'C:\\Users\\Administrator\\Documents\\pcdog',
    AIMarkTool:'D:\\aimarktool',
    PowerEngineerLab:'D:\\Calculator\\_audit_PowerEngineerLab (shallow clone; no D:\\PowerEngineerLab)',
    HVACEngineerLab:'D:\\HVACEngineerLab',
    PrivacyFileLab:'D:\\PrivacyFileLab',
    DataFileLab:'D:\\DataFileLab',
    WaterEngineerLab:'D:\\WaterEngineerLab',
    StructuralEngineerLab:'D:\\StructuralEngineerLab',
    DevEngineerLab:'D:\\DevEngineerLab',
    DIYCalcLab:'D:\\diycalclab',
  },
  countsByWebsite: bySite,
  totalTools: tools.length,
  tools,
};

fs.mkdirSync('D:/Calculator/reports',{recursive:true});
fs.writeFileSync('D:/Calculator/reports/GATE1_TOOL_INVENTORY.json', JSON.stringify(report,null,2));

let md=[];
md.push('# GATE1 Tool Inventory');
md.push('');
md.push(`Generated: ${report.generatedAt}`);
md.push('');
md.push('## Summary counts');
md.push('');
md.push('| Website | Tools |');
md.push('|---|---:|');
for(const [k,v] of Object.entries(bySite).sort()) md.push(`| ${k} | ${v} |`);
md.push(`| **TOTAL** | **${tools.length}** |`);
md.push('');
md.push('## Domain assumptions (production URL base)');
md.push('');
for(const [k,v] of Object.entries(domains)) md.push(`- ${k}: ${v}`);
md.push('');
md.push('## Local roots audited');
md.push('');
for(const [k,v] of Object.entries(report.localRoots)) md.push(`- ${k}: \`${v}\``);
md.push('');
md.push('## Notes');
md.push('');
md.push('- VerificationStatus `SOURCE_REGISTERED*` means present in local registry/source; formula accuracy NOT independently verified in GATE1.');
md.push('- ProductionURL reachability is checked separately; some URL path patterns may differ from live routes.');
md.push('- Non-math tools (privacy scanners, file converters, network tests, marketing templates) are listed as algorithm/protocol tools — do not invent formulas.');
md.push('- PowerEngineerLab had no D:\\\\PowerEngineerLab directory; audited via shallow clone into Calculator/_audit_PowerEngineerLab.');
md.push('');
md.push('## Tools');
md.push('');
for(const site of Object.keys(bySite).sort()){
  md.push(`### ${site}`);
  md.push('');
  md.push('| Tool ID | Name | Production URL | Formula/Algorithm | Source | Verification | Docs |');
  md.push('|---|---|---|---|---|---|---|');
  for(const t of tools.filter(x=>x.Website===site)){
    const esc=s=>String(s||'').replace(/\|/g,'\\\\|').replace(/\n/g,' ');
    md.push(`| ${esc(t.ToolID)} | ${esc(t.ToolName)} | ${esc(t.ProductionURL)} | ${esc(t.FormulaOrAlgorithm).slice(0,120)} | ${esc(t.SourceCodeLocation).slice(0,80)} | ${esc(t.VerificationStatus)} | ${esc(t.DocumentationStatus)} |`);
  }
  md.push('');
}
fs.writeFileSync('D:/Calculator/reports/GATE1_TOOL_INVENTORY.md', md.join('\n'));
console.log(JSON.stringify({total:tools.length, bySite},null,2));

