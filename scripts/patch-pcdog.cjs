const fs = require('fs');
const p = 'D:/Calculator/scripts/extract-gate1-inventory.cjs';
let t = fs.readFileSync(p, 'utf8');
const start = t.indexOf('// --- PCDog ---');
const end = t.indexOf('// --- AIMarkTool ---');
if (start < 0 || end < 0) throw new Error('PCDog markers missing');
const block = `// --- PCDog ---
{
  const files=walkFiles('C:/Users/Administrator/Documents/pcdog/domains', (f,n)=>n.endsWith('.tool.ts'));
  for(const f of files){
    const txt=read(f);
    const id=(txt.match(/export const [A-Z0-9_]+_TOOL_ID\\s*=\\s*[\"']([^\"']+)[\"']/)||[])[1]
      || (txt.match(/\\bid:\\s*[\"'](tool\\.[^\"']+)[\"']/)||[])[1]
      || path.basename(f,'.tool.ts');
    const slug=(txt.match(/export const [A-Z0-9_]+_TOOL_SLUG\\s*=\\s*[\"']([^\"']+)[\"']/)||[])[1]
      || (txt.match(/\\bslug:\\s*[\"']([^\"']+)[\"']/)||[])[1]
      || path.basename(f,'.tool.ts');
    const name=(txt.match(/\\btitle:\\s*[\"']([^\"']+)[\"']/)||[])[1]
      || (txt.match(/\\bshortTitle:\\s*[\"']([^\"']+)[\"']/)||[])[1]
      || slug;
    const status=(txt.match(/\\bstatus:\\s*[\"']([^\"']+)[\"']/)||[])[1] || '';
    const route='/tools/'+slug;
    add({
      Website:'PCDog', ToolID:id, ToolName:name,
      ProductionURL: domains.PCDog + route,
      FormulaOrAlgorithm: 'browser measurement / network / display diagnostic algorithm (not necessarily closed-form math)',
      ApplicableConditions: status,
      SourceCodeLocation: f,
      VerificationStatus:'SOURCE_REGISTERED',
      DocumentationStatus:'REGISTRY_ONLY',
      LocalPath:'C:\\\\Users\\\\Administrator\\\\Documents\\\\pcdog',
      Category: f.includes('\\\\display\\\\')||f.includes('/display/')?'display':f.includes('\\\\network\\\\')||f.includes('/network/')?'network':f.includes('\\\\mobile\\\\')||f.includes('/mobile/')?'mobile':f.includes('\\\\wifi\\\\')||f.includes('/wifi/')?'wifi':'other',
    });
  }
}

`;
t = t.slice(0, start) + block + t.slice(end);
fs.writeFileSync(p, t);
console.log('PCDog block rewritten');
