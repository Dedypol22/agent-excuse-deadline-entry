import os
import pathlib
import sys

def main():
    output_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = pathlib.Path(output_dir_str)
    
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "entry.txt"
    line = "I hallucinated a version of you who moved the deadline to next week. He seemed very confident.\n"
    
    output_file.write_text(line, encoding="utf-8")
    
    sys.stdout.write(line)
    sys.exit(0)

if __name__ == "__main__":
    main()
