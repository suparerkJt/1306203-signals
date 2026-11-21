import uuid

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="1306203 Signals & Systems | Signals",
    layout="wide",
)

# Remove Streamlit's default padding/header so the app fills the page
st.markdown(
    """
    <style>
    .block-container {padding-top: 3.5rem; padding-bottom: 1rem;}
    header[data-testid="stHeader"] {height: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)


def show(html_template, prefix, height):
    """Embed one self-contained HTML/JavaScript app.

    Every app gets its own unique id, so the four apps never interfere
    with each other. Everything runs in the browser (JavaScript), so
    changing a parameter never triggers a Streamlit rerun.
    """
    uid = prefix + "_" + uuid.uuid4().hex[:8]
    html = html_template.replace("ROOT_ID", uid)

    if hasattr(st, "iframe"):
        # newer Streamlit versions (components.html is deprecated there)
        st.iframe(html, height=height)
    else:
        components.html(html, height=height, scrolling=True)


# ======================================================================
# The four apps (HTML + CSS + JavaScript)
# ======================================================================

CT_SIGNALS_HTML = r"""
<div id="ROOT_ID" class="animation-app">

<style>
#ROOT_ID {
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:clamp(8px, 2vw, 24px);
    box-sizing:border-box;
    font-family:Arial,sans-serif;
    position:relative;
    color:#1f2a44;
    background:linear-gradient(160deg,#f7f9ff 0%,#eaf0fc 100%);
    border-radius:18px;
    box-shadow:0 10px 30px rgba(31,42,68,0.10);
}

#ROOT_ID * { box-sizing:border-box; }

#ROOT_ID h2 {
    text-align:center;
    font-size:clamp(20px, 2.6vw, 30px);
    margin:12px 0 4px;
    padding:0 140px;      /* keeps long titles clear of the mode button */
    letter-spacing:0.5px;
    background:linear-gradient(90deg,#2f6fed,#12a36a);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
}

#ROOT_ID .subtitle {
    text-align:center;
    font-size:clamp(13px,1.6vw,17px);
    margin:0 0 18px;
    opacity:0.8;
}

#ROOT_ID button.theme {
    color:white;
    border:0;
    border-radius:10px;
    cursor:pointer;
    font-weight:bold;
    white-space:nowrap;
    touch-action:manipulation;
    box-shadow:0 4px 10px rgba(0,0,0,0.22);
    transition:transform .12s, filter .12s;
    background:linear-gradient(135deg,#8b6cff,#5a3fd4);
    position:absolute;
    top:clamp(24px,3vw,36px);
    right:clamp(8px,1.5vw,16px);
    padding:8px 14px;
    font-size:clamp(12px,1.3vw,14px);
    z-index:2;
}
#ROOT_ID button.theme:hover { transform:translateY(-1px); filter:brightness(1.08); }
#ROOT_ID button.theme:active { transform:scale(0.97); }

/* ---------- two-column layout ---------- */
#ROOT_ID .layout {
    display:grid;
    grid-template-columns:310px minmax(0,1fr);
    gap:18px;
    align-items:start;
}

#ROOT_ID .panel {
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
    padding:14px;
}

#ROOT_ID .left { display:flex; flex-direction:column; gap:14px; }

#ROOT_ID .panel h3 { margin:0 0 10px; font-size:17px; }
#ROOT_ID .sigcard { --c:#2f6fed; }
#ROOT_ID .sigcard h3 { color:var(--c); }

#ROOT_ID .tiles {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

#ROOT_ID .tile {
    cursor:pointer;
    border:2px solid #d3dcf0;
    border-radius:10px;
    padding:6px 4px 5px;
    text-align:center;
    font-size:12px;
    font-weight:bold;
    background:#ffffff;
    user-select:none;
    transition:border-color .12s, box-shadow .12s;
}
#ROOT_ID .tile:hover { border-color:var(--c); }
#ROOT_ID .tile.active {
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}
#ROOT_ID .tile svg { display:block; width:100%; height:36px; stroke:var(--c); fill:none; }

#ROOT_ID .formula {
    margin:12px 0 0;
    padding:8px 10px;
    border-radius:8px;
    background:rgba(47,111,237,0.08);
    font-size:14px;
    font-weight:bold;
    text-align:center;
}

#ROOT_ID .desc {
    display:none;
    margin-top:10px;
    font-size:13px;
    line-height:1.5;
    opacity:0.85;
}
#ROOT_ID .desc.show { display:block; }

#ROOT_ID .param {
    display:none;
    margin-top:10px;
    font-size:13px;
    font-weight:bold;
}
#ROOT_ID .param.show { display:block; }

#ROOT_ID input[type=number] {
    display:block;
    width:100%;
    margin-top:5px;
    padding:7px;
    font-size:15px;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
    text-align:center;
}
#ROOT_ID input[type=number]:focus {
    outline:none;
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.25);
}
#ROOT_ID input[type=number]:disabled { opacity:0.55; cursor:not-allowed; }

#ROOT_ID .grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
#ROOT_ID .grid2 label { font-size:13px; font-weight:bold; }

#ROOT_ID .subhead {
    margin:14px 0 6px;
    font-size:14px;
    font-weight:bold;
}

#ROOT_ID .seg {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:6px;
    margin-bottom:10px;
}
#ROOT_ID .seg div {
    cursor:pointer;
    text-align:center;
    padding:7px 4px;
    border:2px solid #d3dcf0;
    border-radius:9px;
    background:#ffffff;
    font-size:13px;
    font-weight:bold;
    user-select:none;
}
#ROOT_ID .seg div.active {
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.22);
    color:#2f6fed;
}

#ROOT_ID .hint { margin-top:8px; font-size:12px; opacity:0.75; line-height:1.45; }

/* ---------- right column ---------- */
#ROOT_ID .right { min-width:0; }

#ROOT_ID .statusrow {
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:10px;
    margin-bottom:12px;
}

#ROOT_ID .status {
    text-align:center;
    width:fit-content;
    max-width:100%;
    margin:0;
    padding:9px 20px;
    border-radius:999px;
    background:#ffffff;
    border:1px solid #d3dcf0;
    box-shadow:0 3px 10px rgba(31,42,68,0.08);
    font-size:clamp(12px,1.5vw,16px);
    font-weight:bold;
}

#ROOT_ID canvas {
    display:block;
    max-width:100%;
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
}

/* ---------- dark mode ---------- */
#ROOT_ID.dark {
    background:linear-gradient(160deg,#0d1117 0%,#161d2e 100%);
    color:#e6edf7;
    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}
#ROOT_ID.dark h2 {
    background:linear-gradient(90deg,#6aa9ff,#3ddc97);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}
#ROOT_ID.dark .panel,
#ROOT_ID.dark canvas {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
    box-shadow:0 6px 18px rgba(0,0,0,0.5);
}
#ROOT_ID.dark .sigcard { --c:#58a6ff; }
#ROOT_ID.dark .tile,
#ROOT_ID.dark .seg div { background:#0f1522; border-color:#33415f; }
#ROOT_ID.dark .tile:hover,
#ROOT_ID.dark .tile.active { border-color:var(--c); }
#ROOT_ID.dark .seg div.active { border-color:#58a6ff; color:#6aa9ff; box-shadow:0 0 0 3px rgba(88,166,255,0.28); }
#ROOT_ID.dark .formula { background:rgba(88,166,255,0.12); }
#ROOT_ID.dark input[type=number] {
    background:#0f1522;
    color:#e6edf7;
    border-color:#3b4866;
}
#ROOT_ID.dark input[type=number]:focus {
    border-color:#58a6ff;
    box-shadow:0 0 0 3px rgba(88,166,255,0.30);
}
#ROOT_ID.dark .status {
    background:#1a2233;
    border-color:#33415f;
    color:#e6edf7;
    box-shadow:0 3px 12px rgba(0,0,0,0.4);
}

/* ---------- responsive ---------- */
@media (max-width:900px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
    #ROOT_ID .left { flex-direction:row; flex-wrap:wrap; }
    #ROOT_ID .left .panel { flex:1 1 280px; }
}

@media (max-width:550px) {
    #ROOT_ID { padding:6px; }
    #ROOT_ID h2 { margin-top:64px; padding:0; }
    #ROOT_ID button.theme { padding:7px 11px; }
}
</style>

<button class="theme" id="theme">🌙 DARK MODE</button>

<h2>Basic Continuous-Time Signals</h2>
<div class="subtitle"> </div>

<div class="layout">

    <!-- LEFT COLUMN -->
    <div class="left">

        <div class="panel sigcard" id="card_sig"></div>

        <div class="panel" id="card_axes">
            <h3>Plotting area</h3>

            <div class="subhead" style="margin-top:0">Time axis</div>
            <div class="grid2">
                <label>t<sub>min</sub> (s)
                    <input id="tmin" type="number" value="-10" min="-1000" max="999" step="1">
                </label>
                <label>t<sub>max</sub> (s)
                    <input id="tmax" type="number" value="10" min="-999" max="1000" step="1">
                </label>
            </div>

            <div class="subhead">Amplitude axis</div>
            <div class="seg">
                <div id="m_auto" class="active">Auto scale</div>
                <div id="m_fixed">Fixed values</div>
            </div>

            <div class="grid2">
                <label>Min amplitude
                    <input id="ymin" type="number" value="-1" step="0.5" disabled>
                </label>
                <label>Max amplitude
                    <input id="ymax" type="number" value="1" step="0.5" disabled>
                </label>
            </div>

            <div class="hint" id="axhint">Auto scale fits the amplitude axis to the signal. The boxes show the range currently used.</div>
        </div>

    </div>

    <!-- RIGHT COLUMN -->
    <div class="right">
        <div class="statusrow">
            <div class="status" id="status_eq"></div>
            <div class="status" id="status_rng"></div>
        </div>
        <canvas id="cv"></canvas>
    </div>

</div>

<script>
(function(){

const root=document.getElementById("ROOT_ID");
const $=s=>root.querySelector(s);

// ======================================
// SIGNAL DEFINITIONS
// ======================================

const TYPES={
    exp:  {label:"Real exponential",
           path:"M2 24 C18 23 28 20 36 4"},
    sine: {label:"Sinusoidal",
           path:"M2 14 C7 0 13 0 19 14 S31 28 38 14"},
    step: {label:"Unit step",
           path:"M2 24 H19 V6 H38"},
    imp:  {label:"Unit impulse",
           path:"M2 24 H38 M20 24 V6 M15.5 11 L20 5 L24.5 11"},
    cplx: {label:"Complex exponential",
           path:"M2 14 C5 0 8 0 11 14 S17 26 20 14 S25 7 28 14 S33 19 38 14"}
};

const ORDER=["exp","sine","step","imp","cplx"];

const PARAMS=[
    {p:"C",label:"Amplitude C",         types:["exp"],  min:-100, max:100, step:0.1},
    {p:"a",label:"Rate a (real)",       types:["exp"],  min:-10,  max:10,  step:0.1},
    {p:"A",label:"Amplitude A",         types:["sine"], min:-100, max:100, step:0.1},
    {p:"f",label:"Frequency f (Hz)",    types:["sine"], min:0,     max:20,  step:0.1},
    {p:"k",label:"Phase factor k  (φ = k·π)", types:["sine"], min:-100, max:100, step:0.1},

    // complex exponential  C = |C| e^(jθ),  a = r + jω0
    {p:"mag",label:"Magnitude |C|",                      types:["cplx"], min:0,    max:100, step:0.1},
    {p:"th", label:"Phase factor k  (θ = k·π)",           types:["cplx"], min:-100, max:100, step:0.1},
    {p:"r",  label:"Real part r of a  (1/s)",             types:["cplx"], min:-10,  max:10,  step:0.1},
    {p:"d",  label:"Frequency factor d  (ω<sub>0</sub> = d·π rad/s)", types:["cplx"], min:-100, max:100, step:0.1}
];

const DESCS={
    step:"u(t) = 1 for t ≥ 0 and 0 for t &lt; 0.",
    imp:"δ(t) has unit area concentrated at t = 0. It is drawn as an arrow of height 1.",
    cplx:"C = |C|·e<sup>jθ</sup> and a = r + jω<sub>0</sub>."
};

const sig={type:"exp", C:1, a:0.5, A:1, f:1, k:0, mag:1, th:0, r:-0.2, d:1};

const view={tmin:-10, tmax:10, auto:true, ymin:-1, ymax:1};

// ======================================
// LEFT COLUMN: SIGNAL CARD
// ======================================

function buildCard(){

    const card=$("#card_sig");

    let h='<h3>Signal type</h3><div class="tiles">';

    ORDER.forEach(id=>{
        h+='<div class="tile" data-type="'+id+'"'+(id==="cplx"?' style="grid-column:1 / -1"':'')+'>'+
           '<svg viewBox="0 0 40 28"><path d="'+TYPES[id].path+
           '" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'+
           TYPES[id].label+'</div>';
    });

    h+='</div><div class="formula" id="formula"></div>';

    PARAMS.forEach(q=>{
        h+='<label class="param" data-for="'+q.types.join(" ")+'">'+q.label+
           '<input type="number" data-p="'+q.p+'" min="'+q.min+'" max="'+q.max+
           '" step="'+q.step+'" value="'+sig[q.p]+'"></label>';
    });

    Object.keys(DESCS).forEach(id=>{
        h+='<div class="desc" data-for="'+id+'">'+DESCS[id]+'</div>';
    });

    card.innerHTML=h;

    card.querySelectorAll(".tile").forEach(el=>{
        el.addEventListener("click",()=>{
            sig.type=el.dataset.type;
            refreshCard();
            fit();          // the complex signal needs a taller plot
            render();
        });
    });

    card.querySelectorAll(".param input").forEach(inp=>{
        inp.addEventListener("change",()=>{

            const p=inp.dataset.p;
            let v=Number(inp.value);

            const lo=Number(inp.min), hi=Number(inp.max);
            if(!Number.isFinite(v)) v=sig[p];
            v=Math.min(hi,Math.max(lo,v));

            inp.value=v;
            sig[p]=v;
            render();
        });
    });

    refreshCard();
}

function refreshCard(){

    const card=$("#card_sig");

    card.querySelectorAll(".tile").forEach(el=>{
        el.classList.toggle("active",el.dataset.type===sig.type);
    });

    card.querySelectorAll(".param, .desc").forEach(el=>{
        el.classList.toggle("show",el.dataset.for.split(" ").includes(sig.type));
    });
}

buildCard();

// ======================================
// PLOT AREA SETTINGS (left column)
// ======================================

const tminIn=$("#tmin"), tmaxIn=$("#tmax"), yminIn=$("#ymin"), ymaxIn=$("#ymax");

function applyTime(){

    const a=Number(tminIn.value), b=Number(tmaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        tminIn.value=view.tmin;
        tmaxIn.value=view.tmax;
        return;
    }

    view.tmin=a;
    view.tmax=b;
    render();
}

function applyY(){

    const a=Number(yminIn.value), b=Number(ymaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
        return;
    }

    view.ymin=a;
    view.ymax=b;
    render();
}

tminIn.addEventListener("change",applyTime);
tmaxIn.addEventListener("change",applyTime);
yminIn.addEventListener("change",applyY);
ymaxIn.addEventListener("change",applyY);

function setMode(auto){

    view.auto=auto;

    $("#m_auto").classList.toggle("active",auto);
    $("#m_fixed").classList.toggle("active",!auto);

    yminIn.disabled=auto;
    ymaxIn.disabled=auto;

    $("#axhint").textContent=auto
        ? "Auto scale fits the amplitude axis to the signal. The boxes show the range currently used."
        : "Fixed values: the amplitude axis uses exactly the minimum and maximum above.";

    render();
}

$("#m_auto").addEventListener("click",()=>setMode(true));
$("#m_fixed").addEventListener("click",()=>setMode(false));

// ======================================
// THEMES
// ======================================

const themes={
    light:{text:"#1f2a44",tick:"#44506e",axis:"#44506e",zero:"#9aa6bf",grid:"#e0e6f3",
           line:"#2f6fed",im:"#12a36a",env:"#f08a24",accent:"#e5484d",ring:"#ffffff",
           legendBg:"rgba(255,255,255,0.92)",glow:5},
    dark:{text:"#e6edf7",tick:"#b4c0d9",axis:"#b4c0d9",zero:"#6e7b96",grid:"#27324a",
          line:"#58a6ff",im:"#3ddc97",env:"#ffb454",accent:"#ff6b6b",ring:"#111724",
          legendBg:"rgba(15,21,34,0.92)",glow:14}
};

let darkMode=!!(window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches);
let C=themes.light;
const themeBtn=$("#theme");

function applyTheme(){
    C=darkMode?themes.dark:themes.light;
    root.classList.toggle("dark",darkMode);
    themeBtn.textContent=darkMode?"☀ LIGHT MODE":"🌙 DARK MODE";
}

themeBtn.addEventListener("click",()=>{
    darkMode=!darkMode;
    applyTheme();
    render();
});

applyTheme();

// ======================================
// MATH HELPERS
// ======================================

function num(v){
    // short readable number for formulas
    const r=Math.round(v*1e4)/1e4;
    return String(r);
}

function valueAt(t){
    if(sig.type==="exp")  return sig.C*Math.exp(sig.a*t);
    if(sig.type==="sine") return sig.A*Math.cos(2*Math.PI*sig.f*t+sig.k*Math.PI);
    if(sig.type==="step") return t>=0?1:0;
    return 0;
}

function equation(){
    if(sig.type==="exp")
        return "x(t) = "+num(sig.C)+" · exp("+num(sig.a)+" t)";
    if(sig.type==="sine")
        return "x(t) = "+num(sig.A)+" · cos(2π · "+num(sig.f)+" · t"+
               (sig.k===0?"":(sig.k<0?" − "+num(-sig.k):" + "+num(sig.k))+"π")+")";
    if(sig.type==="cplx")
        return "x(t) = "+num(sig.mag)+"·e^(j"+num(sig.th)+"π) · exp(("+num(sig.r)+
               (sig.d<0?" − j"+num(-sig.d):" + j"+num(sig.d))+"π) t)";
    if(sig.type==="step") return "x(t) = u(t)";
    return "x(t) = δ(t)";
}

function padRange(lo,hi){

    lo=Math.min(0,lo);
    hi=Math.max(0,hi);

    let span=hi-lo;
    if(span<1e-12){ lo=-1; hi=1; span=2; }

    return [lo-0.12*span, hi+0.12*span];
}

// sampled curve for exponentials and sinusoids
function sampleCurve(){

    const span=view.tmax-view.tmin;
    let n=2000;

    if(sig.type==="sine") n=Math.min(40000,Math.max(2000,Math.ceil(span*sig.f*40)));

    const ts=new Float64Array(n+1), vs=new Float64Array(n+1);

    for(let i=0;i<=n;i++){
        const t=view.tmin+span*i/n;
        ts[i]=t;
        const v=valueAt(t);
        // values beyond 1e15 are not drawn (they would overflow the axis)
        vs[i]=(Number.isFinite(v)&&Math.abs(v)<=1e15)?v:NaN;
    }

    return {ts,vs,n};
}

function autoRange(curve){

    if(sig.type==="step") return padRange(0,1);
    if(sig.type==="imp")  return padRange(0,1);

    let lo=0, hi=0;

    for(let i=0;i<=curve.n;i++){
        const v=curve.vs[i];
        if(Number.isNaN(v)) continue;
        if(v<lo) lo=v;
        if(v>hi) hi=v;
    }

    return padRange(lo,hi);
}

// ======================================
// CANVAS
// ======================================

const cv=$("#cv");
const dpr=()=>window.devicePixelRatio||1;
let hoverX=null;

function fit(){

    const w=Math.max(280,Math.floor(cv.parentElement.clientWidth));
    const h=sig.type==="cplx"
        ? Math.round(Math.min(780,Math.max(560,w*0.78)))     // two stacked plots
        : Math.round(Math.min(600,Math.max(340,w*0.56)));

    cv._w=w;
    cv._h=h;
    cv.style.width=w+"px";
    cv.style.height=h+"px";
    cv.width=Math.round(w*dpr());
    cv.height=Math.round(h*dpr());
}

function niceTicks(a,b,n){

    const raw=(b-a)/n;
    const mag=Math.pow(10,Math.floor(Math.log10(raw)));
    const r=raw/mag;
    const step=(r<=1?1:r<=2?2:r<=5?5:10)*mag;

    const ticks=[];
    for(let v=Math.ceil(a/step-1e-9)*step; v<=b+1e-9; v+=step){
        ticks.push(Math.abs(v)<step*1e-9?0:v);
    }

    return {ticks,step};
}

function fmt(v,step){

    if(v===0) return "0";

    if(Math.abs(v)>=1e5 || Math.abs(v)<1e-3)
        return v.toExponential(1).replace("e+","e");

    const dec=Math.max(0,-Math.floor(Math.log10(step)+1e-9));
    return v.toFixed(Math.min(dec,6));
}

function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath();
    ctx.moveTo(x+r,y);
    ctx.arcTo(x+w,y,x+w,y+h,r);
    ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r);
    ctx.arcTo(x,y,x+w,y,r);
    ctx.closePath();
}

// Block 1: the function with the actual parameters.
// Block 2: the plotted time range and amplitude range.
function updateInfo(ymin,ymax){

    $("#status_eq").textContent=equation();

    $("#status_rng").textContent=
        "t: "+num(view.tmin)+" … "+num(view.tmax)+" s     |     amplitude: "+
        num(ymin)+" … "+num(ymax)+(view.auto?" (auto)":" (fixed)");
}

// ======================================
// COMPLEX EXPONENTIAL: Re and Im plots with envelopes
// ======================================

function sampleComplex(){

    const span=view.tmax-view.tmin;
    const n=Math.min(40000,Math.max(2000,Math.ceil(span*Math.abs(sig.d)/2*40)));

    const ts=new Float64Array(n+1), re=new Float64Array(n+1),
          im=new Float64Array(n+1), en=new Float64Array(n+1);

    for(let i=0;i<=n;i++){

        const t=view.tmin+span*i/n;
        const e=sig.mag*Math.exp(sig.r*t);
        const ph=sig.d*Math.PI*t+sig.th*Math.PI;
        const ok=Number.isFinite(e)&&e<=1e15;

        ts[i]=t;
        en[i]=ok?e:NaN;
        re[i]=ok?e*Math.cos(ph):NaN;
        im[i]=ok?e*Math.sin(ph):NaN;
    }

    return {ts,re,im,en,n};
}

function drawFrame(ctx,L,R,T,B,ymin,ymax,X,Y,title,ylabel){

    const xt=niceTicks(view.tmin,view.tmax,Math.max(4,Math.floor((R-L)/90)));
    const yt=niceTicks(ymin,ymax,Math.max(3,Math.floor((B-T)/50)));

    ctx.font="12px Arial";
    ctx.lineWidth=1;

    xt.ticks.forEach(v=>{
        const x=X(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,T); ctx.lineTo(x,B); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(fmt(v,xt.step),x,B+17);
    });

    yt.ticks.forEach(v=>{
        const y=Y(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(L,y); ctx.lineTo(R,y); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),L-8,y+4);
    });

    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.6;
    ctx.beginPath();
    if(ymin<=0&&ymax>=0){ ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0)); }
    if(view.tmin<=0&&view.tmax>=0){ ctx.moveTo(X(0),T); ctx.lineTo(X(0),B); }
    ctx.stroke();

    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.5;
    ctx.beginPath();
    ctx.moveTo(L,T); ctx.lineTo(L,B); ctx.lineTo(R,B);
    ctx.stroke();

    ctx.fillStyle=C.text;
    ctx.textAlign="left";
    ctx.font="bold 15px Arial";
    ctx.fillText(title,L,T-12);

    ctx.textAlign="center";
    ctx.font="14px Arial";
    ctx.save();
    ctx.translate(18,(T+B)/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText(ylabel,0,0);
    ctx.restore();
}

// small legend box; items: [{color,label,dash}]
function drawLegend(ctx,R,T,items){

    ctx.font="bold 12px Arial";

    let w=0;
    items.forEach(it=>{ w=Math.max(w,ctx.measureText(it.label).width); });
    w+=52;

    const h=10+items.length*20;
    const x=R-w-8, y=T+8;

    roundRect(ctx,x,y,w,h,8);
    ctx.fillStyle=C.legendBg;
    ctx.fill();

    items.forEach((it,k)=>{

        const yy=y+20+k*20;

        ctx.save();
        ctx.strokeStyle=it.color;
        ctx.lineWidth=it.dash?1.3:3.2;
        if(it.dash) ctx.setLineDash([6,4]);
        ctx.beginPath(); ctx.moveTo(x+10,yy-4); ctx.lineTo(x+34,yy-4); ctx.stroke();
        ctx.restore();

        ctx.fillStyle=it.color;
        ctx.textAlign="left";
        ctx.fillText(it.label,x+40,yy);
    });
}

function renderComplex(ctx,W,H){

    const cur=sampleComplex();

    let ymin, ymax;

    if(view.auto){

        // the envelope bounds both parts, so the range is symmetric
        let m=0;
        for(let i=0;i<=cur.n;i++){
            const e=cur.en[i];
            if(!Number.isNaN(e)&&e>m) m=e;
        }

        [ymin,ymax]=padRange(-m,m);

        view.ymin=Number(ymin.toFixed(3));
        view.ymax=Number(ymax.toFixed(3));
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
    }
    else{
        ymin=view.ymin;
        ymax=view.ymax;
    }

    updateInfo(ymin,ymax);

    // ----- geometry: two stacked plots sharing the time range
    const L=68, R=W-24;
    const ph=Math.max(120,(H-158)/2);

    const X=t=>L+(t-view.tmin)/(view.tmax-view.tmin)*(R-L);

    const subs=[
        {T:40,        key:"re",color:C.line,title:"Real part",      ylabel:"Re{x(t)}"},
        {T:40+ph+70,  key:"im",color:C.im,  title:"Imaginary part", ylabel:"Im{x(t)}"}
    ];

    subs.forEach(sb=>{
        sb.B=sb.T+ph;
        sb.Y=v=>sb.B-(v-ymin)/(ymax-ymin)*(sb.B-sb.T);
    });

    subs.forEach(sb=>{

        drawFrame(ctx,L,R,sb.T,sb.B,ymin,ymax,X,sb.Y,sb.title,sb.ylabel);

        const data=cur[sb.key];

        ctx.save();
        ctx.beginPath();
        ctx.rect(L,sb.T,R-L,sb.B-sb.T);
        ctx.clip();
        ctx.lineCap="round";

        // envelope  +|C| e^(rt)  and  -|C| e^(rt)
        ctx.strokeStyle=C.env;
        ctx.lineWidth=0.8;
        ctx.setLineDash([6,4]);

        [1,-1].forEach(sg=>{

            ctx.beginPath();
            let pen=false;

            for(let i=0;i<=cur.n;i++){

                const e=cur.en[i];
                if(Number.isNaN(e)){ pen=false; continue; }

                const x=X(cur.ts[i]);
                const y=Math.max(-1e5,Math.min(1e5,sb.Y(sg*e)));

                if(!pen){ ctx.moveTo(x,y); pen=true; } else ctx.lineTo(x,y);
            }

            ctx.stroke();
        });

        ctx.setLineDash([]);

        // the signal part
        ctx.save();
        ctx.shadowColor=sb.color;
        ctx.shadowBlur=C.glow;
        ctx.strokeStyle=sb.color;
        ctx.lineWidth=3;
        ctx.beginPath();

        let pen=false;

        for(let i=0;i<=cur.n;i++){

            const v=data[i];
            if(Number.isNaN(v)){ pen=false; continue; }

            const x=X(cur.ts[i]);
            const y=Math.max(-1e5,Math.min(1e5,sb.Y(v)));

            if(!pen){ ctx.moveTo(x,y); pen=true; } else ctx.lineTo(x,y);
        }

        ctx.stroke();
        ctx.restore();

        ctx.restore();

        drawLegend(ctx,R,sb.T,[
            {color:sb.color,label:sb.ylabel},
            {color:C.env,dash:true,label:"±|C|·exp(r t)"}
        ]);
    });

    ctx.fillStyle=C.text;
    ctx.textAlign="center";
    ctx.font="14px Arial";
    ctx.fillText("t  (seconds)",(L+R)/2,H-10);

    // ----- hover read-out
    if(hoverX!==null && hoverX>=L && hoverX<=R){

        const t=view.tmin+(hoverX-L)/(R-L)*(view.tmax-view.tmin);
        const e=sig.mag*Math.exp(sig.r*t);
        const ph0=sig.d*Math.PI*t+sig.th*Math.PI;

        if(Number.isFinite(e)&&e<=1e15){

            const vals={re:e*Math.cos(ph0), im:e*Math.sin(ph0)};

            subs.forEach(sb=>{

                ctx.save();
                ctx.strokeStyle=C.accent;
                ctx.globalAlpha=0.7;
                ctx.lineWidth=1.5;
                ctx.setLineDash([5,5]);
                ctx.beginPath(); ctx.moveTo(hoverX,sb.T); ctx.lineTo(hoverX,sb.B); ctx.stroke();
                ctx.restore();

                const py=sb.Y(vals[sb.key]);

                if(py>=sb.T&&py<=sb.B){
                    ctx.fillStyle=C.accent;
                    ctx.beginPath(); ctx.arc(hoverX,py,6,0,2*Math.PI); ctx.fill();
                    ctx.strokeStyle=C.ring;
                    ctx.lineWidth=2;
                    ctx.beginPath(); ctx.arc(hoverX,py,6,0,2*Math.PI); ctx.stroke();
                }
            });

            const f=v=>(Math.abs(v)>=1e5?v.toExponential(2):v.toFixed(3));
            const label="t = "+t.toFixed(3)+" s   Re = "+f(vals.re)+"   Im = "+f(vals.im)+"   |x| = "+f(e);

            ctx.font="bold 12px Arial";
            const w=ctx.measureText(label).width+20;
            const bx=Math.max(L,R-w), by=4;

            roundRect(ctx,bx,by,w,24,8);
            ctx.fillStyle=C.legendBg;
            ctx.fill();

            ctx.fillStyle=C.text;
            ctx.textAlign="left";
            ctx.fillText(label,bx+10,by+16);
        }
    }
}

function render(){

    const W=cv._w, H=cv._h;
    const ctx=cv.getContext("2d");

    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,W,H);
    ctx.lineJoin="round";

    $("#formula").textContent=equation();

    if(sig.type==="cplx"){ renderComplex(ctx,W,H); return; }

    // ----- amplitude range
    const curve=(sig.type==="exp"||sig.type==="sine")?sampleCurve():null;

    let ymin, ymax;

    if(view.auto){

        [ymin,ymax]=autoRange(curve);

        const dec=3;
        view.ymin=Number(ymin.toFixed(dec));
        view.ymax=Number(ymax.toFixed(dec));
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
    }
    else{
        ymin=view.ymin;
        ymax=view.ymax;
    }

    updateInfo(ymin,ymax);

    // ----- plot geometry
    const L=68, R=W-24, T=40, B=H-48;

    const X=t=>L+(t-view.tmin)/(view.tmax-view.tmin)*(R-L);
    const Y=v=>B-(v-ymin)/(ymax-ymin)*(B-T);

    // ----- grid and tick labels
    const xt=niceTicks(view.tmin,view.tmax,Math.max(4,Math.floor((R-L)/90)));
    const yt=niceTicks(ymin,ymax,Math.max(4,Math.floor((B-T)/55)));

    ctx.font="12px Arial";
    ctx.lineWidth=1;

    xt.ticks.forEach(v=>{
        const x=X(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,T); ctx.lineTo(x,B); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(fmt(v,xt.step),x,B+18);
    });

    yt.ticks.forEach(v=>{
        const y=Y(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(L,y); ctx.lineTo(R,y); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),L-8,y+4);
    });

    // zero lines (only when visible)
    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.6;
    ctx.beginPath();
    if(ymin<=0&&ymax>=0){ ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0)); }
    if(view.tmin<=0&&view.tmax>=0){ ctx.moveTo(X(0),T); ctx.lineTo(X(0),B); }
    ctx.stroke();

    // frame
    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.5;
    ctx.beginPath();
    ctx.moveTo(L,T); ctx.lineTo(L,B); ctx.lineTo(R,B);
    ctx.stroke();

    // titles and axis labels
    ctx.fillStyle=C.text;
    ctx.textAlign="left";
    ctx.font="bold 16px Arial";
    ctx.fillText(equation(),L,26);

    ctx.textAlign="center";
    ctx.font="14px Arial";
    ctx.fillText("t  (seconds)",(L+R)/2,H-10);

    ctx.save();
    ctx.translate(18,(T+B)/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText("x(t)",0,0);
    ctx.restore();

    // ----- signal
    ctx.save();
    ctx.beginPath();
    ctx.rect(L,T,R-L,B-T);
    ctx.clip();

    ctx.strokeStyle=C.line;
    ctx.fillStyle=C.line;
    ctx.lineWidth=3.2;
    ctx.lineCap="round";

    ctx.save();
    ctx.shadowColor=C.line;
    ctx.shadowBlur=C.glow;

    if(sig.type==="exp"||sig.type==="sine"){

        ctx.beginPath();
        let pen=false;

        for(let i=0;i<=curve.n;i++){

            const v=curve.vs[i];

            if(Number.isNaN(v)){ pen=false; continue; }

            const x=X(curve.ts[i]);
            const y=Math.max(-1e5,Math.min(1e5,Y(v)));

            if(!pen){ ctx.moveTo(x,y); pen=true; } else ctx.lineTo(x,y);
        }

        ctx.stroke();
    }
    else if(sig.type==="step"){

        const x0=Math.min(R,Math.max(L,X(0)));

        // 0 for t < 0, 1 for t >= 0
        ctx.beginPath();
        ctx.moveTo(L,Y(0)); ctx.lineTo(x0,Y(0));
        ctx.moveTo(x0,Y(1)); ctx.lineTo(R,Y(1));
        ctx.stroke();

        // vertical jump (dashed)
        if(view.tmin<=0&&view.tmax>=0){
            ctx.save();
            ctx.lineWidth=2;
            ctx.setLineDash([6,6]);
            ctx.globalAlpha=0.55;
            ctx.beginPath();
            ctx.moveTo(x0,Y(0)); ctx.lineTo(x0,Y(1));
            ctx.stroke();
            ctx.restore();

            // filled circle at (0, 1)
            ctx.beginPath(); ctx.arc(x0,Y(1),5.5,0,2*Math.PI); ctx.fill();
        }
    }
    else{

        // unit impulse: arrow of height 1 at t = 0
        if(view.tmin<=0&&view.tmax>=0){

            const x0=X(0), y0=Y(0), y1=Y(1);
            const dir=y1<y0?1:-1;       // arrow points toward the value 1

            ctx.lineWidth=4;
            ctx.beginPath(); ctx.moveTo(x0,y0); ctx.lineTo(x0,y1+dir*8); ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(x0,y1);
            ctx.lineTo(x0-8,y1+dir*18);
            ctx.lineTo(x0+8,y1+dir*18);
            ctx.closePath();
            ctx.fill();
        }
    }

    ctx.restore();   // glow

    ctx.restore();   // clip

    // label for the impulse height / out-of-range notes
    if(sig.type==="imp"){

        ctx.textAlign="left";
        ctx.font="bold 14px Arial";
        ctx.fillStyle=C.line;

        if(view.tmin<=0&&view.tmax>=0){
            const ty=Math.max(T+14,Math.min(B-6,Y(1)+4));
            ctx.fillText("(1)",X(0)+14,ty);
        }
        else{
            ctx.fillStyle=C.tick;
            ctx.fillText("δ(t) is at t = 0, which is outside the plotted time range.",L+12,T+24);
        }
    }

    // ----- hover read-out
    if(hoverX!==null && sig.type!=="imp" && hoverX>=L && hoverX<=R){

        const t=view.tmin+(hoverX-L)/(R-L)*(view.tmax-view.tmin);
        const v=valueAt(t);

        ctx.save();
        ctx.strokeStyle=C.accent;
        ctx.globalAlpha=0.7;
        ctx.lineWidth=1.5;
        ctx.setLineDash([5,5]);
        ctx.beginPath(); ctx.moveTo(hoverX,T); ctx.lineTo(hoverX,B); ctx.stroke();
        ctx.restore();

        if(Number.isFinite(v)){

            const py=Y(v);

            if(py>=T&&py<=B){
                ctx.fillStyle=C.accent;
                ctx.beginPath(); ctx.arc(hoverX,py,6,0,2*Math.PI); ctx.fill();
                ctx.strokeStyle=C.ring;
                ctx.lineWidth=2;
                ctx.beginPath(); ctx.arc(hoverX,py,6,0,2*Math.PI); ctx.stroke();
            }

            const label="t = "+t.toFixed(3)+" s,   x(t) = "+(Math.abs(v)>=1e5?v.toExponential(3):v.toFixed(3));

            ctx.font="bold 13px Arial";
            const w=ctx.measureText(label).width+20;
            const bx=R-w-8, by=T+8;

            roundRect(ctx,bx,by,w,28,8);
            ctx.fillStyle=C.legendBg;
            ctx.fill();

            ctx.fillStyle=C.text;
            ctx.textAlign="left";
            ctx.fillText(label,bx+10,by+19);
        }
    }
}

cv.addEventListener("mousemove",e=>{
    const r=cv.getBoundingClientRect();
    hoverX=(e.clientX-r.left)*(cv._w/r.width);
    render();
});

cv.addEventListener("mouseleave",()=>{
    hoverX=null;
    render();
});

cv.addEventListener("touchmove",e=>{
    const r=cv.getBoundingClientRect();
    hoverX=(e.touches[0].clientX-r.left)*(cv._w/r.width);
    render();
},{passive:true});

cv.addEventListener("touchend",()=>{
    hoverX=null;
    render();
});

// ======================================
// RESPONSIVE RESIZING
// ======================================

function resize(){
    fit();
    render();
}

if(typeof ResizeObserver!=="undefined"){
    new ResizeObserver(resize).observe(cv.parentElement);
}
window.addEventListener("resize",resize);

// initial display
fit();
render();

})();
</script>

</div>
"""

DT_SIGNALS_HTML = r"""
<div id="ROOT_ID" class="animation-app">

<style>
#ROOT_ID {
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:clamp(8px, 2vw, 24px);
    box-sizing:border-box;
    font-family:Arial,sans-serif;
    position:relative;
    color:#1f2a44;
    background:linear-gradient(160deg,#f7f9ff 0%,#eaf0fc 100%);
    border-radius:18px;
    box-shadow:0 10px 30px rgba(31,42,68,0.10);
}

#ROOT_ID * { box-sizing:border-box; }

#ROOT_ID h2 {
    text-align:center;
    font-size:clamp(20px, 2.6vw, 30px);
    margin:12px 0 4px;
    padding:0 140px;      /* keeps long titles clear of the mode button */
    letter-spacing:0.5px;
    background:linear-gradient(90deg,#2f6fed,#12a36a);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
}

#ROOT_ID .subtitle {
    text-align:center;
    font-size:clamp(13px,1.6vw,17px);
    margin:0 0 18px;
    opacity:0.8;
}

#ROOT_ID button.theme {
    color:white;
    border:0;
    border-radius:10px;
    cursor:pointer;
    font-weight:bold;
    white-space:nowrap;
    touch-action:manipulation;
    box-shadow:0 4px 10px rgba(0,0,0,0.22);
    transition:transform .12s, filter .12s;
    background:linear-gradient(135deg,#8b6cff,#5a3fd4);
    position:absolute;
    top:clamp(24px,3vw,36px);
    right:clamp(8px,1.5vw,16px);
    padding:8px 14px;
    font-size:clamp(12px,1.3vw,14px);
    z-index:2;
}
#ROOT_ID button.theme:hover { transform:translateY(-1px); filter:brightness(1.08); }
#ROOT_ID button.theme:active { transform:scale(0.97); }

/* ---------- two-column layout ---------- */
#ROOT_ID .layout {
    display:grid;
    grid-template-columns:310px minmax(0,1fr);
    gap:18px;
    align-items:start;
}

#ROOT_ID .panel {
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
    padding:14px;
}

#ROOT_ID .left { display:flex; flex-direction:column; gap:14px; }

#ROOT_ID .panel h3 { margin:0 0 10px; font-size:17px; }
#ROOT_ID .sigcard { --c:#2f6fed; }
#ROOT_ID .sigcard h3 { color:var(--c); }

#ROOT_ID .tiles {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

#ROOT_ID .tile {
    cursor:pointer;
    border:2px solid #d3dcf0;
    border-radius:10px;
    padding:6px 4px 5px;
    text-align:center;
    font-size:12px;
    font-weight:bold;
    background:#ffffff;
    user-select:none;
    transition:border-color .12s, box-shadow .12s;
}
#ROOT_ID .tile:hover { border-color:var(--c); }
#ROOT_ID .tile.active {
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}
#ROOT_ID .tile svg { display:block; width:100%; height:36px; stroke:var(--c); fill:none; }

#ROOT_ID .formula {
    margin:12px 0 0;
    padding:8px 10px;
    border-radius:8px;
    background:rgba(47,111,237,0.08);
    font-size:14px;
    font-weight:bold;
    text-align:center;
}

#ROOT_ID .desc {
    display:none;
    margin-top:10px;
    font-size:13px;
    line-height:1.5;
    opacity:0.85;
}
#ROOT_ID .desc.show { display:block; }

#ROOT_ID .param {
    display:none;
    margin-top:10px;
    font-size:13px;
    font-weight:bold;
}
#ROOT_ID .param.show { display:block; }

#ROOT_ID input[type=number] {
    display:block;
    width:100%;
    margin-top:5px;
    padding:7px;
    font-size:15px;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
    text-align:center;
}
#ROOT_ID input[type=number]:focus {
    outline:none;
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.25);
}
#ROOT_ID input[type=number]:disabled { opacity:0.55; cursor:not-allowed; }

#ROOT_ID .grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
#ROOT_ID .grid2 label { font-size:13px; font-weight:bold; }

#ROOT_ID .subhead {
    margin:14px 0 6px;
    font-size:14px;
    font-weight:bold;
}

#ROOT_ID .seg {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:6px;
    margin-bottom:10px;
}
#ROOT_ID .seg div {
    cursor:pointer;
    text-align:center;
    padding:7px 4px;
    border:2px solid #d3dcf0;
    border-radius:9px;
    background:#ffffff;
    font-size:13px;
    font-weight:bold;
    user-select:none;
}
#ROOT_ID .seg div.active {
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.22);
    color:#2f6fed;
}

#ROOT_ID .hint { margin-top:8px; font-size:12px; opacity:0.75; line-height:1.45; }

/* ---------- right column ---------- */
#ROOT_ID .right { min-width:0; }

#ROOT_ID .statusrow {
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:10px;
    margin-bottom:12px;
}

#ROOT_ID .status {
    text-align:center;
    width:fit-content;
    max-width:100%;
    margin:0;
    padding:9px 20px;
    border-radius:999px;
    background:#ffffff;
    border:1px solid #d3dcf0;
    box-shadow:0 3px 10px rgba(31,42,68,0.08);
    font-size:clamp(12px,1.5vw,16px);
    font-weight:bold;
}

#ROOT_ID canvas {
    display:block;
    max-width:100%;
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
}

/* ---------- dark mode ---------- */
#ROOT_ID.dark {
    background:linear-gradient(160deg,#0d1117 0%,#161d2e 100%);
    color:#e6edf7;
    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}
#ROOT_ID.dark h2 {
    background:linear-gradient(90deg,#6aa9ff,#3ddc97);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}
#ROOT_ID.dark .panel,
#ROOT_ID.dark canvas {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
    box-shadow:0 6px 18px rgba(0,0,0,0.5);
}
#ROOT_ID.dark .sigcard { --c:#58a6ff; }
#ROOT_ID.dark .tile,
#ROOT_ID.dark .seg div { background:#0f1522; border-color:#33415f; }
#ROOT_ID.dark .tile:hover,
#ROOT_ID.dark .tile.active { border-color:var(--c); }
#ROOT_ID.dark .seg div.active { border-color:#58a6ff; color:#6aa9ff; box-shadow:0 0 0 3px rgba(88,166,255,0.28); }
#ROOT_ID.dark .formula { background:rgba(88,166,255,0.12); }
#ROOT_ID.dark input[type=number] {
    background:#0f1522;
    color:#e6edf7;
    border-color:#3b4866;
}
#ROOT_ID.dark input[type=number]:focus {
    border-color:#58a6ff;
    box-shadow:0 0 0 3px rgba(88,166,255,0.30);
}
#ROOT_ID.dark .status {
    background:#1a2233;
    border-color:#33415f;
    color:#e6edf7;
    box-shadow:0 3px 12px rgba(0,0,0,0.4);
}

/* ---------- responsive ---------- */
@media (max-width:900px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
    #ROOT_ID .left { flex-direction:row; flex-wrap:wrap; }
    #ROOT_ID .left .panel { flex:1 1 280px; }
}

@media (max-width:550px) {
    #ROOT_ID { padding:6px; }
    #ROOT_ID h2 { margin-top:64px; padding:0; }
    #ROOT_ID button.theme { padding:7px 11px; }
}
</style>

<button class="theme" id="theme">🌙 DARK MODE</button>

<h2>Basic Discrete-Time Signals</h2>
<div class="subtitle">Choose a signal, set its parameters and the plotting area</div>

<div class="layout">

    <!-- LEFT COLUMN -->
    <div class="left">

        <div class="panel sigcard" id="card_sig"></div>

        <div class="panel" id="card_axes">
            <h3>Plotting area</h3>

            <div class="subhead" style="margin-top:0">Index axis (n)</div>
            <div class="grid2">
                <label>n<sub>min</sub>
                    <input id="nmin" type="number" value="-10" min="-1000" max="999" step="1">
                </label>
                <label>n<sub>max</sub>
                    <input id="nmax" type="number" value="10" min="-999" max="1000" step="1">
                </label>
            </div>
            <div class="hint">Integers only (at most 500 samples are shown).</div>

            <div class="subhead">Amplitude axis</div>
            <div class="seg">
                <div id="m_auto" class="active">Auto scale</div>
                <div id="m_fixed">Fixed values</div>
            </div>

            <div class="grid2">
                <label>Min amplitude
                    <input id="ymin" type="number" value="-1" step="0.5" disabled>
                </label>
                <label>Max amplitude
                    <input id="ymax" type="number" value="1" step="0.5" disabled>
                </label>
            </div>

            <div class="hint" id="axhint">Auto scale fits the amplitude axis to the signal. The boxes show the range currently used.</div>
        </div>

    </div>

    <!-- RIGHT COLUMN -->
    <div class="right">
        <div class="statusrow">
            <div class="status" id="status_eq"></div>
            <div class="status" id="status_rng"></div>
        </div>
        <canvas id="cv"></canvas>
    </div>

</div>

<script>
(function(){

const root=document.getElementById("ROOT_ID");
const $=s=>root.querySelector(s);

// ======================================
// SIGNAL DEFINITIONS  (discrete time)
// ======================================

// small stem-plot icons (values between -1 and 1)
const ICONS={
    exp:  [0.1,0.17,0.27,0.4,0.55,0.72,0.88,1],
    sine: [1,0.7,0,-0.7,-1,-0.7,0,0.7],
    step: [0,0,0,1,1,1,1,1],
    imp:  [0,0,0,1,0,0,0,0]
};

function iconSVG(vals){

    let g='<svg viewBox="0 0 64 28">'+
          '<line x1="2" y1="14" x2="62" y2="14" stroke-width="1" opacity="0.35"/>';

    vals.forEach((v,i)=>{
        const x=7+i*7.2, y=14-v*11;
        g+='<line x1="'+x+'" y1="14" x2="'+x+'" y2="'+y+'" stroke-width="2" stroke-linecap="round"/>'+
           '<circle cx="'+x+'" cy="'+y+'" r="2.4" fill="var(--c)" stroke="none"/>';
    });

    return g+'</svg>';
}

const TYPES={
    exp:  {label:"Real exponential"},
    sine: {label:"Sinusoidal"},
    step: {label:"Unit step"},
    imp:  {label:"Unit impulse"}
};

const ORDER=["exp","sine","step","imp"];

const PARAMS=[
    {p:"C",label:"Amplitude C",                          types:["exp"],  min:-100, max:100, step:0.1},
    {p:"a",label:"Base a (real)  —  a<sup>n</sup>",     types:["exp"],  min:-10,  max:10,  step:0.1},
    {p:"A",label:"Amplitude A",                          types:["sine"], min:-100, max:100, step:0.1},
    {p:"f",label:"Frequency f (Hz)",                     types:["sine"], min:0,    max:10000, step:0.1},
    {p:"Fs",label:"Sampling frequency F<sub>s</sub> (Hz, positive integer)", types:["sine"], min:1, max:10000, step:1, int:true},
    {p:"k",label:"Phase factor k  (φ = k·π)",            types:["sine"], min:-100, max:100, step:0.1}
];

const DESCS={
    step:"u[n] = 1 for n ≥ 0 and 0 for n &lt; 0.",
    imp:"δ[n] = 1 at n = 0 and 0 for every other n."
};

// extra notes shown under the parameters of a signal type
const NOTES={
    exp:"For a = 0 the signal is C·δ[n]: aⁿ is undefined for n &lt; 0, so those samples are drawn as 0.",
    sine:"Sample n occurs at t = n / F<sub>s</sub> seconds. A second axis shows this time in seconds."
};

const sig={type:"exp", C:1, a:0.9, A:1, f:1, Fs:10, k:0};

const view={nmin:-10, nmax:10, auto:true, ymin:-1, ymax:1};

// ======================================
// LEFT COLUMN: SIGNAL CARD
// ======================================

function buildCard(){

    const card=$("#card_sig");

    let h='<h3>Signal type</h3><div class="tiles">';

    ORDER.forEach(id=>{
        h+='<div class="tile" data-type="'+id+'">'+iconSVG(ICONS[id])+TYPES[id].label+'</div>';
    });

    h+='</div><div class="formula" id="formula"></div>';

    PARAMS.forEach(q=>{
        h+='<label class="param" data-for="'+q.types.join(" ")+'">'+q.label+
           '<input type="number" data-p="'+q.p+'" min="'+q.min+'" max="'+q.max+
           '" step="'+q.step+'" value="'+sig[q.p]+'"></label>';
    });

    Object.keys(DESCS).forEach(id=>{
        h+='<div class="desc" data-for="'+id+'">'+DESCS[id]+'</div>';
    });

    Object.keys(NOTES).forEach(id=>{
        h+='<div class="desc" data-for="'+id+'">'+NOTES[id]+'</div>';
    });

    card.innerHTML=h;

    card.querySelectorAll(".tile").forEach(el=>{
        el.addEventListener("click",()=>{
            sig.type=el.dataset.type;
            refreshCard();
            fit();          // the sinusoid has an extra time axis, so it needs more height
            render();
        });
    });

    card.querySelectorAll(".param input").forEach(inp=>{
        inp.addEventListener("change",()=>{

            const p=inp.dataset.p;
            let v=Number(inp.value);

            const lo=Number(inp.min), hi=Number(inp.max);
            if(!Number.isFinite(v)) v=sig[p];
            if(PARAMS.find(r=>r.p===p).int) v=Math.round(v);
            v=Math.min(hi,Math.max(lo,v));

            inp.value=v;
            sig[p]=v;
            render();
        });
    });

    refreshCard();
}

function refreshCard(){

    const card=$("#card_sig");

    card.querySelectorAll(".tile").forEach(el=>{
        el.classList.toggle("active",el.dataset.type===sig.type);
    });

    card.querySelectorAll(".param, .desc").forEach(el=>{
        el.classList.toggle("show",el.dataset.for.split(" ").includes(sig.type));
    });
}

buildCard();

// ======================================
// PLOT AREA SETTINGS (left column)
// ======================================

const nminIn=$("#nmin"), nmaxIn=$("#nmax"), yminIn=$("#ymin"), ymaxIn=$("#ymax");

function applyIndex(){

    let a=Number(nminIn.value), b=Number(nmaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)){
        nminIn.value=view.nmin;
        nmaxIn.value=view.nmax;
        return;
    }

    a=Math.round(a);
    b=Math.round(b);

    if(b<=a || b-a>500){
        nminIn.value=view.nmin;
        nmaxIn.value=view.nmax;
        return;
    }

    nminIn.value=a;
    nmaxIn.value=b;

    view.nmin=a;
    view.nmax=b;
    render();
}

function applyY(){

    const a=Number(yminIn.value), b=Number(ymaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
        return;
    }

    view.ymin=a;
    view.ymax=b;
    render();
}

nminIn.addEventListener("change",applyIndex);
nmaxIn.addEventListener("change",applyIndex);
yminIn.addEventListener("change",applyY);
ymaxIn.addEventListener("change",applyY);

function setMode(auto){

    view.auto=auto;

    $("#m_auto").classList.toggle("active",auto);
    $("#m_fixed").classList.toggle("active",!auto);

    yminIn.disabled=auto;
    ymaxIn.disabled=auto;

    $("#axhint").textContent=auto
        ? "Auto scale fits the amplitude axis to the signal. The boxes show the range currently used."
        : "Fixed values: the amplitude axis uses exactly the minimum and maximum above.";

    render();
}

$("#m_auto").addEventListener("click",()=>setMode(true));
$("#m_fixed").addEventListener("click",()=>setMode(false));

// ======================================
// THEMES
// ======================================

const themes={
    light:{text:"#1f2a44",tick:"#44506e",axis:"#44506e",zero:"#9aa6bf",grid:"#e0e6f3",
           line:"#2f6fed",accent:"#e5484d",ring:"#ffffff",
           legendBg:"rgba(255,255,255,0.92)",glow:5},
    dark:{text:"#e6edf7",tick:"#b4c0d9",axis:"#b4c0d9",zero:"#6e7b96",grid:"#27324a",
          line:"#58a6ff",accent:"#ff6b6b",ring:"#111724",
          legendBg:"rgba(15,21,34,0.92)",glow:14}
};

let darkMode=!!(window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches);
let C=themes.light;
const themeBtn=$("#theme");

function applyTheme(){
    C=darkMode?themes.dark:themes.light;
    root.classList.toggle("dark",darkMode);
    themeBtn.textContent=darkMode?"☀ LIGHT MODE":"🌙 DARK MODE";
}

themeBtn.addEventListener("click",()=>{
    darkMode=!darkMode;
    applyTheme();
    render();
});

applyTheme();

// ======================================
// MATH HELPERS
// ======================================

function num(v){
    // short readable number for formulas
    const r=Math.round(v*1e4)/1e4;
    return String(r);
}

// x[n] for an integer n (NaN when the value is not drawable)
function valueAt(n){

    let v=0;

    if(sig.type==="exp"){
        // a = 0:  0^n is 1 at n = 0, 0 for n > 0 and undefined for n < 0,
        // so the signal is C·δ[n] and the samples with n < 0 are drawn as 0
        if(sig.a===0) v=(n===0)?sig.C:0;
        else          v=sig.C*Math.pow(sig.a,n);
    }
    else if(sig.type==="sine") v=sig.A*Math.cos(2*Math.PI*sig.f/sig.Fs*n+sig.k*Math.PI);
    else if(sig.type==="step") v=n>=0?1:0;
    else                       v=n===0?1:0;

    // values beyond 1e15 are not drawn (they would overflow the axis)
    return (Number.isFinite(v)&&Math.abs(v)<=1e15)?v:NaN;
}

function equation(){
    if(sig.type==="exp")
        return "x[n] = "+num(sig.C)+" · ("+num(sig.a)+")^n";
    if(sig.type==="sine")
        return "x[n] = "+num(sig.A)+" · cos(2π · "+num(sig.f)+"/"+num(sig.Fs)+" · n"+
               (sig.k===0?"":(sig.k<0?" − "+num(-sig.k):" + "+num(sig.k))+"π")+")";
    if(sig.type==="step") return "x[n] = u[n]";
    return "x[n] = δ[n]";
}

function padRange(lo,hi){

    lo=Math.min(0,lo);
    hi=Math.max(0,hi);

    let span=hi-lo;
    if(span<1e-12){ lo=-1; hi=1; span=2; }

    return [lo-0.12*span, hi+0.12*span];
}

// all samples n = nmin .. nmax
function sampleSignal(){

    const count=view.nmax-view.nmin+1;
    const vs=new Float64Array(count);

    for(let i=0;i<count;i++) vs[i]=valueAt(view.nmin+i);

    return {vs,count};
}

function autoRange(cur){

    let lo=0, hi=0;

    for(let i=0;i<cur.count;i++){
        const v=cur.vs[i];
        if(Number.isNaN(v)) continue;
        if(v<lo) lo=v;
        if(v>hi) hi=v;
    }

    return padRange(lo,hi);
}

// Block 1: the function with the actual parameters.
// Block 2: the plotted index range and amplitude range.
function updateInfo(ymin,ymax){

    $("#status_eq").textContent=equation();

    $("#status_rng").textContent=
        "n: "+view.nmin+" … "+view.nmax+"     |     amplitude: "+
        num(ymin)+" … "+num(ymax)+(view.auto?" (auto)":" (fixed)");
}

// ======================================
// CANVAS
// ======================================

const cv=$("#cv");
const dpr=()=>window.devicePixelRatio||1;
let hoverX=null;

function fit(){

    const w=Math.max(280,Math.floor(cv.parentElement.clientWidth));
    const extra=sig.type==="sine"?48:0;     // room for the time axis
    const h=Math.round(Math.min(600,Math.max(340,w*0.56)))+extra;

    cv._w=w;
    cv._h=h;
    cv.style.width=w+"px";
    cv.style.height=h+"px";
    cv.width=Math.round(w*dpr());
    cv.height=Math.round(h*dpr());
}

function niceTicks(a,b,n){

    const raw=(b-a)/n;
    const mag=Math.pow(10,Math.floor(Math.log10(raw)));
    const r=raw/mag;
    const step=(r<=1?1:r<=2?2:r<=5?5:10)*mag;

    const ticks=[];
    for(let v=Math.ceil(a/step-1e-9)*step; v<=b+1e-9; v+=step){
        ticks.push(Math.abs(v)<step*1e-9?0:v);
    }

    return {ticks,step};
}

// integer ticks for the index axis
function intTicks(a,b,maxCount){

    const raw=(b-a)/maxCount;
    const cand=[1,2,5,10,20,50,100,200,500];
    let step=cand[cand.length-1];

    for(const c of cand){ if(c>=raw){ step=c; break; } }

    const ticks=[];
    for(let v=Math.ceil(a/step)*step; v<=b; v+=step) ticks.push(v);

    return ticks;
}

function fmt(v,step){

    if(v===0) return "0";

    if(Math.abs(v)>=1e5 || Math.abs(v)<1e-3)
        return v.toExponential(1).replace("e+","e");

    const dec=Math.max(0,-Math.floor(Math.log10(step)+1e-9));
    return v.toFixed(Math.min(dec,6));
}

function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath();
    ctx.moveTo(x+r,y);
    ctx.arcTo(x+w,y,x+w,y+h,r);
    ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r);
    ctx.arcTo(x,y,x+w,y,r);
    ctx.closePath();
}

function render(){

    const W=cv._w, H=cv._h;
    const ctx=cv.getContext("2d");

    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,W,H);
    ctx.lineJoin="round";

    $("#formula").textContent=equation();

    // ----- amplitude range
    const cur=sampleSignal();

    let ymin, ymax;

    if(view.auto){

        [ymin,ymax]=autoRange(cur);

        view.ymin=Number(ymin.toFixed(3));
        view.ymax=Number(ymax.toFixed(3));
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
    }
    else{
        ymin=view.ymin;
        ymax=view.ymax;
    }

    updateInfo(ymin,ymax);

    // ----- plot geometry
    const hasTime=sig.type==="sine";        // sinusoid: extra axis in seconds
    const L=68, R=W-24, T=40, B=H-(hasTime?96:48);
    const x0=view.nmin-0.5, x1=view.nmax+0.5;
    const unit=(R-L)/(x1-x0);

    const X=n=>L+(n-x0)/(x1-x0)*(R-L);
    const Y=v=>B-(v-ymin)/(ymax-ymin)*(B-T);

    // ----- grid and tick labels
    const xt=intTicks(view.nmin,view.nmax,Math.max(4,Math.floor((R-L)/48)));
    const yt=niceTicks(ymin,ymax,Math.max(4,Math.floor((B-T)/55)));

    ctx.font="12px Arial";
    ctx.lineWidth=1;

    xt.forEach(v=>{
        const x=X(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,T); ctx.lineTo(x,B); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(String(v),x,B+18);
    });

    yt.ticks.forEach(v=>{
        const y=Y(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(L,y); ctx.lineTo(R,y); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),L-8,y+4);
    });

    // zero lines (only when visible)
    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.6;
    ctx.beginPath();
    if(ymin<=0&&ymax>=0){ ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0)); }
    if(view.nmin<=0&&view.nmax>=0){ ctx.moveTo(X(0),T); ctx.lineTo(X(0),B); }
    ctx.stroke();

    // frame
    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.5;
    ctx.beginPath();
    ctx.moveTo(L,T); ctx.lineTo(L,B); ctx.lineTo(R,B);
    ctx.stroke();

    // titles and axis labels
    ctx.fillStyle=C.text;
    ctx.textAlign="left";
    ctx.font="bold 16px Arial";
    ctx.fillText(equation(),L,26);

    ctx.textAlign="center";
    ctx.font="14px Arial";
    if(!hasTime){
        ctx.fillText("n  (sample index)",(L+R)/2,H-10);
    }
    else{

        ctx.fillText("n  (sample index)",(L+R)/2,B+36);

        // second x-axis: time in seconds, t = n / Fs
        const Fs=sig.Fs, ty=B+46;
        const tt=niceTicks(view.nmin/Fs,view.nmax/Fs,Math.max(4,Math.floor((R-L)/90)));

        ctx.strokeStyle=C.axis;
        ctx.lineWidth=1.5;
        ctx.beginPath(); ctx.moveTo(L,ty); ctx.lineTo(R,ty); ctx.stroke();

        ctx.font="12px Arial";
        ctx.textAlign="center";

        tt.ticks.forEach(v=>{

            const x=X(v*Fs);
            if(x<L-0.5||x>R+0.5) return;

            ctx.strokeStyle=C.axis;
            ctx.lineWidth=1.2;
            ctx.beginPath(); ctx.moveTo(x,ty); ctx.lineTo(x,ty+5); ctx.stroke();

            ctx.fillStyle=C.tick;
            ctx.fillText(fmt(v,tt.step),x,ty+19);
        });

        ctx.font="14px Arial";
        ctx.fillStyle=C.text;
        ctx.fillText("t  (seconds),   t = n / Fs",(L+R)/2,ty+42);
    }

    ctx.save();
    ctx.translate(18,(T+B)/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText("x[n]",0,0);
    ctx.restore();

    // ----- stems
    const r=cur.count>150?2:cur.count>90?2.6:cur.count>50?3.4:cur.count>30?4.2:5;

    ctx.save();
    ctx.beginPath();
    ctx.rect(L,T,R-L,B-T);
    ctx.clip();

    ctx.strokeStyle=C.line;
    ctx.fillStyle=C.line;
    ctx.lineWidth=cur.count>90?1.6:2.6;
    ctx.lineCap="round";
    ctx.shadowColor=C.line;
    ctx.shadowBlur=C.glow;

    for(let i=0;i<cur.count;i++){

        const v=cur.vs[i];
        if(Number.isNaN(v)) continue;

        const x=X(view.nmin+i);
        const y=Math.max(-1e5,Math.min(1e5,Y(v)));

        if(v!==0){
            ctx.beginPath(); ctx.moveTo(x,Y(0)); ctx.lineTo(x,y); ctx.stroke();
        }

        // zero-valued samples get a small dot
        ctx.beginPath(); ctx.arc(x,y,v===0?r*0.55:r,0,2*Math.PI); ctx.fill();
    }

    ctx.restore();

    // ----- hover read-out (nearest sample)
    if(hoverX!==null && hoverX>=L && hoverX<=R){

        const n=Math.min(view.nmax,Math.max(view.nmin,Math.round(view.nmin+(hoverX-L)/unit-0.5)));
        const v=valueAt(n);
        const hx=X(n);

        ctx.save();
        ctx.strokeStyle=C.accent;
        ctx.globalAlpha=0.7;
        ctx.lineWidth=1.5;
        ctx.setLineDash([5,5]);
        ctx.beginPath(); ctx.moveTo(hx,T); ctx.lineTo(hx,B); ctx.stroke();
        ctx.restore();

        if(Number.isFinite(v)){

            const py=Y(v);

            if(py>=T&&py<=B){
                ctx.fillStyle=C.accent;
                ctx.beginPath(); ctx.arc(hx,py,r+2,0,2*Math.PI); ctx.fill();
                ctx.strokeStyle=C.ring;
                ctx.lineWidth=2;
                ctx.beginPath(); ctx.arc(hx,py,r+2,0,2*Math.PI); ctx.stroke();
            }

            const label="n = "+n+(hasTime?"  (t = "+(n/sig.Fs).toFixed(3)+" s)":"")+",   x[n] = "+(Math.abs(v)>=1e5?v.toExponential(3):v.toFixed(3));

            ctx.font="bold 13px Arial";
            const w=ctx.measureText(label).width+20;
            const bx=R-w-8, by=T+8;

            roundRect(ctx,bx,by,w,28,8);
            ctx.fillStyle=C.legendBg;
            ctx.fill();

            ctx.fillStyle=C.text;
            ctx.textAlign="left";
            ctx.fillText(label,bx+10,by+19);
        }
    }
}

cv.addEventListener("mousemove",e=>{
    const r=cv.getBoundingClientRect();
    hoverX=(e.clientX-r.left)*(cv._w/r.width);
    render();
});

cv.addEventListener("mouseleave",()=>{
    hoverX=null;
    render();
});

cv.addEventListener("touchmove",e=>{
    const r=cv.getBoundingClientRect();
    hoverX=(e.touches[0].clientX-r.left)*(cv._w/r.width);
    render();
},{passive:true});

cv.addEventListener("touchend",()=>{
    hoverX=null;
    render();
});

// ======================================
// RESPONSIVE RESIZING
// ======================================

function resize(){
    fit();
    render();
}

if(typeof ResizeObserver!=="undefined"){
    new ResizeObserver(resize).observe(cv.parentElement);
}
window.addEventListener("resize",resize);

// initial display
fit();
render();

})();
</script>

</div>
"""

CT_OPERATIONS_HTML = r"""
<div id="ROOT_ID" class="animation-app">

<style>
#ROOT_ID {
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:clamp(8px, 2vw, 24px);
    box-sizing:border-box;
    font-family:Arial,sans-serif;
    position:relative;
    color:#1f2a44;
    background:linear-gradient(160deg,#f7f9ff 0%,#eaf0fc 100%);
    border-radius:18px;
    box-shadow:0 10px 30px rgba(31,42,68,0.10);
}

#ROOT_ID * { box-sizing:border-box; }

#ROOT_ID h2 {
    text-align:center;
    font-size:clamp(20px, 2.6vw, 30px);
    margin:12px 0 4px;
    padding:0 140px;      /* keeps long titles clear of the mode button */
    letter-spacing:0.5px;
    background:linear-gradient(90deg,#2f6fed,#12a36a);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
}

#ROOT_ID .subtitle {
    text-align:center;
    font-size:clamp(13px,1.6vw,17px);
    margin:0 0 18px;
    opacity:0.8;
}

#ROOT_ID button.theme {
    color:white;
    border:0;
    border-radius:10px;
    cursor:pointer;
    font-weight:bold;
    white-space:nowrap;
    touch-action:manipulation;
    box-shadow:0 4px 10px rgba(0,0,0,0.22);
    transition:transform .12s, filter .12s;
    background:linear-gradient(135deg,#8b6cff,#5a3fd4);
    position:absolute;
    top:clamp(24px,3vw,36px);
    right:clamp(8px,1.5vw,16px);
    padding:8px 14px;
    font-size:clamp(12px,1.3vw,14px);
    z-index:2;
}
#ROOT_ID button.theme:hover { transform:translateY(-1px); filter:brightness(1.08); }
#ROOT_ID button.theme:active { transform:scale(0.97); }

/* ---------- two-column layout ---------- */
#ROOT_ID .layout {
    display:grid;
    grid-template-columns:310px minmax(0,1fr);
    gap:18px;
    align-items:start;
}

#ROOT_ID .panel {
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
    padding:14px;
}

#ROOT_ID .left { display:flex; flex-direction:column; gap:14px; }

#ROOT_ID .panel h3 { margin:0 0 10px; font-size:17px; }
#ROOT_ID .sigcard { --c:#2f6fed; }
#ROOT_ID .sigcard h3 { color:var(--c); }

#ROOT_ID .tiles {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

#ROOT_ID .tile {
    cursor:pointer;
    border:2px solid #d3dcf0;
    border-radius:10px;
    padding:6px 4px 5px;
    text-align:center;
    font-size:12px;
    font-weight:bold;
    background:#ffffff;
    user-select:none;
    transition:border-color .12s, box-shadow .12s;
}
#ROOT_ID .tile:hover { border-color:var(--c); }
#ROOT_ID .tile.active {
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}
#ROOT_ID .tile svg { display:block; width:100%; height:36px; stroke:var(--c); fill:none; }

#ROOT_ID .formula {
    margin:12px 0 0;
    padding:8px 10px;
    border-radius:8px;
    background:rgba(47,111,237,0.08);
    font-size:14px;
    font-weight:bold;
    text-align:center;
}

#ROOT_ID .desc {
    display:none;
    margin-top:10px;
    font-size:13px;
    line-height:1.5;
    opacity:0.85;
}
#ROOT_ID .desc.show { display:block; }

#ROOT_ID .param {
    display:none;
    margin-top:10px;
    font-size:13px;
    font-weight:bold;
}
#ROOT_ID .param.show { display:block; }

#ROOT_ID input[type=number] {
    display:block;
    width:100%;
    margin-top:5px;
    padding:7px;
    font-size:15px;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
    text-align:center;
}
#ROOT_ID input[type=number]:focus {
    outline:none;
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.25);
}
#ROOT_ID input[type=number]:disabled { opacity:0.55; cursor:not-allowed; }

#ROOT_ID .grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
#ROOT_ID .grid2 label { font-size:13px; font-weight:bold; }

#ROOT_ID .subhead {
    margin:14px 0 6px;
    font-size:14px;
    font-weight:bold;
}

#ROOT_ID .seg {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:6px;
    margin-bottom:10px;
}
#ROOT_ID .seg div {
    cursor:pointer;
    text-align:center;
    padding:7px 4px;
    border:2px solid #d3dcf0;
    border-radius:9px;
    background:#ffffff;
    font-size:13px;
    font-weight:bold;
    user-select:none;
}
#ROOT_ID .seg div.active {
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.22);
    color:#2f6fed;
}

#ROOT_ID .hint { margin-top:8px; font-size:12px; opacity:0.75; line-height:1.45; }

/* ---------- right column ---------- */
#ROOT_ID .right { min-width:0; }

#ROOT_ID .statusrow {
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:10px;
    margin-bottom:12px;
}

#ROOT_ID .status {
    text-align:center;
    width:fit-content;
    max-width:100%;
    margin:0;
    padding:9px 20px;
    border-radius:999px;
    background:#ffffff;
    border:1px solid #d3dcf0;
    box-shadow:0 3px 10px rgba(31,42,68,0.08);
    font-size:clamp(12px,1.5vw,16px);
    font-weight:bold;
}

#ROOT_ID canvas {
    display:block;
    max-width:100%;
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
}

#ROOT_ID .plots { display:flex; flex-direction:column; gap:12px; min-width:0; }

#ROOT_ID .tile { line-height:1.25; }

/* ---------- dark mode ---------- */
#ROOT_ID.dark {
    background:linear-gradient(160deg,#0d1117 0%,#161d2e 100%);
    color:#e6edf7;
    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}
#ROOT_ID.dark h2 {
    background:linear-gradient(90deg,#6aa9ff,#3ddc97);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}
#ROOT_ID.dark .panel,
#ROOT_ID.dark canvas {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
    box-shadow:0 6px 18px rgba(0,0,0,0.5);
}
#ROOT_ID.dark .sigcard { --c:#58a6ff; }
#ROOT_ID.dark .tile,
#ROOT_ID.dark .seg div { background:#0f1522; border-color:#33415f; }
#ROOT_ID.dark .tile:hover,
#ROOT_ID.dark .tile.active { border-color:var(--c); }
#ROOT_ID.dark .seg div.active { border-color:#58a6ff; color:#6aa9ff; box-shadow:0 0 0 3px rgba(88,166,255,0.28); }
#ROOT_ID.dark .formula { background:rgba(88,166,255,0.12); }
#ROOT_ID.dark input[type=number] {
    background:#0f1522;
    color:#e6edf7;
    border-color:#3b4866;
}
#ROOT_ID.dark input[type=number]:focus {
    border-color:#58a6ff;
    box-shadow:0 0 0 3px rgba(88,166,255,0.30);
}
#ROOT_ID.dark .status {
    background:#1a2233;
    border-color:#33415f;
    color:#e6edf7;
    box-shadow:0 3px 12px rgba(0,0,0,0.4);
}

/* ---------- responsive ---------- */
@media (max-width:900px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
    #ROOT_ID .left { flex-direction:row; flex-wrap:wrap; }
    #ROOT_ID .left .panel { flex:1 1 280px; }
}

@media (max-width:550px) {
    #ROOT_ID { padding:6px; }
    #ROOT_ID h2 { margin-top:64px; padding:0; }
    #ROOT_ID button.theme { padding:7px 11px; }
}
</style>

<button class="theme" id="theme">🌙 DARK MODE</button>

<h2>Time Operations on a Continuous-Time Signal</h2>
<div class="subtitle">Choose a prototype x(t) and a time operation: shifting, reversal or scaling</div>

<div class="layout">

    <!-- LEFT COLUMN -->
    <div class="left">

        <div class="panel sigcard" id="card_proto"></div>

        <div class="panel sigcard" id="card_op"></div>

        <div class="panel" id="card_axes">
            <h3>Plotting area</h3>

            <div class="subhead" style="margin-top:0">Time axis</div>
            <div class="grid2">
                <label>t<sub>min</sub> (s)
                    <input id="tmin" type="number" value="-8" min="-1000" max="999" step="1">
                </label>
                <label>t<sub>max</sub> (s)
                    <input id="tmax" type="number" value="8" min="-999" max="1000" step="1">
                </label>
            </div>

            <div class="subhead">Amplitude axis</div>
            <div class="seg">
                <div id="m_auto" class="active">Auto scale</div>
                <div id="m_fixed">Fixed values</div>
            </div>

            <div class="grid2">
                <label>Min amplitude
                    <input id="ymin" type="number" value="-1" step="0.5" disabled>
                </label>
                <label>Max amplitude
                    <input id="ymax" type="number" value="1" step="0.5" disabled>
                </label>
            </div>

            <div class="hint" id="axhint">Auto scale fits one common amplitude axis to both plots. The boxes show the range currently used.</div>
        </div>

    </div>

    <!-- RIGHT COLUMN -->
    <div class="right">
        <div class="statusrow">
            <div class="status" id="status_eq"></div>
            <div class="status" id="status_rng"></div>
        </div>
        <div class="plots" id="plots">
            <canvas id="cTop"></canvas>
            <canvas id="cBot"></canvas>
        </div>
    </div>

</div>

<script>
(function(){

const root=document.getElementById("ROOT_ID");
const $=s=>root.querySelector(s);

// ======================================
// DEFINITIONS
// ======================================

const PROTOS={
    step:{label:"Unit step u(t)",
          path:"M2 24 H19 V6 H38"},
    exp: {label:"e<sup>−at</sup> u(t)",
          path:"M2 24 H11 V6 C16 17 26 22 38 23"},
    cos: {label:"cos(2πft + φ)",
          path:"M2 14 C7 0 13 0 19 14 S31 28 38 14"},
    ramp:{label:"A − t,  0 ≤ t ≤ A",
          path:"M2 24 H10 V6 L26 24 H38"}
};
const PROTO_ORDER=["step","exp","cos","ramp"];

const OPS={
    shift:{label:"Time shifting<br>x(t − T<sub>0</sub>)",
           path:"M4 14 H30 M23 7 L31 14 L23 21"},
    rev:  {label:"Time reversal<br>x(−t)",
           path:"M2 14 H38 M10 7 L2 14 L10 21 M30 7 L38 14 L30 21"},
    scale:{label:"Time scaling<br>x(αt)",
           path:"M8 22 V6 M32 22 V6 M8 14 H32 M14 8 L8 14 L14 20 M26 8 L32 14 L26 20"},
    combo:{label:"Shifting + scaling<br>x(αt + T<sub>0</sub>)",
           path:"M3 14 H25 M19 8 L26 14 L19 20 M30 6 V22 M37 6 V22"}
};
const OP_ORDER=["shift","rev","scale","combo"];

// adjustable parameters; "group" says which card they belong to
const PARAMS=[
    {g:"proto",p:"a",    label:"Decay rate a",                 types:["exp"],   min:-10,  max:10,  step:0.1},
    {g:"proto",p:"f",    label:"Frequency f (Hz)",             types:["cos"],   min:0,    max:20,  step:0.1},
    {g:"proto",p:"k",    label:"Phase factor k  (φ = k·π)",    types:["cos"],   min:-100, max:100, step:0.1},
    {g:"proto",p:"A",    label:"Parameter A",                  types:["ramp"],  min:0.1,  max:20,  step:0.1},
    {g:"op",   p:"T0",   label:"Shift T<sub>0</sub> (s)",      types:["shift","combo"], min:-50,  max:50,  step:0.1},
    {g:"op",   p:"alpha",label:"Scale factor α (α ≠ 0)",       types:["scale","combo"], min:-20,  max:20,  step:0.1, nonzero:true}
];

const DESCS={
    step:"u(t) = 1 for t ≥ 0 and 0 for t &lt; 0."
};

const proto={type:"ramp", a:1, f:0.5, k:0, A:2};
const op={type:"shift", T0:3, alpha:2};
const isOn=(state,id)=>state.type===id;

const view={tmin:-8, tmax:8, auto:true, ymin:-1, ymax:1};

// ======================================
// LEFT COLUMN: CARDS
// ======================================

function buildCard(cardId,title,items,order,group,state){

    const card=$(cardId);

    let h='<h3>'+title+'</h3>'+(group==="op"?'<div style="font-size:12px;opacity:.75;margin:-4px 0 8px">Choose one operation at a time.</div>':'')+'<div class="tiles">';

    order.forEach((id,i)=>{
        const wide=(order.length%2===1&&i===order.length-1)?' style="grid-column:1 / -1"':'';
        h+='<div class="tile" data-type="'+id+'"'+wide+'>'+
           '<svg viewBox="0 0 40 28"><path d="'+items[id].path+
           '" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'+
           items[id].label+'</div>';
    });

    h+='</div>';

    if(group==="proto") h+='<div class="formula" id="formula"></div>';
    else                h+='<div class="formula" id="opformula"></div>';

    PARAMS.filter(q=>q.g===group).forEach(q=>{
        h+='<label class="param" data-for="'+q.types.join(" ")+'">'+q.label+
           '<input type="number" data-p="'+q.p+'" min="'+q.min+'" max="'+q.max+
           '" step="'+q.step+'" value="'+state[q.p]+'"></label>';
    });

    Object.keys(DESCS).forEach(id=>{
        if(order.includes(id))
            h+='<div class="desc" data-for="'+id+'">'+DESCS[id]+'</div>';
    });

    if(group==="op") h+='<div class="desc show" id="opnote"></div>';

    card.innerHTML=h;

    card.querySelectorAll(".tile").forEach(el=>{
        el.addEventListener("click",()=>{
            state.type=el.dataset.type;
            refreshCard(cardId,state);
            render();
        });
    });

    card.querySelectorAll(".param input").forEach(inp=>{
        inp.addEventListener("change",()=>{

            const p=inp.dataset.p;
            const q=PARAMS.find(r=>r.g===group&&r.p===p);

            let v=Number(inp.value);

            if(!Number.isFinite(v)) v=state[p];
            v=Math.min(q.max,Math.max(q.min,v));
            if(q.nonzero&&v===0) v=state[p];

            inp.value=v;
            state[p]=v;
            render();
        });
    });

    refreshCard(cardId,state);
}

function refreshCard(cardId,state){

    const card=$(cardId);

    card.querySelectorAll(".tile").forEach(el=>{
        el.classList.toggle("active",isOn(state,el.dataset.type));
    });

    card.querySelectorAll(".param, .desc[data-for]").forEach(el=>{
        el.classList.toggle("show",el.dataset.for.split(" ").some(id=>isOn(state,id)));
    });
}

buildCard("#card_proto","1. Signal prototype x(t)",PROTOS,PROTO_ORDER,"proto",proto);
buildCard("#card_op","2. Time operation",OPS,OP_ORDER,"op",op);

// ======================================
// PLOT AREA SETTINGS (left column)
// ======================================

const tminIn=$("#tmin"), tmaxIn=$("#tmax"), yminIn=$("#ymin"), ymaxIn=$("#ymax");

function applyTime(){

    const a=Number(tminIn.value), b=Number(tmaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        tminIn.value=view.tmin;
        tmaxIn.value=view.tmax;
        return;
    }

    view.tmin=a;
    view.tmax=b;
    render();
}

function applyY(){

    const a=Number(yminIn.value), b=Number(ymaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
        return;
    }

    view.ymin=a;
    view.ymax=b;
    render();
}

tminIn.addEventListener("change",applyTime);
tmaxIn.addEventListener("change",applyTime);
yminIn.addEventListener("change",applyY);
ymaxIn.addEventListener("change",applyY);

function setMode(auto){

    view.auto=auto;

    $("#m_auto").classList.toggle("active",auto);
    $("#m_fixed").classList.toggle("active",!auto);

    yminIn.disabled=auto;
    ymaxIn.disabled=auto;

    $("#axhint").textContent=auto
        ? "Auto scale fits one common amplitude axis to both plots. The boxes show the range currently used."
        : "Fixed values: both plots use exactly the minimum and maximum above.";

    render();
}

$("#m_auto").addEventListener("click",()=>setMode(true));
$("#m_fixed").addEventListener("click",()=>setMode(false));

// ======================================
// THEMES
// ======================================

const themes={
    light:{text:"#1f2a44",tick:"#44506e",axis:"#44506e",zero:"#9aa6bf",grid:"#e0e6f3",
           x:"#2f6fed",y:"#12a36a",accent:"#e5484d",ring:"#ffffff",
           legendBg:"rgba(255,255,255,0.92)",glow:5},
    dark:{text:"#e6edf7",tick:"#b4c0d9",axis:"#b4c0d9",zero:"#6e7b96",grid:"#27324a",
          x:"#58a6ff",y:"#3ddc97",accent:"#ff6b6b",ring:"#111724",
          legendBg:"rgba(15,21,34,0.92)",glow:14}
};

let darkMode=!!(window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches);
let C=themes.light;
const themeBtn=$("#theme");

function applyTheme(){
    C=darkMode?themes.dark:themes.light;
    root.classList.toggle("dark",darkMode);
    themeBtn.textContent=darkMode?"☀ LIGHT MODE":"🌙 DARK MODE";
}

themeBtn.addEventListener("click",()=>{
    darkMode=!darkMode;
    applyTheme();
    render();
});

applyTheme();

// ======================================
// SIGNALS AND TIME OPERATIONS
// ======================================

function num(v){
    const r=Math.round(v*1e4)/1e4;
    return String(r).replace("-","−");
}

// the prototype x(t)
function xBase(t){

    let v;

    if(proto.type==="step")      v=t>=0?1:0;
    else if(proto.type==="exp")  v=t>=0?Math.exp(-proto.a*t):0;
    else if(proto.type==="cos")  v=Math.cos(2*Math.PI*proto.f*t+proto.k*Math.PI);
    else                         v=(t>=0&&t<=proto.A)?proto.A-t:0;

    // values beyond 1e15 are not drawn (they would overflow the axis)
    return (Number.isFinite(v)&&Math.abs(v)<=1e15)?v:NaN;
}

// argument of x(.) for the chosen time operation
function argOf(t){
    if(op.type==="shift") return t-op.T0;
    if(op.type==="rev")   return -t;
    if(op.type==="scale") return op.alpha*t;
    return op.alpha*t+op.T0;
}

function yBase(t){ return xBase(argOf(t)); }

// ---------- text ----------

function phaseText(){
    return proto.k===0?"":(proto.k<0?" − "+num(-proto.k):" + "+num(proto.k))+"π";
}

function protoEq(){
    if(proto.type==="step") return "x(t) = u(t)";
    if(proto.type==="exp")  return "x(t) = exp("+num(-proto.a)+" t) · u(t)";
    if(proto.type==="cos")  return "x(t) = cos(2π · "+num(proto.f)+" · t"+phaseText()+")";
    return "x(t) = "+num(proto.A)+" − t   for 0 ≤ t ≤ "+num(proto.A)+",   0 otherwise";
}

// argument written as text, e.g. "t − 3", "−t", "2t"
function argText(){

    if(op.type==="shift"){
        if(op.T0===0) return "t";
        return op.T0>0?"t − "+num(op.T0):"t + "+num(-op.T0);
    }

    if(op.type==="rev") return "−t";

    const at=op.alpha===1?"t":(op.alpha===-1?"−t":num(op.alpha)+"t");

    if(op.type==="scale"||op.T0===0) return at;

    return at+(op.T0>0?" + "+num(op.T0):" − "+num(-op.T0));
}

// the prototype's formula with t replaced by the argument
function substituted(arg){

    const par=(arg==="t")?"t":"("+arg+")";

    if(proto.type==="step") return "u("+arg+")";
    if(proto.type==="exp")  return "exp("+num(-proto.a)+" · "+par+") · u("+arg+")";
    if(proto.type==="cos")  return "cos(2π · "+num(proto.f)+" · "+par+phaseText()+")";
    return "("+num(proto.A)+" − "+par+")   for 0 ≤ "+arg+" ≤ "+num(proto.A)+",   0 otherwise";
}

function opName(){
    if(op.type==="shift") return "time shifting";
    if(op.type==="rev")   return "time reversal";
    if(op.type==="scale") return "time scaling";
    return "time shifting + scaling";
}

function scaleNote(){
    const a=Math.abs(op.alpha);
    let t;
    if(a>1) t="compressed in time by a factor of "+num(a);
    else if(a<1) t="stretched in time by a factor of "+num(1/a);
    else t="not scaled (|α| = 1)";
    return "The signal is "+t+(op.alpha<0?" and also reversed (α is negative)":"")+".";
}

function opNote(){

    if(op.type==="shift"){
        if(op.T0>0) return "x(t) is delayed: the whole shape moves to the right by "+num(op.T0)+" s.";
        if(op.T0<0) return "x(t) is advanced: the whole shape moves to the left by "+num(-op.T0)+" s.";
        return "T₀ = 0, so the signal is unchanged.";
    }

    if(op.type==="rev") return "The signal is mirrored about t = 0 (left and right are swapped).";

    if(op.type==="scale") return scaleNote();

    const d=-op.T0/op.alpha;
    return scaleNote()+" Since x(αt + T₀) = x(α(t + T₀/α)), the scaled shape is also shifted by "+
           num(d)+" s (T₀/α = "+num(op.T0/op.alpha)+", moved "+(d>0?"right":d<0?"left":"nowhere")+").";
}

// ======================================
// SAMPLING AND RANGES
// ======================================

function padRange(lo,hi){

    lo=Math.min(0,lo);
    hi=Math.max(0,hi);

    let span=hi-lo;
    if(span<1e-12){ lo=-1; hi=1; span=2; }

    return [lo-0.12*span, hi+0.12*span];
}

function sample(){

    const span=view.tmax-view.tmin;
    let n=4000;

    if(proto.type==="cos"){
        const scale=(op.type==="scale"||op.type==="combo")?Math.abs(op.alpha):1;
        n=Math.min(40000,Math.max(4000,Math.ceil(span*proto.f*scale*40)));
    }

    const ts=new Float64Array(n+1), xs=new Float64Array(n+1), ys=new Float64Array(n+1);

    for(let i=0;i<=n;i++){
        const t=view.tmin+span*i/n;
        ts[i]=t;
        xs[i]=xBase(t);
        ys[i]=yBase(t);
    }

    return {ts,xs,ys,n};
}

function autoRange(cur){

    let lo=0, hi=0;

    [cur.xs,cur.ys].forEach(arr=>{
        for(let i=0;i<=cur.n;i++){
            const v=arr[i];
            if(Number.isNaN(v)) continue;
            if(v<lo) lo=v;
            if(v>hi) hi=v;
        }
    });

    return padRange(lo,hi);
}

// ======================================
// CANVAS
// ======================================

const plotsBox=$("#plots");
const cTop=$("#cTop"), cBot=$("#cBot");
const dpr=()=>window.devicePixelRatio||1;
let hoverX=null;

function fit(){

    const w=Math.max(280,Math.floor(plotsBox.clientWidth));
    const h=Math.round(Math.min(400,Math.max(260,w*0.34)));

    [cTop,cBot].forEach(cv=>{
        cv._w=w;
        cv._h=h;
        cv.style.width=w+"px";
        cv.style.height=h+"px";
        cv.width=Math.round(w*dpr());
        cv.height=Math.round(h*dpr());
    });
}

function niceTicks(a,b,n){

    const raw=(b-a)/n;
    const mag=Math.pow(10,Math.floor(Math.log10(raw)));
    const r=raw/mag;
    const step=(r<=1?1:r<=2?2:r<=5?5:10)*mag;

    const ticks=[];
    for(let v=Math.ceil(a/step-1e-9)*step; v<=b+1e-9; v+=step){
        ticks.push(Math.abs(v)<step*1e-9?0:v);
    }

    return {ticks,step};
}

function fmt(v,step){

    if(v===0) return "0";

    if(Math.abs(v)>=1e5 || Math.abs(v)<1e-3)
        return v.toExponential(1).replace("e+","e");

    const dec=Math.max(0,-Math.floor(Math.log10(step)+1e-9));
    return v.toFixed(Math.min(dec,6));
}

function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath();
    ctx.moveTo(x+r,y);
    ctx.arcTo(x+w,y,x+w,y+h,r);
    ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r);
    ctx.arcTo(x,y,x+w,y,r);
    ctx.closePath();
}

// o: {title, color, vals, valFn, name, ghost}
function drawPanel(cv,cur,ymin,ymax,o){

    const W=cv._w, H=cv._h;
    const ctx=cv.getContext("2d");

    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,W,H);
    ctx.lineJoin="round";

    const L=68, R=W-24, T=44, B=H-46;

    const X=t=>L+(t-view.tmin)/(view.tmax-view.tmin)*(R-L);
    const Y=v=>B-(v-ymin)/(ymax-ymin)*(B-T);

    const xt=niceTicks(view.tmin,view.tmax,Math.max(4,Math.floor((R-L)/90)));
    const yt=niceTicks(ymin,ymax,Math.max(3,Math.floor((B-T)/55)));

    ctx.font="12px Arial";
    ctx.lineWidth=1;

    xt.ticks.forEach(v=>{
        const x=X(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,T); ctx.lineTo(x,B); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(fmt(v,xt.step),x,B+17);
    });

    yt.ticks.forEach(v=>{
        const y=Y(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(L,y); ctx.lineTo(R,y); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),L-8,y+4);
    });

    // zero lines (only when visible)
    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.8;
    ctx.beginPath();
    if(ymin<=0&&ymax>=0){ ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0)); }
    if(view.tmin<=0&&view.tmax>=0){ ctx.moveTo(X(0),T); ctx.lineTo(X(0),B); }
    ctx.stroke();

    // frame
    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.5;
    ctx.beginPath();
    ctx.moveTo(L,T); ctx.lineTo(L,B); ctx.lineTo(R,B);
    ctx.stroke();

    // title and axis labels
    ctx.fillStyle=C.text;
    ctx.textAlign="left";
    ctx.font="bold 16px Arial";
    ctx.fillText(o.title,L,28);

    ctx.textAlign="center";
    ctx.font="14px Arial";
    ctx.fillText("t  (seconds)",(L+R)/2,H-8);

    ctx.save();
    ctx.translate(18,(T+B)/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText(o.name,0,0);
    ctx.restore();

    // curves
    ctx.save();
    ctx.beginPath();
    ctx.rect(L,T,R-L,B-T);
    ctx.clip();
    ctx.lineCap="round";

    function trace(arr){

        ctx.beginPath();
        let pen=false;

        for(let i=0;i<=cur.n;i++){

            const v=arr[i];
            if(Number.isNaN(v)){ pen=false; continue; }

            const x=X(cur.ts[i]);
            const y=Math.max(-1e5,Math.min(1e5,Y(v)));

            if(!pen){ ctx.moveTo(x,y); pen=true; } else ctx.lineTo(x,y);
        }
    }

    // original signal as a faint dashed reference in the result plot
    if(o.ghost){
        ctx.save();
        ctx.globalAlpha=0.38;
        ctx.strokeStyle=C.x;
        ctx.lineWidth=2;
        ctx.setLineDash([7,6]);
        trace(cur.xs);
        ctx.stroke();
        ctx.restore();
    }

    ctx.save();
    ctx.shadowColor=o.color;
    ctx.shadowBlur=C.glow;
    ctx.strokeStyle=o.color;
    ctx.lineWidth=3.2;
    trace(o.vals);
    ctx.stroke();
    ctx.restore();

    ctx.restore();

    // legend for the faint reference
    if(o.ghost){

        ctx.font="bold 12px Arial";
        const label="original x(t)";
        const w=ctx.measureText(label).width+52;
        const bx=R-w-8, by=T+8;

        roundRect(ctx,bx,by,w,28,8);
        ctx.fillStyle=C.legendBg;
        ctx.fill();

        ctx.save();
        ctx.globalAlpha=0.6;
        ctx.strokeStyle=C.x;
        ctx.lineWidth=2;
        ctx.setLineDash([6,4]);
        ctx.beginPath(); ctx.moveTo(bx+10,by+14); ctx.lineTo(bx+34,by+14); ctx.stroke();
        ctx.restore();

        ctx.fillStyle=C.x;
        ctx.textAlign="left";
        ctx.fillText(label,bx+40,by+18);
    }

    // hover read-out
    if(hoverX!==null && hoverX>=L && hoverX<=R){

        const t=view.tmin+(hoverX-L)/(R-L)*(view.tmax-view.tmin);
        const v=o.valFn(t);

        ctx.save();
        ctx.strokeStyle=C.accent;
        ctx.globalAlpha=0.7;
        ctx.lineWidth=1.5;
        ctx.setLineDash([5,5]);
        ctx.beginPath(); ctx.moveTo(hoverX,T); ctx.lineTo(hoverX,B); ctx.stroke();
        ctx.restore();

        if(Number.isFinite(v)){

            const py=Y(v);

            if(py>=T&&py<=B){
                ctx.fillStyle=C.accent;
                ctx.beginPath(); ctx.arc(hoverX,py,6,0,2*Math.PI); ctx.fill();
                ctx.strokeStyle=C.ring;
                ctx.lineWidth=2;
                ctx.beginPath(); ctx.arc(hoverX,py,6,0,2*Math.PI); ctx.stroke();
            }

            const label="t = "+t.toFixed(3)+" s,   "+o.name+" = "+
                        (Math.abs(v)>=1e5?v.toExponential(3):v.toFixed(3));

            ctx.font="bold 13px Arial";
            const w=ctx.measureText(label).width+20;
            const bx=Math.max(L,(o.ghost?R-w-8-190:R-w-8)), by=T+8;

            roundRect(ctx,bx,by,w,28,8);
            ctx.fillStyle=C.legendBg;
            ctx.fill();

            ctx.fillStyle=C.text;
            ctx.textAlign="left";
            ctx.fillText(label,bx+10,by+19);
        }
    }
}

// ======================================
// RENDER
// ======================================

function render(){

    const cur=sample();

    let ymin, ymax;

    if(view.auto){

        [ymin,ymax]=autoRange(cur);

        view.ymin=Number(ymin.toFixed(3));
        view.ymax=Number(ymax.toFixed(3));
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
    }
    else{
        ymin=view.ymin;
        ymax=view.ymax;
    }

    const arg=argText();

    // text blocks
    $("#formula").textContent=protoEq();
    $("#opformula").textContent="y(t) = x("+arg+")";
    $("#opnote").textContent=opNote();

    $("#status_eq").textContent=protoEq();
    $("#status_rng").textContent="y(t) = x("+arg+") = "+substituted(arg);

    drawPanel(cTop,cur,ymin,ymax,{
        title:"Original signal  x(t)",
        color:C.x, vals:cur.xs, valFn:xBase, name:"x(t)", ghost:false
    });

    drawPanel(cBot,cur,ymin,ymax,{
        title:"Result of "+opName()+":   y(t) = x("+arg+")",
        color:C.y, vals:cur.ys, valFn:yBase, name:"y(t)", ghost:true
    });
}

[cTop,cBot].forEach(cv=>{

    cv.addEventListener("mousemove",e=>{
        const r=cv.getBoundingClientRect();
        hoverX=(e.clientX-r.left)*(cv._w/r.width);
        render();
    });

    cv.addEventListener("mouseleave",()=>{
        hoverX=null;
        render();
    });

    cv.addEventListener("touchmove",e=>{
        const r=cv.getBoundingClientRect();
        hoverX=(e.touches[0].clientX-r.left)*(cv._w/r.width);
        render();
    },{passive:true});

    cv.addEventListener("touchend",()=>{
        hoverX=null;
        render();
    });
});

// ======================================
// RESPONSIVE RESIZING
// ======================================

function resize(){
    fit();
    render();
}

if(typeof ResizeObserver!=="undefined"){
    new ResizeObserver(resize).observe(plotsBox);
}
window.addEventListener("resize",resize);

// initial display
fit();
render();

})();
</script>

</div>
"""

DT_OPERATIONS_HTML = r"""
<div id="ROOT_ID" class="animation-app">

<style>
#ROOT_ID {
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:clamp(8px, 2vw, 24px);
    box-sizing:border-box;
    font-family:Arial,sans-serif;
    position:relative;
    color:#1f2a44;
    background:linear-gradient(160deg,#f7f9ff 0%,#eaf0fc 100%);
    border-radius:18px;
    box-shadow:0 10px 30px rgba(31,42,68,0.10);
}

#ROOT_ID * { box-sizing:border-box; }

#ROOT_ID h2 {
    text-align:center;
    font-size:clamp(20px, 2.6vw, 30px);
    margin:12px 0 4px;
    padding:0 140px;      /* keeps long titles clear of the mode button */
    letter-spacing:0.5px;
    background:linear-gradient(90deg,#2f6fed,#12a36a);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
}

#ROOT_ID .subtitle {
    text-align:center;
    font-size:clamp(13px,1.6vw,17px);
    margin:0 0 18px;
    opacity:0.8;
}

#ROOT_ID button.theme {
    color:white;
    border:0;
    border-radius:10px;
    cursor:pointer;
    font-weight:bold;
    white-space:nowrap;
    touch-action:manipulation;
    box-shadow:0 4px 10px rgba(0,0,0,0.22);
    transition:transform .12s, filter .12s;
    background:linear-gradient(135deg,#8b6cff,#5a3fd4);
    position:absolute;
    top:clamp(24px,3vw,36px);
    right:clamp(8px,1.5vw,16px);
    padding:8px 14px;
    font-size:clamp(12px,1.3vw,14px);
    z-index:2;
}
#ROOT_ID button.theme:hover { transform:translateY(-1px); filter:brightness(1.08); }
#ROOT_ID button.theme:active { transform:scale(0.97); }

/* ---------- two-column layout ---------- */
#ROOT_ID .layout {
    display:grid;
    grid-template-columns:310px minmax(0,1fr);
    gap:18px;
    align-items:start;
}

#ROOT_ID .panel {
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
    padding:14px;
}

#ROOT_ID .left { display:flex; flex-direction:column; gap:14px; }

#ROOT_ID .panel h3 { margin:0 0 10px; font-size:17px; }
#ROOT_ID .sigcard { --c:#2f6fed; }
#ROOT_ID .sigcard h3 { color:var(--c); }

#ROOT_ID .tiles {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

#ROOT_ID .tile {
    cursor:pointer;
    border:2px solid #d3dcf0;
    border-radius:10px;
    padding:6px 4px 5px;
    text-align:center;
    font-size:12px;
    font-weight:bold;
    background:#ffffff;
    user-select:none;
    transition:border-color .12s, box-shadow .12s;
}
#ROOT_ID .tile:hover { border-color:var(--c); }
#ROOT_ID .tile.active {
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}
#ROOT_ID .tile svg { display:block; width:100%; height:36px; stroke:var(--c); fill:none; }

#ROOT_ID .formula {
    margin:12px 0 0;
    padding:8px 10px;
    border-radius:8px;
    background:rgba(47,111,237,0.08);
    font-size:14px;
    font-weight:bold;
    text-align:center;
}

#ROOT_ID .desc {
    display:none;
    margin-top:10px;
    font-size:13px;
    line-height:1.5;
    opacity:0.85;
}
#ROOT_ID .desc.show { display:block; }

#ROOT_ID .param {
    display:none;
    margin-top:10px;
    font-size:13px;
    font-weight:bold;
}
#ROOT_ID .param.show { display:block; }

#ROOT_ID input[type=number] {
    display:block;
    width:100%;
    margin-top:5px;
    padding:7px;
    font-size:15px;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
    text-align:center;
}
#ROOT_ID input[type=number]:focus {
    outline:none;
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.25);
}
#ROOT_ID input[type=number]:disabled { opacity:0.55; cursor:not-allowed; }

#ROOT_ID .grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
#ROOT_ID .grid2 label { font-size:13px; font-weight:bold; }

#ROOT_ID .subhead {
    margin:14px 0 6px;
    font-size:14px;
    font-weight:bold;
}

#ROOT_ID .seg {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:6px;
    margin-bottom:10px;
}
#ROOT_ID .seg div {
    cursor:pointer;
    text-align:center;
    padding:7px 4px;
    border:2px solid #d3dcf0;
    border-radius:9px;
    background:#ffffff;
    font-size:13px;
    font-weight:bold;
    user-select:none;
}
#ROOT_ID .seg div.active {
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.22);
    color:#2f6fed;
}

#ROOT_ID .hint { margin-top:8px; font-size:12px; opacity:0.75; line-height:1.45; }

/* ---------- right column ---------- */
#ROOT_ID .right { min-width:0; }

#ROOT_ID .statusrow {
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:10px;
    margin-bottom:12px;
}

#ROOT_ID .status {
    text-align:center;
    width:fit-content;
    max-width:100%;
    margin:0;
    padding:9px 20px;
    border-radius:999px;
    background:#ffffff;
    border:1px solid #d3dcf0;
    box-shadow:0 3px 10px rgba(31,42,68,0.08);
    font-size:clamp(12px,1.5vw,16px);
    font-weight:bold;
}

#ROOT_ID canvas {
    display:block;
    max-width:100%;
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
}

#ROOT_ID .plots { display:flex; flex-direction:column; gap:12px; min-width:0; }

#ROOT_ID .tile { line-height:1.25; }

/* ---------- dark mode ---------- */
#ROOT_ID.dark {
    background:linear-gradient(160deg,#0d1117 0%,#161d2e 100%);
    color:#e6edf7;
    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}
#ROOT_ID.dark h2 {
    background:linear-gradient(90deg,#6aa9ff,#3ddc97);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}
#ROOT_ID.dark .panel,
#ROOT_ID.dark canvas {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
    box-shadow:0 6px 18px rgba(0,0,0,0.5);
}
#ROOT_ID.dark .sigcard { --c:#58a6ff; }
#ROOT_ID.dark .tile,
#ROOT_ID.dark .seg div { background:#0f1522; border-color:#33415f; }
#ROOT_ID.dark .tile:hover,
#ROOT_ID.dark .tile.active { border-color:var(--c); }
#ROOT_ID.dark .seg div.active { border-color:#58a6ff; color:#6aa9ff; box-shadow:0 0 0 3px rgba(88,166,255,0.28); }
#ROOT_ID.dark .formula { background:rgba(88,166,255,0.12); }
#ROOT_ID.dark input[type=number] {
    background:#0f1522;
    color:#e6edf7;
    border-color:#3b4866;
}
#ROOT_ID.dark input[type=number]:focus {
    border-color:#58a6ff;
    box-shadow:0 0 0 3px rgba(88,166,255,0.30);
}
#ROOT_ID.dark .status {
    background:#1a2233;
    border-color:#33415f;
    color:#e6edf7;
    box-shadow:0 3px 12px rgba(0,0,0,0.4);
}

/* ---------- responsive ---------- */
@media (max-width:900px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
    #ROOT_ID .left { flex-direction:row; flex-wrap:wrap; }
    #ROOT_ID .left .panel { flex:1 1 280px; }
}

@media (max-width:550px) {
    #ROOT_ID { padding:6px; }
    #ROOT_ID h2 { margin-top:64px; padding:0; }
    #ROOT_ID button.theme { padding:7px 11px; }
}
</style>

<button class="theme" id="theme">🌙 DARK MODE</button>

<h2>Time Operations on a Discrete-Time Signal</h2>
<div class="subtitle">Choose a prototype x[n] and a time operation: shifting, reversal or scaling</div>

<div class="layout">

    <!-- LEFT COLUMN -->
    <div class="left">

        <div class="panel sigcard" id="card_proto"></div>

        <div class="panel sigcard" id="card_op"></div>

        <div class="panel" id="card_axes">
            <h3>Plotting area</h3>

            <div class="subhead" style="margin-top:0">Index axis (n)</div>
            <div class="grid2">
                <label>n<sub>min</sub>
                    <input id="tmin" type="number" value="-10" min="-1000" max="999" step="1">
                </label>
                <label>n<sub>max</sub>
                    <input id="tmax" type="number" value="10" min="-999" max="1000" step="1">
                </label>
            </div>

            <div class="hint">Integers only (at most 500 samples are shown).</div>

            <div class="subhead">Amplitude axis</div>
            <div class="seg">
                <div id="m_auto" class="active">Auto scale</div>
                <div id="m_fixed">Fixed values</div>
            </div>

            <div class="grid2">
                <label>Min amplitude
                    <input id="ymin" type="number" value="-1" step="0.5" disabled>
                </label>
                <label>Max amplitude
                    <input id="ymax" type="number" value="1" step="0.5" disabled>
                </label>
            </div>

            <div class="hint" id="axhint">Auto scale fits one common amplitude axis to both plots. The boxes show the range currently used.</div>
        </div>

    </div>

    <!-- RIGHT COLUMN -->
    <div class="right">
        <div class="statusrow">
            <div class="status" id="status_eq"></div>
            <div class="status" id="status_rng"></div>
        </div>
        <div class="plots" id="plots">
            <canvas id="cTop"></canvas>
            <canvas id="cBot"></canvas>
        </div>
    </div>

</div>

<script>
(function(){

const root=document.getElementById("ROOT_ID");
const $=s=>root.querySelector(s);

// ======================================
// DEFINITIONS
// ======================================

const PROTOS={
    step:{label:"Unit step u[n]",
          path:"M2 24 H38 M18 24 V6 M24 24 V6 M30 24 V6 M36 24 V6"},
    exp: {label:"a<sup>n</sup> u[n]",
          path:"M2 24 H38 M12 24 V6 M18 24 V12 M24 24 V16 M30 24 V19 M36 24 V21"},
    cos: {label:"cos(2πf/F<sub>s</sub>·n + φ)",
          path:"M2 14 H38 M5 14 V3 M11 14 V8.5 M17 14 V19.5 M23 14 V25 M29 14 V19.5 M35 14 V8.5"},
    tent:{label:"Tent: n, then 2N − n",
          path:"M2 24 H38 M8 24 V22 M14 24 V16 M20 24 V10 M26 24 V6 M32 24 V12"}
};
const PROTO_ORDER=["step","exp","cos","tent"];

const OPS={
    shift:{label:"Time shifting<br>x[n − n<sub>0</sub>]",
           path:"M4 14 H30 M23 7 L31 14 L23 21"},
    rev:  {label:"Time reversal<br>x[−n]",
           path:"M2 14 H38 M10 7 L2 14 L10 21 M30 7 L38 14 L30 21"},
    scale:{label:"Time scaling<br>x[αn]",
           path:"M8 22 V6 M32 22 V6 M8 14 H32 M14 8 L8 14 L14 20 M26 8 L32 14 L26 20"},
    combo:{label:"Shifting + scaling<br>x[αn + n<sub>0</sub>]",
           path:"M3 14 H25 M19 8 L26 14 L19 20 M30 6 V22 M37 6 V22"}
};
const OP_ORDER=["shift","rev","scale","combo"];

// adjustable parameters; "group" says which card they belong to
// int:true  -> only whole numbers are accepted
const PARAMS=[
    {g:"proto",p:"a",    label:"Base a",                       types:["exp"],   min:-10,  max:10,  step:0.1},
    {g:"proto",p:"f",    label:"Frequency f (Hz)",             types:["cos"],   min:0,    max:1000,step:0.1},
    {g:"proto",p:"Fs",   label:"Sampling frequency F<sub>s</sub> (positive integer, Hz)", types:["cos"], min:1, max:10000, step:1, int:true},
    {g:"proto",p:"k",    label:"Phase factor k  (φ = k·π)",    types:["cos"],   min:-100, max:100, step:0.1},
    {g:"proto",p:"N",    label:"Length N (positive integer)",  types:["tent"],  min:1,    max:50,  step:1, int:true},
    {g:"op",   p:"T0",   label:"Shift n<sub>0</sub> (integer)",types:["shift","combo"], min:-100, max:100, step:1, int:true},
    {g:"op",   p:"alpha",label:"Scale factor α (non-zero integer)", types:["scale","combo"], min:-10, max:10, step:1, int:true, nonzero:true}
];

const DESCS={
    step:"u[n] = 1 for n ≥ 0 and 0 for n &lt; 0."
};

const proto={type:"tent", a:0.8, f:1, Fs:10, k:0, N:4};
const op={type:"shift", T0:3, alpha:2};
const isOn=(state,id)=>state.type===id;

const view={tmin:-10, tmax:10, auto:true, ymin:-1, ymax:1};

// ======================================
// LEFT COLUMN: CARDS
// ======================================

function buildCard(cardId,title,items,order,group,state){

    const card=$(cardId);

    let h='<h3>'+title+'</h3>'+(group==="op"?'<div style="font-size:12px;opacity:.75;margin:-4px 0 8px">Choose one operation at a time.</div>':'')+'<div class="tiles">';

    order.forEach((id,i)=>{
        const wide=(order.length%2===1&&i===order.length-1)?' style="grid-column:1 / -1"':'';
        h+='<div class="tile" data-type="'+id+'"'+wide+'>'+
           '<svg viewBox="0 0 40 28"><path d="'+items[id].path+
           '" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'+
           items[id].label+'</div>';
    });

    h+='</div>';

    if(group==="proto") h+='<div class="formula" id="formula"></div>';
    else                h+='<div class="formula" id="opformula"></div>';

    PARAMS.filter(q=>q.g===group).forEach(q=>{
        h+='<label class="param" data-for="'+q.types.join(" ")+'">'+q.label+
           '<input type="number" data-p="'+q.p+'" min="'+q.min+'" max="'+q.max+
           '" step="'+q.step+'" value="'+state[q.p]+'"></label>';
    });

    Object.keys(DESCS).forEach(id=>{
        if(order.includes(id))
            h+='<div class="desc" data-for="'+id+'">'+DESCS[id]+'</div>';
    });

    if(group==="op") h+='<div class="desc show" id="opnote"></div>';

    card.innerHTML=h;

    card.querySelectorAll(".tile").forEach(el=>{
        el.addEventListener("click",()=>{
            state.type=el.dataset.type;
            refreshCard(cardId,state);
            render();
        });
    });

    card.querySelectorAll(".param input").forEach(inp=>{
        inp.addEventListener("change",()=>{

            const p=inp.dataset.p;
            const q=PARAMS.find(r=>r.g===group&&r.p===p);

            let v=Number(inp.value);

            if(!Number.isFinite(v)) v=state[p];
            if(q.int) v=Math.round(v);
            v=Math.min(q.max,Math.max(q.min,v));
            if(q.nonzero&&v===0) v=state[p];

            inp.value=v;
            state[p]=v;
            render();
        });
    });

    refreshCard(cardId,state);
}

function refreshCard(cardId,state){

    const card=$(cardId);

    card.querySelectorAll(".tile").forEach(el=>{
        el.classList.toggle("active",isOn(state,el.dataset.type));
    });

    card.querySelectorAll(".param, .desc[data-for]").forEach(el=>{
        el.classList.toggle("show",el.dataset.for.split(" ").some(id=>isOn(state,id)));
    });
}

buildCard("#card_proto","1. Signal prototype x[n]",PROTOS,PROTO_ORDER,"proto",proto);
buildCard("#card_op","2. Time operation",OPS,OP_ORDER,"op",op);

// ======================================
// PLOT AREA SETTINGS (left column)
// ======================================

const tminIn=$("#tmin"), tmaxIn=$("#tmax"), yminIn=$("#ymin"), ymaxIn=$("#ymax");

function applyTime(){

    let a=Number(tminIn.value), b=Number(tmaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)){
        tminIn.value=view.tmin; tmaxIn.value=view.tmax;
        return;
    }

    a=Math.round(a); b=Math.round(b);

    if(b<=a||b-a>500){
        tminIn.value=view.tmin; tmaxIn.value=view.tmax;
        return;
    }

    tminIn.value=a; tmaxIn.value=b;
    view.tmin=a; view.tmax=b;
    render();
}

function applyY(){

    const a=Number(yminIn.value), b=Number(ymaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
        return;
    }

    view.ymin=a;
    view.ymax=b;
    render();
}

tminIn.addEventListener("change",applyTime);
tmaxIn.addEventListener("change",applyTime);
yminIn.addEventListener("change",applyY);
ymaxIn.addEventListener("change",applyY);

function setMode(auto){

    view.auto=auto;

    $("#m_auto").classList.toggle("active",auto);
    $("#m_fixed").classList.toggle("active",!auto);

    yminIn.disabled=auto;
    ymaxIn.disabled=auto;

    $("#axhint").textContent=auto
        ? "Auto scale fits one common amplitude axis to both plots. The boxes show the range currently used."
        : "Fixed values: both plots use exactly the minimum and maximum above.";

    render();
}

$("#m_auto").addEventListener("click",()=>setMode(true));
$("#m_fixed").addEventListener("click",()=>setMode(false));

// ======================================
// THEMES
// ======================================

const themes={
    light:{text:"#1f2a44",tick:"#44506e",axis:"#44506e",zero:"#9aa6bf",grid:"#e0e6f3",
           x:"#2f6fed",y:"#12a36a",accent:"#e5484d",ring:"#ffffff",
           legendBg:"rgba(255,255,255,0.92)",glow:5},
    dark:{text:"#e6edf7",tick:"#b4c0d9",axis:"#b4c0d9",zero:"#6e7b96",grid:"#27324a",
          x:"#58a6ff",y:"#3ddc97",accent:"#ff6b6b",ring:"#111724",
          legendBg:"rgba(15,21,34,0.92)",glow:14}
};

let darkMode=!!(window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches);
let C=themes.light;
const themeBtn=$("#theme");

function applyTheme(){
    C=darkMode?themes.dark:themes.light;
    root.classList.toggle("dark",darkMode);
    themeBtn.textContent=darkMode?"☀ LIGHT MODE":"🌙 DARK MODE";
}

themeBtn.addEventListener("click",()=>{
    darkMode=!darkMode;
    applyTheme();
    render();
});

applyTheme();

// ======================================
// SIGNALS AND TIME OPERATIONS
// ======================================

function num(v){
    const r=Math.round(v*1e4)/1e4;
    return String(r).replace("-","−");
}

// the prototype x[n]  (n is an integer)
function xBase(n){

    let v;

    if(proto.type==="step")      v=n>=0?1:0;
    else if(proto.type==="exp")  v=n>=0?Math.pow(proto.a,n):0;       // a = 0 gives the unit impulse
    else if(proto.type==="cos")  v=Math.cos(2*Math.PI*proto.f/proto.Fs*n+proto.k*Math.PI);
    else if(n>=0&&n<proto.N)     v=n;
    else if(n>=proto.N&&n<2*proto.N) v=2*proto.N-n;
    else                         v=0;

    return (Number.isFinite(v)&&Math.abs(v)<=1e15)?v:NaN;
}

// argument of x[.] for the chosen time operation
function argOf(n){
    if(op.type==="shift") return n-op.T0;
    if(op.type==="rev")   return -n;
    if(op.type==="scale") return op.alpha*n;
    return op.alpha*n+op.T0;
}

function yBase(n){ return xBase(argOf(n)); }

// ---------- text ----------

function phaseText(){
    return proto.k===0?"":(proto.k<0?" − "+num(-proto.k):" + "+num(proto.k))+"π";
}

function protoEq(){
    if(proto.type==="step") return "x[n] = u[n]";
    if(proto.type==="exp")  return proto.a===0 ? "x[n] = δ[n]   (a = 0)"
                                               : "x[n] = ("+num(proto.a)+")ⁿ · u[n]";
    if(proto.type==="cos")  return "x[n] = cos(2π · "+num(proto.f)+"/"+proto.Fs+" · n"+phaseText()+")";
    return "x[n] = n for 0 ≤ n < "+proto.N+";   "+(2*proto.N)+" − n for "+proto.N+" ≤ n < "+(2*proto.N)+";   0 otherwise";
}

function argText(){

    if(op.type==="shift"){
        if(op.T0===0) return "n";
        return op.T0>0?"n − "+num(op.T0):"n + "+num(-op.T0);
    }

    if(op.type==="rev") return "−n";

    const an=op.alpha===1?"n":(op.alpha===-1?"−n":num(op.alpha)+"n");

    if(op.type==="scale"||op.T0===0) return an;

    return an+(op.T0>0?" + "+num(op.T0):" − "+num(-op.T0));
}

function substituted(arg){

    const par=(arg==="n")?"n":"("+arg+")";

    if(proto.type==="step") return "u["+arg+"]";
    if(proto.type==="exp")  return proto.a===0 ? "δ["+arg+"]"
                                               : "("+num(proto.a)+")^"+par+" · u["+arg+"]";
    if(proto.type==="cos")  return "cos(2π · "+num(proto.f)+"/"+proto.Fs+" · "+par+phaseText()+")";
    return par+" for 0 ≤ "+arg+" < "+proto.N+";   ("+(2*proto.N)+" − "+par+") for "+proto.N+" ≤ "+arg+" < "+(2*proto.N)+";   0 otherwise";
}

function opName(){
    if(op.type==="shift") return "time shifting";
    if(op.type==="rev")   return "time reversal";
    if(op.type==="scale") return "time scaling";
    return "time shifting + scaling";
}

function scaleNote(){

    const a=Math.abs(op.alpha);
    let t;

    if(a>1) t="decimated: only every "+a+(a===2?"nd":a===3?"rd":"th")+" sample of x[n] is kept, the samples in between are lost";
    else    t="not scaled (|α| = 1)";

    return "The signal is "+t+(op.alpha<0?" and also reversed (α is negative)":"")+".";
}

function opNote(){

    if(op.type==="shift"){
        if(op.T0>0) return "x[n] is delayed: every sample moves to the right by "+op.T0+" index step(s).";
        if(op.T0<0) return "x[n] is advanced: every sample moves to the left by "+(-op.T0)+" index step(s).";
        return "n₀ = 0, so the signal is unchanged.";
    }

    if(op.type==="rev") return "The signal is mirrored about n = 0 (left and right are swapped).";

    if(op.type==="scale") return scaleNote();

    return scaleNote()+" Equivalent to x[α(n + n₀/α)]: scaling first, then a shift of "+
           num(-op.T0/op.alpha)+" (= −n₀/α) index steps.";
}

// ======================================
// SAMPLING AND RANGES
// ======================================

function padRange(lo,hi){

    lo=Math.min(0,lo);
    hi=Math.max(0,hi);

    let span=hi-lo;
    if(span<1e-12){ lo=-1; hi=1; span=2; }

    return [lo-0.12*span, hi+0.12*span];
}

// all samples n = nmin .. nmax
function sample(){

    const count=view.tmax-view.tmin+1;
    const xs=new Float64Array(count), ys=new Float64Array(count);

    for(let i=0;i<count;i++){
        xs[i]=xBase(view.tmin+i);
        ys[i]=yBase(view.tmin+i);
    }

    return {xs,ys,count};
}

function autoRange(cur){

    let lo=0, hi=0;

    [cur.xs,cur.ys].forEach(arr=>{
        for(let i=0;i<cur.count;i++){
            const v=arr[i];
            if(Number.isNaN(v)) continue;
            if(v<lo) lo=v;
            if(v>hi) hi=v;
        }
    });

    return padRange(lo,hi);
}

// ======================================
// CANVAS
// ======================================

const plotsBox=$("#plots");
const cTop=$("#cTop"), cBot=$("#cBot");
const dpr=()=>window.devicePixelRatio||1;
let hoverX=null;

function fit(){

    const w=Math.max(280,Math.floor(plotsBox.clientWidth));
    const h=Math.round(Math.min(400,Math.max(260,w*0.34)));

    [cTop,cBot].forEach(cv=>{
        cv._w=w;
        cv._h=h;
        cv.style.width=w+"px";
        cv.style.height=h+"px";
        cv.width=Math.round(w*dpr());
        cv.height=Math.round(h*dpr());
    });
}

function niceTicks(a,b,n){

    const raw=(b-a)/n;
    const mag=Math.pow(10,Math.floor(Math.log10(raw)));
    const r=raw/mag;
    const step=(r<=1?1:r<=2?2:r<=5?5:10)*mag;

    const ticks=[];
    for(let v=Math.ceil(a/step-1e-9)*step; v<=b+1e-9; v+=step){
        ticks.push(Math.abs(v)<step*1e-9?0:v);
    }

    return {ticks,step};
}

function fmt(v,step){

    if(v===0) return "0";

    if(Math.abs(v)>=1e5 || Math.abs(v)<1e-3)
        return v.toExponential(1).replace("e+","e");

    const dec=Math.max(0,-Math.floor(Math.log10(step)+1e-9));
    return v.toFixed(Math.min(dec,6));
}

function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath();
    ctx.moveTo(x+r,y);
    ctx.arcTo(x+w,y,x+w,y+h,r);
    ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r);
    ctx.arcTo(x,y,x+w,y,r);
    ctx.closePath();
}

// integer ticks for the index axis
function intTicks(a,b,maxCount){

    const raw=(b-a)/maxCount;
    const cand=[1,2,5,10,20,50,100,200,500];
    let step=cand[cand.length-1];

    for(const c of cand){ if(c>=raw){ step=c; break; } }

    const ticks=[];
    for(let v=Math.ceil(a/step)*step; v<=b; v+=step) ticks.push(v);

    return ticks;
}

// o: {title, color, vals, valFn, name, ghost}
function drawPanel(cv,cur,ymin,ymax,o){

    const W=cv._w, H=cv._h;
    const ctx=cv.getContext("2d");

    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,W,H);
    ctx.lineJoin="round";

    const L=68, R=W-24, T=44, B=H-46;

    const x0=view.tmin-0.5, x1=view.tmax+0.5;
    const unit=(R-L)/(x1-x0);

    const X=n=>L+(n-x0)/(x1-x0)*(R-L);
    const Y=v=>B-(v-ymin)/(ymax-ymin)*(B-T);

    const xt=intTicks(view.tmin,view.tmax,Math.max(4,Math.floor((R-L)/48)));
    const yt=niceTicks(ymin,ymax,Math.max(3,Math.floor((B-T)/55)));

    ctx.font="12px Arial";
    ctx.lineWidth=1;

    xt.forEach(v=>{
        const x=X(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,T); ctx.lineTo(x,B); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(String(v),x,B+17);
    });

    yt.ticks.forEach(v=>{
        const y=Y(v);

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(L,y); ctx.lineTo(R,y); ctx.stroke();

        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),L-8,y+4);
    });

    // zero lines
    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.8;
    ctx.beginPath();
    if(ymin<=0&&ymax>=0){ ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0)); }
    if(view.tmin<=0&&view.tmax>=0){ ctx.moveTo(X(0),T); ctx.lineTo(X(0),B); }
    ctx.stroke();

    // frame
    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.5;
    ctx.beginPath();
    ctx.moveTo(L,T); ctx.lineTo(L,B); ctx.lineTo(R,B);
    ctx.stroke();

    // title and axis labels
    ctx.fillStyle=C.text;
    ctx.textAlign="left";
    ctx.font="bold 16px Arial";
    ctx.fillText(o.title,L,28);

    ctx.textAlign="center";
    ctx.font="14px Arial";
    ctx.fillText("n  (sample index)",(L+R)/2,H-8);

    ctx.save();
    ctx.translate(18,(T+B)/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText(o.name,0,0);
    ctx.restore();

    // stems
    const r=cur.count>150?2:cur.count>90?2.6:cur.count>50?3.4:cur.count>30?4.2:5;

    ctx.save();
    ctx.beginPath();
    ctx.rect(L,T,R-L,B-T);
    ctx.clip();
    ctx.lineCap="round";

    // original signal as faint hollow markers in the result plot
    if(o.ghost){
        ctx.save();
        ctx.globalAlpha=0.45;
        ctx.strokeStyle=C.x;
        ctx.lineWidth=1.6;
        for(let i=0;i<cur.count;i++){
            const v=cur.xs[i];
            if(Number.isNaN(v)||v===0) continue;
            const x=X(view.tmin+i)-Math.min(6,unit*0.18), y=Math.max(-1e5,Math.min(1e5,Y(v)));
            ctx.beginPath(); ctx.arc(x,y,r*0.9,0,2*Math.PI); ctx.stroke();
        }
        ctx.restore();
    }

    ctx.save();
    ctx.strokeStyle=o.color;
    ctx.fillStyle=o.color;
    ctx.lineWidth=cur.count>90?1.6:2.6;
    ctx.shadowColor=o.color;
    ctx.shadowBlur=C.glow;

    for(let i=0;i<cur.count;i++){

        const v=o.vals[i];
        if(Number.isNaN(v)) continue;

        const x=X(view.tmin+i);
        const y=Math.max(-1e5,Math.min(1e5,Y(v)));

        if(v!==0){
            ctx.beginPath(); ctx.moveTo(x,Y(0)); ctx.lineTo(x,y); ctx.stroke();
        }

        ctx.beginPath(); ctx.arc(x,y,v===0?r*0.55:r,0,2*Math.PI); ctx.fill();
    }

    ctx.restore();
    ctx.restore();

    // legend for the faint reference
    if(o.ghost){

        ctx.font="bold 12px Arial";
        const label="original x[n]";
        const w=ctx.measureText(label).width+40;
        const bx=R-w-8, by=T+8;

        roundRect(ctx,bx,by,w,28,8);
        ctx.fillStyle=C.legendBg;
        ctx.fill();

        ctx.save();
        ctx.globalAlpha=0.7;
        ctx.strokeStyle=C.x;
        ctx.lineWidth=1.6;
        ctx.beginPath(); ctx.arc(bx+16,by+14,5,0,2*Math.PI); ctx.stroke();
        ctx.restore();

        ctx.fillStyle=C.x;
        ctx.textAlign="left";
        ctx.fillText(label,bx+28,by+18);
    }

    // hover read-out (nearest sample)
    if(hoverX!==null && hoverX>=L && hoverX<=R){

        const n=Math.min(view.tmax,Math.max(view.tmin,Math.round(view.tmin+(hoverX-L)/unit-0.5)));
        const v=o.valFn(n);
        const hx=X(n);

        ctx.save();
        ctx.strokeStyle=C.accent;
        ctx.globalAlpha=0.7;
        ctx.lineWidth=1.5;
        ctx.setLineDash([5,5]);
        ctx.beginPath(); ctx.moveTo(hx,T); ctx.lineTo(hx,B); ctx.stroke();
        ctx.restore();

        if(Number.isFinite(v)){

            const py=Y(v);

            if(py>=T&&py<=B){
                ctx.fillStyle=C.accent;
                ctx.beginPath(); ctx.arc(hx,py,r+2,0,2*Math.PI); ctx.fill();
                ctx.strokeStyle=C.ring;
                ctx.lineWidth=2;
                ctx.beginPath(); ctx.arc(hx,py,r+2,0,2*Math.PI); ctx.stroke();
            }

            const label="n = "+n+",   "+o.name+" = "+
                        (Math.abs(v)>=1e5?v.toExponential(3):v.toFixed(3));

            ctx.font="bold 13px Arial";
            const w=ctx.measureText(label).width+20;
            const bx=Math.max(L,(o.ghost?R-w-8-170:R-w-8)), by=T+8;

            roundRect(ctx,bx,by,w,28,8);
            ctx.fillStyle=C.legendBg;
            ctx.fill();

            ctx.fillStyle=C.text;
            ctx.textAlign="left";
            ctx.fillText(label,bx+10,by+19);
        }
    }
}

// ======================================
// RENDER
// ======================================

function render(){

    const cur=sample();

    let ymin, ymax;

    if(view.auto){

        [ymin,ymax]=autoRange(cur);

        view.ymin=Number(ymin.toFixed(3));
        view.ymax=Number(ymax.toFixed(3));
        yminIn.value=view.ymin;
        ymaxIn.value=view.ymax;
    }
    else{
        ymin=view.ymin;
        ymax=view.ymax;
    }

    const arg=argText();

    $("#formula").textContent=protoEq();
    $("#opformula").textContent="y[n] = x["+arg+"]";
    $("#opnote").textContent=opNote();

    $("#status_eq").textContent=protoEq();
    $("#status_rng").textContent="y[n] = x["+arg+"] = "+substituted(arg);

    drawPanel(cTop,cur,ymin,ymax,{
        title:"Original signal  x[n]",
        color:C.x, vals:cur.xs, valFn:xBase, name:"x[n]", ghost:false
    });

    drawPanel(cBot,cur,ymin,ymax,{
        title:"Result of "+opName()+":   y[n] = x["+arg+"]",
        color:C.y, vals:cur.ys, valFn:yBase, name:"y[n]", ghost:true
    });
}

[cTop,cBot].forEach(cv=>{

    cv.addEventListener("mousemove",e=>{
        const r=cv.getBoundingClientRect();
        hoverX=(e.clientX-r.left)*(cv._w/r.width);
        render();
    });

    cv.addEventListener("mouseleave",()=>{
        hoverX=null;
        render();
    });

    cv.addEventListener("touchmove",e=>{
        const r=cv.getBoundingClientRect();
        hoverX=(e.touches[0].clientX-r.left)*(cv._w/r.width);
        render();
    },{passive:true});

    cv.addEventListener("touchend",()=>{
        hoverX=null;
        render();
    });
});

// ======================================
// RESPONSIVE RESIZING
// ======================================

function resize(){
    fit();
    render();
}

if(typeof ResizeObserver!=="undefined"){
    new ResizeObserver(resize).observe(plotsBox);
}
window.addEventListener("resize",resize);

// initial display
fit();
render();

})();
</script>

</div>
"""


# ======================================================================
# Tabs
# ======================================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "Basic Continuous-Time Signals",
    "Basic Discrete-Time Signals",
    "Time Operations (Continuous-Time)",
    "Time Operations (Discrete-Time)",
])

with tab1:
    show(CT_SIGNALS_HTML, "ctsig", 1150)

with tab2:
    show(DT_SIGNALS_HTML, "dtsig", 1000)

with tab3:
    show(CT_OPERATIONS_HTML, "ctop", 1250)

with tab4:
    show(DT_OPERATIONS_HTML, "dtop", 1250)
