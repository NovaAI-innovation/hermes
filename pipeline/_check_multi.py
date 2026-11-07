import json
import collections
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = [json.loads(l) for l in open(root / "corpus" / "chunks.jsonl", encoding="utf-8")]

print("chunks:", len(rows))
print("by source:", collections.Counter(r["corpus_source"] for r in rows))
print("by source+type:", collections.Counter((r["corpus_source"], r["doc_type"]) for r in rows).most_common(8))

ids = [r["chunk_id"] for r in rows]
print("unique ids:", len(set(ids)))
print("all qualified:", all(":" in i.split("#")[0] for i in ids))

for src in ("hermes", "mcp"):
    sample = next(r for r in rows if r["corpus_source"] == src)
    print(f"\n{src}:")
    print("  chunk_id :", sample["chunk_id"])
    print("  doc_id   :", sample["doc_id"])
    print("  title    :", sample["title"])
    print("  doc_type :", sample["doc_type"])
    print("  url      :", sample["source_url"])
    print("  section  :", sample["section"])

docs = [json.loads(l) for l in open(root / "corpus" / "documents.jsonl", encoding="utf-8")]
no_url = [d for d in docs if not d["source_url"]]
print("\ndocs missing source_url:", len(no_url))
print("sources in manifest set:", sorted({d["corpus_source"] for d in docs}))
