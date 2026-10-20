import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def load_json(path):
    full_path = os.path.join(ROOT, path)
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)

def check_deliverables(layer, layer_path):
    missing = []
    for d in layer.get("deliverables", []):
        file_path = os.path.join(ROOT, layer_path, d)
        if not os.path.exists(file_path):
            missing.append(d)
    return missing

def check_toolkits(layer, layer_path):
    missing = []
    for t in layer.get("toolkits", []):
        file_path = os.path.join(ROOT, layer_path, t)
        if not os.path.exists(file_path):
            missing.append(t)
    return missing

def summarize_layers(roadmap):
    print("\n=== Stage‑1 Layer Summary ===")
    for layer in roadmap["layers"]:
        print(f"\nLayer: {layer['title']}")
        print(f"ID: {layer['id']}")
        print(f"Status: {layer.get('status', 'unknown')}")
        print(f"Deliverables: {len(layer.get('deliverables', []))}")
        print(f"Toolkits: {len(layer.get('toolkits', []))}")

def summarize_tasks(tasks):
    print("\n=== Task Summary ===")
    for t in tasks:
        print(f"\nTask {t['id']}: {t['description']}")
        print(f"Layer: {t['layer']}")
        print(f"Priority: {t['priority']}")
        print(f"Status: {t['status']}")
        print(f"Dependencies: {t['dependencies']}")

def check_dependencies(tasks):
    print("\n=== Dependency Check ===")
    task_ids = {t["id"] for t in tasks}
    for t in tasks:
        for dep in t["dependencies"]:
            if dep not in task_ids:
                print(f"WARNING: Task {t['id']} depends on missing task {dep}")

def check_repo_state(roadmap):
    print("\n=== Repository State Check ===")
    for layer in roadmap["layers"]:
        layer_path = layer["id"]
        print(f"\nChecking layer: {layer['title']} ({layer_path})")

        missing_docs = check_deliverables(layer, layer_path)
        missing_tools = check_toolkits(layer, layer_path)

        if missing_docs:
            print("Missing deliverables:")
            for m in missing_docs:
                print(f"  - {m}")
        else:
            print("All deliverables present.")

        if missing_tools:
            print("Missing toolkits:")
            for m in missing_tools:
                print(f"  - {m}")
        else:
            print("All toolkits present.")

def main():
    roadmap = load_json("roadmap.json")
    tracker = load_json("task-tracker.json")

    summarize_layers(roadmap)
    summarize_tasks(tracker["tasks"])
    check_dependencies(tracker["tasks"])
    check_repo_state(roadmap)

if __name__ == "__main__":
    main()
