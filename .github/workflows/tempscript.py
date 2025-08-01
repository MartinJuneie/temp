# .github/workflows/scripts/tempscript.py

import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: python tempscript.py <path-to-json>")
        sys.exit(1)

    json_path = sys.argv[1]
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            print("📄 Loaded JSON data:")
            print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"❌ Failed to read or parse {json_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
