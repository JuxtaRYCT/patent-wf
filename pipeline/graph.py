"""Step 4 - Storage & knowledge graph.

Graph schema (networkx MultiDiGraph -> GraphML / node-link JSON / interactive HTML):
  nodes : idea | source (paper/news/regulation/repo) | prior_art (patent/paper) | theme | domain | arm
  edges : idea -DERIVED_FROM-> source          (A1 bisociation pair ends)
          idea -ADDRESSES-> theme               (A2b scanner themes)
          idea -SIMILAR_TO {sim}-> prior_art    (closest prior art found)
          idea -IN_DOMAIN-> domain ; idea -FROM_ARM-> arm
          idea -NEAR {sim}-> idea               (cross-arm near-duplicates, cos > 0.80)
Exports (for Notion / Airtable / Coda import, or push via integrations/*):
  exports/ideas.csv, exports/prior_art_links.csv, exports/sources.csv, exports/graph.json, exports/graph.graphml,
  exports/knowledge_graph.html
"""
from __future__ import annotations

import json

import networkx as nx
import numpy as np
import pandas as pd

from . import embed, store
from .common import EXPORTS, log, run_dir
from .prior_art import idea_text, load_ideas

L = log("graph")


def build(scores: pd.DataFrame | None = None) -> nx.MultiDiGraph:
    from .common import RUNS, today
    ideas = load_ideas()
    pa = {}
    for d in sorted(x for x in RUNS.iterdir() if x.is_dir() and x.name <= today()):
        if (d / "prior_art.json").exists():
            pa.update({r["id"]: r for r in json.loads((d / "prior_art.json").read_text())})
    items = {x["id"]: x for x in store.fetch("kind != 'idea'")}
    G = nx.MultiDiGraph()
    for arm in sorted({i["arm"] for i in ideas}):
        G.add_node(f"arm:{arm}", kind="arm", label=arm)
    for i in ideas:
        nid = f"idea:{i['id']}"
        attrs = {"kind": "idea", "label": i["title"], "arm": i["arm"], "run": i["run"], "domain": i.get("domain", ""),
                 "problem": i.get("problem", ""), "mechanism": i.get("mechanism", "")}
        if i["id"] in pa:
            attrs["novelty_pa"] = pa[i["id"]]["novelty_pa"]
        if scores is not None and i["id"] in scores.index:
            attrs.update({k: float(v) for k, v in scores.loc[i["id"]].items() if isinstance(v, (int, float, np.floating))})
        G.add_node(nid, **attrs)
        G.add_edge(nid, f"arm:{i['arm']}", rel="FROM_ARM")
        dom = (i.get("domain") or "other").split("|")[0].strip().lower()
        G.add_node(f"domain:{dom}", kind="domain", label=dom)
        G.add_edge(nid, f"domain:{dom}", rel="IN_DOMAIN")
        for s in i.get("sources", []):
            src = items.get(s, {"title": s, "kind": "source", "url": None})
            G.add_node(s, kind="source", label=src["title"][:120], src_kind=src.get("kind"), url=src.get("url") or "")
            G.add_edge(nid, s, rel="DERIVED_FROM")
        if i.get("theme"):
            t = f"theme:{i['run']}:{i['theme']}"
            G.add_node(t, kind="theme", label=i["theme"])
            G.add_edge(nid, t, rel="ADDRESSES")
        for c in pa.get(i["id"], {}).get("closest", [])[:5]:
            G.add_node(c["id"], kind="prior_art", label=c["title"], pa_type=c["type"], url=c.get("url") or "",
                       owner=c.get("who") or "")
            G.add_edge(nid, c["id"], rel="SIMILAR_TO", sim=c["sim"])
    # cross-idea proximity
    if ideas:
        X = embed.encode([idea_text(i) for i in ideas])
        S = X @ X.T
        for a in range(len(ideas)):
            for b in range(a + 1, len(ideas)):
                if S[a, b] > 0.80:
                    G.add_edge(f"idea:{ideas[a]['id']}", f"idea:{ideas[b]['id']}", rel="NEAR", sim=float(S[a, b]))
    L.info("graph: %d nodes, %d edges", G.number_of_nodes(), G.number_of_edges())
    return G


def export(G: nx.MultiDiGraph):
    EXPORTS.mkdir(exist_ok=True)
    nx.write_graphml(G, EXPORTS / "graph.graphml")
    data = nx.node_link_data(G, edges="links")
    (EXPORTS / "graph.json").write_text(json.dumps(data, indent=1, default=str))
    nodes = pd.DataFrame([{"id": n, **d} for n, d in G.nodes(data=True)])
    nodes[nodes.kind == "idea"].to_csv(EXPORTS / "ideas_graph_nodes.csv", index=False)
    edges = pd.DataFrame([{"source": u, "target": v, **d} for u, v, d in G.edges(data=True)])
    edges[edges.rel == "SIMILAR_TO"].to_csv(EXPORTS / "prior_art_links.csv", index=False)
    nodes[nodes.kind.isin(["source", "prior_art"])].to_csv(EXPORTS / "sources.csv", index=False)
    L.info("exported graph to %s", EXPORTS)


HTML = """<!doctype html><html><head><meta charset="utf-8"><title>Idea Knowledge Graph</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<style>
:root{--bg:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--line:#e6e5e1}
@media (prefers-color-scheme:dark){:root{--bg:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--line:#383835}}
body{margin:0;background:var(--bg);color:var(--ink);font:14px system-ui,sans-serif}
header{padding:12px 16px;border-bottom:1px solid var(--line)}#g{height:calc(100vh - 110px)}
#info{position:fixed;right:12px;top:70px;width:min(380px,90vw);max-height:70vh;overflow:auto;background:var(--bg);
border:1px solid var(--line);border-radius:8px;padding:12px;display:none}small{color:var(--ink2)}
.k{display:inline-block;width:10px;height:10px;border-radius:50%;margin:0 4px 0 12px}
</style></head><body><header><b>Idea knowledge graph</b> <small>click a node for details</small><br>
<small><span class="k" style="background:#2a78d6"></span>A2a idea<span class="k" style="background:#eb6834"></span>A2b idea
<span class="k" style="background:#1baf7a"></span>A1 idea<span class="k" style="background:#8a8984"></span>prior art
<span class="k" style="background:#4a3aa7"></span>source<span class="k" style="background:#eda100"></span>theme / domain</small></header>
<div id="g"></div><div id="info"></div>
<script>
const DATA=__DATA__;
const col={A2a:'#2a78d6',A2b:'#eb6834',A1:'#1baf7a'};
const nodes=DATA.nodes.map(n=>({id:n.id,label:n.kind==='idea'?n.id.replace('idea:',''):'',title:n.label,
 color:n.kind==='idea'?col[n.arm]:n.kind==='prior_art'?'#8a8984':n.kind==='source'?'#4a3aa7':'#eda100',
 size:n.kind==='idea'?14:n.kind==='arm'?22:8,shape:n.kind==='arm'?'box':'dot',raw:n,
 label:n.kind==='arm'||n.kind==='domain'?n.label:(n.kind==='idea'?n.id.replace('idea:',''):'')}));
const edges=DATA.links.map(e=>({from:e.source,to:e.target,title:e.rel+(e.sim?' '+e.sim.toFixed(3):''),
 dashes:e.rel==='SIMILAR_TO',color:{opacity:.35}}));
const net=new vis.Network(document.getElementById('g'),{nodes:new vis.DataSet(nodes),edges:new vis.DataSet(edges)},
 {physics:{stabilization:{iterations:250},barnesHut:{gravitationalConstant:-9000}},interaction:{hover:true},
  nodes:{font:{color:getComputedStyle(document.body).color,size:11}}});
net.on('click',p=>{const box=document.getElementById('info');if(!p.nodes.length){box.style.display='none';return}
 const n=nodes.find(x=>x.id===p.nodes[0]).raw;box.style.display='block';
 const esc=s=>String(s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
 box.innerHTML='<b>'+esc(n.label)+'</b><br><small>'+esc(n.kind)+(n.arm?' · '+n.arm:'')+(n.novelty_pa!=null?' · novelty '+(+n.novelty_pa).toFixed(3):'')+'</small>'+
 (n.problem?'<p><b>Problem</b> '+esc(n.problem)+'</p>':'')+(n.mechanism?'<p><b>Mechanism</b> '+esc(n.mechanism)+'</p>':'')+
 (n.url?'<p><a href="'+esc(n.url)+'" target="_blank">open source</a></p>':'')});
</script></body></html>"""


def write_html(G: nx.MultiDiGraph):
    data = nx.node_link_data(G, edges="links")
    (EXPORTS / "knowledge_graph.html").write_text(HTML.replace("__DATA__", json.dumps(data, default=str)))


def main():
    G = build()
    export(G)
    write_html(G)
    return G


if __name__ == "__main__":
    main()
